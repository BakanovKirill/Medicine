from django.db import connection

from medicine.models import DatabaseQuery

class QueryCountDebugMiddleware(object):
    """
    This middleware will log the number of queries run
    and the total time taken for each request (with a
    status code of 200). It does not currently support
    multi-db setups.
    """
    def process_response(self, request, response):
        if response.status_code == 200:
            for query in connection.queries:
                sql = query.get('sql',False)
                if sql and not 'INSERT INTO "medicine_databasequery"' in sql:
                    DatabaseQuery.objects.create(query=sql)

        return response