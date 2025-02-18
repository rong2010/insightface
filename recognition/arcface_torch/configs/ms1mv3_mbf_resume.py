from easydict import EasyDict as edict

# make training faster
# our RAM is 256G
# mount -t tmpfs -o size=140G  tmpfs /train_tmp

config = edict()
config.margin_list = (1.0, 0.5, 0.0)
config.network = "mbf"
config.resume = True
config.output = None
config.embedding_size = 512
config.sample_rate = 1.0
config.fp16 = True


config.optimizer = "adamw"
config.momentum = 0.9
config.weight_decay = 0.1
config.batch_size = 128
config.lr = 0.001
config.verbose = 100
config.dali = False

config.rec = "/group/20002/train_data/ms1m-retinaface-t1"
config.num_classes = 93431
config.num_image = 5179510
config.num_epoch = 40
config.warmup_epoch = 2
config.val_targets = ['lfw', 'cfp_fp', "agedb_30"]
config.val_targets = []
