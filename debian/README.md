In order to build this on OBS, follow these steps:

1. Create a login for yourself at build.opensuse.org.
2. Either use your home project or create a subproject, and select
    Repositories matching those of [home:cvmfs:contrib](https://build.opensuse.org/repositories/home:cvmfs:contrib).  Edit each repository so the
    Architectures and Additional package repositories match those of
    home:cvmfs:contrib.
3. On the Overview tab for the project, select "Branch existing package".
    Use "home:cvmfs:contrib" as "Name of original project" and 
    "cvmfs-config-egi" as "Name of package in original project" and select
    "Create Branch".  It should then build, and you can reload the page
    until it finishes.  You can also select the "\_service" link, click
    "show latest", and edit the source of the paths to be from
    different sources if you want to and click "Save".
4. Note that only Debian/Ubuntu repos are built in "home:cvmfs:contrib"
    for this package; for the rpms see "home:cvmfs:contrib-egi" and
    either create a separate branch of that or merge in the portions
    of "\_service" from there to build those together in your package.
5.  To find the built packages, click on Repositories back in the
    project and select "Go to download repository".
