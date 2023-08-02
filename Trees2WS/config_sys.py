# Input config file for running trees2ws

trees2wsCfg = {

  # Name of RooDirectory storing input tree
  'inputTreeDir':'tagsDumper/trees',

  # Variables to be added to dataframe: use wildcard * for common strings
  'mainVars':["CMS_hgg_mass","weight","dZ", "*sigma", "centralObjectWeight"], # Var for the nominal RooDataSets
  'dataVars':["CMS_hgg_mass","weight"], # Vars to be added for data
  'stxsVar':'stage1p2bin',
  'notagVars':["weight"], # Vars to add to NOTAG RooDataset
  'systematicsVars':["CMS_hgg_mass","weight"], # Variables to add to sytematic RooDataHists
  'theoryWeightContainers':{'alphaSWeights':2,'scaleWeights':9,'pdfWeights':60},

  # List of systematics: use string YEAR for year-dependent systematics
  'systematics':['FNUFEB', 'FNUFEE', 'JEC', 'JER', 'MCScaleGain1EB', 'MCScaleGain6EB', 'MCScaleHighR9EB', 'MCScaleHighR9EE', 'MCScaleLowR9EB', 'MCScaleLowR9EE', 
                 'MCSmearHighR9EBPhi', 'MCSmearHighR9EBRho', 'MCSmearHighR9EEPhi', 'MCSmearHighR9EERho', 'MCSmearLowR9EBPhi', 'MCSmearLowR9EBRho', 'MCSmearLowR9EEPhi', 'MCSmearLowR9EERho',
                 'MaterialCentralBarrel', 'MaterialForward', 'MaterialOuterBarrel', 'MvaShift', 'PUJIDShift', 
                 'ShowerShapeHighR9EB', 'ShowerShapeHighR9EE', 'ShowerShapeLowR9EB', 'ShowerShapeLowR9EE', 'SigmaEOverEShift',
                 'metJecUncertainty', 'metJerUncertainty', 'metPhoUncertainty', 'metUncUncertainty'],

  # Analysis categories: python list of cats or use 'auto' to extract from input tree
  'cats':'auto'
}
