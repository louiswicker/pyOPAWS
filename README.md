
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">



  <link crossorigin="anonymous" href="https://assets-cdn.github.com/assets/frameworks-722d5e7b1dad7337873eb9e5df225130f9619c70d109a26aebf344b98cbff091.css" media="all" rel="stylesheet" />
  <link crossorigin="anonymous" href="https://assets-cdn.github.com/assets/github-8f7d19ccb1b9871a0a66804035b4bc3936aa69e67ebfc8322969849f3cf2ad79.css" media="all" rel="stylesheet" />
  
  
  
  

  <meta name="viewport" content="width=device-width">
  

    
  <div id="readme" class="readme blob instapaper_body">
    <article class="markdown-body entry-content" itemprop="text"><h2><a id="user-content-synopsis" class="anchor" href="#synopsis" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Synopsis</h2>
<p>pyOPAWS is intended to be a replacement package for David Dowell and Lou Wicker's OPAWS radar gridding software (Observation Processing and Wind Synthesis) that was originally created in the late 1990's and became used by a number of groups during the last 10 years.  The original code was capable of reading DORADE sweep files and later CFradial files created from operational radars or a variety of mobile radars.  The code is intended to replace the original fortran and C code, be able to process WSR-88D level-II files directly. However, it is not capable or reading DORADE format, only level-II and CFradial are supported.  This is due to the use of the python ARM-CART toolkit for radar ingest and processing as its base</p>
<h2><a id="user-content-code-example" class="anchor" href="#code-example" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Usage Examples</h2>
<p>

**Example command lines for lvl2_plot.py:**

1.	python lvl2_plot.py -f KDDC20160525_001527_V06.gz -q None -p 1 -u phase
    <p>creates plot of 6 variables (REF, VR, SPEC_W, Zdr, KDP, PHIDP), no QC, plot 2nd tilt level, phase unfolding</p>

2.	python lvl2_plot.py --plot2 -f KDDC20160525_001527_V06.gz -q None -p 1 -u phase

    *creates plot of REF and VR, no DBZ QC, plot 2nd title, phase unfolding*

3.	python lvl2_plot.py --plot2 -f KDDC20160525_001527_V06.gz -q MetSignal -p 1 -u phase

    *creates plot of REF and VR, MetSig QC, plot 2nd title, phase unfolding*

**Example command lines for opaws2d.py:**

1.	python opaws2d.py -f KDDC20160525_001527_V06.gz -q None -p 1 –w -u phase

    *opaws2d with no QC, plot 2nd tilt level, phase unfolding, -w to DART and netCDF files*

2.	python opaws2d.py -f KDDC20160525_001527_V06.gz -q None -p 1 –w -u region
    *opaws2d with no QC, plot 2nd tilt level, region unfolding, write out DART and netCDF files*

3.	python opaws2d.py -f KDDC20160525_001527_V06.gz -q MetSignal -u phase
    *opaws2d with MetSig QC, plot 2nd title, phase unfolding, write out DART and netCDF files*

**_You can compare the outputs from your tests to the files in KDDC directory_**
</p>
<h2><a id="user-content-motivation" class="anchor" href="#motivation" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Motivation</h2>
<p>The current fortran-based OPAWS was written to do two things:  create a 3D Cartesian interpolated for dual-doppler analysis, or as a second (and added later option) superobb reflectivity and radial velocity data for storm-scale data assimilation.  Lacking was quality control on the data itself, a minimal unfolding technique, and only thresholding reflectivity as a form of QC.  pyOPAWS is written with several goals:  

1.  modernize the data analysis with python (less code)

2.  read level-II files directly (useful for realtime applications, as well as case studies)

3.  incorporate the velocity unfolding algorithms available in the python ARM-CART toolkit

4.  Incorporate reflectvity (and velocity, where needed) quality control via use of dual-pol data available from most radars today.


</p>
<h2><a id="user-content-installation" class="anchor" href="#installation" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Installation</h2>
<p>Python packages Required:  pyart, numpy, scipy, optparse, netCDF4, datetime, pyproj.  Was built based on the Anaconda-2 system.

1.	To run the lvl-2 plotting, you can simply run the script. 
2.	To run the opaws2d.py script, you must first:
3.	fcompile_cressman.py – compiles the fortran cressman routine, assumes GNU compiler is installed before the Anaconda python was installed.  Note:  “conda install libgfortran” can be helpful.
4.	Once a “cressman.so” exists and can be loaded – opaws2d is ready to run
</p>
<h2><a id="user-content-api-reference" class="anchor" href="#api-reference" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>IMPORTANT INFORMATION!</h2>
<p>

There are several current limitations of the software - and the velocity unfolding has an important "buyer beward clause..."

1.  Opaws2d.py has only been extensively tested on WSR-88D level-II archive files.  In theory (not practice), it should work on CFradial files with little modification (there is already the ability to read in data).  It has not yet been tested on CFradial files - particularily with the data QC.  Use "-q None" if you want to grid a CFradial file. 

2.  Split cut level-II files created from the superres levels are difficult to manage.  For example, the reflectivity and dual-pol variables are all on one sweep, and radial velocity is on the next sweep.  The code "maps" which levels go together, BUT, on superres radial velocity sweeps, there is ALSO reflectivity (only).  So for simple masking, the reflectivity collected with the radial velocity is used.  For more complicated QC, then the mapped sweep is used to QC the radial velocity.

3.  For level-II collection with dual-PRF (PRT?), I cannot find documentation as to what velocity field is stored in the level-II file, except that it is NOT unfolded.  The pyART unfolding algorithms CANNOT handle multiple nyquists on a single sweep, which is what is stored in the file.  The way it currently works is that the nyquist velocity for a sweep is reset to the minimum nyquist velocity on that sweep, and then the unfolding algorithm is applied.  Comparing to level-III data from the same sweep, it seems to work.  But its unclear what is going on here, and if anyone knows better - please contact me.

</p>
<h2><a id="user-content-tests" class="anchor" href="#tests" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Tests</h2>

<p> To test the scripts:  

Copy from KDDC directory the file:  KDDC20160525_001527_V06.gz into the main directory.  Try several of the commands listed above.

Lvl2 files will be placed in a directory called “images”, and opaws2d files will be placed in a directory called “opaws_files”.  

Plots of gridded superobbed fields (REF and VR) are placed in the main directory when created.

</p>

<h2><a id="user-content-contributors" class="anchor" href="#contributors" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Contributors</h2>
<p>

I wish to thank David Dowell, Robin Tanamachi, Dan Dawson, Glen Romine, Wen-Chau Lee, Corey Potvin, and Mike Coniglio for their help in the development and maintanance of the original OPAWS code.  A version of the software can be found on GitHub currently - [OPAWS] (https://github.com/hhuangwx/opaws).

I also wish to thank developers of the py-ART software, Scott Collis and Jon Helmus for their package - this rewrite would not have occured without their development of their package. 

People wishing to contribute to this project are very much welcome, please email me at Louis.Wicker @ noaa.gov.  If you plan to do much development, please make your own branch, and we can collaborate to get things pulled into the main branch at a later date.

</p>
<h2><a id="user-content-license" class="anchor" href="#license" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>License</h2>
<p>We welcome contributions for all used of Py-ART provided the code can be distributed under the BSD 3-clause license.</p>
</article>
  </div>

  </div>
  
</div>



</html>

