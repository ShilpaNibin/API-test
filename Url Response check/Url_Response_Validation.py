import http.client
import time
import urllib.request


def get_status_code(host):

    try:
        execution_started_on = time.process_time()
        conn = urllib.request.urlopen(host)
        elapsed_time = time.process_time() - execution_started_on

        print( '\n Time taken to get the response back from ['+ host +'] is : ' + str( elapsed_time ) )
        print( '\n Response Status code for ['+ host +'] is : ' + str( conn.getcode() ) )
        
        return True
        
    except Exception as e:

        print( '\n Response Status code for ['+ host +'] is : ' + str(e.code) + '\n' )
        return True

get_status_code("https://www.atg.world")
get_status_code("https://www.atg.world/about")


