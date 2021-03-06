# settings for various experiments

from FlowCytometryTools import FCMeasurement, FCPlate, PolyGate


class settings(object):
    def __init__(self, directory, toFilter, liveGate, singletGate, makePlate):
        self.directory = directory
        self.toFilter = toFilter
        self.liveGate = liveGate
        self.singletGate = singletGate
        self.makePlate = makePlate


def makeSettings(run):
    #returns the settings for the specified run
    if run == 'titrationD2':
        # NCS titration day1
        directory = './titration'
        toFilter = [6]

        liveGate = PolyGate([(8.924e+04, 2.587e+05), (2.844e+04, 3.233e+04), (4.515e+04, 1.601e+04), (2.601e+05, 1.241e+05), (2.605e+05, 2.608e+05), (8.924e+04, 2.587e+05)],('FSC-A', 'SSC-A'), region='in', name='gate1')
        singletGate = PolyGate([(3.139e+04, 3.590e+04), (1.941e+05, 1.726e+05), (2.481e+05, 1.733e+05), (3.139e+04, 2.3e+04), (3.139e+04, 3.590e+04)], ('FSC-A', 'FSC-H'), region='in', name='gate1')

        def makePlate(data):
            ## makes the plate layout with the current data
            nameMap = {'par-1': data[1], 'par-2': data[3], 'par-4': data[4], 'par-8': data[5], 'par-16':data[2], 'par-ctl': data[6], 'par-ctl-plate': data[7],
                'tag-1': data[8], 'tag-2': data[10], 'tag-4': data[12], 'tag-8': data[13], 'tag-16': data[9], 'tag-32': data[11], 'tag-ctl': data[14],
                'tag-rep-2': data[16], 'tag-rep-4': data[17], 'tag-rep-8': data[18], 'tag-rep-16': data[15]}

            plateMap = {'par-1': ('A', 1), 'par-2': ('A', 2), 'par-4': ('A', 3), 'par-8': ('A', 4), 'par-16': ('A', 5), 'par-ctl': ('A', 6), 'par-ctl-plate': ('A', 7),
                'tag-1': ('B', 1), 'tag-2': ('B', 2), 'tag-4': ('B', 3), 'tag-8': ('B', 4), 'tag-16': ('B', 5), 'tag-32': ('B', 6), 'tag-ctl': ('B', 7),
                'tag-rep-2': ('C', 2), 'tag-rep-4': ('C', 3), 'tag-rep-8': ('C', 4), 'tag-rep-16': ('C', 5)
            }

            plateView = FCPlate('aggregated',nameMap, None, shape=(3,7), positions=plateMap)

            return plateView


    if run == 'titrationD4':
        #NCS titration day 2
        directory = './titrationD4'
        toFilter = []

        liveGate = PolyGate([(1.501e+04, 2.513e+04), (8.787e+04, 2.615e+05), (2.605e+05, 2.615e+05), (2.619e+05, 1.593e+05), (5.074e+04, 7.421e+03), (2.754e+04, 8.102e+03), (1.547e+04, 2.445e+04)], ('FSC-A', 'SSC-A'), region='in', name='gate1')
        singletGate = PolyGate([(1.645e+04, 1.105e+04), (1.733e+04, 2.295e+04), (1.621e+05, 1.481e+05), (2.158e+05, 1.481e+05), (2.393e+04, 1.069e+04), (1.733e+04, 1.069e+04)], ('FSC-A', 'FSC-H'), region='in', name='gate1')

        def makePlate(data):
            ## makes the plate layout with the current data
            nameMap = {'par-1': data[0], 'par-2': data[2], 'par-4': data[4], 'par-8': data[5], 'par-16':data[1], 'par-32':data[3], 'par-ctl': data[6],
                'tag-1': data[7], 'tag-2': data[9], 'tag-4': data[11], 'tag-8': data[12], 'tag-16': data[8], 'tag-32': data[10], 'tag-ctl': data[13] }

            plateMap = {'par-1': ('A', 1), 'par-2': ('A', 2), 'par-4': ('A', 3), 'par-8': ('A', 4), 'par-16': ('A', 5), 'par-32': ('A', 6), 'par-ctl': ('A', 7),
                'tag-1': ('B', 1), 'tag-2': ('B', 2), 'tag-4': ('B', 3), 'tag-8': ('B', 4), 'tag-16': ('B', 5), 'tag-32': ('B', 6), 'tag-ctl': ('B', 7),
            }

            plateView = FCPlate('aggregated',nameMap, None, shape=(2,7), positions=plateMap)

            return plateView


    if run[:-3] == 'timecourse':
        #Initial timecourse experiment
        directory = './timecourse/'+run[-3:]
        toFilter = []

        liveGate = PolyGate([(5.104e+04, 2.257e+03), (2.792e+04, 2.725e+03), (1.451e+04, 1.147e+04), (2.930e+04, 2.162e+04), (2.610e+05, 2.254e+05), (2.619e+05, 3.869e+04), (5.274e+04, 2.583e+03), (5.274e+04, 2.583e+03)], ('FSC-A', 'SSC-A'), region='in', name='gate1')
        singletGate = PolyGate([(2.463e+04, 3.052e+04), (2.257e+05, 2.116e+05), (2.588e+05, 2.121e+05), (2.588e+05, 1.725e+05), (4.248e+04, 2.238e+04), (2.463e+04, 3.052e+04), (2.463e+04, 3.052e+04)], ('FSC-A', 'FSC-H'), region='in', name='gate1')


        def makePlate(data):
            ## makes the plate layout with the current data
            nameMap = {'d0.-': data[0], 
                        'd2.-': data[1], 'd2.+': data[2],
                        'd4.--': data[3], 'd4.-+': data[4], 'd4.+-': data[5], 'd4.++': data[6],
                        'd8.---': data[7], 'd8.--+': data[8], 'd8.-+-': data[9], 'd8.-++': data[10], 'd8.+--': data[11], 'd8.+-+': data[12], 'd8.++-': data[13], 'd8.+++': data[14]
            }

            plateMap = {'d0.-': ('A', 1), 
                        'd2.-': ('A', 2), 'd2.+': ('B', 2),
                        'd4.--': ('A', 3), 'd4.-+': ('B', 3), 'd4.+-': ('C', 3), 'd4.++': ('D', 3),
                        'd8.---': ('A', 4), 'd8.--+': ('B', 4), 'd8.-+-': ('C', 4), 'd8.-++': ('D', 4), 'd8.+--': ('E', 4), 'd8.+-+': ('F', 4), 'd8.++-': ('G', 4), 'd8.+++': ('H', 4)
            }

            plateView = FCPlate('aggregated',nameMap, None, shape=(8,4), positions=plateMap)

            return plateView

    if run == 'finalRun':
        directory = './finalRun'
        toFilter = []

        #liveGate = PolyGate([(2.943e+04, 1.232e+04), (7.212e+04, 1.307e+04), (2.614e+05, 1.476e+05), (2.601e+05, 2.8e+05), (8.651e+04, 2.8e+05), (1.551e+04, 4.355e+04), (1.923e+04, 1.530e+04), (2.897e+04, 1.232e+04), (3.129e+04, 1.307e+04)], ('FSC-A', 'SSC-A'), region='in', name='gate1')
        liveGate = PolyGate([(2.943e+04, 1.232e+04), (7.212e+04, 1.307e+04), (2.614e+05, 1.476e+05), (2.601e+05, 2.6e+05), (8.651e+04, 2.6e+05), (1.551e+04, 4.355e+04), (1.923e+04, 1.530e+04), (2.897e+04, 1.232e+04), (3.129e+04, 1.307e+04)], ('FSC-A', 'SSC-A'), region='in', name='gate2')
        # top is all data, bottom is fitting data

        singletGate = PolyGate([(1.2e+04, 1.5e+04), (2.257e+05, 2.116e+05), (2.588e+05, 2.121e+05), (2.588e+05, 1.725e+05), (4.248e+04, 2.238e+04), (1.2e+04, 1.5e+04), (1.2e+04, 1.5e+04)], ('FSC-A', 'FSC-H'), region='in', name='gate2')


        #offGate = PolyGate([(10**3.435e+00, 10**5.415e+00), (10**2.888e+00, 10**4.878e+00), (10**2.748e+00, 10**4.621e+00), (10**2.534e+00, 10**4.314e+00), (10**1.951e+00, 10**4.206e+00), (10**1.821e+00, 10**4.391e+00), (10**2.982e+00, 10**5.419e+00), (10**3.435e+00, 10**5.419e+00)], ('M Cherry-A', 'SSC-A'), region='in', name='gate1')


        def makePlate(data):
            ## makes the plate layout with the current data
            nameMap = {'d0.-': data[0], 
                        'd2.-': data[2], 'd2.+': data[1], 
                        'd4.--': data[6], 'd4.-+': data[5], 'd4.+-': data[4], 'd4.++': data[3],
                        'd8.---': data[14], 'd8.--+': data[13], 'd8.-+-': data[12], 'd8.-++': data[11], 'd8.+--': data[10], 'd8.+-+': data[9], 'd8.++-': data[8], 'd8.+++': data[7]
            }

            plateMap = {'d0.-': ('A', 1), 
                        'd2.-': ('A', 2), 'd2.+': ('B', 2), 
                        'd4.--': ('A', 3), 'd4.-+': ('B', 3), 'd4.+-': ('C', 3), 'd4.++': ('D', 3),
                        'd8.---': ('A', 4), 'd8.--+': ('B', 4), 'd8.-+-': ('C', 4), 'd8.-++': ('D', 4), 'd8.+--': ('E', 4), 'd8.+-+': ('F', 4), 'd8.++-': ('G', 4), 'd8.+++': ('H', 4)
            }

            plateView = FCPlate('aggregated',nameMap, None, shape=(8,4), positions=plateMap)

            return plateView


    if run == 'quorumPilot':
        directory = './quorumPilot'
        toFilter = []

        liveGate = PolyGate([(1.148e+04, 2.789e+04), (2.148e+04, 6.104e+03), (6.696e+04, 6.104e+03), (2.596e+05, 1.471e+05), (2.591e+05, 2.608e+05), (1.004e+05, 2.574e+05), (1.148e+04, 2.721e+04), (1.148e+04, 2.721e+04)], ('FSC-A', 'SSC-A'), region='in', name='live')
        singletGate = PolyGate([(2.055e+04, 2.754e+04), (2.797e+04, 1.781e+04), (2.587e+05, 1.556e+05), (2.582e+05, 1.991e+05), (2.211e+05, 2.001e+05), (2.055e+04, 2.806e+04)], ('FSC-A', 'FSC-H'), region='in', name='singlets')

        def makePlate(data):
            ## makes the plate layout with the current data
            nameMap = {'mixed0': data[0], 'mixed100': data[1], 'mixed20': data[2], 'mixed40': data[3], 'mixed60': data[4], 'mixed80': data[5], 
                        'pure100': data[6],'pure20': data[7], 'pure40': data[8], 'pure60': data[9], 'pure80': data[10] }

            plateMap = {'mixed0': ('A', 1), 'mixed20': ('A', 2), 'mixed40': ('A', 3), 'mixed60': ('A', 4), 'mixed80': ('A', 5), 'mixed100': ('A', 6), 
                        'pure20': ('B', 2), 'pure40': ('B', 3), 'pure60': ('B', 4), 'pure80': ('B', 5), 'pure100': ('B', 6) }

            plateView = FCPlate('aggregated',nameMap, None, shape=(2,6), positions=plateMap)

            return plateView


    output = settings(directory, toFilter, liveGate, singletGate, makePlate)
    return output



