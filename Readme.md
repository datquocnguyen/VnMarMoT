# VnMarMoT for Vietnamese POS tagging

VnMarMoT is a pre-trained [MarMoT](http://cistern.cis.lmu.de/marmot/) model for Vietnamese Part-of-Speech (POS) tagging. VnMarMoT obtains a state-of-the-art POS tagging accuracy at **95.88%** on the benchmark Vietnamese treebank, with a tagging speed at **25K** words/second computed on a personal computer of Intel Core i7 2.2 GHz. See more details in our paper: 

Dat Quoc Nguyen, Thanh Vu, Dai Quoc Nguyen, Mark Dras and Mark Johnson. **2017**. [From Word Segmentation to POS Tagging for Vietnamese](http://aclweb.org/anthology/U17-1013). In *Proceedings of the 15th Annual Workshop of the Australasian Language Technology Association*, [ALTA 2017](http://alta2017.alta.asn.au), pages 108-113. [[.bib]](http://aclweb.org/anthology/U17-1013.bib)
	
**Please cite** our ALTA 2017 paper when VnMarMoT is used to produce published results or incorporated into other software. 

VnMarMoT has also been incorporated into our Java NLP annotation pipeline [VnCoreNLP](https://github.com/vncorenlp/VnCoreNLP) for Vietnamese. VnCoreNLP provides rich linguistic annotations through key NLP components of word segmentation, POS tagging, named entity recognition and dependency parsing.

## Usage
    
    // Convert a word-segmented corpus into column-based representation
    $ python Utility.py test.txt test.col.txt
    // Perform POS tagging using VnMarMoT
	$ java -cp marmot.jar marmot.morph.cmd.Annotator --model-file vn.marmot --test-file form-index=<WORD-FORM-COLUMN-INDEX>,<INPUT-COLUMN-FORMATTED-FILE> --pred-file <OUTPUT-FILE>
	// Example:
    $ java -cp marmot.jar marmot.morph.cmd.Annotator --model-file vn.marmot --test-file form-index=0,test.col.txt --pred-file test.pred.txt