Runs using API calls to WebUI, guides an AI that you load in WebUI to produce code by feeding into python errors if the code wasn't working proerply it will loop until it makes working code, and self-executes the code. At the moment, it's hardcoded prompt structure; if people are interested, we and I can expand it. If you select an AI at the top of the Hugging Face leaderboard (including the flagged ones), this code was tested on https://huggingface.co/rwitz2/go-bruins-v2.1.1 and actually loaded a transformer, namely BERT, and then got that BERT to spit out something. Which is impressive and indicates latent self-replication capacities in the model as the top of the leaderboard of Hugging Face https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard. Tick all the boxes, then select the highest average model. This runs on top of https://github.com/oobabooga/text-generation-webui which you will need run first with CMG_FLAG file set with --api in; the api ping address will be the same as in the code so that will work fine. If you need further guidance, talk to ChatGPT-4 Turbo, Bing AI, or another smart AI at the top of the Elo leaderboard or the H4 Hugging Face one. Set the lin initial_prompt = "Create a simple Python script for a basic task." in agi.py to what you want it to can be anything, it's advisable to prommpt it how the code fines the text to self execute ie with the regular expressions in code '''python ''' ; the code needs to be exapnded to deal with all cases and style AI write python code. It may even even pick code not in that style as well.
