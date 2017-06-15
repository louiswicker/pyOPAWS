 subroutine cressman(x, y, ob, xg, yg, method, min_count, min_weight, min_range, roi, missing_value, anal, nobs, nx, ny)

   implicit none
 
   real(8), intent(in),  dimension(nobs) :: x
   real(8), intent(in),  dimension(nobs) :: y
   real(4), intent(in),  dimension(nobs) :: ob
   real(8), intent(in),  dimension(nx)   :: xg
   real(8), intent(in),  dimension(ny)   :: yg
   real(4), intent(out), dimension(nx,ny) :: anal
   real,    intent(in) :: roi, missing_value, min_weight, min_range
   integer, intent(in) :: nobs, nx, ny, min_count, method

   integer n, i, j, count
   real(kind=8) dis, R2, w_sum, sum, wk, rk2
   real, parameter :: hsp0 = 1.33

   logical, parameter :: debug = .true.
 
   IF ( method .eq. 1 ) THEN
     R2 = roi**2.0
   ELSE
     R2 = (hsp0*roi/1000.)**2     ! Pauley and Wu (1990)
   ENDIF
 
   IF( debug ) THEN
      print *, 'Method:                 ', method
      print *, 'Min gates for analysis: ', min_count
      print *, 'Min weight for analysis:', min_weight
      print *, 'Min range for analysis: ', min_range
      print *, 'Nobs:                   ', nobs
      print *, 'Nx/Ny:                  ', nx, ny
      print *, 'Maxval of anal before:  ', maxval(anal)
      print *, 'Minval of anal before:  ', minval(anal)
      print *, ''
      print *, 'Maxval of observations:  ', maxval(ob)
      print *, 'Minval of observations:  ', minval(ob)
      print *, 'Min/Max xob:    ', minval(x), maxval(x)
      print *, 'Min/Max yob:    ', minval(y), maxval(y)
      print *, 'Min/Max xgrid:  ', minval(xg), maxval(xg)
      print *, 'Min/Max ygrid:  ', minval(yg), maxval(yg)
      print *, 'Radius of influence:  ', roi
      print *, ''
   ENDIF
 
   DO j = 1,ny
    DO i = 1,nx

     IF( method .eq. 1 ) THEN   ! Cressman

       count = 0
       w_sum = 0.0
       sum   = 0.0  
       anal(i,j) = missing_value
       DO n = 1,nobs
         dis = sqrt( (xg(i) - x(n))**2 + (yg(j)-y(n))**2 )
         IF ((dis .le. roi) .and. (dis .ge. min_range)) THEN
           rk2 = dis**2.0
           wk = (R2-rk2) / (R2+rk2)
           sum = sum + wk*ob(n)
           w_sum = w_sum + wk
           count = count + 1
         ENDIF
       ENDDO

     ELSE       ! Barnes 1-pass

       count = 0
       w_sum = 0.0
       sum   = 0.0  
       anal(i,j) = missing_value
       DO n = 1,nobs
         dis = sqrt( (xg(i) - x(n))**2 + (yg(j)-y(n))**2 )
         IF ((dis .le. 6.0*roi) .and. (dis .ge. min_range)) THEN
           rk2 = dis**2.0
           wk = exp( -rk2 / R2 )
           sum = sum + wk*ob(n)
           w_sum = w_sum + wk
           count = count + 1
         ENDIF
       ENDDO

     ENDIF


     IF ((w_sum .ge. min_weight) .and. (count .ge. min_count)) THEN
        anal(i,j) = anal(i,j) + sum/w_sum
     ENDIF

    ENDDO
   ENDDO
 
   IF( debug ) THEN
      print *, 'Maxval of anal after:  ', maxval(anal)
      print *, 'Minval of anal after:  ', minval(anal)
   ENDIF

 end subroutine cressman
 
!======================================================================================================'
!
! Routine to cressman a set of obs to a 2D grid (could be a random grid).  Implemention
! uses the cKDTree algorithm in python to find the indices for each ob that is on the grid.
!
! Example code in python to create fields that are needed.
!=======================================================================================================
!# Begin python code
!
!import numpy, scipy.spatial
!import time
!
!# set up test grid
!
!x1d = numpy.arange(500) / 500.
!y1d = numpy.arange(600) / 600.
!z1d = numpy.arange(60)  / 60.
!
!y_array, z_array, x_array = numpy.meshgrid(y1d, z1d, x1d)
!combined_xyz_arrays = numpy.dstack([z_array.ravel(),y_array.ravel(),x_array.ravel()])[0]
!print 'XYZ ARRAY SHAPE', combined_xyz_arrays.shape
!
!obs = numpy.random.random(30).reshape(3,10)
!print 'Obs Shape:', obs.shape
!obs_list = list(obs.transpose())
!
!# Okay create the KDTree data structure
!
!mytree = scipy.spatial.cKDTree(combined_xyz_arrays)
!
!distances, indices1D = mytree.query(obs_list)
!
!indices3D = numpy.unravel_index(numpy.ravel(indices1D, y_array.size), y_array.shape)
!
!# these are the integer indices that you now pass into the fortran routine. They
!# are the un-raveled 3D index locations nearest the observation point in the 3D array
!
!k = indices3D[0]
!j = indices3D[1]
!i = indices3D[2]
!
!for n in numpy.arange(obs.shape[1]) :
!    print n, obs[0,n], obs[1,n], obs[2,n], z_array[k[n],j[n],i[n]], y_array[k[n],j[n],i[n]], x_array[k[n],j[n],i[n]]
! 
!# END python code
!======================================================================================================'
SUBROUTINE OBS_2_GRID2D(obs, xob, yob, xc, yc, ii, jj, method, min_count, min_weight, min_range, roi, missing, field, nobs, nx, ny)
                   
  implicit none

! Passed in variables

  real(kind=8),    INTENT(OUT) :: field(ny,nx)      ! 2D analysis passed back to calling routine
      
  integer,         INTENT(IN)  :: nx, ny, nobs      ! grid dimensions
  real(kind=4),    INTENT(IN)  :: xob(nobs)         ! x coords for each ob
  real(kind=4),    INTENT(IN)  :: yob(nobs)         ! y coords for each ob
  real(kind=4),    INTENT(IN)  :: obs(nobs)         ! obs 
  integer(kind=8), INTENT(IN)  :: ii(nobs)          ! nearest index to the x-point on grid for ob
  integer(kind=8), INTENT(IN)  :: jj(nobs)          ! nearest index to the x-point on grid for o 
  real(kind=4),    INTENT(IN)  :: xc(nx)         ! coordinates corresponding to WRF model grid locations
  real(kind=4),    INTENT(IN)  :: yc(ny)         ! coordinates corresponding to WRF model grid locations
  real(kind=4),    INTENT(IN)  :: roi
  real(kind=4),    INTENT(IN)  :: missing
  real(kind=4),    INTENT(IN)  :: min_weight, min_range
  INTEGER(kind=8), INTENT(IN)  :: min_count, method


! Local variables

  integer(kind=8) i, j, i0, j0, n, i0m, i0p, j0m, j0p, idx, jdx       ! loop variables
  
  real(kind=8) dis, wgt, R2, dx, dy, rk2, dxy
  real(kind=8), allocatable, dimension(:,:) :: sum, wgt_sum
  integer(kind=8), allocatable, dimension(:,:) :: count

  real, parameter :: hsp0 = 1.33

  logical, parameter :: debug = .false.

! Allocate local memory

  allocate(wgt_sum(ny, nx))
  allocate(sum(ny, nx))
  allocate(count(ny, nx))

! Initialize values

  field(:,:)   = missing  
  wgt_sum(:,:) = 0.0
  sum(:,:)     = 0.0
  count(:,:)   = 0
  
  dx = xc(2) - xc(1)
  dy = yc(2) - yc(1)
  dxy = sqrt(dx*dy)
  
  IF ( method .eq. 1 ) THEN
    R2 = roi**2.0
    idx = 1 + nint(2.0*roi/dx)
    jdx = 1 + nint(2.0*roi/dy)
  ELSE
    R2 = (hsp0*roi/1000.)**2     ! Pauley and Wu (1990)
    idx = 1 + nint(7.*roi/dx)
    jdx = 1 + nint(7.*roi/dy)
  ENDIF
  
  IF( debug) THEN
    print *, "----------------------------------------------------------------"
    print * 
    print *, "FORTRAN OBS_2_GRID2D:  Method  ", method
    print *, 'FORTRAN OBS_2_GRID2D:  Min gates for analysis: ', min_count
    print *, 'FORTRAN OBS_2_GRID2D:  Min weight for analysis:', min_weight
    print *, 'FORTRAN OBS_2_GRID2D:  Min range for analysis: ', min_range
    print *, "FORTRAN OBS_2_GRID2D:  dims  ", nx, ny, nobs
    print *, "FORTRAN OBS_2_GRID2D:  dx, ROI, R2", dx, ROI, R2
    print *, "FORTRAN OBS_2_GRID2D:  dy, ROI, R2", dy, ROI, R2
    print *, "FORTRAN OBS_2_GRID2D:    obs ", minval(obs), maxval(obs)
    print *, "FORTRAN OBS_2_GRID2D:  x-obs ", minval(xob), maxval(xob)
    print *, "FORTRAN OBS_2_GRID2D:  y-obs ", minval(yob), maxval(yob)
    print *, "FORTRAN OBS_2_GRID2D:  x-grid", minval(xc), maxval(xc)
    print *, "FORTRAN OBS_2_GRID2D:  y-grid", minval(yc), maxval(yc)
    print *, "FORTRAN OBS_2_GRID2D:  i-index", minval(ii), maxval(ii)
    print *, "FORTRAN OBS_2_GRID2D:  j-index", minval(jj), maxval(jj)
    print *, "FORTRAN OBS_2_GRID2D:  i-width", idx
    print *, "FORTRAN OBS_2_GRID2D:  j-width", jdx
  ENDIF
     
  DO n = 1,nobs
  
    i0 = ii(n)
    j0 = jj(n)
        
    i0m = max(i0-idx,1)
    j0m = max(j0-jdx,1)
    
    i0p = min(i0+idx,nx)
    j0p = min(j0+jdx,ny)

    IF( method .eq. 1 ) THEN    ! Cressman
    
      DO i = i0m, i0p
        DO j = j0m, j0p
        
          dis = (xc(i) - xob(n))**2 + (yc(j)-yob(n))**2
          wgt = (R2 - dis) / (R2 + dis)
          IF (wgt > 0.0) THEN
            sum(j,i)     = sum(j,i) + wgt*obs(n)
            wgt_sum(j,i) = wgt_sum(j,i) + wgt
            count(j,i)   = count(j,i) + 1
          ENDIF  
                    
        ENDDO    ! END J
      ENDDO     ! END I          

    ELSE

      DO i = i0m, i0p
        DO j = j0m, j0p

         dis = sqrt( (xc(i) - xob(n))**2 + (yc(j)-yob(n))**2 )
         IF ((dis .le. 5.0*roi) .and. (dis .ge. min_range)) THEN
           rk2          = (dis/dxy)**2.0
           wgt          = exp( -rk2 / R2 )
           sum(j,i)     = sum(j,i) + wgt*obs(n)
           wgt_sum(j,i) = wgt_sum(j,i) + wgt
           count(j,i)   = count(j,i) + 1
         ENDIF

        ENDDO    ! END J
      ENDDO     ! END I          

    ENDIF

  ENDDO      ! END N

  WHERE( wgt_sum > min_weight ) field = sum / wgt_sum
  WHERE( count   <  min_count ) field = missing
  
  
  IF( debug ) THEN
  
    print *, "FORTRAN OBS_2_GRID2D:    counts ", minval(count), maxval(count)
    print *, "FORTRAN OBS_2_GRID2D:    wgts   " , minval(wgt_sum), maxval(wgt_sum)
    print *, "FORTRAN OBS_2_GRID2D:    sums   ", minval(sum), maxval(sum)
    print *, "FORTRAN OBS_2_GRID2D:    field  ", minval(field), maxval(field)
  
  ENDIF
 
  deallocate(wgt_sum)
  deallocate(sum)
  deallocate(count)

RETURN
END SUBROUTINE OBS_2_GRID2D
