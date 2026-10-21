---
key: 图片生成/文生图/全能图片G-IMAGE-2.5｜API调用智能体，文生图图生图双支持_2099888363720499201.json
name: 全能图片G-IMAGE-2.5｜API调用智能体，文生图图生图双支持_2099888363720499201
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/全能图片G-IMAGE-2.5｜API调用智能体，文生图图生图双支持_2099888363720499201.json
hash: 7c13a4f46e5828f4
coverage: 0.752688
learned_at: 2026-10-20 01:35:19
nodes: [Fast Groups Bypasser (rgthree), llama_cpp_model_loader, llama_cpp_parameters, Fast Groups Bypasser (rgthree), llama_cpp_instruct_adv, LoadImage, CR Text, LoadImage, Fast Groups Bypasser (rgthree), LoadImage, RHLLMChatNode, easy showAnything, ImageConcatMulti, Any Switch (rgthree), Any Switch (rgthree), SaveImage, CR Text, llama_cpp_parameters, llama_cpp_model_loader, llama_cpp_instruct_adv, LoadImage, ShowText|pysssss, RHSettingsNode, CR Text, easy showAnything, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), easy showAnything, Fast Groups Bypasser (rgthree), CR Text, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), RHLLMChatNode, easy showAnything, llama_cpp_model_loader, llama_cpp_parameters, llama_cpp_instruct_adv, RH_RhartImageG25OfficialTokenSunburstTextToImage, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, RH_RhartImageG2OfficialImageToImage, RH_RhartImageG25OfficialTokenFlareEdit, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), RH_RhartImageG25OfficialTokenFlareTextToImage, SaveImage, RHSettingsNode, LayerUtility: ImageScaleByAspectRatio V2, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, solarL_SaveImagesToZip, JjkText, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/全能图片G-IMAGE-2.5｜API调用智能体，文生图图生图双支持_2099888363720499201.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/全能图片G-IMAGE-2.5｜API调用智能体，文生图图生图双支持_2099888363720499201.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（93 个）：
- `Fast Groups Bypasser (rgthree)`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `Fast Groups Bypasser (rgthree)`
- `llama_cpp_instruct_adv`
- `LoadImage`
- `CR Text`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `RHLLMChatNode`
- `easy showAnything`
- `ImageConcatMulti`
- `Any Switch (rgthree)`
- `Any Switch (rgthree)`
- `SaveImage`
- `CR Text`
- `llama_cpp_parameters`
- `llama_cpp_model_loader`
- `llama_cpp_instruct_adv`
- `LoadImage`
- `ShowText|pysssss`
- `RHSettingsNode`
- `CR Text`
- `easy showAnything`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `easy showAnything`
- `Fast Groups Bypasser (rgthree)`
- `CR Text`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `RHLLMChatNode`
- `easy showAnything`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `llama_cpp_instruct_adv`
- `RH_RhartImageG25OfficialTokenSunburstTextToImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `RH_RhartImageG2OfficialImageToImage`
- `RH_RhartImageG25OfficialTokenFlareEdit`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `RH_RhartImageG25OfficialTokenFlareTextToImage`
- `SaveImage`
- `RHSettingsNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `solarL_SaveImagesToZip`
- `JjkText`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `80`
- `height` = `80`
- `batch_size` = `1`
- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **75%**（70/93）

**有卡**：`llama_cpp_model_loader`、`llama_cpp_parameters`、`llama_cpp_instruct_adv`、`LoadImage`、`CR Text`、`RHLLMChatNode`、`ImageConcatMulti`、`SaveImage`、`RHSettingsNode`、`RH_RhartImageG25OfficialTokenSunburstTextToImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`RH_RhartImageG2OfficialImageToImage`、`RH_RhartImageG25OfficialTokenFlareEdit`、`RH_RhartImageG25OfficialTokenFlareTextToImage`、`UNETLoader`、`CLIPLoader`、`CLIPTextEncode`、`VAELoader`、`EmptyLatentImage`、`KSampler`、`VAEDecode`、`solarL_SaveImagesToZip`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
