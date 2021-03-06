############################################################
#
# Autogenerated by the KBase type compiler -
# any changes made here will be overwritten
#
############################################################

from __future__ import print_function
# the following is a hack to get the baseclient to import whether we're in a
# package or not. This makes pep8 unhappy hence the annotations.
try:
    # baseclient and this client are in a package
    from .baseclient import BaseClient as _BaseClient  # @UnusedImport
except:
    # no they aren't
    from baseclient import BaseClient as _BaseClient  # @Reimport


class gaprice_convert_assy_file_to_contigs(object):

    def __init__(
            self, url=None, timeout=30 * 60, user_id=None,
            password=None, token=None, ignore_authrc=False,
            trust_all_ssl_certificates=False,
            auth_svc='https://kbase.us/services/authorization/Sessions/Login'):
        if url is None:
            raise ValueError('A url is required')
        self._service_ver = None
        self._client = _BaseClient(
            url, timeout=timeout, user_id=user_id, password=password,
            token=token, ignore_authrc=ignore_authrc,
            trust_all_ssl_certificates=trust_all_ssl_certificates,
            auth_svc=auth_svc)

    def convert(self, params, context=None):
        """
        :param params: instance of type "ConvertParams" (Input parameters for
           the conversion function. string workspace_name - the name of the
           workspace from which to take input and store output. string
           assembly_file - the name of the input KBaseFile.AssemblyFile to
           convert to a ContigSet. string output_name - the name for the
           produced ContigSet.) -> structure: parameter "workspace_name" of
           String, parameter "assembly_file" of String, parameter
           "output_name" of String
        :returns: instance of type "ConvertOutput" (Output parameters the
           conversion. string report_name - the name of the
           KBaseReport.Report workspace object. string report_ref - the
           workspace reference of the report.) -> structure: parameter
           "report_name" of String, parameter "report_ref" of String
        """
        return self._client.call_method(
            'gaprice_convert_assy_file_to_contigs.convert',
            [params], self._service_ver, context)
