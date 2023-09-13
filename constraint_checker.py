import pymel.core as pm

# pm.delete(parent_cnst_list, orient_cnst_list, point_cnst_list)  # Only run this if you want to delete constraints

# YOU CAN RUN THIS FIRST TO CHECK IF THE CONSTRAINTS ARE AVAILABLE;
# Build type lists of constraints using ls commands
parent_cnst_list = pm.ls(type="parentConstraint")
orient_cnst_list = pm.ls(type="orientConstraint")
point_cnst_list = pm.ls(type="pointConstraint")

# Loop through our lists of constraints
for cnst in parent_cnst_list:
    trans = []
    rot = []
    for attr in "XYZ":
        # Check for translate connections
        t = cnst.attr("constraintTranslate" + attr).listConnections()
        r = cnst.attr("constraintRotate" + attr).listConnections()

        # Add attribute to the list if it is missing an attribute connection
        if not t:
            trans.append(attr.lower())
        if not r:
            rot.append(attr.lower())

        # Get driver and driven objects
        driver = pm.parentConstraint(cnst, query=True, targetList=True)[0]
        driven = cnst.replace("_parentConstraint1", "")

    # Print out the Python command for parent constraint
    # Use the trans list to address skipped axes
    print("pm.parentConstraint('{}', '{}', skipRotate='{}', skipTranslate='{}', mo=True)".format(
        driver, driven, "".join(rot), "".join(trans)))

# Loop through our lists of constraints
for cnst in orient_cnst_list:
    rot = []
    for attr in "XYZ":
        # Check for rotate connections
        r = cnst.attr("constraintRotate" + attr).listConnections()

        # Add attribute to the list if it is missing an attribute connection
        if not r:
            rot.append(attr.lower())

        # Get driver and driven objects
        driver = pm.orientConstraint(cnst, query=True, targetList=True)[0]
        driven = cnst.replace("_orientConstraint1", "")

    # Print out the Python command for orient constraint
    print("pm.orientConstraint('{}', '{}', skip='{}', mo=True)".format(
        driver, driven, "".join(rot)))

# Loop through our lists of constraints
for cnst in point_cnst_list:
    trans = []
    for attr in "XYZ":
        # Check for translate connections
        r = cnst.attr("constraintTranslate" + attr).listConnections()

        # Add attribute to the list if it is missing an attribute connection
        if not r:
            trans.append(attr.lower())

        # Get driver and driven objects
        driver = pm.pointConstraint(cnst, query=True, targetList=True)[0]
        driven = cnst.replace("_pointConstraint1", "")

    # Print out the Python command for point constraint
    print("pm.pointConstraint('{}', '{}', skip='{}', mo=True)".format(
        driver, driven, "".join(trans)))
