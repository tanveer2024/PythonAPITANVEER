# -*- coding: utf-8 -*-

###############################################################################
#
# GetAccount
# Retrieves information about a user's account.
#
# Python versions 2.6, 2.7, 3.x
#
# Copyright 2014, Temboo Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied. See the License for the specific
# language governing permissions and limitations under the License.
#
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetAccount(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetAccount Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetAccount, self).__init__(temboo_session, '/Library/Dropbox/Users/GetAccount')


    def new_input_set(self):
        return GetAccountInputSet()

    def _make_result_set(self, result, path):
        return GetAccountResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetAccountChoreographyExecution(session, exec_id, path)

class GetAccountInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetAccount
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The access token for a specific Dropbox user.)
        """
        super(GetAccountInputSet, self)._set_input('AccessToken', value)
    def set_AccountID(self, value):
        """
        Set the value of the AccountID input for this Choreo. ((required, string) A user's account identifier.)
        """
        super(GetAccountInputSet, self)._set_input('AccountID', value)

class GetAccountResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetAccount Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    pass

class GetAccountChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetAccountResultSet(response, path)
