---
key: 图片生成/文生图/Qwen 3.5_DeepSeek_JoyCaption_提示词反推多方案集合  Z-image b_2031980126619049986.json
name: Qwen 3.5_DeepSeek_JoyCaption_提示词反推多方案集合  Z-image b_2031980126619049986
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen 3.5_DeepSeek_JoyCaption_提示词反推多方案集合  Z-image b_2031980126619049986.json
hash: a74ca249e965ca22
coverage: 0.608696
learned_at: 2026-10-21 02:54:04
nodes: [Joy_extra_options, Joy_caption_two_load, JanusImageUnderstanding, RH_LLMAPI_NODE, llama_cpp_model_loader, CLIPLoader, VAELoader, KSampler, VAEDecode, ModelSamplingAuraFlow, ConditioningZeroOut, EmptyLatentImage, SaveImage, UNETLoader, LoraLoaderModelOnly, Int, llama_cpp_instruct_adv, PrimitiveStringMultiline, ShowText|pysssss, PreviewAny, llama_cpp_instruct_adv, PreviewAny, LayerUtility: LoadJoyCaptionBeta1Model, LayerUtility: JoyCaptionBeta1ExtraOptions, LayerUtility: JoyCaptionBeta1, ShowText|pysssss, Joy_caption_two_advanced, RH_Translator, ShowText|pysssss, WD14Tagger|pysssss, ShowText|pysssss, JanusModelLoader, RH_Translator, ShowText|pysssss, Florence2Run, Florence2ModelLoader, SaveImage, ShowText|pysssss, RH_Translator, ShowText|pysssss, ShowText|pysssss, RH_Translator, ShowText|pysssss, RH_LLMAPI_Pro_Node, Qwen3_VQA, easy saveText, easy saveText, RH_Translator, llama_cpp_parameters, llama_cpp_model_loader, Note, Note, llama_cpp_parameters, CLIPTextEncode, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Int, Fast Groups Bypasser (rgthree), LoadImage, Reroute, Fast Groups Muter (rgthree)]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1920, "sampler_name": "euler", "scheduler": "simple", "seed": 422567644848104, "steps": 8, "width": 1280}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen 3.5_DeepSeek_JoyCaption_提示词反推多方案集合  Z-image b_2031980126619049986.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen 3.5_DeepSeek_JoyCaption_提示词反推多方案集合  Z-image b_2031980126619049986.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（69 个）：
- `Joy_extra_options`
- `Joy_caption_two_load`
- `JanusImageUnderstanding`
- `RH_LLMAPI_NODE`
- `llama_cpp_model_loader`
- `CLIPLoader`
- `VAELoader`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `ModelSamplingAuraFlow`
- `ConditioningZeroOut`
- `EmptyLatentImage` ★核心
- `SaveImage`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `Int`
- `llama_cpp_instruct_adv`
- `PrimitiveStringMultiline`
- `ShowText|pysssss`
- `PreviewAny`
- `llama_cpp_instruct_adv`
- `PreviewAny`
- `LayerUtility: LoadJoyCaptionBeta1Model`
- `LayerUtility: JoyCaptionBeta1ExtraOptions`
- `LayerUtility: JoyCaptionBeta1`
- `ShowText|pysssss`
- `Joy_caption_two_advanced`
- `RH_Translator`
- `ShowText|pysssss`
- `WD14Tagger|pysssss`
- `ShowText|pysssss`
- `JanusModelLoader`
- `RH_Translator`
- `ShowText|pysssss`
- `Florence2Run`
- `Florence2ModelLoader`
- `SaveImage`
- `ShowText|pysssss`
- `RH_Translator`
- `ShowText|pysssss`
- `ShowText|pysssss`
- `RH_Translator`
- `ShowText|pysssss`
- `RH_LLMAPI_Pro_Node`
- `Qwen3_VQA`
- `easy saveText`
- `easy saveText`
- `RH_Translator`
- `llama_cpp_parameters`
- `llama_cpp_model_loader`
- `Note`
- `Note`
- `llama_cpp_parameters`
- `CLIPTextEncode` ★核心
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Int`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `Reroute`
- `Fast Groups Muter (rgthree)`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `422567644848104`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1280`
- `height` = `1920`
- `batch_size` = `1`

## 知识

覆盖率 **61%**（42/69）

**有卡**：`Joy_extra_options`、`Joy_caption_two_load`、`JanusImageUnderstanding`、`RH_LLMAPI_NODE`、`llama_cpp_model_loader`、`CLIPLoader`、`VAELoader`、`KSampler`、`VAEDecode`、`ModelSamplingAuraFlow`、`ConditioningZeroOut`、`EmptyLatentImage`、`SaveImage`、`UNETLoader`、`LoraLoaderModelOnly`、`Int`、`llama_cpp_instruct_adv`、`LayerUtility: LoadJoyCaptionBeta1Model`、`LayerUtility: JoyCaptionBeta1ExtraOptions`、`LayerUtility: JoyCaptionBeta1`、`Joy_caption_two_advanced`、`RH_Translator`、`WD14Tagger|pysssss`、`JanusModelLoader`、`Florence2Run`、`Florence2ModelLoader`、`RH_LLMAPI_Pro_Node`、`Qwen3_VQA`、`easy saveText`、`llama_cpp_parameters`、`CLIPTextEncode`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
