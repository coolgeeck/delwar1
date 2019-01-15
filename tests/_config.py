# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

"""This file contains the configs needed for the tests"""

# You need to fill in the variables with names of the resources you already have
# When you are finished setting the configs then you can run test.cmd

# The create devops objects setting sets whether the test will run create commands. The default is false
CREATE_DEVOPS_OBJECTS = False

# Specify the name of your already created devops objects
ORGANIZATION_NAME = 'colbys-donut-pizza'
PROJECT_NAME = 'donut-pizza-2'
REPOSITORY_NAME = 'donut-pizza-2'
SERVICE_ENDPOINT_NAME = ORGANIZATION_NAME + PROJECT_NAME
GITHUB_REPOSITORY_NAME = 'python_simple_functionapp_tester'

BUILD_DEFINITION_NAME_GIT = 'github-test-3'
BUILD_DEFINITION_NAME = 'normal-test-1'
RELEASE_DEFINITION_NAME = 'release blah'

# Do not change this from default.
POOL_NAME = 'Default'

# Specify the details of your azure functions resource
FUNCTIONAPP_NAME = 'dolk-devops-python'
SUBSCRIPTION_NAME = 'dolk-devops-python'
STORAGE_NAME = 'dolkdevops-9283'
RESOURCE_GROUP_NAME = 'dolk-devops-python'