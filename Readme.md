# VnMarMoT for Vietnamese POS tagging

VnMarMoT is a pre-trained [MarMoT](http://cistern.cis.lmu.de/marmot/) model for Vietnamese Part-of-Speech (POS) tagging. VnMarMoT obtains a state-of-the-art POS tagging accuracy at **95.88%** on the benchmark Vietnamese treebank, with a tagging speed at **25K** words/second computed on a personal computer of Intel Core i7 2.2 GHz. See more details in the following paper: 

	@InProceedings{NguyenVNDJ-ALTA-2017,
	author={Dat Quoc Nguyen and Thanh Vu and Dai Quoc Nguyen and Mark Dras and Mark Johnson},
	title={{From Word Segmentation to POS Tagging for Vietnamese}},
	booktitle = {Proceedings of the Australasian Language Technology Association Workshop 2017},
	year={2017}
	}
	
Please cite the paper above when VnMarMoT is used to produce published results or incorporated into other software. 

## Usage
    
    // Convert a word-segmented corpus into column-based representation
    $ python Utility.py test.txt test.col.txt
    // Perform POS tagging using VnMarMoT
    $ java -cp marmot.jar marmot.morph.cmd.Annotator --model-file vn.marmot --test-file form-index=0,test.col.txt --pred-file test.pred.txt