import os

from lib.conf import tts_dir, voices_dir
loaded_tts = {}

TTS_ENGINES = {
    "XTTSv2": "xtts", 
    "BARK": "bark", 
    "VITS": "vits", 
    "FAIRSEQ": "fairseq", 
    "TACOTRON2": "tacotron", 
    "YOURTTS": "yourtts"
}

default_tts_engine = TTS_ENGINES['XTTSv2']
default_fine_tuned = 'internal'

r"""
voice_conversion_models/multilingual/vctk/freevc24
voice_conversion_models/multilingual/multi-dataset/knnvc
voice_conversion_models/multilingual/multi-dataset/openvoice_v1
voice_conversion_models/multilingual/multi-dataset/openvoice_v2
"""
default_vc_model = 'voice_conversion_models/multilingual/multi-dataset/knnvc'
default_voice_detection_model = 'drewThomasson/segmentation'

max_tts_in_memory = 2 # TTS engines to keep in memory (1 tts engine ~= 4GB to 8GB RAM).
max_custom_model = 100
max_custom_voices = 1000
max_upload_size = '6GB'

default_engine_settings = {
    TTS_ENGINES['XTTSv2']: {
        "samplerate": 24000,
        "temperature": 0.85,
        "length_penalty": 0.8,
        "num_beams": 1,
        "repetition_penalty": 4.0,
        "top_k": 40,
        "top_p": 0.90,
        "speed": 0.95,
        "enable_text_splitting": False,
        # to enable deepspeed, you must install it first:
        # conda activate ./python_env (linux/mac) or .\python_env (windows)
        # pip install deepspeed
        # conda deactivate
        "use_deepspeed": False,
        "files": ['config.json', 'model.pth', 'vocab.json', 'ref.wav', 'speakers_xtts.pth'],
        "voices": {
            "ClaribelDervla": "Claribel Dervla", "DaisyStudious": "Daisy Studious", "GracieWise": "Gracie Wise",
            "TammieEma": "Tammie Ema", "AlisonDietlinde": "Alison Dietlinde", "AnaFlorence": "Ana Florence",
            "AnnmarieNele": "Annmarie Nele", "AsyaAnara": "Asya Anara", "BrendaStern": "Brenda Stern",
            "GittaNikolina": "Gitta Nikolina", "HenrietteUsha": "Henriette Usha", "SofiaHellen": "Sofia Hellen",
            "TammyGrit": "Tammy Grit", "TanjaAdelina": "Tanja Adelina", "VjollcaJohnnie": "Vjollca Johnnie",
            "AndrewChipper": "Andrew Chipper", "BadrOdhiambo": "Badr Odhiambo", "DionisioSchuyler": "Dionisio Schuyler",
            "RoystonMin": "Royston Min", "ViktorEka": "Viktor Eka", "AbrahanMack": "Abrahan Mack",
            "AddeMichal": "Adde Michal", "BaldurSanjin": "Baldur Sanjin", "CraigGutsy": "Craig Gutsy",
            "DamienBlack": "Damien Black", "GilbertoMathias": "Gilberto Mathias", "IlkinUrbano": "Ilkin Urbano",
            "KazuhikoAtallah": "Kazuhiko Atallah", "LudvigMilivoj": "Ludvig Milivoj", "SuadQasim": "Suad Qasim",
            "TorcullDiarmuid": "Torcull Diarmuid", "ViktorMenelaos": "Viktor Menelaos", "ZacharieAimilios": "Zacharie Aimilios",
            "NovaHogarth": "Nova Hogarth", "MajaRuoho": "Maja Ruoho", "UtaObando": "Uta Obando",
            "LidiyaSzekeres": "Lidiya Szekeres", "ChandraMacFarland": "Chandra MacFarland", "SzofiGranger": "Szofi Granger",
            "CamillaHolmström": "Camilla Holmström", "LilyaStainthorpe": "Lilya Stainthorpe", "ZofijaKendrick": "Zofija Kendrick",
            "NarelleMoon": "Narelle Moon", "BarboraMacLean": "Barbora MacLean", "AlexandraHisakawa": "Alexandra Hisakawa",
            "AlmaMaría": "Alma María", "RosemaryOkafor": "Rosemary Okafor", "IgeBehringer": "Ige Behringer",
            "FilipTraverse": "Filip Traverse", "DamjanChapman": "Damjan Chapman", "WulfCarlevaro": "Wulf Carlevaro",
            "AaronDreschner": "Aaron Dreschner", "KumarDahl": "Kumar Dahl", "EugenioMataracı": "Eugenio Mataracı",
            "FerranSimen": "Ferran Simen", "XavierHayasaka": "Xavier Hayasaka", "LuisMoray": "Luis Moray",
            "MarcosRudaski": "Marcos Rudaski"
        },
        "rating": {"GPU VRAM": 4, "CPU": 3, "RAM": 8, "Realism": 4}
    },
    TTS_ENGINES['BARK']: {
        "samplerate": 24000,
        "text_temp": 0.65,
        "waveform_temp": 0.60,
        "files": ["text_2.pt", "coarse_2.pt", "fine_2.pt"],
        "speakers_path": os.path.join(voices_dir, '__bark'),
        "voices": {
            "de_speaker_0": "Speaker 0", "de_speaker_1": "Speaker 1", "de_speaker_2": "Speaker 2",
            "de_speaker_3": "Speaker 3", "de_speaker_4": "Speaker 4", "de_speaker_5": "Speaker 5",
            "de_speaker_6": "Speaker 6", "de_speaker_7": "Speaker 7", "de_speaker_8": "Speaker 8",
            "de_speaker_9": "Speaker 9", "en_speaker_0": "Speaker 0", "en_speaker_1": "Speaker 1",
            "en_speaker_2": "Speaker 2", "en_speaker_3": "Speaker 3", "en_speaker_4": "Speaker 4",
            "en_speaker_5": "Speaker 5", "en_speaker_6": "Speaker 6", "en_speaker_7": "Speaker 7",
            "en_speaker_8": "Speaker 8", "en_speaker_9": "Speaker 9", "es_speaker_0": "Speaker 0",
            "es_speaker_1": "Speaker 1", "es_speaker_2": "Speaker 2", "es_speaker_3": "Speaker 3",
            "es_speaker_4": "Speaker 4", "es_speaker_5": "Speaker 5", "es_speaker_6": "Speaker 6",
            "es_speaker_7": "Speaker 7", "es_speaker_8": "Speaker 8", "es_speaker_9": "Speaker 9",
            "fr_speaker_0": "Speaker 0", "fr_speaker_1": "Speaker 1", "fr_speaker_2": "Speaker 2",
            "fr_speaker_3": "Speaker 3", "fr_speaker_4": "Speaker 4", "fr_speaker_5": "Speaker 5",
            "fr_speaker_6": "Speaker 6", "fr_speaker_7": "Speaker 7", "fr_speaker_8": "Speaker 8",
            "fr_speaker_9": "Speaker 9", "hi_speaker_0": "Speaker 0", "hi_speaker_1": "Speaker 1",
            "hi_speaker_2": "Speaker 2", "hi_speaker_3": "Speaker 3", "hi_speaker_4": "Speaker 4",
            "hi_speaker_5": "Speaker 5", "hi_speaker_6": "Speaker 6", "hi_speaker_7": "Speaker 7",
            "hi_speaker_8": "Speaker 8", "hi_speaker_9": "Speaker 9", "it_speaker_0": "Speaker 0",
            "it_speaker_1": "Speaker 1", "it_speaker_2": "Speaker 2", "it_speaker_3": "Speaker 3",
            "it_speaker_4": "Speaker 4", "it_speaker_5": "Speaker 5", "it_speaker_6": "Speaker 6",
            "it_speaker_7": "Speaker 7", "it_speaker_8": "Speaker 8", "it_speaker_9": "Speaker 9",
            "ja_speaker_0": "Speaker 0", "ja_speaker_1": "Speaker 1", "ja_speaker_2": "Speaker 2",
            "ja_speaker_3": "Speaker 3", "ja_speaker_4": "Speaker 4", "ja_speaker_5": "Speaker 5",
            "ja_speaker_6": "Speaker 6", "ja_speaker_7": "Speaker 7", "ja_speaker_8": "Speaker 8",
            "ja_speaker_9": "Speaker 9", "ko_speaker_0": "Speaker 0", "ko_speaker_1": "Speaker 1",
            "ko_speaker_2": "Speaker 2", "ko_speaker_3": "Speaker 3", "ko_speaker_4": "Speaker 4",
            "ko_speaker_5": "Speaker 5", "ko_speaker_6": "Speaker 6", "ko_speaker_7": "Speaker 7",
            "ko_speaker_8": "Speaker 8", "ko_speaker_9": "Speaker 9", "pl_speaker_0": "Speaker 0",
            "pl_speaker_1": "Speaker 1", "pl_speaker_2": "Speaker 2", "pl_speaker_3": "Speaker 3",
            "pl_speaker_4": "Speaker 4", "pl_speaker_5": "Speaker 5", "pl_speaker_6": "Speaker 6",
            "pl_speaker_7": "Speaker 7", "pl_speaker_8": "Speaker 8", "pl_speaker_9": "Speaker 9",
            "pt_speaker_0": "Speaker 0", "pt_speaker_1": "Speaker 1", "pt_speaker_2": "Speaker 2",
            "pt_speaker_3": "Speaker 3", "pt_speaker_4": "Speaker 4", "pt_speaker_5": "Speaker 5",
            "pt_speaker_6": "Speaker 6", "pt_speaker_7": "Speaker 7", "pt_speaker_8": "Speaker 8",
            "pt_speaker_9": "Speaker 9", "ru_speaker_0": "Speaker 0", "ru_speaker_1": "Speaker 1",
            "ru_speaker_2": "Speaker 2", "ru_speaker_3": "Speaker 3", "ru_speaker_4": "Speaker 4",
            "ru_speaker_5": "Speaker 5", "ru_speaker_6": "Speaker 6", "ru_speaker_7": "Speaker 7",
            "ru_speaker_8": "Speaker 8", "ru_speaker_9": "Speaker 9", "tr_speaker_0": "Speaker 0",
            "tr_speaker_1": "Speaker 1", "tr_speaker_2": "Speaker 2", "tr_speaker_3": "Speaker 3",
            "tr_speaker_4": "Speaker 4", "tr_speaker_5": "Speaker 5", "tr_speaker_6": "Speaker 6",
            "tr_speaker_7": "Speaker 7", "tr_speaker_8": "Speaker 8", "tr_speaker_9": "Speaker 9",
            "zh_speaker_0": "Speaker 0", "zh_speaker_1": "Speaker 1", "zh_speaker_2": "Speaker 2",
            "zh_speaker_3": "Speaker 3", "zh_speaker_4": "Speaker 4", "zh_speaker_5": "Speaker 5",
            "zh_speaker_6": "Speaker 6", "zh_speaker_7": "Speaker 7", "zh_speaker_8": "Speaker 8",
            "zh_speaker_9": "Speaker 9"
        },
        "rating": {"GPU VRAM": 4, "CPU": 1, "RAM": 16, "Realism": 3}
    },
    TTS_ENGINES['VITS']: {
        "samplerate": 22050,
        "files": ['config.json', 'model_file.pth', 'language_ids.json'],
        "voices": {},
        "rating": {"GPU VRAM": 2, "CPU": 3, "RAM": 4, "Realism": 2}
    },
    TTS_ENGINES['FAIRSEQ']: {
        "samplerate": 16000,
        "files": ['config.json', 'G_100000.pth', 'vocab.json'],
        "voices": {},
        "rating": {"GPU VRAM": 2, "CPU": 3, "RAM": 4, "Realism": 2}
    },
    TTS_ENGINES['TACOTRON2']: {
        "samplerate": 22050,
        "files": ['config.json', 'best_model.pth', 'vocoder_config.json', 'vocoder_model.pth'],
        "voices": {},
        "rating": {"GPU VRAM": 2, "CPU": 3, "RAM": 4, "Realism": 2}
    },
    TTS_ENGINES['YOURTTS']: {
        "samplerate": 16000,
        "files": ['config.json', 'model_file.pth'],
        "voices": {"Machinella-5": "female-en-5", "ElectroMale-2": "male-en-2", 'Machinella-4': 'female-pt-4\n', 'ElectroMale-3': 'male-pt-3\n'},
        "rating": {"GPU VRAM": 1, "CPU": 5, "RAM": 4, "Realism": 1}
    }
}
models = {
    TTS_ENGINES['XTTSv2']: {
        "internal": {
            "lang": "multi",
            "repo": "coqui/XTTS-v2",
            "sub": "tts_models/multilingual/multi-dataset/xtts_v2/",
            "voice": os.path.join(voices_dir, "eng", "adult", "male", f"KumarDahl_{default_engine_settings[TTS_ENGINES['XTTSv2']]['samplerate']}.wav"),
            "files": default_engine_settings[TTS_ENGINES['XTTSv2']]['files'],
            "samplerate": default_engine_settings[TTS_ENGINES['XTTSv2']]['samplerate']
        },
        "AiExplained": {
            "lang": "eng",
            "repo": "drewThomasson/fineTunedTTSModels",
            "sub": "xtts-v2/eng/AiExplained/",
            "voice": os.path.join(voices_dir, "eng", "adult", "male", f"AiExplained_{default_engine_settings[TTS_ENGINES['XTTSv2']]['samplerate']}.wav"),
            "files": default_engine_settings[TTS_ENGINES['XTTSv2']]['files'],
            "samplerate": default_engine_settings[TTS_ENGINES['XTTSv2']]['samplerate']
        },
        "AsmrRacoon": {
            "lang": "eng",
            "repo": "drewThomasson/fineTunedTTSModels",
            "sub": "xtts-v2/eng/AsmrRacoon/",
            "voice": os.path.join(voices_dir, "eng", "adult", "male", f"AsmrRacoon_{default_engine_settings[TTS_ENGINES['XTTSv2']]['samplerate']}.wav"),
            "files": default_engine_settings[TTS_ENGINES['XTTSv2']]['files'],
            "samplerate": default_engine_settings[TTS_ENGINES['XTTSv2']]['samplerate']
        },
        "Awkwafina": {
            "lang": "eng",
            "repo": "drewThomasson/fineTunedTTSModels",
            "sub": "xtts-v2/eng/Awkwafina/",
            "voice": os.path.join(voices_dir, "eng", "adult", "female", f"Awkwafina_{default_engine_settings[TTS_ENGINES['XTTSv2']]['samplerate']}.wav"),
            "files": default_engine_settings[TTS_ENGINES['XTTSv2']]['files'],
            "samplerate": default_engine_settings[TTS_ENGINES['XTTSv2']]['samplerate']
        },
        "BobOdenkirk": {
            "lang": "eng",
            "repo": "drewThomasson/fineTunedTTSModels",
            "sub": "xtts-v2/eng/BobOdenkirk/",
            "voice": os.path.join(voices_dir, "eng", "adult", "male", f"BobOdenkirk_{default_engine_settings[TTS_ENGINES['XTTSv2']]['samplerate']}.wav"),
            "files": default_engine_settings[TTS_ENGINES['XTTSv2']]['files'],
            "samplerate": default_engine_settings[TTS_ENGINES['XTTSv2']]['samplerate']
        },
        "BobRoss": {
            "lang": "eng",
            "repo": "drewThomasson/fineTunedTTSModels",
            "sub": "xtts-v2/eng/BobRoss/",
            "voice": os.path.join(voices_dir, "eng", "adult", "male", f"BobRoss_{default_engine_settings[TTS_ENGINES['XTTSv2']]['samplerate']}.wav"),
            "files": default_engine_settings[TTS_ENGINES['XTTSv2']]['files'],
            "samplerate": default_engine_settings[TTS_ENGINES['XTTSv2']]['samplerate']
        },
        "BrinaPalencia": {
            "lang": "eng",
            "repo": "drewThomasson/fineTunedTTSModels",
            "sub": "xtts-v2/eng/BrinaPalencia/",
            "voice": os.path.join(voices_dir, "eng", "adult", "female", f"BrinaPalencia_{default_engine_settings[TTS_ENGINES['XTTSv2']]['samplerate']}.wav"),
            "files": default_engine_settings[TTS_ENGINES['XTTSv2']]['files'],
            "samplerate": default_engine_settings[TTS_ENGINES['XTTSv2']]['samplerate']
        },
        "BryanCranston": {
            "lang": "eng",
            "repo": "drewThomasson/fineTunedTTSModels",
            "sub": "xtts-v2/eng/BryanCranston/",
            "voice": os.path.join(voices_dir, "eng", "adult", "male", f"BryanCranston_{default_engine_settings[TTS_ENGINES['XTTSv2']]['samplerate']}.wav"),
            "files": default_engine_settings[TTS_ENGINES['XTTSv2']]['files'],
            "samplerate": default_engine_settings[TTS_ENGINES['XTTSv2']]['samplerate']
        },
        "DavidAttenborough": {
            "lang": "eng",
            "repo": "drewThomasson/fineTunedTTSModels",
            "sub": "xtts-v2/eng/DavidAttenborough/",
            "voice": os.path.join(voices_dir, "eng", "elder", "male", f"DavidAttenborough_{default_engine_settings[TTS_ENGINES['XTTSv2']]['samplerate']}.wav"),
            "files": default_engine_settings[TTS_ENGINES['XTTSv2']]['files'],
            "samplerate": default_engine_settings[TTS_ENGINES['XTTSv2']]['samplerate']
        },
        "DeathPussInBoots": {
            "lang": "eng",
            "repo": "drewThomasson/fineTunedTTSModels",
            "sub": "xtts-v2/eng/DeathPussInBoots/",
            "voice": os.path.join(voices_dir, "eng", "adult", "male", f"DeathPussInBoots_{default_engine_settings[TTS_ENGINES['XTTSv2']]['samplerate']}.wav"),
            "files": default_engine_settings[TTS_ENGINES['XTTSv2']]['files'],
            "samplerate": default_engine_settings[TTS_ENGINES['XTTSv2']]['samplerate']
        },
        "DermotCrowley": {
            "lang": "eng",
            "repo": "drewThomasson/fineTunedTTSModels",
            "sub": "xtts-v2/eng/DermotCrowley/",
            "voice": os.path.join(voices_dir, "eng", "elder", "male", f"DermotCrowley_{default_engine_settings[TTS_ENGINES['XTTSv2']]['samplerate']}.wav"),
            "files": default_engine_settings[TTS_ENGINES['XTTSv2']]['files'],
            "samplerate": default_engine_settings[TTS_ENGINES['XTTSv2']]['samplerate']
        },
        "EvaSeymour": {
            "lang": "eng",
            "repo": "drewThomasson/fineTunedTTSModels",
            "sub": "xtts-v2/eng/EvaSeymour/",
            "voice": os.path.join(voices_dir, "eng", "adult", "female", f"EvaSeymour_{default_engine_settings[TTS_ENGINES['XTTSv2']]['samplerate']}.wav"),
            "files": default_engine_settings[TTS_ENGINES['XTTSv2']]['files'],
            "samplerate": default_engine_settings[TTS_ENGINES['XTTSv2']]['samplerate']
        },
        "GideonOfnirEldenRing": {
            "lang": "eng",
            "repo": "drewThomasson/fineTunedTTSModels",
            "sub": "xtts-v2/eng/GideonOfnirEldenRing/",
            "voice": os.path.join(voices_dir, "eng", "elder", "male", f"GideonOfnirEldenRing_{default_engine_settings[TTS_ENGINES['XTTSv2']]['samplerate']}.wav"),
            "files": default_engine_settings[TTS_ENGINES['XTTSv2']]['files'],
            "samplerate": default_engine_settings[TTS_ENGINES['XTTSv2']]['samplerate']
        },
        "GhostMW2": {
            "lang": "eng",
            "repo": "drewThomasson/fineTunedTTSModels",
            "sub": "xtts-v2/eng/GhostMW2/",
            "voice": os.path.join(voices_dir, "eng", "adult", "male", f"GhostMW2_{default_engine_settings[TTS_ENGINES['XTTSv2']]['samplerate']}.wav"),
            "files": default_engine_settings[TTS_ENGINES['XTTSv2']]['files'],
            "samplerate": default_engine_settings[TTS_ENGINES['XTTSv2']]['samplerate']
        },
        "JhonButlerASMR": {
            "lang": "eng",
            "repo": "drewThomasson/fineTunedTTSModels",
            "sub": "xtts-v2/eng/JhonButlerASMR/",
            "voice": os.path.join(voices_dir, "eng", "elder", "male", f"JhonButlerASMR_{default_engine_settings[TTS_ENGINES['XTTSv2']]['samplerate']}.wav"),
            "files": default_engine_settings[TTS_ENGINES['XTTSv2']]['files'],
            "samplerate": default_engine_settings[TTS_ENGINES['XTTSv2']]['samplerate']
        },
        "JhonMulaney": {
            "lang": "eng",
            "repo": "drewThomasson/fineTunedTTSModels",
            "sub": "xtts-v2/eng/JhonMulaney/",
            "voice": os.path.join(voices_dir, "eng", "adult", "male", f"JhonMulaney_{default_engine_settings[TTS_ENGINES['XTTSv2']]['samplerate']}.wav"),
            "files": default_engine_settings[TTS_ENGINES['XTTSv2']]['files'],
            "samplerate": default_engine_settings[TTS_ENGINES['XTTSv2']]['samplerate']
        },
        "JillRedfield": {
            "lang": "eng",
            "repo": "drewThomasson/fineTunedTTSModels",
            "sub": "xtts-v2/eng/JillRedfield/",
            "voice": os.path.join(voices_dir, "eng", "adult", "female", f"JillRedfield_{default_engine_settings[TTS_ENGINES['XTTSv2']]['samplerate']}.wav"),
            "files": default_engine_settings[TTS_ENGINES['XTTSv2']]['files'],
            "samplerate": default_engine_settings[TTS_ENGINES['XTTSv2']]['samplerate']
        },
        "JuliaWhenlan": {
            "lang": "eng",
            "repo": "drewThomasson/fineTunedTTSModels",
            "sub": "xtts-v2/eng/JuliaWhenlan/",
            "voice": os.path.join(voices_dir, "eng", "adult", "female", f"JuliaWhenlan_{default_engine_settings[TTS_ENGINES['XTTSv2']]['samplerate']}.wav"),
            "files": default_engine_settings[TTS_ENGINES['XTTSv2']]['files'],
            "samplerate": default_engine_settings[TTS_ENGINES['XTTSv2']]['samplerate']
        },
        "LeeHorsley": {
            "lang": "eng",
            "repo": "drewThomasson/fineTunedTTSModels",
            "sub": "xtts-v2/eng/LeeHorsley/",
            "voice": os.path.join(voices_dir, "eng", "adult", "male", f"LeeHorsley_{default_engine_settings[TTS_ENGINES['XTTSv2']]['samplerate']}.wav"),
            "files": default_engine_settings[TTS_ENGINES['XTTSv2']]['files'],
            "samplerate": default_engine_settings[TTS_ENGINES['XTTSv2']]['samplerate']
        },
        "MelinaEldenRing": {
            "lang": "eng",
            "repo": "drewThomasson/fineTunedTTSModels",
            "sub": "xtts-v2/eng/MelinaEldenRing/",
            "voice": os.path.join(voices_dir, "eng", "adult", "female", f"MelinaEldenRing_{default_engine_settings[TTS_ENGINES['XTTSv2']]['samplerate']}.wav"),
            "files": default_engine_settings[TTS_ENGINES['XTTSv2']]['files'],
            "samplerate": default_engine_settings[TTS_ENGINES['XTTSv2']]['samplerate']
        },
        "MorganFreeman": {
            "lang": "eng",
            "repo": "drewThomasson/fineTunedTTSModels",
            "sub": "xtts-v2/eng/MorganFreeman/",
            "voice": os.path.join(voices_dir, "eng", "adult", "male", f"MorganFreeman_{default_engine_settings[TTS_ENGINES['XTTSv2']]['samplerate']}.wav"),
            "files": default_engine_settings[TTS_ENGINES['XTTSv2']]['files'],
            "samplerate": default_engine_settings[TTS_ENGINES['XTTSv2']]['samplerate']
        },
        "NeilGaiman": {
            "lang": "eng",
            "repo": "drewThomasson/fineTunedTTSModels",
            "sub": "xtts-v2/eng/NeilGaiman/",
            "voice": os.path.join(voices_dir, "eng", "adult", "male", f"NeilGaiman_{default_engine_settings[TTS_ENGINES['XTTSv2']]['samplerate']}.wav"),
            "files": default_engine_settings[TTS_ENGINES['XTTSv2']]['files'],
            "samplerate": default_engine_settings[TTS_ENGINES['XTTSv2']]['samplerate']
        },
        "RainyDayHeadSpace": {
            "lang": "eng",
            "repo": "drewThomasson/fineTunedTTSModels",
            "sub": "xtts-v2/eng/RainyDayHeadSpace/",
            "voice": os.path.join(voices_dir, "eng", "elder", "male", f"RainyDayHeadSpace_{default_engine_settings[TTS_ENGINES['XTTSv2']]['samplerate']}.wav"),
            "files": default_engine_settings[TTS_ENGINES['XTTSv2']]['files'],
            "samplerate": default_engine_settings[TTS_ENGINES['XTTSv2']]['samplerate']
        },
        "RayPorter": {
            "lang": "eng",
            "repo": "drewThomasson/fineTunedTTSModels",
            "sub": "xtts-v2/eng/RayPorter/",
            "voice": os.path.join(voices_dir, "eng", "adult", "male", f"RayPorter_{default_engine_settings[TTS_ENGINES['XTTSv2']]['samplerate']}.wav"),
            "files": default_engine_settings[TTS_ENGINES['XTTSv2']]['files'],
            "samplerate": default_engine_settings[TTS_ENGINES['XTTSv2']]['samplerate']
        },
        "RelaxForAWhile": {
            "lang": "eng",
            "repo": "drewThomasson/fineTunedTTSModels",
            "sub": "xtts-v2/eng/RelaxForAWhile/",
            "voice": os.path.join(voices_dir, "eng", "adult", "female", f"RelaxForAWhile_{default_engine_settings[TTS_ENGINES['XTTSv2']]['samplerate']}.wav"),
            "files": default_engine_settings[TTS_ENGINES['XTTSv2']]['files'],
            "samplerate": default_engine_settings[TTS_ENGINES['XTTSv2']]['samplerate']
        },
        "RosamundPike": {
            "lang": "eng",
            "repo": "drewThomasson/fineTunedTTSModels",
            "sub": "xtts-v2/eng/RosamundPike/",
            "voice": os.path.join(voices_dir, "eng", "adult", "female", f"RosamundPike_{default_engine_settings[TTS_ENGINES['XTTSv2']]['samplerate']}.wav"),
            "files": default_engine_settings[TTS_ENGINES['XTTSv2']]['files'],
            "samplerate": default_engine_settings[TTS_ENGINES['XTTSv2']]['samplerate']
        },
        "ScarlettJohansson": {
            "lang": "eng",
            "repo": "drewThomasson/fineTunedTTSModels",
            "sub": "xtts-v2/eng/ScarlettJohansson/",
            "voice": os.path.join(voices_dir, "eng", "adult", "female", f"ScarlettJohansson_{default_engine_settings[TTS_ENGINES['XTTSv2']]['samplerate']}.wav"),
            "files": default_engine_settings[TTS_ENGINES['XTTSv2']]['files'],
            "samplerate": default_engine_settings[TTS_ENGINES['XTTSv2']]['samplerate']
        },
        "SladeTeenTitans": {
            "lang": "eng",
            "repo": "drewThomasson/fineTunedTTSModels",
            "sub": "xtts-v2/eng/SladeTeenTitans/",
            "voice": os.path.join(voices_dir, "eng", "adult", "male", f"SladeTeenTitans_{default_engine_settings[TTS_ENGINES['XTTSv2']]['samplerate']}.wav"),
            "files": default_engine_settings[TTS_ENGINES['XTTSv2']]['files'],
            "samplerate": default_engine_settings[TTS_ENGINES['XTTSv2']]['samplerate']
        },
        "StanleyParable": {
            "lang": "eng",
            "repo": "drewThomasson/fineTunedTTSModels",
            "sub": "xtts-v2/eng/StanleyParable/",
            "voice": os.path.join(voices_dir, "eng", "adult", "male", f"StanleyParable_{default_engine_settings[TTS_ENGINES['XTTSv2']]['samplerate']}.wav"),
            "files": default_engine_settings[TTS_ENGINES['XTTSv2']]['files'],
            "samplerate": default_engine_settings[TTS_ENGINES['XTTSv2']]['samplerate']
        },
        "WhisperSalemASMR": {
            "lang": "eng",
            "repo": "drewThomasson/fineTunedTTSModels",
            "sub": "xtts-v2/eng/WhisperSalemASMR/",
            "voice": os.path.join(voices_dir, "eng", "adult", "male", f"WhisperSalemASMR_{default_engine_settings[TTS_ENGINES['XTTSv2']]['samplerate']}.wav"),
            "files": default_engine_settings[TTS_ENGINES['XTTSv2']]['files'],
            "samplerate": default_engine_settings[TTS_ENGINES['XTTSv2']]['samplerate']
        },
        "Konishev": {
            "lang": "rus",
            "repo": "drewThomasson/fineTunedTTSModels",
            "sub": "xtts-v2/rus/Konishev/",
            "voice": os.path.join(voices_dir, "rus", "adult", "male", f"Konishev_{default_engine_settings[TTS_ENGINES['XTTSv2']]['samplerate']}.wav"),
            "files": default_engine_settings[TTS_ENGINES['XTTSv2']]['files'],
            "samplerate": default_engine_settings[TTS_ENGINES['XTTSv2']]['samplerate']
        }
    },
    TTS_ENGINES['BARK']: {
        "internal": {
            "lang": "multi",
            "repo": "erogol/bark", # suno/bark, rsxdalv/suno, tts_models/multilingual/multi-dataset/bark
            "sub": "", # {"big-bf16": "big-bf16/", "small-bf16": "small-bf16/", "big": "big/", "small": "small/"}
            "voice": os.path.join(voices_dir, "eng", "adult", "male", f"KumarDahl_{default_engine_settings[TTS_ENGINES['BARK']]['samplerate']}.wav"),
            "files": default_engine_settings[TTS_ENGINES['BARK']]['files'],
            "samplerate": default_engine_settings[TTS_ENGINES['BARK']]['samplerate']
        }
    },
    TTS_ENGINES['VITS']: {
        "internal": {
            "lang": "multi",
            "repo": "tts_models/[lang_iso1]/[xxx]",
            "sub": {
                "css10/vits": ['es','hu','fi','fr','nl','ru','el'],
                "custom/vits": ['ca'],
                "custom/vits-female": ['bn', 'fa'],
                "cv/vits": ['bg','cs','da','et','ga','hr','lt','lv','mt','pt','ro','sk','sl','sv'],
                "mai/vits": ['uk'],
                "mai_female/vits": ['pl'],
                "mai_male/vits": ['it'],
                "openbible/vits": ['ewe','hau','lin','tw_akuapem','tw_asante','yor'],
                "vctk/vits": ['en'],
                "thorsten/vits": ['de']
            },
            "voice": None,
            "files": default_engine_settings[TTS_ENGINES['VITS']]['files'],
            "samplerate": {
                "css10/vits": default_engine_settings[TTS_ENGINES['VITS']]['samplerate'],
                "custom/vits": default_engine_settings[TTS_ENGINES['VITS']]['samplerate'],
                "custom/vits-female": default_engine_settings[TTS_ENGINES['VITS']]['samplerate'],
                "cv/vits": default_engine_settings[TTS_ENGINES['VITS']]['samplerate'],
                "mai/vits": default_engine_settings[TTS_ENGINES['VITS']]['samplerate'],
                "mai_female/vits": 24000,
                "mai_male/vits": 16000,
                "openbible/vits": default_engine_settings[TTS_ENGINES['VITS']]['samplerate'],
                "vctk/vits": default_engine_settings[TTS_ENGINES['VITS']]['samplerate'],
                "thorsten/vits": default_engine_settings[TTS_ENGINES['VITS']]['samplerate']
            }
        }
    },
    TTS_ENGINES['FAIRSEQ']: {
        "internal": {
            "lang": "multi",
            "repo": "tts_models/[lang]/fairseq/vits",
            "sub": "",
            "voice": None,
            "files": default_engine_settings[TTS_ENGINES['FAIRSEQ']]['files'],
            "samplerate": default_engine_settings[TTS_ENGINES['FAIRSEQ']]['samplerate']
        }
    },
    TTS_ENGINES['TACOTRON2']: {
       "internal": {
            "lang": "multi",
            "repo": "tts_models/[lang_iso1]/[xxx]",
            "sub": {
                "mai/tacotron2-DDC": ['fr', 'es', 'nl'],
                "thorsten/tacotron2-DDC": ['de'],
                "kokoro/tacotron2-DDC": ['ja'],
                "ljspeech/tacotron2-DDC": ['en'],
                "baker/tacotron2-DDC-GST": ['zh-CN']              
            },
            "voice": None,
            "files": default_engine_settings[TTS_ENGINES['TACOTRON2']]['files'],
            "samplerate": {
                "mai/tacotron2-DDC": default_engine_settings[TTS_ENGINES['TACOTRON2']]['samplerate'],
                "thorsten/tacotron2-DDC": default_engine_settings[TTS_ENGINES['TACOTRON2']]['samplerate'],
                "kokoro/tacotron2-DDC": default_engine_settings[TTS_ENGINES['TACOTRON2']]['samplerate'],
                "ljspeech/tacotron2-DDC": default_engine_settings[TTS_ENGINES['TACOTRON2']]['samplerate'],
                "baker/tacotron2-DDC-GST": default_engine_settings[TTS_ENGINES['TACOTRON2']]['samplerate']
            },
        }
    },
    TTS_ENGINES['YOURTTS']: {
        "internal": {
            "lang": "multi",
            "repo": "tts_models/multilingual/multi-dataset/your_tts",
            "sub": "",
            "voice": None,
            "files": default_engine_settings[TTS_ENGINES['YOURTTS']]['files'],
            "samplerate": default_engine_settings[TTS_ENGINES['YOURTTS']]['samplerate']
        }
    }
}
