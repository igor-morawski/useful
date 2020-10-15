mv_model(){
    if [[ -f $1 ]]; then
        local ORIGIN=$(pwd)
        local FILEPATH=$1
        local BASENAME=$(basename -- $FILEPATH)
        local MODEL_DIR="$(dirname "$FILEPATH")"
        local MODEL_DIR_BASENAME="$(basename -- $MODEL_DIR)"
        local PARENT_DIR="$(dirname "$MODEL_DIR")"
        local PT_N_EXT=${BASENAME##*_}
        local CP_DIR="Models"
        local SRC_DIR=$MODEL_DIR
        local DST_DIR="$PARENT_DIR/$CP_DIR/$MODEL_DIR_BASENAME"
        if [[ ${FILEPATH: -3} != ".pt" ]]; then
            echo "Must be .pt"
        else
            echo "Navigating to $PARENT_DIR..."
            cd $PARENT_DIR
            if [ ! -d $DST_DIR ]; then
                echo "Making destination directory..."
                if [ ! -d $DST_DIR ]; then
                    mkdir "$PARENT_DIR/$CP_DIR"
                fi
                mkdir $DST_DIR
            fi 

            echo "Inferring filepaths from $BASENAME..."
            echo "Moving args.txt and events.out..."
            cp "$SRC_DIR/args.txt" $DST_DIR
            cp "$SRC_DIR/events"* $DST_DIR
            echo "OK"
            echo "Moving checkpoints number ${PT_N_EXT%.*}..."
            cp "$SRC_DIR/"*"_$PT_N_EXT" $DST_DIR
            echo "OK"

            echo "Success! Navigating back to $ORIGIN..."
            cd $ORIGIN
        fi
else
    echo "Not a file."
fi
}
