---
key: 平台全量/Kontext Dev-单图编辑V2.3_1941487840805208065.json
name: Kontext Dev-单图编辑V2.3_1941487840805208065
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Kontext Dev-单图编辑V2.3_1941487840805208065.json
hash: 8c7190ed19475a6f
coverage: 0.75
learned_at: 2026-11-14 00:34:12
nodes: [BasicScheduler, ModelSamplingFlux, VAELoader, DualCLIPLoader, ReferenceLatent, RandomNoise, EmptySD3LatentImage, KSamplerSelect, CLIPTextEncode, VAEEncode, ImageConcanate, FluxGuidance, BasicGuider, FluxKontextImageScale, DualCLIPLoader, easy cleanGpuUsed, CLIPTextEncode, CLIPTextEncode, UltimateSDUpscale, SamplerCustomAdvanced, RH_Captioner, SDXLPromptStyler, UpscaleModelLoader, VAEDecode, LayerUtility: PurgeVRAM V2, SetNode, GetImageSize+, UNETLoader, VAELoader, ModelSamplingFlux, Image Comparer (rgthree), GetNode, SaveImage, GetImageSize+, UNETLoader, LoraLoader, LoraLoaderModelOnly, DeepTranslatorTextNode, PreviewImage, RH_LLMAPI_NODE, easy showAnything, SaveImage, LoadImage, LoadKontextPresets, CR Text, easy showAnything, Reroute, DeepTranslatorTextNode, easy showAnything, Note, Reroute, Fast Groups Bypasser (rgthree), Reroute, Note, Fast Groups Bypasser (rgthree), RH_LLMAPI_NODE]
patterns: [lora]
missing: []
parameters: {"lora_name": "Flux洗图神器.safetensors", "strength_clip": 1, "strength_model": 0.6000000000000001}
---

# 平台全量/Kontext Dev-单图编辑V2.3_1941487840805208065.json

> 来源文件 `comfyui_library/workflows/平台全量/Kontext Dev-单图编辑V2.3_1941487840805208065.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（56 个）：
- `BasicScheduler`
- `ModelSamplingFlux`
- `VAELoader`
- `DualCLIPLoader`
- `ReferenceLatent`
- `RandomNoise`
- `EmptySD3LatentImage`
- `KSamplerSelect` ★核心
- `CLIPTextEncode` ★核心
- `VAEEncode` ★核心
- `ImageConcanate`
- `FluxGuidance`
- `BasicGuider`
- `FluxKontextImageScale`
- `DualCLIPLoader`
- `easy cleanGpuUsed`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `UltimateSDUpscale`
- `SamplerCustomAdvanced` ★核心
- `RH_Captioner`
- `SDXLPromptStyler`
- `UpscaleModelLoader`
- `VAEDecode` ★核心
- `LayerUtility: PurgeVRAM V2`
- `SetNode`
- `GetImageSize+`
- `UNETLoader` ★核心
- `VAELoader`
- `ModelSamplingFlux`
- `Image Comparer (rgthree)`
- `GetNode`
- `SaveImage`
- `GetImageSize+`
- `UNETLoader` ★核心
- `LoraLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `DeepTranslatorTextNode`
- `PreviewImage`
- `RH_LLMAPI_NODE`
- `easy showAnything`
- `SaveImage`
- `LoadImage`
- `LoadKontextPresets`
- `CR Text`
- `easy showAnything`
- `Reroute`
- `DeepTranslatorTextNode`
- `easy showAnything`
- `Note`
- `Reroute`
- `Fast Groups Bypasser (rgthree)`
- `Reroute`
- `Note`
- `Fast Groups Bypasser (rgthree)`
- `RH_LLMAPI_NODE`

**识别到的模式**：lora

## 关键参数

- `lora_name` = `Flux洗图神器.safetensors`
- `strength_model` = `0.6000000000000001`
- `strength_clip` = `1`

## 知识

覆盖率 **75%**（42/56）

**有卡**：`BasicScheduler`、`ModelSamplingFlux`、`VAELoader`、`DualCLIPLoader`、`ReferenceLatent`、`RandomNoise`、`EmptySD3LatentImage`、`KSamplerSelect`、`CLIPTextEncode`、`VAEEncode`、`ImageConcanate`、`FluxGuidance`、`BasicGuider`、`FluxKontextImageScale`、`easy cleanGpuUsed`、`UltimateSDUpscale`、`SamplerCustomAdvanced`、`RH_Captioner`、`SDXLPromptStyler`、`UpscaleModelLoader`、`VAEDecode`、`LayerUtility: PurgeVRAM V2`、`GetImageSize+`、`UNETLoader`、`SaveImage`、`LoraLoader`、`LoraLoaderModelOnly`、`DeepTranslatorTextNode`、`RH_LLMAPI_NODE`、`LoadImage`、`LoadKontextPresets`、`CR Text`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、LoadImage、FluxGuidance、KSamplerSelect
