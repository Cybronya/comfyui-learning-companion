---
key: 图片生成/图生图/Flux多重控制参考图片风格转绘（EasyControl Canny）_1909451347215659009.json
name: Flux多重控制参考图片风格转绘（EasyControl Canny）_1909451347215659009
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux多重控制参考图片风格转绘（EasyControl Canny）_1909451347215659009.json
hash: 382f4b99b45806c9
coverage: 0.825
learned_at: 2026-10-23 11:02:05
nodes: [easy showAnything, easy showAnything, EasyControlLoadLora, UpscaleModelLoader, CR Prompt Text, JjkShowText, UNETLoader, DualCLIPLoader, VAELoader, easy cleanGpuUsed, MirroredImage, EasyControlGenerate, FluxGuidance, CLIPTextEncode, ModelSamplingFlux, CLIPTextEncode, CLIPTextEncode, GetImageSize+, RandomNoise, BasicGuider, KSamplerSelect, SamplerCustomAdvanced, VAEDecode, PreviewImage, VAEEncode, Image Comparer (rgthree), BasicScheduler, SDXLPromptStyler, Image Comparer (rgthree), LayerUtility: ImageScaleByAspectRatio V2, UltimateSDUpscale, RH_Captioner, easy cleanGpuUsed, PreviewImage, Image Comparer (rgthree), EasyControlLoadFlux, LoraLoader, LoadImage, LoadImage, SaveImage]
patterns: [lora]
missing: []
parameters: {"lora_name": "FLUX -- Enhance Details and Texture -- FLUX DETAILER_V1.0.safetensors", "strength_clip": 1, "strength_model": 0.30000000000000004}
---

# 图片生成/图生图/Flux多重控制参考图片风格转绘（EasyControl Canny）_1909451347215659009.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux多重控制参考图片风格转绘（EasyControl Canny）_1909451347215659009.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（40 个）：
- `easy showAnything`
- `easy showAnything`
- `EasyControlLoadLora`
- `UpscaleModelLoader`
- `CR Prompt Text`
- `JjkShowText`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `VAELoader`
- `easy cleanGpuUsed`
- `MirroredImage`
- `EasyControlGenerate`
- `FluxGuidance`
- `CLIPTextEncode` ★核心
- `ModelSamplingFlux`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `GetImageSize+`
- `RandomNoise`
- `BasicGuider`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `PreviewImage`
- `VAEEncode` ★核心
- `Image Comparer (rgthree)`
- `BasicScheduler`
- `SDXLPromptStyler`
- `Image Comparer (rgthree)`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `UltimateSDUpscale`
- `RH_Captioner`
- `easy cleanGpuUsed`
- `PreviewImage`
- `Image Comparer (rgthree)`
- `EasyControlLoadFlux`
- `LoraLoader` ★核心
- `LoadImage`
- `LoadImage`
- `SaveImage`

**识别到的模式**：lora

## 关键参数

- `lora_name` = `FLUX -- Enhance Details and Texture -- FLUX DETAILER_V1.0.safetensors`
- `strength_model` = `0.30000000000000004`
- `strength_clip` = `1`

## 知识

覆盖率 **82%**（33/40）

**有卡**：`EasyControlLoadLora`、`UpscaleModelLoader`、`CR Prompt Text`、`JjkShowText`、`UNETLoader`、`DualCLIPLoader`、`VAELoader`、`easy cleanGpuUsed`、`MirroredImage`、`EasyControlGenerate`、`FluxGuidance`、`CLIPTextEncode`、`ModelSamplingFlux`、`GetImageSize+`、`RandomNoise`、`BasicGuider`、`KSamplerSelect`、`SamplerCustomAdvanced`、`VAEDecode`、`VAEEncode`、`BasicScheduler`、`SDXLPromptStyler`、`LayerUtility: ImageScaleByAspectRatio V2`、`UltimateSDUpscale`、`RH_Captioner`、`EasyControlLoadFlux`、`LoraLoader`、`LoadImage`、`SaveImage`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、LoadImage、FluxGuidance、KSamplerSelect、SamplerCustomAdvanced
