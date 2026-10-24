---
key: 图片生成/图生图/WAN2.2超真实洗图【细节增强】_1958730830350876674.json
name: WAN2.2超真实洗图【细节增强】_1958730830350876674
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/WAN2.2超真实洗图【细节增强】_1958730830350876674.json
hash: 99ecf03a071350dc
coverage: 0.933333
learned_at: 2026-10-23 11:27:32
nodes: [ModelSamplingSD3, UNETLoader, BasicScheduler, RandomNoise, CLIPLoader, CLIPTextEncode, LoraLoaderModelOnly, CLIPTextEncode, WanVideoNAG, ModelSamplingSD3, CFGGuider, KSampler, SamplerCustomAdvanced, SamplerCustomAdvanced, SplitSigmas, DisableNoise, KSamplerSelect, SplitSigmasDenoise, VAELoader, VAEEncode, Text Concatenate, RH_Captioner, VAEDecode, Image Comparer (rgthree), SaveImage, LayerUtility: ImageScaleRestore, VAEDecode, SaveImage, LayerUtility: ImageScaleRestore, Image Comparer (rgthree), LoadImage, CLIPLoader, CLIPTextEncode, VAEEncode, VAELoader, RH_Captioner, CLIPTextEncode, LoraLoaderModelOnly, UNETLoader, LayerUtility: ImageScaleByAspectRatio V2, UpscaleModelLoader, ImageUpscaleWithModel, ImageScaleBy, Fast Groups Bypasser (rgthree), Text Multiline]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 0.20000000000000004, "sampler_name": "euler", "scheduler": "simple", "seed": 739, "steps": 10}
---

# 图片生成/图生图/WAN2.2超真实洗图【细节增强】_1958730830350876674.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/WAN2.2超真实洗图【细节增强】_1958730830350876674.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（45 个）：
- `ModelSamplingSD3`
- `UNETLoader` ★核心
- `BasicScheduler`
- `RandomNoise`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `WanVideoNAG`
- `ModelSamplingSD3`
- `CFGGuider`
- `KSampler` ★核心
- `SamplerCustomAdvanced` ★核心
- `SamplerCustomAdvanced` ★核心
- `SplitSigmas`
- `DisableNoise`
- `KSamplerSelect` ★核心
- `SplitSigmasDenoise`
- `VAELoader`
- `VAEEncode` ★核心
- `Text Concatenate`
- `RH_Captioner`
- `VAEDecode` ★核心
- `Image Comparer (rgthree)`
- `SaveImage`
- `LayerUtility: ImageScaleRestore`
- `VAEDecode` ★核心
- `SaveImage`
- `LayerUtility: ImageScaleRestore`
- `Image Comparer (rgthree)`
- `LoadImage`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAEEncode` ★核心
- `VAELoader`
- `RH_Captioner`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `UpscaleModelLoader`
- `ImageUpscaleWithModel`
- `ImageScaleBy`
- `Fast Groups Bypasser (rgthree)`
- `Text Multiline`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `739`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.20000000000000004`

## 知识

覆盖率 **93%**（42/45）

**有卡**：`ModelSamplingSD3`、`UNETLoader`、`BasicScheduler`、`RandomNoise`、`CLIPLoader`、`CLIPTextEncode`、`LoraLoaderModelOnly`、`WanVideoNAG`、`CFGGuider`、`KSampler`、`SamplerCustomAdvanced`、`SplitSigmas`、`DisableNoise`、`KSamplerSelect`、`SplitSigmasDenoise`、`VAELoader`、`VAEEncode`、`Text Concatenate`、`RH_Captioner`、`VAEDecode`、`SaveImage`、`LayerUtility: ImageScaleRestore`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`UpscaleModelLoader`、`ImageUpscaleWithModel`、`ImageScaleBy`、`Text Multiline`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader
