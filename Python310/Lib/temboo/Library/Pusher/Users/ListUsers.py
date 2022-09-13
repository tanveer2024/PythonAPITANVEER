# -*- coding: utf-8 -*-

###############################################################################
#
# ListUsers
# Retrieves IDs for users currently subscribed to a presence channel.
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

class ListUsers(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ListUsers Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(ListUsers, self).__init__(temboo_session, '/Library/Pusher/Users/ListUsers')


    def new_input_set(self):
        return ListUsersInputSet()

    def _make_result_set(self, result, path):
        return ListUsersResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListUsersChoreographyExecution(session, exec_id, path)

class ListUsersInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ListUsers
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AppID(self, value):
        """
        Set the value of the AppID input for this Choreo. ((required, string) The application ID provided by Pusher.)
        """
        super(ListUsersInputSet, self)._set_input('AppID', value)
    def set_AppKey(self, value):
        """
        Set the value of the AppKey input for this Choreo. ((required, string) The authenticaion key provided by Pusher.)
        """
        super(ListUsersInputSet, self)._set_input('AppKey', value)
    def set_AppSecret(self, value):
        """
        Set the value of the AppSecret input for this Choreo. ((required, string) The authentication secret provided by Pusher.)
        """
        super(ListUsersInputSet, self)._set_input('AppSecret', value)
    def set_ChannelName(self, value):
        """
        Set the value of the ChannelName input for this Choreo. ((required, string) The name of the channel that the users are subscribed to.)
        """
        super(ListUsersInputSet, self)._set_input('ChannelName', value)

class ListUsersResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ListUsers Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Pusher.)
        """
        return self._output.get('Response', None)

class ListUsersChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return ListUsersResultSet(response, path)
