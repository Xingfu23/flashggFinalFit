# FLASHgg Final Fits (lite)
Welcome to the new Final Fits package. Here lies a a series of scripts which are used to run the final stages of the CMS Hgg analysis: signal modelling, background modelling, datacard creation and final statistical interpretation and final result plots.

## Download and setup instructions

```
export SCRAM_ARCH=slc7_amd64_gcc700
cmsrel CMSSW_10_2_13
cd CMSSW_10_2_13/src
cmsenv
git cms-init

# Install the GBRLikelihood package which contains the RooDoubleCBFast implementation
git clone git@github.com:jonathon-langford/HiggsAnalysis.git
# Install Combine as per the documentation here: cms-analysis.github.io/HiggsAnalysis-CombinedLimit/
git clone git@github.com:cms-analysis/HiggsAnalysis-CombinedLimit.git HiggsAnalysis/CombinedLimit
# Install Combine Harvester for parallelizing fits
git clone https://github.com/cms-analysis/CombineHarvester.git CombineHarvester

# Compile external libraries
cmsenv
scram b -j 9

# Install Flashgg Final Fit packages
git clone -b dev_runII_102x git@github.com:cms-analysis/flashggFinalFit.git
cd flashggFinalFit/
```

In every new shell please run the following to add commonTools and commonObjects to PYTHONPATH:
```
./setup.sh
```

## Contents

The FLASHgg Finals Fits package contains several subfolders which are used for the following steps:

* Create the Signal Model (see `Signal` dir)
* Create the Background Model (see `Background` dir)
* Generate a Datacard (see `Datacard` dir)
* Running fits with combine (see `Combine` dir)
* Run `combine` and generate statistical interpretation plots. (see `Plots/FinalResults` dir)

Each of the relevant folders are documented with specific `README.md` files. Some (temporary) instructions can be found in this [google docs](https://docs.google.com/document/d/1NwUrPvOZ2bByaHNqt_Fr6oYcP7icpbw1mPlw_3lHhEE/edit)
