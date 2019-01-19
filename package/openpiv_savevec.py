import numpy as np

def save_openpiv_vec(filename,data,xUnits,tUnits,numrows,numcols):
    """
    % data is called res in OpenPIV and it shall be N rows x 5 cols
    % in print, it's rotated to 5 rows x N cols
    if size(data,2) == 5
        data = data';
    elseif size(data,1) ~= 5
        error('Wrong number of columns');
    end

    % print the header
    % example of the VEC header
    % TITLE="E:\2CM_FP500_5%G_68K\C001H001S0015CC\Soapfilmone\Analysis\Run00000
    % 1.T000.D000.P000.H001.L.vec" VARIABLES="X mm", "Y mm", "U m/s", "V m/s",
    % "CHC", DATASETAUXDATA Application="PIV" DATASETAUXDATA
    % SourceImageWidth="1024" DATASETAUXDATA SourceImageHeight="1024"
    % DATASETAUXDATA MicrometersPerPixelX="19.530001" DATASETAUXDATA
    % MicrometersPerPixelY="19.530001" DATASETAUXDATA LengthUnit="mm"
    % DATASETAUXDATA OriginInImageX="0.000000" DATASETAUXDATA
    % OriginInImageY="0.000000" DATASETAUXDATA
    % MicrosecondsPerDeltaT="2000.000000" DATASETAUXDATA TimeUnit="ms"
    % DATASETAUXDATA SecondaryPeakNumber="0" DATASETAUXDATA
    % DewarpedImageSource="0" ZONE I=63, J=63, F=POINT
    """
    
    # check the data is of the right size
    if data.shape[1] == 5:
        data = data.T
    elif data.shape[1] != 5:
        raise ValueError('Wrong number of columns')
    
    zone = 'ZONE I={:d}, J={:d}'.format(numrows,numcols)
    title = 'TITLE={}\n'.format(filename.split('.')[0])
    variables = 'VARIABLES= "X {0}", "Y {0}", "U {0}/{1}","V {0}/{1}", "CHC" \n'.format(xUnits,tUnits)
    
    header = title + variables + zone
    np.savetxt(filename,data.T, fmt='%3d %3d %7.4f %7.4f %7.4f', header=header, comments='')