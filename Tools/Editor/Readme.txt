================================
==      SURREAL SOFTWARE      ==
==  RIOT ENGINE LEVEL EDITOR  ==
==     AND MODELING TOOLS     ==
==                            ==
==      "Drakan Edition"      ==
==                            ==
==    README.TXT (11/23/99)   ==
================================

For the latest Drakan Editor information, go to http://www.surreal.com/tech

To inquire about licensing the Surreal Software Riot Engine and Tools for
commercial use, send e-mail to licensing@surreal.com


NEW: (See additional sections on plug-ins and the 3D modeler, added 11/23/99).


-----------------------------------------------------------------------------------

IMPORTANT-PLEASE READ CAREFULLY.  The use of this "Drakan Level Editor" software (the "Program") is subject to the following terms and conditions (this "Agreement").  By installing or otherwise using the Program, you agree to be legally bound by the terms of this Agreement.  If you do not agree to the terms of this Agreement, you are not authorized to install or otherwise use the Program in any way.

The Program is protected by the copyright laws of the United States, international copyright treaties and conventions and other laws.

The Program is licensed and this Agreement confers no title or ownership to the Program or any derivative work based on the Program, all of which are retained by Surreal Software and Psygnosis, Ltd.

The Program may be freely distributed by you as long as the original setup and files remain exactly the same and are not modified in any way and as long as you do not, directly or indirectly, charge a fee in connection with distributing a copy of the Program.  Any content or electronic media OF ANY FORM that is created using the Program is freely transferable by you, provided that you do not, directly or indirectly, charge a fee for such content or media.  Commercial use of the Program and its content (including any modifications made by you) will violate International copyright laws and will subject you to possible civil and criminal penalties.

The Program is made available to you on an "as-is" basis, without any warranty of any kind or nature, including any implied warranties of fitness for a particular purpose, merchantability or non-infringement.  No support of any kind for the Program is provided or made available.
Surreal Software, Inc. and Psygnosis, Ltd. are not responsible for any damages
that may have been caused as a result of using the Program.  All use
of the Program is at your sole risk.

(c) 1999 Surreal Software, Inc.  All rights reserved.  Surreal Software and the Surreal Software logo are (tm) of Surreal Software, Inc.

Drakan: Order of the Flame is (c) 1999 Psygnosis Ltd.  Developed by Surreal Software, Inc.  Drakan Order of the Flame, Psygnosis, and the Psygnosis logo are (tm) or (r) of Psygnosis, Ltd.  All rights reserved.

-----------------------------------------------------------------------------------



------------------------------------------
INTRODUCTION
------------------------------------------

This document will be VERY brief. More information will be available from other
users and from Surreal as time goes on. We recommend that you experiment and play
with all the windows and features of the editor to figure stuff out. There is some
online help down in the status bar at the bottom of the main window.

More tools may be released at a later date which will allow model and texture
editing, as well as REO exporters for 3D Studio MAX.


------------------------------------------
THE 3D VIEW
------------------------------------------

In this version of the editor, the 3D view is used for three things: viewing the
level as it would appear in the game, creating and viewing STOMP sequences
(cut-scenes), and painting textures onto the landscape. You cannot move objects
or edit geometry from within this window. These operations occur in the main,
top-down view.

To bring up the 3D view, select "Window->3D View" from the Main Menu. You should
get a gray window. This is because the camera is positioned at the origin of the
level. Move the camera onto the level by selecting the Camera Tool and
left-clicking on the location you want to place the camera on the top-down view.
The 3D view should then display that location on the level.

To fly around in the 3D view, select the "Riot Engine" window and then press
the SPACE-BAR to toggle between fly mode and texture painting mode.

The 3D view requires more memory than the basic editor. The 3D view transfers its
data from the Level Editor, so things may be delayed by quite a bit as you edit.
So be patient, wait for the operation to complete in the 3D view.

The 3D view requires a 3D accelerator card that supports 3D-in-a-window. So a
Voodoo 2 card will not work. Nvidia, Voodoo 3, ATI Rage, Matrox G400 and others
work great.


------------------------------------------
EXPORT PLUG-INS FOR 3D MODELING TOOLS
------------------------------------------

3D STUDIO MAX 2.x or 3.0

Put the export files from the proper directory in the "Editor\Plug-ins\" folder
into the plug-ins directory where you have 3D Studio Max installed. Then you
can export an object (after selecting it) by choosing REO format. This model
can then be read into the modeler to apply bounding information or texture
mapping information.

SOFTIMAGE

Copy the *.cus files into the existing "custom\tools" folder in Softimage.
Copy the *.dll files into the existing "custom\bin" folder in Softimage.
To use it, go to the Tools module, select Export->Objects->SoftToREO.


------------------------------------------
THE SURREAL SOFTWARE 3D MODELER
------------------------------------------

The modeler allows you to texture-map and add bounding information to 3D models
in the Riot Engine format (REO). These models can then be imported or exported
into the Level Editor for use in any Drakan level. A model must be properly
bounded by hand in the 3D modeler in order to have proper collision-detection
within the game. The modeler can delete polygons and has other VERY basic
modeling tools, but it not meant as a constructive modeler. It is recommended
that new models be created in 3D Studio Max or SoftImage, and then textured
and bound using the 3D Modeler before being imported into the Level Editor.


------------------------------------------
TIPS FOR IMPROVED EDITING
------------------------------------------

+ Start by modifying an existing Drakan level. All levels require certain objects
  like players and cameras and sky boxes, and the game will not work without them.
+ Learn by example. Load Drakan levels into the editor and figure them out before
  making your own levels.
+ Back up the existing Drakan Databases (Common, Mountain World, etc) before
  editing them. If you change existing Databases or levels, you will not be able
  to play multiplayer games or load in previous saved games. Try to create new
  databases and levels for the changes you make, do not modify the existing
  Drakan databases.
+ Make sure the Engine is in Developer Mode so you can see debugging messages. To
  enable these options, hold down SHIFT when running Drakan. A new Developer TAB
  will appear in the Engine Options dialog. You must be in developer mode to
  load in new levels. You can also load your level using the +level "file"
  command-line option.
+ If you want to edit object, make sure you are in Object Edit mode. To edit
  Layers, make sure you are in Layer Edit mode. There are also shortcut icons
  at the bottom right of the main window.
+ Hide all the objects while you are editing layers to speed up everying. To do
  this, go to Object Editing Mode, click "Edit->Select All", then click "View->
  Hide Selected Objects".
+ Open up as many windows as you can. Always keep Databases and
+ You should have at least 64 MB memory, 128 MB recommended.
+ 3D view is delayed from operations you perform in the main editor. When changing
  view options and editing geometry or textures, make sure you wait for the
  changes to take effect in the 3D view before performing the next operation or
  redoing the one you just did.
+ 3D view will be faster if you disable Layer Textures from the View Options,
  3D View Tab and also if you hide all objects.
+ To work more efficiently with Drakan levels, it is usually easier to hide certain
  objects like Sounds and Detectors. For example, to hide all Detector objects,
  select any Detector, and choose "Select All Similar" or press Ctrl+Shift+E and
  then select "Hide Selected Objects" or press Ctrl+H.
+ Under Level Properties, turn down the number of UNDO levels if you do not have
  much memory or are working with large levels. A large number of UNDO levels will
  cause hard-drive thrashing.
+ Right click on everything. Most everything has a shortcut menu with common
  operations.
+ When texture painting, to paint a NULL texture, select the background of the
  textures view in the Databases window.
+ There is a list of hotkeys in the Help menu.
+ Check http://www.surreal.com/tech for the latest level editor updates.
