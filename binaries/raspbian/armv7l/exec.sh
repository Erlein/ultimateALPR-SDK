IMGPATH="${1:-$../../../imgs}"
RESPATH="${2:-$'results.csv'}"

echo "Image path: $IMGPATH, Result path: $RESPATH"

PYTHONPATH=$PYTHONPATH:.:../../../python \
LD_LIBRARY_PATH=.:$LD_LIBRARY_PATH \
python3 ../../../pythondev/timedDirDet.py -i $IMGPATH -o $RESPATH
