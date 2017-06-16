





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
<h2><a id="user-content-code-example" class="anchor" href="#code-example" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Code Example</h2>
<p>Show what the library does as concisely as possible, developers should be able to figure out <strong>how</strong> your project solves their problem by looking at the code example. Make sure the API you are showing off is obvious, and that your code is short and concise.</p>
<h2><a id="user-content-motivation" class="anchor" href="#motivation" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Motivation</h2>
<p>A short description of the motivation behind the creation and maintenance of the project. This should explain <strong>why</strong> the project exists.</p>
<h2><a id="user-content-installation" class="anchor" href="#installation" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Installation</h2>
<p>Python packages Required:  pyart, numpy, scipy, optparse, netCDF4, datetime, pyproj.  Was built based on the Anaconda-2 system.

1.	To run the lvl-2 plotting, you can simply run the script. 
2.	To run the opaws2d.py script, you must first:
a.	fcompile_cressman.py – compiles the fortran cressman routine, assumes GNU compiler is installed before the Anaconda python was installed.  Note:  “conda install libgfortran” can be helpful.
b.	Once a “cressman.so” exists and can be loaded – opaws2d is ready to run
</p>
<h2><a id="user-content-api-reference" class="anchor" href="#api-reference" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>API Reference</h2>
<p>Depending on the size of the project, if it is small and simple enough the reference docs can be added to the README. For medium size to larger projects it is important to at least provide a link to where the API reference docs live.</p>
<h2><a id="user-content-tests" class="anchor" href="#tests" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Tests</h2>
<p>Describe and show how to run the tests with code examples.</p>
<p> To test the scripts:  cp from KDDC directory the file:  KDDC20160525_001527_V06.gz into the main directory.  Lvl2 files will be placed in a directory called “images”, and opaws2d files will be placed in a directory called “opaws_files”.  Plots of gridded superobbed fields (REF and VR) are placed in the main directory when created.<p>
<h2><a id="user-content-contributors" class="anchor" href="#contributors" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Contributors</h2>
<p>Let people know how they can dive into the project, include important links to things like issue trackers, irc, twitter accounts if applicable.</p>
<h2><a id="user-content-license" class="anchor" href="#license" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>License</h2>
<p>A short snippet describing the license (MIT, Apache, etc.)</p>
</article>
  </div>

  </div>
  
</div>


    <a name="comments"></a>
    <div class="discussion-timeline gist-discussion-timeline js-quote-selection-container ">
      <div class="js-discussion js-socket-channel" data-channel="marked-as-read:gist:1784669">
        

  
  <div class="timeline-comment-wrapper js-comment-container">

    

<div class="avatar-parent-child timeline-comment-avatar">
    <img alt="@ghost" class="avatar rounded-1" height="44" src="https://avatars1.githubusercontent.com/u/10137?v=3&amp;s=88" width="44" />

</div>



      
<div id="gistcomment-964964"
     class="comment previewable-edit js-comment js-task-list-container  timeline-comment js-reorderable-task-lists reorderable-task-lists "
     data-body-version="7950921677b54ed44e46a0a92c9f4e2a">

  
<div class="timeline-comment-header">
  <div class="timeline-comment-actions">


  </div>

    



  <h3 class="timeline-comment-header-text f5 text-normal">

    <strong>
        <a href="/ghost" class="author">ghost</a>
    </strong>

    commented

    <a href="#gistcomment-964964" class="timestamp"><relative-time datetime="2013-12-07T06:58:49Z">Dec 7, 2013</relative-time></a>


  </h3>
</div>


  <div class="edit-comment-hide">
    <table class="d-block">
      <tbody class="d-block">
        <tr class="d-block">
          <td class="d-block comment-body markdown-body  js-comment-body">
              <p>Thank you :)</p>
          </td>
        </tr>
      </tbody>
    </table>

  </div>

</div>

  </div>

  
  <div class="timeline-comment-wrapper js-comment-container">

    

<div class="avatar-parent-child timeline-comment-avatar">
    <a href="/aloisdg">
      <img alt="@aloisdg" class="avatar rounded-1" height="44" src="https://avatars0.githubusercontent.com/u/3449303?v=3&amp;s=88" width="44" />
    </a>

</div>



      
<div id="gistcomment-1175545"
     class="comment previewable-edit js-comment js-task-list-container  timeline-comment js-reorderable-task-lists reorderable-task-lists "
     data-body-version="11155d87837d268c6d3716e2e475a236">

  
<div class="timeline-comment-header">
  <div class="timeline-comment-actions">


  </div>

    



  <h3 class="timeline-comment-header-text f5 text-normal">

    <strong>
        <a href="/aloisdg" class="author">aloisdg</a>
        
    </strong>

    commented

    <a href="#gistcomment-1175545" class="timestamp"><relative-time datetime="2014-02-19T22:42:32Z">Feb 19, 2014</relative-time></a>


  </h3>
</div>


  <div class="edit-comment-hide">
    <table class="d-block">
      <tbody class="d-block">
        <tr class="d-block">
          <td class="d-block comment-body markdown-body  js-comment-body">
              <p>Thanks !</p>
          </td>
        </tr>
      </tbody>
    </table>

  </div>

</div>

  </div>

  
  <div class="timeline-comment-wrapper js-comment-container">

    

<div class="avatar-parent-child timeline-comment-avatar">
    <a href="/BrainCrumbz">
      <img alt="@BrainCrumbz" class="avatar rounded-1" height="44" src="https://avatars2.githubusercontent.com/u/3185573?v=3&amp;s=88" width="44" />
    </a>

</div>



      
<div id="gistcomment-1223491"
     class="comment previewable-edit js-comment js-task-list-container  timeline-comment js-reorderable-task-lists reorderable-task-lists "
     data-body-version="3c1c35c674e6aaa0fa1548ef40215bf9">

  
<div class="timeline-comment-header">
  <div class="timeline-comment-actions">


  </div>

    



  <h3 class="timeline-comment-header-text f5 text-normal">

    <strong>
        <a href="/BrainCrumbz" class="author">BrainCrumbz</a>
        
    </strong>

    commented

    <a href="#gistcomment-1223491" class="timestamp"><relative-time datetime="2014-05-06T16:27:18Z">May 6, 2014</relative-time></a>


  </h3>
</div>


  <div class="edit-comment-hide">
    <table class="d-block">
      <tbody class="d-block">
        <tr class="d-block">
          <td class="d-block comment-body markdown-body  js-comment-body">
              <p>Thank you! (...If I remember, you will not receive a notification for this)</p>
          </td>
        </tr>
      </tbody>
    </table>

  </div>

</div>

  </div>

  
  <div class="timeline-comment-wrapper js-comment-container">

    

<div class="avatar-parent-child timeline-comment-avatar">
    <a href="/Sovietaced">
      <img alt="@Sovietaced" class="avatar rounded-1" height="44" src="https://avatars1.githubusercontent.com/u/1274471?v=3&amp;s=88" width="44" />
    </a>

</div>



      
<div id="gistcomment-1408376"
     class="comment previewable-edit js-comment js-task-list-container  timeline-comment js-reorderable-task-lists reorderable-task-lists "
     data-body-version="80ce6f91c7fead37a752034c267678f9">

  
<div class="timeline-comment-header">
  <div class="timeline-comment-actions">


  </div>

    



  <h3 class="timeline-comment-header-text f5 text-normal">

    <strong>
        <a href="/Sovietaced" class="author">Sovietaced</a>
        
    </strong>

    commented

    <a href="#gistcomment-1408376" class="timestamp"><relative-time datetime="2015-03-08T08:35:20Z">Mar 8, 2015</relative-time></a>


  </h3>
</div>


  <div class="edit-comment-hide">
    <table class="d-block">
      <tbody class="d-block">
        <tr class="d-block">
          <td class="d-block comment-body markdown-body  js-comment-body">
              <p>Thank you!</p>
          </td>
        </tr>
      </tbody>
    </table>

  </div>

</div>

  </div>

  
  <div class="timeline-comment-wrapper js-comment-container">

    

<div class="avatar-parent-child timeline-comment-avatar">
    <a href="/carlosloslas">
      <img alt="@carlosloslas" class="avatar rounded-1" height="44" src="https://avatars3.githubusercontent.com/u/10100481?v=3&amp;s=88" width="44" />
    </a>

</div>



      
<div id="gistcomment-1413352"
     class="comment previewable-edit js-comment js-task-list-container  timeline-comment js-reorderable-task-lists reorderable-task-lists "
     data-body-version="96eabdabdcfaeb9da5c9f5976b560a11">

  
<div class="timeline-comment-header">
  <div class="timeline-comment-actions">


  </div>

    



  <h3 class="timeline-comment-header-text f5 text-normal">

    <strong>
        <a href="/carlosloslas" class="author">carlosloslas</a>
        
    </strong>

    commented

    <a href="#gistcomment-1413352" class="timestamp"><relative-time datetime="2015-03-15T20:23:31Z">Mar 15, 2015</relative-time></a>


  </h3>
</div>


  <div class="edit-comment-hide">
    <table class="d-block">
      <tbody class="d-block">
        <tr class="d-block">
          <td class="d-block comment-body markdown-body  js-comment-body">
              <p>Thanks very much for a great template!</p>
          </td>
        </tr>
      </tbody>
    </table>

  </div>

</div>

  </div>

  
  <div class="timeline-comment-wrapper js-comment-container">

    

<div class="avatar-parent-child timeline-comment-avatar">
    <a href="/angajime">
      <img alt="@angajime" class="avatar rounded-1" height="44" src="https://avatars0.githubusercontent.com/u/9084879?v=3&amp;s=88" width="44" />
    </a>

</div>



      
<div id="gistcomment-1435312"
     class="comment previewable-edit js-comment js-task-list-container  timeline-comment js-reorderable-task-lists reorderable-task-lists "
     data-body-version="eb648f170f9c5d1464bd9332272bf04b">

  
<div class="timeline-comment-header">
  <div class="timeline-comment-actions">


  </div>

    



  <h3 class="timeline-comment-header-text f5 text-normal">

    <strong>
        <a href="/angajime" class="author">angajime</a>
        
    </strong>

    commented

    <a href="#gistcomment-1435312" class="timestamp"><relative-time datetime="2015-04-17T09:44:49Z">Apr 17, 2015</relative-time></a>


  </h3>
</div>


  <div class="edit-comment-hide">
    <table class="d-block">
      <tbody class="d-block">
        <tr class="d-block">
          <td class="d-block comment-body markdown-body  js-comment-body">
              <p>Great template, thank you very much!</p>
          </td>
        </tr>
      </tbody>
    </table>

  </div>

</div>

  </div>

  
  <div class="timeline-comment-wrapper js-comment-container">

    

<div class="avatar-parent-child timeline-comment-avatar">
    <a href="/Plimsky">
      <img alt="@Plimsky" class="avatar rounded-1" height="44" src="https://avatars0.githubusercontent.com/u/1219936?v=3&amp;s=88" width="44" />
    </a>

</div>



      
<div id="gistcomment-1485508"
     class="comment previewable-edit js-comment js-task-list-container  timeline-comment js-reorderable-task-lists reorderable-task-lists "
     data-body-version="4badb31a141fad46c7f30a5f522aed3f">

  
<div class="timeline-comment-header">
  <div class="timeline-comment-actions">


  </div>

    



  <h3 class="timeline-comment-header-text f5 text-normal">

    <strong>
        <a href="/Plimsky" class="author">Plimsky</a>
        
    </strong>

    commented

    <a href="#gistcomment-1485508" class="timestamp"><relative-time datetime="2015-07-03T06:48:01Z">Jul 3, 2015</relative-time></a>


  </h3>
</div>


  <div class="edit-comment-hide">
    <table class="d-block">
      <tbody class="d-block">
        <tr class="d-block">
          <td class="d-block comment-body markdown-body  js-comment-body">
              <p>Nice ! Thanks :-D</p>
          </td>
        </tr>
      </tbody>
    </table>

  </div>

</div>

  </div>

  
  <div class="timeline-comment-wrapper js-comment-container">

    

<div class="avatar-parent-child timeline-comment-avatar">
    <a href="/rayfoss">
      <img alt="@rayfoss" class="avatar rounded-1" height="44" src="https://avatars0.githubusercontent.com/u/876076?v=3&amp;s=88" width="44" />
    </a>

</div>



      
<div id="gistcomment-1487776"
     class="comment previewable-edit js-comment js-task-list-container  timeline-comment js-reorderable-task-lists reorderable-task-lists "
     data-body-version="f6ec133000a732ca82e819358f19f1aa">

  
<div class="timeline-comment-header">
  <div class="timeline-comment-actions">


  </div>

    



  <h3 class="timeline-comment-header-text f5 text-normal">

    <strong>
        <a href="/rayfoss" class="author">rayfoss</a>
        
    </strong>

    commented

    <a href="#gistcomment-1487776" class="timestamp"><relative-time datetime="2015-07-07T16:10:49Z">Jul 7, 2015</relative-time></a>


  </h3>
</div>


  <div class="edit-comment-hide">
    <table class="d-block">
      <tbody class="d-block">
        <tr class="d-block">
          <td class="d-block comment-body markdown-body  js-comment-body">
              <p>Would be nice to have some more basic markdown in it.</p>
          </td>
        </tr>
      </tbody>
    </table>

  </div>

</div>

  </div>

  
  <div class="timeline-comment-wrapper js-comment-container">

    

<div class="avatar-parent-child timeline-comment-avatar">
    <a href="/ccywch">
      <img alt="@ccywch" class="avatar rounded-1" height="44" src="https://avatars2.githubusercontent.com/u/5518643?v=3&amp;s=88" width="44" />
    </a>

</div>



      
<div id="gistcomment-1574981"
     class="comment previewable-edit js-comment js-task-list-container  timeline-comment js-reorderable-task-lists reorderable-task-lists "
     data-body-version="d02374da413f8217ed516f1848af5507">

  
<div class="timeline-comment-header">
  <div class="timeline-comment-actions">


  </div>

    



  <h3 class="timeline-comment-header-text f5 text-normal">

    <strong>
        <a href="/ccywch" class="author">ccywch</a>
        
    </strong>

    commented

    <a href="#gistcomment-1574981" class="timestamp"><relative-time datetime="2015-09-16T09:23:17Z">Sep 16, 2015</relative-time></a>


  </h3>
</div>


  <div class="edit-comment-hide">
    <table class="d-block">
      <tbody class="d-block">
        <tr class="d-block">
          <td class="d-block comment-body markdown-body  js-comment-body">
              <p>Thanks a lot!</p>
          </td>
        </tr>
      </tbody>
    </table>

  </div>

</div>

  </div>

  
  <div class="timeline-comment-wrapper js-comment-container">

    

<div class="avatar-parent-child timeline-comment-avatar">
    <a href="/mitbal">
      <img alt="@mitbal" class="avatar rounded-1" height="44" src="https://avatars1.githubusercontent.com/u/326048?v=3&amp;s=88" width="44" />
    </a>

</div>



      
<div id="gistcomment-1631605"
     class="comment previewable-edit js-comment js-task-list-container  timeline-comment js-reorderable-task-lists reorderable-task-lists "
     data-body-version="315ec4e908f870789760764a26f7028a">

  
<div class="timeline-comment-header">
  <div class="timeline-comment-actions">


  </div>

    



  <h3 class="timeline-comment-header-text f5 text-normal">

    <strong>
        <a href="/mitbal" class="author">mitbal</a>
        
    </strong>

    commented

    <a href="#gistcomment-1631605" class="timestamp"><relative-time datetime="2015-11-27T07:55:47Z">Nov 27, 2015</relative-time></a>


  </h3>
</div>


  <div class="edit-comment-hide">
    <table class="d-block">
      <tbody class="d-block">
        <tr class="d-block">
          <td class="d-block comment-body markdown-body  js-comment-body">
              <p>This is helpful. Thank you</p>
          </td>
        </tr>
      </tbody>
    </table>

  </div>

</div>

  </div>

  
  <div class="timeline-comment-wrapper js-comment-container">

    

<div class="avatar-parent-child timeline-comment-avatar">
    <a href="/gkbluestocking">
      <img alt="@gkbluestocking" class="avatar rounded-1" height="44" src="https://avatars0.githubusercontent.com/u/10524699?v=3&amp;s=88" width="44" />
    </a>

</div>



      
<div id="gistcomment-1643678"
     class="comment previewable-edit js-comment js-task-list-container  timeline-comment js-reorderable-task-lists reorderable-task-lists "
     data-body-version="ce5403e7eddda50665e4daddc55dd50e">

  
<div class="timeline-comment-header">
  <div class="timeline-comment-actions">


  </div>

    



  <h3 class="timeline-comment-header-text f5 text-normal">

    <strong>
        <a href="/gkbluestocking" class="author">gkbluestocking</a>
        
    </strong>

    commented

    <a href="#gistcomment-1643678" class="timestamp"><relative-time datetime="2015-12-08T02:02:24Z">Dec 7, 2015</relative-time></a>


  </h3>
</div>


  <div class="edit-comment-hide">
    <table class="d-block">
      <tbody class="d-block">
        <tr class="d-block">
          <td class="d-block comment-body markdown-body  js-comment-body">
              <p>This is an excellent guide. Thank you.</p>
          </td>
        </tr>
      </tbody>
    </table>

  </div>

</div>

  </div>

  
  <div class="timeline-comment-wrapper js-comment-container">

    

<div class="avatar-parent-child timeline-comment-avatar">
    <a href="/colkito">
      <img alt="@colkito" class="avatar rounded-1" height="44" src="https://avatars0.githubusercontent.com/u/98502?v=3&amp;s=88" width="44" />
    </a>

</div>



      
<div id="gistcomment-1668515"
     class="comment previewable-edit js-comment js-task-list-container  timeline-comment js-reorderable-task-lists reorderable-task-lists "
     data-body-version="b45475bc517e442c6d7fa5b9fd6c731e">

  
<div class="timeline-comment-header">
  <div class="timeline-comment-actions">


  </div>

    



  <h3 class="timeline-comment-header-text f5 text-normal">

    <strong>
        <a href="/colkito" class="author">colkito</a>
        
    </strong>

    commented

    <a href="#gistcomment-1668515" class="timestamp"><relative-time datetime="2016-01-12T21:33:05Z">Jan 12, 2016</relative-time></a>


  </h3>
</div>


  <div class="edit-comment-hide">
    <table class="d-block">
      <tbody class="d-block">
        <tr class="d-block">
          <td class="d-block comment-body markdown-body  js-comment-body">
              <p>great! thanks!</p>
          </td>
        </tr>
      </tbody>
    </table>

  </div>

</div>

  </div>

  
  <div class="timeline-comment-wrapper js-comment-container">

    

<div class="avatar-parent-child timeline-comment-avatar">
    <a href="/sameerkhoja">
      <img alt="@sameerkhoja" class="avatar rounded-1" height="44" src="https://avatars0.githubusercontent.com/u/7923359?v=3&amp;s=88" width="44" />
    </a>

</div>



      
<div id="gistcomment-1668908"
     class="comment previewable-edit js-comment js-task-list-container  timeline-comment js-reorderable-task-lists reorderable-task-lists "
     data-body-version="673bc8787b7fb07a9964159620bb7530">

  
<div class="timeline-comment-header">
  <div class="timeline-comment-actions">


  </div>

    



  <h3 class="timeline-comment-header-text f5 text-normal">

    <strong>
        <a href="/sameerkhoja" class="author">sameerkhoja</a>
        
    </strong>

    commented

    <a href="#gistcomment-1668908" class="timestamp"><relative-time datetime="2016-01-13T08:59:44Z">Jan 13, 2016</relative-time></a>


  </h3>
</div>


  <div class="edit-comment-hide">
    <table class="d-block">
      <tbody class="d-block">
        <tr class="d-block">
          <td class="d-block comment-body markdown-body  js-comment-body">
              <p>Awesome, thanks!</p>
          </td>
        </tr>
      </tbody>
    </table>

  </div>

</div>

  </div>

  
  <div class="timeline-comment-wrapper js-comment-container">

    

<div class="avatar-parent-child timeline-comment-avatar">
    <a href="/KevDoy">
      <img alt="@KevDoy" class="avatar rounded-1" height="44" src="https://avatars1.githubusercontent.com/u/11251011?v=3&amp;s=88" width="44" />
    </a>

</div>



      
<div id="gistcomment-1672306"
     class="comment previewable-edit js-comment js-task-list-container  timeline-comment js-reorderable-task-lists reorderable-task-lists "
     data-body-version="198f301a87db8d27d634ee5810b0d525">

  
<div class="timeline-comment-header">
  <div class="timeline-comment-actions">


  </div>

    



  <h3 class="timeline-comment-header-text f5 text-normal">

    <strong>
        <a href="/KevDoy" class="author">KevDoy</a>
        
    </strong>

    commented

    <a href="#gistcomment-1672306" class="timestamp"><relative-time datetime="2016-01-17T21:45:54Z">Jan 17, 2016</relative-time></a>


  </h3>
</div>


  <div class="edit-comment-hide">
    <table class="d-block">
      <tbody class="d-block">
        <tr class="d-block">
          <td class="d-block comment-body markdown-body  js-comment-body">
              <p>This is great. Thank you!</p>
          </td>
        </tr>
      </tbody>
    </table>

  </div>

</div>

  </div>

  
  <div class="timeline-comment-wrapper js-comment-container">

    

<div class="avatar-parent-child timeline-comment-avatar">
    <a href="/Herm71">
      <img alt="@Herm71" class="avatar rounded-1" height="44" src="https://avatars1.githubusercontent.com/u/1000543?v=3&amp;s=88" width="44" />
    </a>

</div>



      
<div id="gistcomment-1676996"
     class="comment previewable-edit js-comment js-task-list-container  timeline-comment js-reorderable-task-lists reorderable-task-lists "
     data-body-version="ed42fcbbb3c4f90096e872edf636dbdc">

  
<div class="timeline-comment-header">
  <div class="timeline-comment-actions">


  </div>

    



  <h3 class="timeline-comment-header-text f5 text-normal">

    <strong>
        <a href="/Herm71" class="author">Herm71</a>
        
    </strong>

    commented

    <a href="#gistcomment-1676996" class="timestamp"><relative-time datetime="2016-01-21T22:10:24Z">Jan 21, 2016</relative-time></a>


  </h3>
</div>


  <div class="edit-comment-hide">
    <table class="d-block">
      <tbody class="d-block">
        <tr class="d-block">
          <td class="d-block comment-body markdown-body  js-comment-body">
              <p>Nice template, thanks!</p>
          </td>
        </tr>
      </tbody>
    </table>

  </div>

</div>

  </div>

  
  <div class="timeline-comment-wrapper js-comment-container">

    

<div class="avatar-parent-child timeline-comment-avatar">
    <a href="/Laicure">
      <img alt="@Laicure" class="avatar rounded-1" height="44" src="https://avatars2.githubusercontent.com/u/8619566?v=3&amp;s=88" width="44" />
    </a>

</div>



      
<div id="gistcomment-1679467"
     class="comment previewable-edit js-comment js-task-list-container  timeline-comment js-reorderable-task-lists reorderable-task-lists "
     data-body-version="09393f006a59f3219b4a02feb287c01e">

  
<div class="timeline-comment-header">
  <div class="timeline-comment-actions">


  </div>

    



  <h3 class="timeline-comment-header-text f5 text-normal">

    <strong>
        <a href="/Laicure" class="author">Laicure</a>
        
    </strong>

    commented

    <a href="#gistcomment-1679467" class="timestamp"><relative-time datetime="2016-01-25T16:47:13Z">Jan 25, 2016</relative-time></a>


  </h3>
</div>


  <div class="edit-comment-hide">
    <table class="d-block">
      <tbody class="d-block">
        <tr class="d-block">
          <td class="d-block comment-body markdown-body  js-comment-body">
              <p>Thanks! Nice template! &lt;3</p>
          </td>
        </tr>
      </tbody>
    </table>

  </div>

</div>

  </div>

  
  <div class="timeline-comment-wrapper js-comment-container">

    

<div class="avatar-parent-child timeline-comment-avatar">
    <a href="/priyankinfinnov">
      <img alt="@priyankinfinnov" class="avatar rounded-1" height="44" src="https://avatars3.githubusercontent.com/u/15610225?v=3&amp;s=88" width="44" />
    </a>

</div>



      
<div id="gistcomment-1691196"
     class="comment previewable-edit js-comment js-task-list-container  timeline-comment js-reorderable-task-lists reorderable-task-lists "
     data-body-version="71b0d0c413206b36791c5850e5e9c4fe">

  
<div class="timeline-comment-header">
  <div class="timeline-comment-actions">


  </div>

    



  <h3 class="timeline-comment-header-text f5 text-normal">

    <strong>
        <a href="/priyankinfinnov" class="author">priyankinfinnov</a>
        
    </strong>

    commented

    <a href="#gistcomment-1691196" class="timestamp"><relative-time datetime="2016-02-07T09:52:49Z">Feb 7, 2016</relative-time></a>


  </h3>
</div>


  <div class="edit-comment-hide">
    <table class="d-block">
      <tbody class="d-block">
        <tr class="d-block">
          <td class="d-block comment-body markdown-body  js-comment-body">
              <p>nice</p>
          </td>
        </tr>
      </tbody>
    </table>

  </div>

</div>

  </div>

  
  <div class="timeline-comment-wrapper js-comment-container">

    

<div class="avatar-parent-child timeline-comment-avatar">
    <a href="/rohit2389">
      <img alt="@rohit2389" class="avatar rounded-1" height="44" src="https://avatars1.githubusercontent.com/u/13431053?v=3&amp;s=88" width="44" />
    </a>

</div>



      
<div id="gistcomment-1703794"
     class="comment previewable-edit js-comment js-task-list-container  timeline-comment js-reorderable-task-lists reorderable-task-lists "
     data-body-version="17f624fab96356487b99999d3e245287">

  
<div class="timeline-comment-header">
  <div class="timeline-comment-actions">


  </div>

    



  <h3 class="timeline-comment-header-text f5 text-normal">

    <strong>
        <a href="/rohit2389" class="author">rohit2389</a>
        
    </strong>

    commented

    <a href="#gistcomment-1703794" class="timestamp"><relative-time datetime="2016-02-22T07:10:39Z">Feb 22, 2016</relative-time></a>


  </h3>
</div>


  <div class="edit-comment-hide">
    <table class="d-block">
      <tbody class="d-block">
        <tr class="d-block">
          <td class="d-block comment-body markdown-body  js-comment-body">
              <p>Thanks a lot &lt;3</p>
          </td>
        </tr>
      </tbody>
    </table>

  </div>

</div>

  </div>

  
  <div class="timeline-comment-wrapper js-comment-container">

    

<div class="avatar-parent-child timeline-comment-avatar">
    <a href="/uilianries">
      <img alt="@uilianries" class="avatar rounded-1" height="44" src="https://avatars2.githubusercontent.com/u/4870173?v=3&amp;s=88" width="44" />
    </a>

</div>



      
<div id="gistcomment-1716294"
     class="comment previewable-edit js-comment js-task-list-container  timeline-comment js-reorderable-task-lists reorderable-task-lists "
     data-body-version="653362502bc91a4fae9d7c9e1fea852f">

  
<div class="timeline-comment-header">
  <div class="timeline-comment-actions">


  </div>

    



  <h3 class="timeline-comment-header-text f5 text-normal">

    <strong>
        <a href="/uilianries" class="author">uilianries</a>
        
    </strong>

    commented

    <a href="#gistcomment-1716294" class="timestamp"><relative-time datetime="2016-03-06T15:07:27Z">Mar 6, 2016</relative-time></a>


  </h3>
</div>


  <div class="edit-comment-hide">
    <table class="d-block">
      <tbody class="d-block">
        <tr class="d-block">
          <td class="d-block comment-body markdown-body  js-comment-body">
              <p>Really useful! Tks!</p>
          </td>
        </tr>
      </tbody>
    </table>

  </div>

</div>

  </div>

  
  <div class="timeline-comment-wrapper js-comment-container">

    

<div class="avatar-parent-child timeline-comment-avatar">
    <a href="/XiaoZYang">
      <img alt="@XiaoZYang" class="avatar rounded-1" height="44" src="https://avatars1.githubusercontent.com/u/8848479?v=3&amp;s=88" width="44" />
    </a>

</div>



      
<div id="gistcomment-1745350"
     class="comment previewable-edit js-comment js-task-list-container  timeline-comment js-reorderable-task-lists reorderable-task-lists "
     data-body-version="11155d87837d268c6d3716e2e475a236">

  
<div class="timeline-comment-header">
  <div class="timeline-comment-actions">


  </div>

    



  <h3 class="timeline-comment-header-text f5 text-normal">

    <strong>
        <a href="/XiaoZYang" class="author">XiaoZYang</a>
        
    </strong>

    commented

    <a href="#gistcomment-1745350" class="timestamp"><relative-time datetime="2016-04-08T02:14:28Z">Apr 7, 2016</relative-time></a>


  </h3>
</div>


  <div class="edit-comment-hide">
    <table class="d-block">
      <tbody class="d-block">
        <tr class="d-block">
          <td class="d-block comment-body markdown-body  js-comment-body">
              <p>Thanks !</p>
          </td>
        </tr>
      </tbody>
    </table>

  </div>

</div>

  </div>

  
  <div class="timeline-comment-wrapper js-comment-container">

    

<div class="avatar-parent-child timeline-comment-avatar">
    <a href="/cAtilre">
      <img alt="@cAtilre" class="avatar rounded-1" height="44" src="https://avatars1.githubusercontent.com/u/13943873?v=3&amp;s=88" width="44" />
    </a>

</div>



      
<div id="gistcomment-1756762"
     class="comment previewable-edit js-comment js-task-list-container  timeline-comment js-reorderable-task-lists reorderable-task-lists "
     data-body-version="874bb14ea1e443a5305a2b97ef08466d">

  
<div class="timeline-comment-header">
  <div class="timeline-comment-actions">


  </div>

    



  <h3 class="timeline-comment-header-text f5 text-normal">

    <strong>
        <a href="/cAtilre" class="author">cAtilre</a>
        
    </strong>

    commented

    <a href="#gistcomment-1756762" class="timestamp"><relative-time datetime="2016-04-19T21:20:09Z">Apr 19, 2016</relative-time></a>


  </h3>
</div>


  <div class="edit-comment-hide">
    <table class="d-block">
      <tbody class="d-block">
        <tr class="d-block">
          <td class="d-block comment-body markdown-body  js-comment-body">
              <p>This is great, thanks.</p>
          </td>
        </tr>
      </tbody>
    </table>

  </div>

</div>

  </div>

  
  <div class="timeline-comment-wrapper js-comment-container">

    

<div class="avatar-parent-child timeline-comment-avatar">
    <a href="/asikhalaban">
      <img alt="@asikhalaban" class="avatar rounded-1" height="44" src="https://avatars1.githubusercontent.com/u/5946339?v=3&amp;s=88" width="44" />
    </a>

</div>



      
<div id="gistcomment-1758100"
     class="comment previewable-edit js-comment js-task-list-container  timeline-comment js-reorderable-task-lists reorderable-task-lists "
     data-body-version="83bab6376450f9f9500735fa437998d7">

  
<div class="timeline-comment-header">
  <div class="timeline-comment-actions">


  </div>

    



  <h3 class="timeline-comment-header-text f5 text-normal">

    <strong>
        <a href="/asikhalaban" class="author">asikhalaban</a>
        
    </strong>

    commented

    <a href="#gistcomment-1758100" class="timestamp"><relative-time datetime="2016-04-21T04:30:33Z">Apr 20, 2016</relative-time></a>


  </h3>
</div>


  <div class="edit-comment-hide">
    <table class="d-block">
      <tbody class="d-block">
        <tr class="d-block">
          <td class="d-block comment-body markdown-body  js-comment-body">
              <p>Nice job!</p>
          </td>
        </tr>
      </tbody>
    </table>

  </div>

</div>

  </div>

  
  <div class="timeline-comment-wrapper js-comment-container">

    

<div class="avatar-parent-child timeline-comment-avatar">
    <a href="/Karan-nassa">
      <img alt="@Karan-nassa" class="avatar rounded-1" height="44" src="https://avatars0.githubusercontent.com/u/15867097?v=3&amp;s=88" width="44" />
    </a>

</div>



      
<div id="gistcomment-1767759"
     class="comment previewable-edit js-comment js-task-list-container  timeline-comment js-reorderable-task-lists reorderable-task-lists "
     data-body-version="7389d39ff3ad29e869d0de44d0c84668">

  
<div class="timeline-comment-header">
  <div class="timeline-comment-actions">


  </div>

    



  <h3 class="timeline-comment-header-text f5 text-normal">

    <strong>
        <a href="/Karan-nassa" class="author">Karan-nassa</a>
        
    </strong>

    commented

    <a href="#gistcomment-1767759" class="timestamp"><relative-time datetime="2016-05-03T13:24:37Z">May 3, 2016</relative-time></a>


  </h3>
</div>


  <div class="edit-comment-hide">
    <table class="d-block">
      <tbody class="d-block">
        <tr class="d-block">
          <td class="d-block comment-body markdown-body  js-comment-body">
              <p>Really nice.</p>
          </td>
        </tr>
      </tbody>
    </table>

  </div>

</div>

  </div>

  
  <div class="timeline-comment-wrapper js-comment-container">

    

<div class="avatar-parent-child timeline-comment-avatar">
    <a href="/AndrewDawes">
      <img alt="@AndrewDawes" class="avatar rounded-1" height="44" src="https://avatars3.githubusercontent.com/u/19176869?v=3&amp;s=88" width="44" />
    </a>

</div>



      
<div id="gistcomment-1769176"
     class="comment previewable-edit js-comment js-task-list-container  timeline-comment js-reorderable-task-lists reorderable-task-lists "
     data-body-version="2e4dd6c49a3577104d748e8b5ccaa9d8">

  
<div class="timeline-comment-header">
  <div class="timeline-comment-actions">


  </div>

    



  <h3 class="timeline-comment-header-text f5 text-normal">

    <strong>
        <a href="/AndrewDawes" class="author">AndrewDawes</a>
        
    </strong>

    commented

    <a href="#gistcomment-1769176" class="timestamp"><relative-time datetime="2016-05-04T20:55:35Z">May 4, 2016</relative-time></a>


  </h3>
</div>


  <div class="edit-comment-hide">
    <table class="d-block">
      <tbody class="d-block">
        <tr class="d-block">
          <td class="d-block comment-body markdown-body  js-comment-body">
              <p>Thanks very much.</p>
          </td>
        </tr>
      </tbody>
    </table>

  </div>

</div>

  </div>

  
  <div class="timeline-comment-wrapper js-comment-container">

    

<div class="avatar-parent-child timeline-comment-avatar">
    <a href="/douglasdeodato">
      <img alt="@douglasdeodato" class="avatar rounded-1" height="44" src="https://avatars3.githubusercontent.com/u/993318?v=3&amp;s=88" width="44" />
    </a>

</div>



      
<div id="gistcomment-1772879"
     class="comment previewable-edit js-comment js-task-list-container  timeline-comment js-reorderable-task-lists reorderable-task-lists "
     data-body-version="bd57f98b7eeff990d174dda96674d4b1">

  
<div class="timeline-comment-header">
  <div class="timeline-comment-actions">


  </div>

    



  <h3 class="timeline-comment-header-text f5 text-normal">

    <strong>
        <a href="/douglasdeodato" class="author">douglasdeodato</a>
        
    </strong>

    commented

    <a href="#gistcomment-1772879" class="timestamp"><relative-time datetime="2016-05-09T14:59:33Z">May 9, 2016</relative-time></a>


  </h3>
</div>


  <div class="edit-comment-hide">
    <table class="d-block">
      <tbody class="d-block">
        <tr class="d-block">
          <td class="d-block comment-body markdown-body  js-comment-body">
              <p>thanks</p>
          </td>
        </tr>
      </tbody>
    </table>

  </div>

</div>

  </div>

  
  <div class="timeline-comment-wrapper js-comment-container">

    

<div class="avatar-parent-child timeline-comment-avatar">
    <a href="/IrfaanKamo">
      <img alt="@IrfaanKamo" class="avatar rounded-1" height="44" src="https://avatars0.githubusercontent.com/u/11619808?v=3&amp;s=88" width="44" />
    </a>

</div>



      
<div id="gistcomment-1777122"
     class="comment previewable-edit js-comment js-task-list-container  timeline-comment js-reorderable-task-lists reorderable-task-lists "
     data-body-version="bb3667d3461fd8ce506c5cd37ba54c1e">

  
<div class="timeline-comment-header">
  <div class="timeline-comment-actions">


  </div>

    



  <h3 class="timeline-comment-header-text f5 text-normal">

    <strong>
        <a href="/IrfaanKamo" class="author">IrfaanKamo</a>
        
    </strong>

    commented

    <a href="#gistcomment-1777122" class="timestamp"><relative-time datetime="2016-05-13T19:26:49Z">May 13, 2016</relative-time></a>


  </h3>
</div>


  <div class="edit-comment-hide">
    <table class="d-block">
      <tbody class="d-block">
        <tr class="d-block">
          <td class="d-block comment-body markdown-body  js-comment-body">
              <p>Thanks, exactly what I was looking for!</p>
          </td>
        </tr>
      </tbody>
    </table>

  </div>

</div>

  </div>

  
  <div class="timeline-comment-wrapper js-comment-container">

    

<div class="avatar-parent-child timeline-comment-avatar">
    <a href="/S1v4">
      <img alt="@S1v4" class="avatar rounded-1" height="44" src="https://avatars2.githubusercontent.com/u/15009110?v=3&amp;s=88" width="44" />
    </a>

</div>



      
<div id="gistcomment-1777708"
     class="comment previewable-edit js-comment js-task-list-container  timeline-comment js-reorderable-task-lists reorderable-task-lists "
     data-body-version="80ce6f91c7fead37a752034c267678f9">

  
<div class="timeline-comment-header">
  <div class="timeline-comment-actions">


  </div>

    



  <h3 class="timeline-comment-header-text f5 text-normal">

    <strong>
        <a href="/S1v4" class="author">S1v4</a>
        
    </strong>

    commented

    <a href="#gistcomment-1777708" class="timestamp"><relative-time datetime="2016-05-14T19:19:42Z">May 14, 2016</relative-time></a>


  </h3>
</div>


  <div class="edit-comment-hide">
    <table class="d-block">
      <tbody class="d-block">
        <tr class="d-block">
          <td class="d-block comment-body markdown-body  js-comment-body">
              <p>Thank you!</p>
          </td>
        </tr>
      </tbody>
    </table>

  </div>

</div>

  </div>

  
  <div class="timeline-comment-wrapper js-comment-container">

    

<div class="avatar-parent-child timeline-comment-avatar">
    <a href="/kapoor-rakshit">
      <img alt="@kapoor-rakshit" class="avatar rounded-1" height="44" src="https://avatars0.githubusercontent.com/u/16061059?v=3&amp;s=88" width="44" />
    </a>

</div>



      
<div id="gistcomment-1778448"
     class="comment previewable-edit js-comment js-task-list-container  timeline-comment js-reorderable-task-lists reorderable-task-lists "
     data-body-version="5f7e6de099fd22d5c82e152dd521c8be">

  
<div class="timeline-comment-header">
  <div class="timeline-comment-actions">


  </div>

    



  <h3 class="timeline-comment-header-text f5 text-normal">

    <strong>
        <a href="/kapoor-rakshit" class="author">kapoor-rakshit</a>
        
    </strong>

    commented

    <a href="#gistcomment-1778448" class="timestamp"><relative-time datetime="2016-05-16T07:13:21Z">May 16, 2016</relative-time></a>


  </h3>
</div>


  <div class="edit-comment-hide">
    <table class="d-block">
      <tbody class="d-block">
        <tr class="d-block">
          <td class="d-block comment-body markdown-body  js-comment-body">
              <p>How should i add a screenshot of my code , so that it gives an example how my code works ?</p>
          </td>
        </tr>
      </tbody>
    </table>

  </div>

</div>

  </div>

  
  <div class="timeline-comment-wrapper js-comment-container">

    

<div class="avatar-parent-child timeline-comment-avatar">
    <a href="/romamaslennikov">
      <img alt="@romamaslennikov" class="avatar rounded-1" height="44" src="https://avatars1.githubusercontent.com/u/17795655?v=3&amp;s=88" width="44" />
    </a>

</div>



      
<div id="gistcomment-1779653"
     class="comment previewable-edit js-comment js-task-list-container  timeline-comment js-reorderable-task-lists reorderable-task-lists "
     data-body-version="019bed3975f2d1fb0cb09f6d7f928c21">

  
<div class="timeline-comment-header">
  <div class="timeline-comment-actions">


  </div>

    



  <h3 class="timeline-comment-header-text f5 text-normal">

    <strong>
        <a href="/romamaslennikov" class="author">romamaslennikov</a>
        
    </strong>

    commented

    <a href="#gistcomment-1779653" class="timestamp"><relative-time datetime="2016-05-17T14:25:07Z">May 17, 2016</relative-time></a>


  </h3>
</div>


  <div class="edit-comment-hide">
    <table class="d-block">
      <tbody class="d-block">
        <tr class="d-block">
          <td class="d-block comment-body markdown-body  js-comment-body">
              <p>o ya ya</p>
          </td>
        </tr>
      </tbody>
    </table>

  </div>

</div>

  </div>

  
  <div class="timeline-comment-wrapper js-comment-container">

    

<div class="avatar-parent-child timeline-comment-avatar">
    <a href="/romamaslennikov">
      <img alt="@romamaslennikov" class="avatar rounded-1" height="44" src="https://avatars1.githubusercontent.com/u/17795655?v=3&amp;s=88" width="44" />
    </a>

</div>



      
<div id="gistcomment-1779654"
     class="comment previewable-edit js-comment js-task-list-container  timeline-comment js-reorderable-task-lists reorderable-task-lists "
     data-body-version="bd57f98b7eeff990d174dda96674d4b1">

  
<div class="timeline-comment-header">
  <div class="timeline-comment-actions">


  </div>

    



  <h3 class="timeline-comment-header-text f5 text-normal">

    <strong>
        <a href="/romamaslennikov" class="author">romamaslennikov</a>
        
    </strong>

    commented

    <a href="#gistcomment-1779654" class="timestamp"><relative-time datetime="2016-05-17T14:25:19Z">May 17, 2016</relative-time></a>


  </h3>
</div>


  <div class="edit-comment-hide">
    <table class="d-block">
      <tbody class="d-block">
        <tr class="d-block">
          <td class="d-block comment-body markdown-body  js-comment-body">
              <p>thanks</p>
          </td>
        </tr>
      </tbody>
    </table>

  </div>

</div>

  </div>

  
  <div class="timeline-comment-wrapper js-comment-container">

    

<div class="avatar-parent-child timeline-comment-avatar">
    <a href="/abjzb70">
      <img alt="@abjzb70" class="avatar rounded-1" height="44" src="https://avatars3.githubusercontent.com/u/12211748?v=3&amp;s=88" width="44" />
    </a>

</div>



      
<div id="gistcomment-1783684"
     class="comment previewable-edit js-comment js-task-list-container  timeline-comment js-reorderable-task-lists reorderable-task-lists "
     data-body-version="c8fadb1ea6432892a4d0293f4a0477ad">

  
<div class="timeline-comment-header">
  <div class="timeline-comment-actions">


  </div>

    



  <h3 class="timeline-comment-header-text f5 text-normal">

    <strong>
        <a href="/abjzb70" class="author">abjzb70</a>
        
    </strong>

    commented

    <a href="#gistcomment-1783684" class="timestamp"><relative-time datetime="2016-05-22T08:07:50Z">May 22, 2016</relative-time></a>


  </h3>
</div>


  <div class="edit-comment-hide">
    <table class="d-block">
      <tbody class="d-block">
        <tr class="d-block">
          <td class="d-block comment-body markdown-body  js-comment-body">
              <p>thanks!!!</p>
          </td>
        </tr>
      </tbody>
    </table>

  </div>

</div>

  </div>

  
  <div class="timeline-comment-wrapper js-comment-container">

    

<div class="avatar-parent-child timeline-comment-avatar">
    <a href="/alissaom">
      <img alt="@alissaom" class="avatar rounded-1" height="44" src="https://avatars1.githubusercontent.com/u/14224029?v=3&amp;s=88" width="44" />
    </a>

</div>



      
<div id="gistcomment-1787320"
     class="comment previewable-edit js-comment js-task-list-container  timeline-comment js-reorderable-task-lists reorderable-task-lists "
     data-body-version="80ce6f91c7fead37a752034c267678f9">

  
<div class="timeline-comment-header">
  <div class="timeline-comment-actions">


  </div>

    



  <h3 class="timeline-comment-header-text f5 text-normal">

    <strong>
        <a href="/alissaom" class="author">alissaom</a>
        
    </strong>

    commented

    <a href="#gistcomment-1787320" class="timestamp"><relative-time datetime="2016-05-26T13:41:05Z">May 26, 2016</relative-time></a>


  </h3>
</div>


  <div class="edit-comment-hide">
    <table class="d-block">
      <tbody class="d-block">
        <tr class="d-block">
          <td class="d-block comment-body markdown-body  js-comment-body">
              <p>Thank you!</p>
          </td>
        </tr>
      </tbody>
    </table>

  </div>

</div>

  </div>

  
  <div class="timeline-comment-wrapper js-comment-container">

    

<div class="avatar-parent-child timeline-comment-avatar">
    <a href="/boompah">
      <img alt="@boompah" class="avatar rounded-1" height="44" src="https://avatars2.githubusercontent.com/u/855296?v=3&amp;s=88" width="44" />
    </a>

</div>



      
<div id="gistcomment-1789041"
     class="comment previewable-edit js-comment js-task-list-container  timeline-comment js-reorderable-task-lists reorderable-task-lists "
     data-body-version="21c91f1b16e2feb39048899c1abbf600">

  
<div class="timeline-comment-header">
  <div class="timeline-comment-actions">


  </div>

    



  <h3 class="timeline-comment-header-text f5 text-normal">

    <strong>
        <a href="/boompah" class="author">boompah</a>
        
    </strong>

    commented

    <a href="#gistcomment-1789041" class="timestamp"><relative-time datetime="2016-05-28T17:07:43Z">May 28, 2016</relative-time></a>


  </h3>
</div>


  <div class="edit-comment-hide">
    <table class="d-block">
      <tbody class="d-block">
        <tr class="d-block">
          <td class="d-block comment-body markdown-body  js-comment-body">
              <p>Thank you so much, going to start using this right now! :)</p>
          </td>
        </tr>
      </tbody>
    </table>

  </div>

</div>

  </div>

  
  <div class="timeline-comment-wrapper js-comment-container">

    

<div class="avatar-parent-child timeline-comment-avatar">
    <a href="/shyamalmunshi">
      <img alt="@shyamalmunshi" class="avatar rounded-1" height="44" src="https://avatars0.githubusercontent.com/u/17392157?v=3&amp;s=88" width="44" />
    </a>

</div>



      
<div id="gistcomment-1802467"
     class="comment previewable-edit js-comment js-task-list-container  timeline-comment js-reorderable-task-lists reorderable-task-lists "
     data-body-version="8357d8883aa9b8d6e97bdbff457f20c2">

  
<div class="timeline-comment-header">
  <div class="timeline-comment-actions">


  </div>

    



  <h3 class="timeline-comment-header-text f5 text-normal">

    <strong>
        <a href="/shyamalmunshi" class="author">shyamalmunshi</a>
        
    </strong>

    commented

    <a href="#gistcomment-1802467" class="timestamp"><relative-time datetime="2016-06-15T21:07:36Z">Jun 15, 2016</relative-time></a>


  </h3>
</div>


  <div class="edit-comment-hide">
    <table class="d-block">
      <tbody class="d-block">
        <tr class="d-block">
          <td class="d-block comment-body markdown-body  js-comment-body">
              <p>Thank you, this was very helpful!</p>
          </td>
        </tr>
      </tbody>
    </table>

  </div>

</div>

  </div>

  
  <div class="timeline-comment-wrapper js-comment-container">

    

<div class="avatar-parent-child timeline-comment-avatar">
    <a href="/ox-harris">
      <img alt="@ox-harris" class="avatar rounded-1" height="44" src="https://avatars0.githubusercontent.com/u/13555392?v=3&amp;s=88" width="44" />
    </a>

</div>



      
<div id="gistcomment-1816186"
     class="comment previewable-edit js-comment js-task-list-container  timeline-comment js-reorderable-task-lists reorderable-task-lists "
     data-body-version="658d98a85f26f9950e106d950e7ad6c7">

  
<div class="timeline-comment-header">
  <div class="timeline-comment-actions">


  </div>

    



  <h3 class="timeline-comment-header-text f5 text-normal">

    <strong>
        <a href="/ox-harris" class="author">ox-harris</a>
        
    </strong>

    commented

    <a href="#gistcomment-1816186" class="timestamp"><relative-time datetime="2016-07-01T16:47:15Z">Jul 1, 2016</relative-time></a>


  </h3>
</div>


  <div class="edit-comment-hide">
    <table class="d-block">
      <tbody class="d-block">
        <tr class="d-block">
          <td class="d-block comment-body markdown-body  js-comment-body">
              <p>What the beginner me really needed</p>
          </td>
        </tr>
      </tbody>
    </table>

  </div>

</div>

  </div>

  
  <div class="timeline-comment-wrapper js-comment-container">

    

<div class="avatar-parent-child timeline-comment-avatar">
    <a href="/myson1515">
      <img alt="@myson1515" class="avatar rounded-1" height="44" src="https://avatars3.githubusercontent.com/u/15943990?v=3&amp;s=88" width="44" />
    </a>

</div>



      
<div id="gistcomment-1832277"
     class="comment previewable-edit js-comment js-task-list-container  timeline-comment js-reorderable-task-lists reorderable-task-lists "
     data-body-version="b526bb2b2f5a099c0525d82593d62d7d">

  
<div class="timeline-comment-header">
  <div class="timeline-comment-actions">


  </div>

    



  <h3 class="timeline-comment-header-text f5 text-normal">

    <strong>
        <a href="/myson1515" class="author">myson1515</a>
        
    </strong>

    commented

    <a href="#gistcomment-1832277" class="timestamp"><relative-time datetime="2016-07-23T01:56:11Z">Jul 22, 2016</relative-time></a>


  </h3>
</div>


  <div class="edit-comment-hide">
    <table class="d-block">
      <tbody class="d-block">
        <tr class="d-block">
          <td class="d-block comment-body markdown-body  js-comment-body">
              <p>thanks bro!</p>
          </td>
        </tr>
      </tbody>
    </table>

  </div>

</div>

  </div>

  
  <div class="timeline-comment-wrapper js-comment-container">

    

<div class="avatar-parent-child timeline-comment-avatar">
    <a href="/sfilhu">
      <img alt="@sfilhu" class="avatar rounded-1" height="44" src="https://avatars3.githubusercontent.com/u/2460421?v=3&amp;s=88" width="44" />
    </a>

</div>



      
<div id="gistcomment-1853872"
     class="comment previewable-edit js-comment js-task-list-container  timeline-comment js-reorderable-task-lists reorderable-task-lists "
     data-body-version="d537ecc74a21d5ec1f9d8e995f8c8da3">

  
<div class="timeline-comment-header">
  <div class="timeline-comment-actions">


  </div>

    



  <h3 class="timeline-comment-header-text f5 text-normal">

    <strong>
        <a href="/sfilhu" class="author">sfilhu</a>
        
    </strong>

    commented

    <a href="#gistcomment-1853872" class="timestamp"><relative-time datetime="2016-08-20T00:29:47Z">Aug 19, 2016</relative-time></a>


  </h3>
</div>


  <div class="edit-comment-hide">
    <table class="d-block">
      <tbody class="d-block">
        <tr class="d-block">
          <td class="d-block comment-body markdown-body  js-comment-body">
              <p>Thank's for template man! But, if I  to want write a code, what I do?</p>
          </td>
        </tr>
      </tbody>
    </table>

  </div>

</div>

  </div>

  
  <div class="timeline-comment-wrapper js-comment-container">

    

<div class="avatar-parent-child timeline-comment-avatar">
    <a href="/zarque">
      <img alt="@zarque" class="avatar rounded-1" height="44" src="https://avatars1.githubusercontent.com/u/1884246?v=3&amp;s=88" width="44" />
    </a>

</div>



      
<div id="gistcomment-1854021"
     class="comment previewable-edit js-comment js-task-list-container  timeline-comment js-reorderable-task-lists reorderable-task-lists "
     data-body-version="2001727c1ed66a4499e454b14d761bbc">

  
<div class="timeline-comment-header">
  <div class="timeline-comment-actions">


  </div>

    



  <h3 class="timeline-comment-header-text f5 text-normal">

    <strong>
        <a href="/zarque" class="author">zarque</a>
        
    </strong>

    commented

    <a href="#gistcomment-1854021" class="timestamp"><relative-time datetime="2016-08-20T12:42:15Z">Aug 20, 2016</relative-time></a>


  </h3>
</div>


  <div class="edit-comment-hide">
    <table class="d-block">
      <tbody class="d-block">
        <tr class="d-block">
          <td class="d-block comment-body markdown-body  js-comment-body">
              <p>merci</p>
          </td>
        </tr>
      </tbody>
    </table>

  </div>

</div>

  </div>

  
  <div class="timeline-comment-wrapper js-comment-container">

    

<div class="avatar-parent-child timeline-comment-avatar">
    <a href="/khrishan">
      <img alt="@khrishan" class="avatar rounded-1" height="44" src="https://avatars1.githubusercontent.com/u/9061602?v=3&amp;s=88" width="44" />
    </a>

</div>



      
<div id="gistcomment-1858723"
     class="comment previewable-edit js-comment js-task-list-container  timeline-comment js-reorderable-task-lists reorderable-task-lists "
     data-body-version="a99abbcda101f54695087ed89dbdf7b2">

  
<div class="timeline-comment-header">
  <div class="timeline-comment-actions">


  </div>

    



  <h3 class="timeline-comment-header-text f5 text-normal">

    <strong>
        <a href="/khrishan" class="author">khrishan</a>
        
    </strong>

    commented

    <a href="#gistcomment-1858723" class="timestamp"><relative-time datetime="2016-08-26T10:21:27Z">Aug 26, 2016</relative-time></a>


  </h3>
</div>


  <div class="edit-comment-hide">
    <table class="d-block">
      <tbody class="d-block">
        <tr class="d-block">
          <td class="d-block comment-body markdown-body  js-comment-body">
              <p>Thanks for this template :) Much Appreciated</p>
          </td>
        </tr>
      </tbody>
    </table>

  </div>

</div>

  </div>

  
  <div class="timeline-comment-wrapper js-comment-container">

    

<div class="avatar-parent-child timeline-comment-avatar">
    <a href="/sebacruzd">
      <img alt="@sebacruzd" class="avatar rounded-1" height="44" src="https://avatars0.githubusercontent.com/u/14894992?v=3&amp;s=88" width="44" />
    </a>

</div>



      
<div id="gistcomment-1859792"
     class="comment previewable-edit js-comment js-task-list-container  timeline-comment js-reorderable-task-lists reorderable-task-lists "
     data-body-version="dcb073da06e80a80da7314e6f96647fb">

  
<div class="timeline-comment-header">
  <div class="timeline-comment-actions">


  </div>

    



  <h3 class="timeline-comment-header-text f5 text-normal">

    <strong>
        <a href="/sebacruzd" class="author">sebacruzd</a>
        
    </strong>

    commented

    <a href="#gistcomment-1859792" class="timestamp"><relative-time datetime="2016-08-28T04:13:49Z">Aug 27, 2016</relative-time></a>


  </h3>
</div>


  <div class="edit-comment-hide">
    <table class="d-block">
      <tbody class="d-block">
        <tr class="d-block">
          <td class="d-block comment-body markdown-body  js-comment-body">
              <p><a href="https://github.com/sfilhu" class="user-mention">@sfilhu</a><br>
You have you write ``` at the start and end of that code and that'll do.</p>
          </td>
        </tr>
      </tbody>
    </table>

  </div>

</div>

  </div>

  
  <div class="timeline-comment-wrapper js-comment-container">

    

<div class="avatar-parent-child timeline-comment-avatar">
    <a href="/Arthurturtle">
      <img alt="@Arthurturtle" class="avatar rounded-1" height="44" src="https://avatars3.githubusercontent.com/u/22332536?v=3&amp;s=88" width="44" />
    </a>

</div>



      
<div id="gistcomment-1892569"
     class="comment previewable-edit js-comment js-task-list-container  timeline-comment js-reorderable-task-lists reorderable-task-lists "
     data-body-version="59db042ae9f334844ed508d6a57158b5">

  
<div class="timeline-comment-header">
  <div class="timeline-comment-actions">


  </div>

    



  <h3 class="timeline-comment-header-text f5 text-normal">

    <strong>
        <a href="/Arthurturtle" class="author">Arthurturtle</a>
        
    </strong>

    commented

    <a href="#gistcomment-1892569" class="timestamp"><relative-time datetime="2016-10-07T17:36:32Z">Oct 7, 2016</relative-time></a>


  </h3>
</div>


  <div class="edit-comment-hide">
    <table class="d-block">
      <tbody class="d-block">
        <tr class="d-block">
          <td class="d-block comment-body markdown-body  js-comment-body">
              <p>PFUDOR</p>
          </td>
        </tr>
      </tbody>
    </table>

  </div>

</div>

  </div>

  
  <div class="timeline-comment-wrapper js-comment-container">

    

<div class="avatar-parent-child timeline-comment-avatar">
    <a href="/rojcosta">
      <img alt="@rojcosta" class="avatar rounded-1" height="44" src="https://avatars1.githubusercontent.com/u/22751339?v=3&amp;s=88" width="44" />
    </a>

</div>



      
<div id="gistcomment-1900314"
     class="comment previewable-edit js-comment js-task-list-container  timeline-comment js-reorderable-task-lists reorderable-task-lists "
     data-body-version="80ce6f91c7fead37a752034c267678f9">

  
<div class="timeline-comment-header">
  <div class="timeline-comment-actions">


  </div>

    



  <h3 class="timeline-comment-header-text f5 text-normal">

    <strong>
        <a href="/rojcosta" class="author">rojcosta</a>
        
    </strong>

    commented

    <a href="#gistcomment-1900314" class="timestamp"><relative-time datetime="2016-10-18T13:14:51Z">Oct 18, 2016</relative-time></a>


  </h3>
</div>


  <div class="edit-comment-hide">
    <table class="d-block">
      <tbody class="d-block">
        <tr class="d-block">
          <td class="d-block comment-body markdown-body  js-comment-body">
              <p>Thank you!</p>
          </td>
        </tr>
      </tbody>
    </table>

  </div>

</div>

  </div>

  
  <div class="timeline-comment-wrapper js-comment-container">

    

<div class="avatar-parent-child timeline-comment-avatar">
    <a href="/nachodox">
      <img alt="@nachodox" class="avatar rounded-1" height="44" src="https://avatars0.githubusercontent.com/u/1728854?v=3&amp;s=88" width="44" />
    </a>

</div>



      
<div id="gistcomment-1902365"
     class="comment previewable-edit js-comment js-task-list-container  timeline-comment js-reorderable-task-lists reorderable-task-lists "
     data-body-version="237a65b18a70d9fbd87aab3d76e42c3d">

  
<div class="timeline-comment-header">
  <div class="timeline-comment-actions">


  </div>

    



  <h3 class="timeline-comment-header-text f5 text-normal">

    <strong>
        <a href="/nachodox" class="author">nachodox</a>
        
    </strong>

    commented

    <a href="#gistcomment-1902365" class="timestamp"><relative-time datetime="2016-10-20T16:09:38Z">Oct 20, 2016</relative-time></a>


  </h3>
</div>


  <div class="edit-comment-hide">
    <table class="d-block">
      <tbody class="d-block">
        <tr class="d-block">
          <td class="d-block comment-body markdown-body  js-comment-body">
              <p>thx</p>
          </td>
        </tr>
      </tbody>
    </table>

  </div>

</div>

  </div>

  
  <div class="timeline-comment-wrapper js-comment-container">

    

<div class="avatar-parent-child timeline-comment-avatar">
    <a href="/Kitanga">
      <img alt="@Kitanga" class="avatar rounded-1" height="44" src="https://avatars1.githubusercontent.com/u/14119482?v=3&amp;s=88" width="44" />
    </a>

</div>



      
<div id="gistcomment-1902616"
     class="comment previewable-edit js-comment js-task-list-container  timeline-comment js-reorderable-task-lists reorderable-task-lists "
     data-body-version="3fb050b64e1cc26eb2ed867ffdae3061">

  
<div class="timeline-comment-header">
  <div class="timeline-comment-actions">


  </div>

    



  <h3 class="timeline-comment-header-text f5 text-normal">

    <strong>
        <a href="/Kitanga" class="author">Kitanga</a>
        
    </strong>

    commented

    <a href="#gistcomment-1902616" class="timestamp"><relative-time datetime="2016-10-20T20:45:54Z">Oct 20, 2016</relative-time></a>


  </h3>
</div>


  <div class="edit-comment-hide">
    <table class="d-block">
      <tbody class="d-block">
        <tr class="d-block">
          <td class="d-block comment-body markdown-body  js-comment-body">
              <p>Thank you!!</p>
          </td>
        </tr>
      </tbody>
    </table>

  </div>

</div>

  </div>

  
  <div class="timeline-comment-wrapper js-comment-container">

    

<div class="avatar-parent-child timeline-comment-avatar">
    <a href="/vroomcam">
      <img alt="@vroomcam" class="avatar rounded-1" height="44" src="https://avatars3.githubusercontent.com/u/19295836?v=3&amp;s=88" width="44" />
    </a>

</div>



      
<div id="gistcomment-1904017"
     class="comment previewable-edit js-comment js-task-list-container  timeline-comment js-reorderable-task-lists reorderable-task-lists "
     data-body-version="4385cc6e56008b15876fd49c9a569106">

  
<div class="timeline-comment-header">
  <div class="timeline-comment-actions">


  </div>

    



  <h3 class="timeline-comment-header-text f5 text-normal">

    <strong>
        <a href="/vroomcam" class="author">vroomcam</a>
        
    </strong>

    commented

    <a href="#gistcomment-1904017" class="timestamp"><relative-time datetime="2016-10-23T07:07:09Z">Oct 23, 2016</relative-time></a>


  </h3>
</div>


  <div class="edit-comment-hide">
    <table class="d-block">
      <tbody class="d-block">
        <tr class="d-block">
          <td class="d-block comment-body markdown-body  js-comment-body">
              <p>Thanks!</p>
          </td>
        </tr>
      </tbody>
    </table>

  </div>

</div>

  </div>

  
  <div class="timeline-comment-wrapper js-comment-container">

    

<div class="avatar-parent-child timeline-comment-avatar">
    <a href="/tkaghdo">
      <img alt="@tkaghdo" class="avatar rounded-1" height="44" src="https://avatars2.githubusercontent.com/u/3038091?v=3&amp;s=88" width="44" />
    </a>

</div>



      
<div id="gistcomment-1909456"
     class="comment previewable-edit js-comment js-task-list-container  timeline-comment js-reorderable-task-lists reorderable-task-lists "
     data-body-version="61df2a4caabcbe859c690c9ae77b42bb">

  
<div class="timeline-comment-header">
  <div class="timeline-comment-actions">


  </div>

    



  <h3 class="timeline-comment-header-text f5 text-normal">

    <strong>
        <a href="/tkaghdo" class="author">tkaghdo</a>
        
    </strong>

    commented

    <a href="#gistcomment-1909456" class="timestamp"><relative-time datetime="2016-10-29T21:43:32Z">Oct 29, 2016</relative-time></a>


  </h3>
</div>


  <div class="edit-comment-hide">
    <table class="d-block">
      <tbody class="d-block">
        <tr class="d-block">
          <td class="d-block comment-body markdown-body  js-comment-body">
              <p>Thank you very much!</p>
          </td>
        </tr>
      </tbody>
    </table>

  </div>

</div>

  </div>

  
  <div class="timeline-comment-wrapper js-comment-container">

    

<div class="avatar-parent-child timeline-comment-avatar">
    <a href="/navneet1075">
      <img alt="@navneet1075" class="avatar rounded-1" height="44" src="https://avatars3.githubusercontent.com/u/6396611?v=3&amp;s=88" width="44" />
    </a>

</div>



      
<div id="gistcomment-1917477"
     class="comment previewable-edit js-comment js-task-list-container  timeline-comment js-reorderable-task-lists reorderable-task-lists "
     data-body-version="bb163d8eff5e870a7fc4cf35fe26443e">

  
<div class="timeline-comment-header">
  <div class="timeline-comment-actions">


  </div>

    



  <h3 class="timeline-comment-header-text f5 text-normal">

    <strong>
        <a href="/navneet1075" class="author">navneet1075</a>
        
    </strong>

    commented

    <a href="#gistcomment-1917477" class="timestamp"><relative-time datetime="2016-11-09T06:18:21Z">Nov 9, 2016</relative-time></a>


      &#8226;
      <span class="timestamp timestamp-edited tooltipped tooltipped-n"
            aria-label="navneet1075 edited this comment 7 months ago">
          edited
      </span>
  </h3>
</div>


  <div class="edit-comment-hide">
    <table class="d-block">
      <tbody class="d-block">
        <tr class="d-block">
          <td class="d-block comment-body markdown-body  js-comment-body">
              <p>Thanks a lot . It really helped .</p>
          </td>
        </tr>
      </tbody>
    </table>

  </div>

</div>

  </div>

  
  <div class="timeline-comment-wrapper js-comment-container">

    

<div class="avatar-parent-child timeline-comment-avatar">
    <a href="/accendino">
      <img alt="@accendino" class="avatar rounded-1" height="44" src="https://avatars3.githubusercontent.com/u/23463325?v=3&amp;s=88" width="44" />
    </a>

</div>



      
<div id="gistcomment-1926649"
     class="comment previewable-edit js-comment js-task-list-container  timeline-comment js-reorderable-task-lists reorderable-task-lists "
     data-body-version="05c8ac704e69c8f0f361ad82d5f9675f">

  
<div class="timeline-comment-header">
  <div class="timeline-comment-actions">


  </div>

    



  <h3 class="timeline-comment-header-text f5 text-normal">

    <strong>
        <a href="/accendino" class="author">accendino</a>
        
    </strong>

    commented

    <a href="#gistcomment-1926649" class="timestamp"><relative-time datetime="2016-11-21T02:42:30Z">Nov 20, 2016</relative-time></a>


  </h3>
</div>


  <div class="edit-comment-hide">
    <table class="d-block">
      <tbody class="d-block">
        <tr class="d-block">
          <td class="d-block comment-body markdown-body  js-comment-body">
              <p>Great template, thank`s a lot!</p>
          </td>
        </tr>
      </tbody>
    </table>

  </div>

</div>

  </div>

  
  <div class="timeline-comment-wrapper js-comment-container">

    

<div class="avatar-parent-child timeline-comment-avatar">
    <a href="/ebanfa">
      <img alt="@ebanfa" class="avatar rounded-1" height="44" src="https://avatars2.githubusercontent.com/u/1817570?v=3&amp;s=88" width="44" />
    </a>

</div>



      
<div id="gistcomment-1928513"
     class="comment previewable-edit js-comment js-task-list-container  timeline-comment js-reorderable-task-lists reorderable-task-lists "
     data-body-version="6d5484ac8583041e3e09a48997967a5e">

  
<div class="timeline-comment-header">
  <div class="timeline-comment-actions">


  </div>

    



  <h3 class="timeline-comment-header-text f5 text-normal">

    <strong>
        <a href="/ebanfa" class="author">ebanfa</a>
        
    </strong>

    commented

    <a href="#gistcomment-1928513" class="timestamp"><relative-time datetime="2016-11-23T00:14:17Z">Nov 22, 2016</relative-time></a>


  </h3>
</div>


  <div class="edit-comment-hide">
    <table class="d-block">
      <tbody class="d-block">
        <tr class="d-block">
          <td class="d-block comment-body markdown-body  js-comment-body">
              <p>Great. Thanks</p>
          </td>
        </tr>
      </tbody>
    </table>

  </div>

</div>

  </div>

  
  <div class="timeline-comment-wrapper js-comment-container">

    

<div class="avatar-parent-child timeline-comment-avatar">
    <a href="/Rolandkuku">
      <img alt="@Rolandkuku" class="avatar rounded-1" height="44" src="https://avatars2.githubusercontent.com/u/6169736?v=3&amp;s=88" width="44" />
    </a>

</div>



      
<div id="gistcomment-1932659"
     class="comment previewable-edit js-comment js-task-list-container  timeline-comment js-reorderable-task-lists reorderable-task-lists "
     data-body-version="e7cbf67460e47dea4b13e81304850d5f">

  
<div class="timeline-comment-header">
  <div class="timeline-comment-actions">


  </div>

    



  <h3 class="timeline-comment-header-text f5 text-normal">

    <strong>
        <a href="/Rolandkuku" class="author">Rolandkuku</a>
        
    </strong>

    commented

    <a href="#gistcomment-1932659" class="timestamp"><relative-time datetime="2016-11-28T16:36:46Z">Nov 28, 2016</relative-time></a>


  </h3>
</div>


  <div class="edit-comment-hide">
    <table class="d-block">
      <tbody class="d-block">
        <tr class="d-block">
          <td class="d-block comment-body markdown-body  js-comment-body">
              <p>&lt;3</p>
          </td>
        </tr>
      </tbody>
    </table>

  </div>

</div>

  </div>

  
  <div class="timeline-comment-wrapper js-comment-container">

    

<div class="avatar-parent-child timeline-comment-avatar">
    <a href="/WeeHong">
      <img alt="@WeeHong" class="avatar rounded-1" height="44" src="https://avatars0.githubusercontent.com/u/6753022?v=3&amp;s=88" width="44" />
    </a>

</div>



      
<div id="gistcomment-1943843"
     class="comment previewable-edit js-comment js-task-list-container  timeline-comment js-reorderable-task-lists reorderable-task-lists "
     data-body-version="7da082730ce8e9a5e2672e11cf85147a">

  
<div class="timeline-comment-header">
  <div class="timeline-comment-actions">


  </div>

    



  <h3 class="timeline-comment-header-text f5 text-normal">

    <strong>
        <a href="/WeeHong" class="author">WeeHong</a>
        
    </strong>

    commented

    <a href="#gistcomment-1943843" class="timestamp"><relative-time datetime="2016-12-12T02:45:42Z">Dec 11, 2016</relative-time></a>


  </h3>
</div>


  <div class="edit-comment-hide">
    <table class="d-block">
      <tbody class="d-block">
        <tr class="d-block">
          <td class="d-block comment-body markdown-body  js-comment-body">
              <p>Thank you for sharing. &lt;3</p>
          </td>
        </tr>
      </tbody>
    </table>

  </div>

</div>

  </div>

  
  <div class="timeline-comment-wrapper js-comment-container">

    

<div class="avatar-parent-child timeline-comment-avatar">
    <a href="/AnythingTechPro">
      <img alt="@AnythingTechPro" class="avatar rounded-1" height="44" src="https://avatars2.githubusercontent.com/u/22750553?v=3&amp;s=88" width="44" />
    </a>

</div>



      
<div id="gistcomment-1947007"
     class="comment previewable-edit js-comment js-task-list-container  timeline-comment js-reorderable-task-lists reorderable-task-lists "
     data-body-version="38f5c24717fedaa404babb0c4710152e">

  
<div class="timeline-comment-header">
  <div class="timeline-comment-actions">


  </div>

    



  <h3 class="timeline-comment-header-text f5 text-normal">

    <strong>
        <a href="/AnythingTechPro" class="author">AnythingTechPro</a>
        
    </strong>

    commented

    <a href="#gistcomment-1947007" class="timestamp"><relative-time datetime="2016-12-14T14:21:23Z">Dec 14, 2016</relative-time></a>


  </h3>
</div>


  <div class="edit-comment-hide">
    <table class="d-block">
      <tbody class="d-block">
        <tr class="d-block">
          <td class="d-block comment-body markdown-body  js-comment-body">
              <p>Thanks!</p>
          </td>
        </tr>
      </tbody>
    </table>

  </div>

</div>

  </div>

  
  <div class="timeline-comment-wrapper js-comment-container">

    

<div class="avatar-parent-child timeline-comment-avatar">
    <a href="/jpbourgeon">
      <img alt="@jpbourgeon" class="avatar rounded-1" height="44" src="https://avatars2.githubusercontent.com/u/3356641?v=3&amp;s=88" width="44" />
    </a>

</div>



      
<div id="gistcomment-1960943"
     class="comment previewable-edit js-comment js-task-list-container  timeline-comment js-reorderable-task-lists reorderable-task-lists "
     data-body-version="7a7c46aab7e07559c6f7a8b25f2b9ef4">

  
<div class="timeline-comment-header">
  <div class="timeline-comment-actions">


  </div>

    



  <h3 class="timeline-comment-header-text f5 text-normal">

    <strong>
        <a href="/jpbourgeon" class="author">jpbourgeon</a>
        
    </strong>

    commented

    <a href="#gistcomment-1960943" class="timestamp"><relative-time datetime="2017-01-02T13:40:53Z">Jan 2, 2017</relative-time></a>


  </h3>
</div>


  <div class="edit-comment-hide">
    <table class="d-block">
      <tbody class="d-block">
        <tr class="d-block">
          <td class="d-block comment-body markdown-body  js-comment-body">
              <p>Thank you</p>
          </td>
        </tr>
      </tbody>
    </table>

  </div>

</div>

  </div>

  
  <div class="timeline-comment-wrapper js-comment-container">

    

<div class="avatar-parent-child timeline-comment-avatar">
    <a href="/avinashbarfa">
      <img alt="@avinashbarfa" class="avatar rounded-1" height="44" src="https://avatars1.githubusercontent.com/u/22172887?v=3&amp;s=88" width="44" />
    </a>

</div>



      
<div id="gistcomment-1962649"
     class="comment previewable-edit js-comment js-task-list-container  timeline-comment js-reorderable-task-lists reorderable-task-lists "
     data-body-version="71d3e8b42792b5e476804f4f7fbddc58">

  
<div class="timeline-comment-header">
  <div class="timeline-comment-actions">


  </div>

    



  <h3 class="timeline-comment-header-text f5 text-normal">

    <strong>
        <a href="/avinashbarfa" class="author">avinashbarfa</a>
        
    </strong>

    commented

    <a href="#gistcomment-1962649" class="timestamp"><relative-time datetime="2017-01-04T14:09:46Z">Jan 4, 2017</relative-time></a>


  </h3>
</div>


  <div class="edit-comment-hide">
    <table class="d-block">
      <tbody class="d-block">
        <tr class="d-block">
          <td class="d-block comment-body markdown-body  js-comment-body">
              <p>thanks</p>
          </td>
        </tr>
      </tbody>
    </table>

  </div>

</div>

  </div>

  
  <div class="timeline-comment-wrapper js-comment-container">

    

<div class="avatar-parent-child timeline-comment-avatar">
    <a href="/richoseptaalfian">
      <img alt="@richoseptaalfian" class="avatar rounded-1" height="44" src="https://avatars2.githubusercontent.com/u/24996697?v=3&amp;s=88" width="44" />
    </a>

</div>



      
<div id="gistcomment-1967915"
     class="comment previewable-edit js-comment js-task-list-container  timeline-comment js-reorderable-task-lists reorderable-task-lists "
     data-body-version="e053f6b2c0d75eb0c89a5f99c92eae43">

  
<div class="timeline-comment-header">
  <div class="timeline-comment-actions">


  </div>

    



  <h3 class="timeline-comment-header-text f5 text-normal">

    <strong>
        <a href="/richoseptaalfian" class="author">richoseptaalfian</a>
        
    </strong>

    commented

    <a href="#gistcomment-1967915" class="timestamp"><relative-time datetime="2017-01-11T03:47:52Z">Jan 10, 2017</relative-time></a>


  </h3>
</div>


  <div class="edit-comment-hide">
    <table class="d-block">
      <tbody class="d-block">
        <tr class="d-block">
          <td class="d-block comment-body markdown-body  js-comment-body">
              <p>how his men dwonload</p>
          </td>
        </tr>
      </tbody>
    </table>

  </div>

</div>

  </div>

  
  <div class="timeline-comment-wrapper js-comment-container">

    

<div class="avatar-parent-child timeline-comment-avatar">
    <a href="/kevinbazira">
      <img alt="@kevinbazira" class="avatar rounded-1" height="44" src="https://avatars1.githubusercontent.com/u/24711431?v=3&amp;s=88" width="44" />
    </a>

</div>



      
<div id="gistcomment-1968091"
     class="comment previewable-edit js-comment js-task-list-container  timeline-comment js-reorderable-task-lists reorderable-task-lists "
     data-body-version="3dd0e14b580c3ed611610018132d27e1">

  
<div class="timeline-comment-header">
  <div class="timeline-comment-actions">


  </div>

    



  <h3 class="timeline-comment-header-text f5 text-normal">

    <strong>
        <a href="/kevinbazira" class="author">kevinbazira</a>
        
    </strong>

    commented

    <a href="#gistcomment-1968091" class="timestamp"><relative-time datetime="2017-01-11T09:22:06Z">Jan 11, 2017</relative-time></a>


  </h3>
</div>


  <div class="edit-comment-hide">
    <table class="d-block">
      <tbody class="d-block">
        <tr class="d-block">
          <td class="d-block comment-body markdown-body  js-comment-body">
              <p>Thanks a bunch</p>
          </td>
        </tr>
      </tbody>
    </table>

  </div>

</div>

  </div>

  
  <div class="timeline-comment-wrapper js-comment-container">

    

<div class="avatar-parent-child timeline-comment-avatar">
    <a href="/jaysheelshah">
      <img alt="@jaysheelshah" class="avatar rounded-1" height="44" src="https://avatars3.githubusercontent.com/u/14299658?v=3&amp;s=88" width="44" />
    </a>

</div>



      
<div id="gistcomment-1971973"
     class="comment previewable-edit js-comment js-task-list-container  timeline-comment js-reorderable-task-lists reorderable-task-lists "
     data-body-version="3349edcf75c6f646ba3da5ca43e36393">

  
<div class="timeline-comment-header">
  <div class="timeline-comment-actions">


  </div>

    



  <h3 class="timeline-comment-header-text f5 text-normal">

    <strong>
        <a href="/jaysheelshah" class="author">jaysheelshah</a>
        
    </strong>

    commented

    <a href="#gistcomment-1971973" class="timestamp"><relative-time datetime="2017-01-16T01:26:04Z">Jan 15, 2017</relative-time></a>


  </h3>
</div>


  <div class="edit-comment-hide">
    <table class="d-block">
      <tbody class="d-block">
        <tr class="d-block">
          <td class="d-block comment-body markdown-body  js-comment-body">
              <p>Cool template. Thanks for sharing!</p>
          </td>
        </tr>
      </tbody>
    </table>

  </div>

</div>

  </div>

  
  <div class="timeline-comment-wrapper js-comment-container">

    

<div class="avatar-parent-child timeline-comment-avatar">
    <a href="/Odame">
      <img alt="@Odame" class="avatar rounded-1" height="44" src="https://avatars2.githubusercontent.com/u/12601074?v=3&amp;s=88" width="44" />
    </a>

</div>



      
<div id="gistcomment-1975785"
     class="comment previewable-edit js-comment js-task-list-container  timeline-comment js-reorderable-task-lists reorderable-task-lists "
     data-body-version="2f2a9164e4bfc66052b45cc66ff7f706">

  
<div class="timeline-comment-header">
  <div class="timeline-comment-actions">


  </div>

    



  <h3 class="timeline-comment-header-text f5 text-normal">

    <strong>
        <a href="/Odame" class="author">Odame</a>
        
    </strong>

    commented

    <a href="#gistcomment-1975785" class="timestamp"><relative-time datetime="2017-01-19T19:38:31Z">Jan 19, 2017</relative-time></a>


  </h3>
</div>


  <div class="edit-comment-hide">
    <table class="d-block">
      <tbody class="d-block">
        <tr class="d-block">
          <td class="d-block comment-body markdown-body  js-comment-body">
              <p>Thanks for sharing</p>
          </td>
        </tr>
      </tbody>
    </table>

  </div>

</div>

  </div>

  
  <div class="timeline-comment-wrapper js-comment-container">

    

<div class="avatar-parent-child timeline-comment-avatar">
    <a href="/Nyakato">
      <img alt="@Nyakato" class="avatar rounded-1" height="44" src="https://avatars0.githubusercontent.com/u/22750163?v=3&amp;s=88" width="44" />
    </a>

</div>



      
<div id="gistcomment-1979084"
     class="comment previewable-edit js-comment js-task-list-container  timeline-comment js-reorderable-task-lists reorderable-task-lists "
     data-body-version="e95121ac5f555b98a829a31957d7661e">

  
<div class="timeline-comment-header">
  <div class="timeline-comment-actions">


  </div>

    



  <h3 class="timeline-comment-header-text f5 text-normal">

    <strong>
        <a href="/Nyakato" class="author">Nyakato</a>
        
    </strong>

    commented

    <a href="#gistcomment-1979084" class="timestamp"><relative-time datetime="2017-01-24T08:36:25Z">Jan 24, 2017</relative-time></a>


  </h3>
</div>


  <div class="edit-comment-hide">
    <table class="d-block">
      <tbody class="d-block">
        <tr class="d-block">
          <td class="d-block comment-body markdown-body  js-comment-body">
              <p>Thanks alot</p>
          </td>
        </tr>
      </tbody>
    </table>

  </div>

</div>

  </div>

  
  <div class="timeline-comment-wrapper js-comment-container">

    

<div class="avatar-parent-child timeline-comment-avatar">
    <a href="/a13ks3y">
      <img alt="@a13ks3y" class="avatar rounded-1" height="44" src="https://avatars2.githubusercontent.com/u/509254?v=3&amp;s=88" width="44" />
    </a>

</div>



      
<div id="gistcomment-1979841"
     class="comment previewable-edit js-comment js-task-list-container  timeline-comment js-reorderable-task-lists reorderable-task-lists "
     data-body-version="498cd895eb5a102c5aeb977e2b928dee">

  
<div class="timeline-comment-header">
  <div class="timeline-comment-actions">


  </div>

    



  <h3 class="timeline-comment-header-text f5 text-normal">

    <strong>
        <a href="/a13ks3y" class="author">a13ks3y</a>
        
    </strong>

    commented

    <a href="#gistcomment-1979841" class="timestamp"><relative-time datetime="2017-01-24T22:50:25Z">Jan 24, 2017</relative-time></a>


  </h3>
</div>


  <div class="edit-comment-hide">
    <table class="d-block">
      <tbody class="d-block">
        <tr class="d-block">
          <td class="d-block comment-body markdown-body  js-comment-body">
              <p>Thank you!</p>
          </td>
        </tr>
      </tbody>
    </table>

  </div>

</div>

  </div>

  
  <div class="timeline-comment-wrapper js-comment-container">

    

<div class="avatar-parent-child timeline-comment-avatar">
    <a href="/Colobri">
      <img alt="@Colobri" class="avatar rounded-1" height="44" src="https://avatars0.githubusercontent.com/u/20686623?v=3&amp;s=88" width="44" />
    </a>

</div>



      
<div id="gistcomment-1986076"
     class="comment previewable-edit js-comment js-task-list-container  timeline-comment js-reorderable-task-lists reorderable-task-lists "
     data-body-version="125a99e3257092dca48f0ccb98947ee9">

  
<div class="timeline-comment-header">
  <div class="timeline-comment-actions">


  </div>

    



  <h3 class="timeline-comment-header-text f5 text-normal">

    <strong>
        <a href="/Colobri" class="author">Colobri</a>
        
    </strong>

    commented

    <a href="#gistcomment-1986076" class="timestamp"><relative-time datetime="2017-02-01T18:27:57Z">Feb 1, 2017</relative-time></a>


  </h3>
</div>


  <div class="edit-comment-hide">
    <table class="d-block">
      <tbody class="d-block">
        <tr class="d-block">
          <td class="d-block comment-body markdown-body  js-comment-body">
              <p>Awesome!</p>
          </td>
        </tr>
      </tbody>
    </table>

  </div>

</div>

  </div>

  
  <div class="timeline-comment-wrapper js-comment-container">

    

<div class="avatar-parent-child timeline-comment-avatar">
    <a href="/enajenkins">
      <img alt="@enajenkins" class="avatar rounded-1" height="44" src="https://avatars1.githubusercontent.com/u/110690?v=3&amp;s=88" width="44" />
    </a>

</div>



      
<div id="gistcomment-2001920"
     class="comment previewable-edit js-comment js-task-list-container  timeline-comment js-reorderable-task-lists reorderable-task-lists "
     data-body-version="45ef5291e396b8b145158f8f8e661e4f">

  
<div class="timeline-comment-header">
  <div class="timeline-comment-actions">


  </div>

    



  <h3 class="timeline-comment-header-text f5 text-normal">

    <strong>
        <a href="/enajenkins" class="author">enajenkins</a>
        
    </strong>

    commented

    <a href="#gistcomment-2001920" class="timestamp"><relative-time datetime="2017-02-16T00:43:15Z">Feb 15, 2017</relative-time></a>


  </h3>
</div>


  <div class="edit-comment-hide">
    <table class="d-block">
      <tbody class="d-block">
        <tr class="d-block">
          <td class="d-block comment-body markdown-body  js-comment-body">
              <p>Thank you! Great guide :)</p>
          </td>
        </tr>
      </tbody>
    </table>

  </div>

</div>

  </div>

  
  <div class="timeline-comment-wrapper js-comment-container">

    

<div class="avatar-parent-child timeline-comment-avatar">
    <a href="/haimerb">
      <img alt="@haimerb" class="avatar rounded-1" height="44" src="https://avatars0.githubusercontent.com/u/6827210?v=3&amp;s=88" width="44" />
    </a>

</div>



      
<div id="gistcomment-2007923"
     class="comment previewable-edit js-comment js-task-list-container  timeline-comment js-reorderable-task-lists reorderable-task-lists "
     data-body-version="498cd895eb5a102c5aeb977e2b928dee">

  
<div class="timeline-comment-header">
  <div class="timeline-comment-actions">


  </div>

    



  <h3 class="timeline-comment-header-text f5 text-normal">

    <strong>
        <a href="/haimerb" class="author">haimerb</a>
        
    </strong>

    commented

    <a href="#gistcomment-2007923" class="timestamp"><relative-time datetime="2017-02-22T12:54:07Z">Feb 22, 2017</relative-time></a>


  </h3>
</div>


  <div class="edit-comment-hide">
    <table class="d-block">
      <tbody class="d-block">
        <tr class="d-block">
          <td class="d-block comment-body markdown-body  js-comment-body">
              <p>Thank you!</p>
          </td>
        </tr>
      </tbody>
    </table>

  </div>

</div>

  </div>

  
  <div class="timeline-comment-wrapper js-comment-container">

    

<div class="avatar-parent-child timeline-comment-avatar">
    <a href="/Nikita-Sharma-94">
      <img alt="@Nikita-Sharma-94" class="avatar rounded-1" height="44" src="https://avatars3.githubusercontent.com/u/18711844?v=3&amp;s=88" width="44" />
    </a>

</div>



      
<div id="gistcomment-2014075"
     class="comment previewable-edit js-comment js-task-list-container  timeline-comment js-reorderable-task-lists reorderable-task-lists "
     data-body-version="e6f295be6ad475fcd927064a1aaac2c5">

  
<div class="timeline-comment-header">
  <div class="timeline-comment-actions">


  </div>

    



  <h3 class="timeline-comment-header-text f5 text-normal">

    <strong>
        <a href="/Nikita-Sharma-94" class="author">Nikita-Sharma-94</a>
        
    </strong>

    commented

    <a href="#gistcomment-2014075" class="timestamp"><relative-time datetime="2017-02-28T22:43:11Z">Feb 28, 2017</relative-time></a>


  </h3>
</div>


  <div class="edit-comment-hide">
    <table class="d-block">
      <tbody class="d-block">
        <tr class="d-block">
          <td class="d-block comment-body markdown-body  js-comment-body">
              <p>Thank you</p>
          </td>
        </tr>
      </tbody>
    </table>

  </div>

</div>

  </div>

  
  <div class="timeline-comment-wrapper js-comment-container">

    

<div class="avatar-parent-child timeline-comment-avatar">
    <a href="/danitome24">
      <img alt="@danitome24" class="avatar rounded-1" height="44" src="https://avatars2.githubusercontent.com/u/7501990?v=3&amp;s=88" width="44" />
    </a>

</div>



      
<div id="gistcomment-2018917"
     class="comment previewable-edit js-comment js-task-list-container  timeline-comment js-reorderable-task-lists reorderable-task-lists "
     data-body-version="ff1d28d281dd3ccc6c5a9a8e9edf4321">

  
<div class="timeline-comment-header">
  <div class="timeline-comment-actions">


  </div>

    



  <h3 class="timeline-comment-header-text f5 text-normal">

    <strong>
        <a href="/danitome24" class="author">danitome24</a>
        
    </strong>

    commented

    <a href="#gistcomment-2018917" class="timestamp"><relative-time datetime="2017-03-06T10:26:32Z">Mar 6, 2017</relative-time></a>


  </h3>
</div>


  <div class="edit-comment-hide">
    <table class="d-block">
      <tbody class="d-block">
        <tr class="d-block">
          <td class="d-block comment-body markdown-body  js-comment-body">
              <p><g-emoji alias="top" fallback-src="https://assets-cdn.github.com/images/icons/emoji/unicode/1f51d.png" ios-version="6.0">🔝</g-emoji></p>
          </td>
        </tr>
      </tbody>
    </table>

  </div>

</div>

  </div>

  
  <div class="timeline-comment-wrapper js-comment-container">

    

<div class="avatar-parent-child timeline-comment-avatar">
    <a href="/GirardR1006">
      <img alt="@GirardR1006" class="avatar rounded-1" height="44" src="https://avatars1.githubusercontent.com/u/19275558?v=3&amp;s=88" width="44" />
    </a>

</div>



      
<div id="gistcomment-2047315"
     class="comment previewable-edit js-comment js-task-list-container  timeline-comment js-reorderable-task-lists reorderable-task-lists "
     data-body-version="8d142373593fa66bfd66cac8b467292a">

  
<div class="timeline-comment-header">
  <div class="timeline-comment-actions">


  </div>

    



  <h3 class="timeline-comment-header-text f5 text-normal">

    <strong>
        <a href="/GirardR1006" class="author">GirardR1006</a>
        
    </strong>

    commented

    <a href="#gistcomment-2047315" class="timestamp"><relative-time datetime="2017-04-05T15:04:30Z">Apr 5, 2017</relative-time></a>


  </h3>
</div>


  <div class="edit-comment-hide">
    <table class="d-block">
      <tbody class="d-block">
        <tr class="d-block">
          <td class="d-block comment-body markdown-body  js-comment-body">
              <p>Thank for the template</p>
          </td>
        </tr>
      </tbody>
    </table>

  </div>

</div>

  </div>

  
  <div class="timeline-comment-wrapper js-comment-container">

    

<div class="avatar-parent-child timeline-comment-avatar">
    <a href="/Woiyl">
      <img alt="@Woiyl" class="avatar rounded-1" height="44" src="https://avatars1.githubusercontent.com/u/2580120?v=3&amp;s=88" width="44" />
    </a>

</div>



      
<div id="gistcomment-2058390"
     class="comment previewable-edit js-comment js-task-list-container  timeline-comment js-reorderable-task-lists reorderable-task-lists "
     data-body-version="e46d47e91c14d9e10f1df07527618cef">

  
<div class="timeline-comment-header">
  <div class="timeline-comment-actions">


  </div>

    



  <h3 class="timeline-comment-header-text f5 text-normal">

    <strong>
        <a href="/Woiyl" class="author">Woiyl</a>
        
    </strong>

    commented

    <a href="#gistcomment-2058390" class="timestamp"><relative-time datetime="2017-04-13T06:38:34Z">Apr 13, 2017</relative-time></a>


  </h3>
</div>


  <div class="edit-comment-hide">
    <table class="d-block">
      <tbody class="d-block">
        <tr class="d-block">
          <td class="d-block comment-body markdown-body  js-comment-body">
              <p>Easy to integrate , thanks a lot !</p>
          </td>
        </tr>
      </tbody>
    </table>

  </div>

</div>

  </div>

  
  <div class="timeline-comment-wrapper js-comment-container">

    

<div class="avatar-parent-child timeline-comment-avatar">
    <a href="/oumarxy">
      <img alt="@oumarxy" class="avatar rounded-1" height="44" src="https://avatars3.githubusercontent.com/u/5592576?v=3&amp;s=88" width="44" />
    </a>

</div>



      
<div id="gistcomment-2091059"
     class="comment previewable-edit js-comment js-task-list-container  timeline-comment js-reorderable-task-lists reorderable-task-lists "
     data-body-version="7a7c46aab7e07559c6f7a8b25f2b9ef4">

  
<div class="timeline-comment-header">
  <div class="timeline-comment-actions">


  </div>

    



  <h3 class="timeline-comment-header-text f5 text-normal">

    <strong>
        <a href="/oumarxy" class="author">oumarxy</a>
        
    </strong>

    commented

    <a href="#gistcomment-2091059" class="timestamp"><relative-time datetime="2017-05-11T15:32:09Z">May 11, 2017</relative-time></a>


  </h3>
</div>


  <div class="edit-comment-hide">
    <table class="d-block">
      <tbody class="d-block">
        <tr class="d-block">
          <td class="d-block comment-body markdown-body  js-comment-body">
              <p>Thank you</p>
          </td>
        </tr>
      </tbody>
    </table>

  </div>

</div>

  </div>

  
  <div class="timeline-comment-wrapper js-comment-container">

    

<div class="avatar-parent-child timeline-comment-avatar">
    <a href="/azinio">
      <img alt="@azinio" class="avatar rounded-1" height="44" src="https://avatars3.githubusercontent.com/u/26373163?v=3&amp;s=88" width="44" />
    </a>

</div>



      
<div id="gistcomment-2107071"
     class="comment previewable-edit js-comment js-task-list-container  timeline-comment js-reorderable-task-lists reorderable-task-lists "
     data-body-version="247f324c2616b3ba60cc709c6185ebd3">

  
<div class="timeline-comment-header">
  <div class="timeline-comment-actions">


  </div>

    



  <h3 class="timeline-comment-header-text f5 text-normal">

    <strong>
        <a href="/azinio" class="author">azinio</a>
        
    </strong>

    commented

    <a href="#gistcomment-2107071" class="timestamp"><relative-time datetime="2017-05-26T09:30:35Z">May 26, 2017</relative-time></a>


  </h3>
</div>


  <div class="edit-comment-hide">
    <table class="d-block">
      <tbody class="d-block">
        <tr class="d-block">
          <td class="d-block comment-body markdown-body  js-comment-body">
              <p>Arigato u Gozaimasu</p>
          </td>
        </tr>
      </tbody>
    </table>

  </div>

</div>

  </div>

  
  <div class="timeline-comment-wrapper js-comment-container">

    

<div class="avatar-parent-child timeline-comment-avatar">
    <a href="/winnie131212592">
      <img alt="@winnie131212592" class="avatar rounded-1" height="44" src="https://avatars2.githubusercontent.com/u/23657442?v=3&amp;s=88" width="44" />
    </a>

</div>



      
<div id="gistcomment-2111329"
     class="comment previewable-edit js-comment js-task-list-container  timeline-comment js-reorderable-task-lists reorderable-task-lists "
     data-body-version="df62917d33ec14eab95ce389759a6628">

  
<div class="timeline-comment-header">
  <div class="timeline-comment-actions">


  </div>

    



  <h3 class="timeline-comment-header-text f5 text-normal">

    <strong>
        <a href="/winnie131212592" class="author">winnie131212592</a>
        
    </strong>

    commented

    <a href="#gistcomment-2111329" class="timestamp"><relative-time datetime="2017-06-01T02:00:42Z">May 31, 2017</relative-time></a>


  </h3>
</div>


  <div class="edit-comment-hide">
    <table class="d-block">
      <tbody class="d-block">
        <tr class="d-block">
          <td class="d-block comment-body markdown-body  js-comment-body">
              <p>tnx. really appreciate it.</p>
          </td>
        </tr>
      </tbody>
    </table>

  </div>

</div>

  </div>

  
  <div class="timeline-comment-wrapper js-comment-container">

    

<div class="avatar-parent-child timeline-comment-avatar">
    <a href="/manpreetzenefits">
      <img alt="@manpreetzenefits" class="avatar rounded-1" height="44" src="https://avatars0.githubusercontent.com/u/11285633?v=3&amp;s=88" width="44" />
    </a>

</div>



      
<div id="gistcomment-2121696"
     class="comment previewable-edit js-comment js-task-list-container  timeline-comment js-reorderable-task-lists reorderable-task-lists "
     data-body-version="00d06796e489999226fb5bb27fe1b3b2">

  
<div class="timeline-comment-header">
  <div class="timeline-comment-actions">


  </div>

    



  <h3 class="timeline-comment-header-text f5 text-normal">

    <strong>
        <a href="/manpreetzenefits" class="author">manpreetzenefits</a>
        
    </strong>

    commented

    <a href="#gistcomment-2121696" class="timestamp"><relative-time datetime="2017-06-12T22:33:06Z">Jun 12, 2017</relative-time></a>


  </h3>
</div>


  <div class="edit-comment-hide">
    <table class="d-block">
      <tbody class="d-block">
        <tr class="d-block">
          <td class="d-block comment-body markdown-body  js-comment-body">
              <p>Thanks</p>
          </td>
        </tr>
      </tbody>
    </table>

  </div>

</div>

  </div>



<!-- Rendered timeline since 2017-06-15 13:37:42 -->
<div id="partial-timeline-marker"
      class="js-timeline-marker js-updatable-content"
      data-url="/jxson/1784669/show_partial?partial=gist%2Ftimeline_marker&amp;since=1497559062"
      data-last-modified="Thu, 15 Jun 2017 20:37:42 GMT"
      >
</div>


        <div class="discussion-timeline-actions">
            <div class="timeline-comment-wrapper timeline-new-comment js-comment-container">
  <a href="/louiswicker"><img alt="@louiswicker" class="timeline-comment-avatar" height="44" src="https://avatars0.githubusercontent.com/u/476478?v=3&amp;s=88" width="44" /></a>

  <!-- '"` --><!-- </textarea></xmp> --></option></form><form accept-charset="UTF-8" action="/jxson/1784669/comments" class="js-new-comment-form" data-remote="true" data-type="json" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="9/pCAOxDJdk5OyU4rOMEjHNdYLOd5lmjfyfxI8ctSzfEXAz5+nmZBwwWR+/YXEiG12obWzeUVFqWhyZaksVxSQ==" /></div>
    <div class="timeline-comment">
      <div class="js-suggester-container  js-previewable-comment-form previewable-comment-form write-selected" data-preview-url="/preview?markdown_unsupported=false&amp;subject=1784669&amp;subject_type=Gist" data-preview-authenticity-token="0+YPqy5VT2WhTM1aW4dmjUdEoI/0s27mGY0it89BVODDfUxT8XyKhT+xBsXoRsF/Tpzv8UJ65nWu1yCU/qeruw==">
  <div class="comment-form-head tabnav">
      <div class="js-toolbar toolbar-commenting">
  <div class="toolbar-group">
    <div class="toolbar-item dropdown js-menu-container">
      <button type="button" tabindex="-1" class="js-menu-target menu-target tooltipped tooltipped-n" aria-label="Add header text" aria-expanded="false" aria-haspopup="true">
        <svg aria-hidden="true" class="octicon octicon-text-size" height="16" version="1.1" viewBox="0 0 18 16" width="18"><path fill-rule="evenodd" d="M13.62 9.08L12.1 3.66h-.06l-1.5 5.42h3.08zM5.7 10.13S4.68 6.52 4.53 6.02h-.08l-1.13 4.11H5.7zM17.31 14h-2.25l-.95-3.25h-4.07L9.09 14H6.84l-.69-2.33H2.87L2.17 14H0l3.3-9.59h2.5l2.17 6.34L10.86 2h2.52l3.94 12h-.01z"/></svg>
        <span class="dropdown-caret"></span>
      </button>

      <div class="dropdown-menu-content js-menu-content">
        <ul class="dropdown-menu dropdown-menu-s">
          <button type="button" class="js-toolbar-item dropdown-item dropdown-header1" data-prefix="# " data-ga-click="Markdown Toolbar, click, header1">
            Header
          </button>
          <button type="button" class="js-toolbar-item dropdown-item dropdown-header2" data-prefix="## " data-ga-click="Markdown Toolbar, click, header2">
            Header
          </button>
          <button type="button" class="js-toolbar-item dropdown-item dropdown-header3" data-prefix="### " data-ga-click="Markdown Toolbar, click, header3">
            Header
          </button>
        </ul>
      </div>
    </div>

    <button type="button" tabindex="-1" class="js-toolbar-item toolbar-item tooltipped tooltipped-n" aria-label="Add bold text <ctrl+b>" data-prefix="**" data-suffix="**" data-toolbar-hotkey="b" data-ga-click="Markdown Toolbar, click, bold" data-trim-first>
      <svg aria-hidden="true" class="octicon octicon-bold" height="16" version="1.1" viewBox="0 0 10 16" width="10"><path fill-rule="evenodd" d="M1 2h3.83c2.48 0 4.3.75 4.3 2.95 0 1.14-.63 2.23-1.67 2.61v.06c1.33.3 2.3 1.23 2.3 2.86 0 2.39-1.97 3.52-4.61 3.52H1V2zm3.66 4.95c1.67 0 2.38-.66 2.38-1.69 0-1.17-.78-1.61-2.34-1.61H3.13v3.3h1.53zm.27 5.39c1.77 0 2.75-.64 2.75-1.98 0-1.27-.95-1.81-2.75-1.81h-1.8v3.8h1.8v-.01z"/></svg>
    </button>

    <button type="button" tabindex="-1" class="js-toolbar-item toolbar-item tooltipped tooltipped-n" aria-label="Add italic text <ctrl+i>" data-prefix="_" data-suffix="_" data-toolbar-hotkey="i" data-ga-click="Markdown Toolbar, click, italic" data-trim-first>
      <svg aria-hidden="true" class="octicon octicon-italic" height="16" version="1.1" viewBox="0 0 6 16" width="6"><path fill-rule="evenodd" d="M2.81 5h1.98L3 14H1l1.81-9zm.36-2.7c0-.7.58-1.3 1.33-1.3.56 0 1.13.38 1.13 1.03 0 .75-.59 1.3-1.33 1.3-.58 0-1.13-.38-1.13-1.03z"/></svg>
    </button>
  </div>

  <div class="toolbar-group">
    <button type="button" tabindex="-1" class="js-toolbar-item toolbar-item tooltipped tooltipped-n" aria-label="Insert a quote" data-prefix="> " data-multiline="true" data-ga-click="Markdown Toolbar, click, quote" data-surround-with-newlines>
      <svg aria-hidden="true" class="octicon octicon-quote" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path fill-rule="evenodd" d="M6.16 3.5C3.73 5.06 2.55 6.67 2.55 9.36c.16-.05.3-.05.44-.05 1.27 0 2.5.86 2.5 2.41 0 1.61-1.03 2.61-2.5 2.61-1.9 0-2.99-1.52-2.99-4.25 0-3.8 1.75-6.53 5.02-8.42L6.16 3.5zm7 0c-2.43 1.56-3.61 3.17-3.61 5.86.16-.05.3-.05.44-.05 1.27 0 2.5.86 2.5 2.41 0 1.61-1.03 2.61-2.5 2.61-1.89 0-2.98-1.52-2.98-4.25 0-3.8 1.75-6.53 5.02-8.42l1.14 1.84h-.01z"/></svg>
    </button>

    <button type="button" tabindex="-1" class="js-toolbar-item toolbar-item tooltipped tooltipped-n" aria-label="Insert code" data-prefix="`" data-suffix="`" data-block-prefix="```" data-block-suffix="```" data-ga-click="Markdown Toolbar, click, code">
      <svg aria-hidden="true" class="octicon octicon-code" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path fill-rule="evenodd" d="M9.5 3L8 4.5 11.5 8 8 11.5 9.5 13 14 8 9.5 3zm-5 0L0 8l4.5 5L6 11.5 2.5 8 6 4.5 4.5 3z"/></svg>
    </button>

    <button type="button" tabindex="-1" class="js-toolbar-item toolbar-item tooltipped tooltipped-n" aria-label="Add a link <ctrl+k>" data-prefix="[" data-suffix="](url)" data-replace-next="url" data-toolbar-hotkey="k" data-scan-for="https?://" data-ga-click="Markdown Toolbar, click, link">
      <svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"/></svg>
    </button>
  </div>

  <div class="toolbar-group">
    <button type="button" tabindex="-1" class="js-toolbar-item toolbar-item tooltipped tooltipped-n" aria-label="Add a bulleted list" data-multiline="true" data-prefix="- " data-multiline="true" data-ga-click="Markdown Toolbar, click, unordered list" data-surround-with-newlines>
      <svg aria-hidden="true" class="octicon octicon-list-unordered" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M2 13c0 .59 0 1-.59 1H.59C0 14 0 13.59 0 13c0-.59 0-1 .59-1h.81c.59 0 .59.41.59 1H2zm2.59-9h6.81c.59 0 .59-.41.59-1 0-.59 0-1-.59-1H4.59C4 2 4 2.41 4 3c0 .59 0 1 .59 1zM1.41 7H.59C0 7 0 7.41 0 8c0 .59 0 1 .59 1h.81c.59 0 .59-.41.59-1 0-.59 0-1-.59-1h.01zm0-5H.59C0 2 0 2.41 0 3c0 .59 0 1 .59 1h.81c.59 0 .59-.41.59-1 0-.59 0-1-.59-1h.01zm10 5H4.59C4 7 4 7.41 4 8c0 .59 0 1 .59 1h6.81c.59 0 .59-.41.59-1 0-.59 0-1-.59-1h.01zm0 5H4.59C4 12 4 12.41 4 13c0 .59 0 1 .59 1h6.81c.59 0 .59-.41.59-1 0-.59 0-1-.59-1h.01z"/></svg>
    </button>
    <button type="button" tabindex="-1" class="js-toolbar-item toolbar-item tooltipped tooltipped-n" aria-label="Add a numbered list" data-prefix="1. " data-multiline="true" data-ga-click="Markdown Toolbar, click, ordered list" data-ordered-list>
      <svg aria-hidden="true" class="octicon octicon-list-ordered" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 13c0 .59 0 1-.59 1H4.59C4 14 4 13.59 4 13c0-.59 0-1 .59-1h6.81c.59 0 .59.41.59 1H12zM4.59 4h6.81c.59 0 .59-.41.59-1 0-.59 0-1-.59-1H4.59C4 2 4 2.41 4 3c0 .59 0 1 .59 1zm6.81 3H4.59C4 7 4 7.41 4 8c0 .59 0 1 .59 1h6.81c.59 0 .59-.41.59-1 0-.59 0-1-.59-1zM2 1h-.72c-.3.19-.58.25-1.03.34V2H1v2.14H.16V5H3v-.86H2V1zm.25 8.13c-.17 0-.45.03-.66.06.53-.56 1.14-1.25 1.14-1.89C2.71 6.52 2.17 6 1.37 6c-.59 0-.97.2-1.38.64l.58.58c.19-.19.38-.38.64-.38.28 0 .48.16.48.52 0 .53-.77 1.2-1.7 2.06V10h3l-.09-.88h-.66l.01.01zm-.08 3.78v-.03c.44-.19.64-.47.64-.86 0-.7-.56-1.11-1.44-1.11-.48 0-.89.19-1.28.52l.55.64c.25-.2.44-.31.69-.31.27 0 .42.13.42.36 0 .27-.2.44-.86.44v.75c.83 0 .98.17.98.47 0 .25-.23.38-.58.38-.28 0-.56-.14-.81-.38l-.48.66c.3.36.77.56 1.41.56.83 0 1.53-.41 1.53-1.16 0-.5-.31-.81-.77-.94v.01z"/></svg>
    </button>

      <button type="button" tabindex="-1" class="js-toolbar-item toolbar-item tooltipped tooltipped-n" aria-label="Add a task list" data-prefix="- [ ] " data-toolbar-hotkey="L" data-multiline data-ga-click="Markdown Toolbar, click, task list" data-surround-with-newlines>
        <svg aria-hidden="true" class="octicon octicon-tasklist" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M15.41 9H7.59C7 9 7 8.59 7 8c0-.59 0-1 .59-1h7.81c.59 0 .59.41.59 1 0 .59 0 1-.59 1h.01zM9.59 4C9 4 9 3.59 9 3c0-.59 0-1 .59-1h5.81c.59 0 .59.41.59 1 0 .59 0 1-.59 1H9.59zM0 3.91l1.41-1.3L3 4.2 7.09 0 8.5 1.41 3 6.91l-3-3zM7.59 12h7.81c.59 0 .59.41.59 1 0 .59 0 1-.59 1H7.59C7 14 7 13.59 7 13c0-.59 0-1 .59-1z"/></svg>
      </button>
  </div>

  <div class="toolbar-group">
      <div class="toolbar-item select-menu select-menu-modal-right js-menu-container js-select-menu js-load-contents js-saved-reply-container"
          data-contents-url="/settings/replies">
        <button type="button" tabindex="-1" class="js-menu-target menu-target tooltipped tooltipped-nw"
           aria-label="Insert a saved reply" aria-expanded="false" aria-haspopup="true" data-ga-click="Markdown Toolbar, click, saved reply">
          <svg aria-hidden="true" class="octicon octicon-reply" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path fill-rule="evenodd" d="M6 3.5c3.92.44 8 3.125 8 10-2.312-5.062-4.75-6-8-6V11L.5 5.5 6 0v3.5z"/></svg>
          <span class="dropdown-caret"></span>
        </button>

        <div class="select-menu-modal-holder js-menu-content js-navigation-container">
          <div class="select-menu-modal">
            <div class="select-menu-header">
              <svg aria-label="Close" class="octicon octicon-x js-menu-close" height="16" role="img" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48z"/></svg>
              <span class="select-menu-title">Select a saved reply</span>
            </div>
            <div class="js-select-menu-deferred-content"></div>
            <div class="select-menu-loading-overlay anim-pulse">
              <svg aria-hidden="true" class="octicon octicon-octoface" height="32" version="1.1" viewBox="0 0 16 16" width="32"><path fill-rule="evenodd" d="M14.7 5.34c.13-.32.55-1.59-.13-3.31 0 0-1.05-.33-3.44 1.3-1-.28-2.07-.32-3.13-.32s-2.13.04-3.13.32c-2.39-1.64-3.44-1.3-3.44-1.3-.68 1.72-.26 2.99-.13 3.31C.49 6.21 0 7.33 0 8.69 0 13.84 3.33 15 7.98 15S16 13.84 16 8.69c0-1.36-.49-2.48-1.3-3.35zM8 14.02c-3.3 0-5.98-.15-5.98-3.35 0-.76.38-1.48 1.02-2.07 1.07-.98 2.9-.46 4.96-.46 2.07 0 3.88-.52 4.96.46.65.59 1.02 1.3 1.02 2.07 0 3.19-2.68 3.35-5.98 3.35zM5.49 9.01c-.66 0-1.2.8-1.2 1.78s.54 1.79 1.2 1.79c.66 0 1.2-.8 1.2-1.79s-.54-1.78-1.2-1.78zm5.02 0c-.66 0-1.2.79-1.2 1.78s.54 1.79 1.2 1.79c.66 0 1.2-.8 1.2-1.79s-.53-1.78-1.2-1.78z"/></svg>
            </div>
          </div>
        </div>
      </div>

      <button type="button" tabindex="-1" class="js-toolbar-item toolbar-item tooltipped tooltipped-nw" aria-label="Directly mention a user or team" data-prefix="@" data-prefix-space data-ga-click="Markdown Toolbar, click, mention">
        <svg aria-hidden="true" class="octicon octicon-mention" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path fill-rule="evenodd" d="M6.58 15c1.25 0 2.52-.31 3.56-.94l-.42-.94c-.84.52-1.89.83-3.03.83-3.23 0-5.64-2.08-5.64-5.72 0-4.37 3.23-7.18 6.58-7.18 3.45 0 5.22 2.19 5.22 5.2 0 2.39-1.34 3.86-2.5 3.86-1.05 0-1.36-.73-1.05-2.19l.73-3.75H8.98l-.11.72c-.41-.63-.94-.83-1.56-.83-2.19 0-3.66 2.39-3.66 4.38 0 1.67.94 2.61 2.3 2.61.84 0 1.67-.53 2.3-1.25.11.94.94 1.45 1.98 1.45 1.67 0 3.77-1.67 3.77-5C14 2.61 11.59 0 7.83 0 3.66 0 0 3.33 0 8.33 0 12.71 2.92 15 6.58 15zm-.31-5c-.73 0-1.36-.52-1.36-1.67 0-1.45.94-3.22 2.41-3.22.52 0 .84.2 1.25.83l-.52 3.02c-.63.73-1.25 1.05-1.78 1.05V10z"/></svg>
      </button>

      <button type="button" tabindex="-1" class="js-toolbar-item toolbar-item tooltipped tooltipped-nw" aria-label="Reference an issue or pull request" data-prefix="#" data-prefix-space data-ga-click="Markdown Toolbar, click, reference">
        <svg aria-hidden="true" class="octicon octicon-bookmark" height="16" version="1.1" viewBox="0 0 10 16" width="10"><path fill-rule="evenodd" d="M9 0H1C.27 0 0 .27 0 1v15l5-3.09L10 16V1c0-.73-.27-1-1-1zm-.78 4.25L6.36 5.61l.72 2.16c.06.22-.02.28-.2.17L5 6.6 3.12 7.94c-.19.11-.25.05-.2-.17l.72-2.16-1.86-1.36c-.17-.16-.14-.23.09-.23l2.3-.03.7-2.16h.25l.7 2.16 2.3.03c.23 0 .27.08.09.23h.01z"/></svg>
      </button>
  </div>
</div>

      <nav class="tabnav-tabs" role="tablist">
        <button type="button" class="btn-link tabnav-tab write-tab js-write-tab selected " role="tab" aria-selected="true">Write</button>
        <button type="button" class="btn-link tabnav-tab preview-tab js-preview-tab " role="tab">Preview</button>
      </nav>
  </div>


  <div class="comment-form-error js-comment-form-error" style="display:none">    There was an error creating your Gist.
</div>
  <div class="write-content js-write-bucket js-uploadable-container js-upload-markdown-image is-default upload-enabled"
      data-upload-policy-url="/upload/policies/assets" data-upload-policy-authenticity-token="89C1n4DT5CFiK51OADCLc8yRRsU+auiUQPFLNs2Ne0WYANNZztqQGYJgBVlFHPwhodGQcAEcNRH1GWdOhoR/tg=="
      >

    <input type="hidden" name="saved_reply_id" class="js-saved-reply-id js-resettable-field" value="" data-reset-value="">

    <textarea name="comment[body]"
              id="new_comment_field"
              
              placeholder="Leave a comment"
              aria-label="Comment body"
              class="form-control input-contrast comment-form-textarea js-comment-field js-improved-comment-field js-task-list-field js-quick-submit js-size-to-fit js-suggester-field js-quote-selection-target js-session-resumable"
              ></textarea>

        <p class="drag-and-drop">
    <span class="default">
        Attach files by dragging &amp; dropping or
        <input type="file" multiple="multiple" class="manual-file-chooser js-manual-file-chooser" aria-label="Attach files to your comment">
        <span class="btn-link manual-file-chooser-text">selecting them</span>.
    </span>
    <span class="loading">
      <img alt="" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" /> Uploading your files…
    </span>
    <span class="error bad-file">
      We don’t support that file type.
      <input type="file" multiple="multiple" class="manual-file-chooser js-manual-file-chooser">
      <span class="drag-and-drop-error-info">
        <button type="button" class="btn-link manual-file-chooser-text">Try again</button> with a
        PNG, GIF, JPG, DOCX, PPTX, XLSX, TXT, PDF, or ZIP.
      </span>
    </span>
    <span class="error bad-permissions">
      Attaching documents requires write permission to this repository.
      <input type="file" multiple="multiple" class="manual-file-chooser js-manual-file-chooser">
      <span class="drag-and-drop-error-info">
        <button type="button" class="btn-link manual-file-chooser-text">Try again</button> with a PNG, GIF, or JPG.
      </span>
    </span>
    <span class="error repository-required">
      We don’t support that file type.
      <input type="file" multiple="multiple" class="manual-file-chooser js-manual-file-chooser">
      <span class="drag-and-drop-error-info">
        <button type="button" class="btn-link manual-file-chooser-text">Try again</button> with a PNG, GIF, or JPG.
      </span>
    </span>
    <span class="error too-big">
      Yowza, that’s a big file.
      <input type="file" multiple="multiple" class="manual-file-chooser js-manual-file-chooser">
      <span class="drag-and-drop-error-info">
        <button type="button" class="btn-link manual-file-chooser-text">Try again</button> with a file smaller than 10MB.
      </span>
    </span>
    <span class="error empty">
      This file is empty.
      <input type="file" multiple="multiple" class="manual-file-chooser js-manual-file-chooser">
      <span class="drag-and-drop-error-info">
        <button type="button" class="btn-link manual-file-chooser-text">Try again</button> with a file that’s not empty.
      </span>
    </span>
    <span class="error hidden-file">
      This file is hidden.
      <input type="file" multiple="multiple" class="manual-file-chooser js-manual-file-chooser">
      <span class="drag-and-drop-error-info">
        <button type="button" class="btn-link manual-file-chooser-text">Try again</button> with another file.
      </span>
    </span>
    <span class="error failed-request">
      Something went really wrong, and we can’t process that file.
      <input type="file" multiple="multiple" class="manual-file-chooser js-manual-file-chooser">
      <span class="drag-and-drop-error-info">
        <button type="button" class="btn-link manual-file-chooser-text">Try again.</button>
      </span>
    </span>
  </p>


    <div class="suggester-container">
      <div class="suggester js-suggester js-navigation-container"
           data-url="/jxson/1784669/suggestions"
>
      </div>
    </div>
  </div>

  <div class="preview-content">
    <div class="comment">
  <div class="comment-body markdown-body js-preview-body">
    <p>Nothing to preview</p>
  </div>
</div>

  </div>

  <div class="float-left">
      <a class="tabnav-extra" href="https://guides.github.com/features/mastering-markdown/" target="_blank" data-ga-click="Markdown Toolbar, click, help">
        <svg aria-hidden="true" class="octicon octicon-markdown v-align-bottom" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M14.85 3H1.15C.52 3 0 3.52 0 4.15v7.69C0 12.48.52 13 1.15 13h13.69c.64 0 1.15-.52 1.15-1.15v-7.7C16 3.52 15.48 3 14.85 3zM9 11H7V8L5.5 9.92 4 8v3H2V5h2l1.5 2L7 5h2v6zm2.99.5L9.5 8H11V5h2v3h1.5l-2.51 3.5z"/></svg>
        Styling with Markdown is supported
      </a>
  </div>


  <div class="comment-form-error comment-form-bottom js-comment-update-error"></div>
</div>


      <div class="form-actions">
        <div id="partial-new-comment-form-actions">
  <button type="submit" class="btn btn-primary" data-disable-with data-disable-invalid>
    Comment
  </button>
</div>

      </div>
    </div>
</form></div>

        </div>
      </div>
    </div>
</div>
  </div>

  <div class="modal-backdrop js-touch-events"></div>
</div><!-- /.container -->

    </div>
  </div>

  </div>

      
<div class="container site-footer-container">
  <div class="site-footer " role="contentinfo">
    <ul class="site-footer-links float-right">
        <li><a href="https://github.com/contact" data-ga-click="Footer, go to contact, text:contact">Contact GitHub</a></li>
      <li><a href="https://developer.github.com" data-ga-click="Footer, go to api, text:api">API</a></li>
      <li><a href="https://training.github.com" data-ga-click="Footer, go to training, text:training">Training</a></li>
      <li><a href="https://shop.github.com" data-ga-click="Footer, go to shop, text:shop">Shop</a></li>
        <li><a href="https://github.com/blog" data-ga-click="Footer, go to blog, text:blog">Blog</a></li>
        <li><a href="https://github.com/about" data-ga-click="Footer, go to about, text:about">About</a></li>

    </ul>

    <a href="https://github.com" aria-label="Homepage" class="site-footer-mark" title="GitHub">
      <svg aria-hidden="true" class="octicon octicon-mark-github" height="24" version="1.1" viewBox="0 0 16 16" width="24"><path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"/></svg>
</a>
    <ul class="site-footer-links">
      <li>&copy; 2017 <span title="0.68551s from github-fe154-cp1-prd.iad.github.net">GitHub</span>, Inc.</li>
        <li><a href="https://github.com/site/terms" data-ga-click="Footer, go to terms, text:terms">Terms</a></li>
        <li><a href="https://github.com/site/privacy" data-ga-click="Footer, go to privacy, text:privacy">Privacy</a></li>
        <li><a href="https://github.com/security" data-ga-click="Footer, go to security, text:security">Security</a></li>
        <li><a href="https://status.github.com/" data-ga-click="Footer, go to status, text:status">Status</a></li>
        <li><a href="https://help.github.com" data-ga-click="Footer, go to help, text:help">Help</a></li>
    </ul>
  </div>
</div>



  <div id="ajax-error-message" class="ajax-error-message flash flash-error">
    <svg aria-hidden="true" class="octicon octicon-alert" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M8.865 1.52c-.18-.31-.51-.5-.87-.5s-.69.19-.87.5L.275 13.5c-.18.31-.18.69 0 1 .19.31.52.5.87.5h13.7c.36 0 .69-.19.86-.5.17-.31.18-.69.01-1L8.865 1.52zM8.995 13h-2v-2h2v2zm0-3h-2V6h2v4z"/></svg>
    <button type="button" class="flash-close js-flash-close js-ajax-error-dismiss" aria-label="Dismiss error">
      <svg aria-hidden="true" class="octicon octicon-x" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48z"/></svg>
    </button>
    You can't perform that action at this time.
  </div>


    <script crossorigin="anonymous" src="https://assets-cdn.github.com/assets/compat-91f98c37fc84eac24836eec2567e9912742094369a04c4eba6e3cd1fa18902d9.js"></script>
    <script crossorigin="anonymous" src="https://assets-cdn.github.com/assets/frameworks-9a826bf88546b5cbaf9bc7db0484ad9380dce1267e0e7553b9dd1510cadc61b6.js"></script>
    
    <script async="async" crossorigin="anonymous" src="https://assets-cdn.github.com/assets/github-3ca5cf1e25d896a142d351f61eeb1a0bc2aa6d547e0a331ea948875d11ffadaa.js"></script>
    
    
    
    
  <div class="js-stale-session-flash stale-session-flash flash flash-warn flash-banner d-none">
    <svg aria-hidden="true" class="octicon octicon-alert" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M8.865 1.52c-.18-.31-.51-.5-.87-.5s-.69.19-.87.5L.275 13.5c-.18.31-.18.69 0 1 .19.31.52.5.87.5h13.7c.36 0 .69-.19.86-.5.17-.31.18-.69.01-1L8.865 1.52zM8.995 13h-2v-2h2v2zm0-3h-2V6h2v4z"/></svg>
    <span class="signed-in-tab-flash">You signed in with another tab or window. <a href="">Reload</a> to refresh your session.</span>
    <span class="signed-out-tab-flash">You signed out in another tab or window. <a href="">Reload</a> to refresh your session.</span>
  </div>
  <div class="facebox" id="facebox" style="display:none;">
  <div class="facebox-popup">
    <div class="facebox-content" role="dialog" aria-labelledby="facebox-header" aria-describedby="facebox-description">
    </div>
    <button type="button" class="facebox-close js-facebox-close" aria-label="Close modal">
      <svg aria-hidden="true" class="octicon octicon-x" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48z"/></svg>
    </button>
  </div>
</div>


  </body>
</html>

