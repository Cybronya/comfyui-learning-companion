---
key: 平台全量/SDXL漫画转真人：Manga to Real Photo_1871019765580824578.json
name: SDXL漫画转真人：Manga to Real Photo_1871019765580824578
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/SDXL漫画转真人：Manga to Real Photo_1871019765580824578.json
hash: 14baf7e56494d85b
coverage: 0.891892
learned_at: 2026-11-14 00:56:27
nodes: [KSampler, VAEDecode, VAEEncode, AnyLinePreprocessor, CLIPTextEncode, PreviewImage, CLIPTextEncode, UltralyticsDetectorProvider, SAMLoader, PreviewBridge, ControlNetApplyAdvanced, ControlNetApplyAdvanced, ControlNetApplyAdvanced, Note, LoadImage, AegisFlow/aflogo, ImageResize+, LoraLoaderModelOnly, Note, CheckpointLoaderSimple, CLIPTextEncode, DepthAnythingV2Preprocessor, ACN_ControlNet++LoaderSingle, ACN_ControlNet++LoaderSingle, ACN_ControlNet++LoaderSingle, PreviewBridge, AV_FaceDetailer, SaveImage, easy promptConcat, easy promptReplace, easy stylesSelector, easy showAnything, RH_Captioner, UpscaleModelLoader, UltimateSDUpscale, SaveImage, LoraLoaderModelOnly]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "dreamshaperXL_v21TurboDPMSDE.safetensors", "controlnet_strength": 0.08, "denoise": 0.8, "sampler_name": "dpmpp_sde", "scheduler": "karras", "seed": 1020177553773995, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/SDXL漫画转真人：Manga to Real Photo_1871019765580824578.json

> 来源文件 `comfyui_library/workflows/平台全量/SDXL漫画转真人：Manga to Real Photo_1871019765580824578.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（37 个）：
- `KSampler` ★核心
- `VAEDecode` ★核心
- `VAEEncode` ★核心
- `AnyLinePreprocessor`
- `CLIPTextEncode` ★核心
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `UltralyticsDetectorProvider`
- `SAMLoader`
- `PreviewBridge`
- `ControlNetApplyAdvanced` ★核心
- `ControlNetApplyAdvanced` ★核心
- `ControlNetApplyAdvanced` ★核心
- `Note`
- `LoadImage`
- `AegisFlow/aflogo`
- `ImageResize+`
- `LoraLoaderModelOnly` ★核心
- `Note`
- `CheckpointLoaderSimple` ★核心
- `CLIPTextEncode` ★核心
- `DepthAnythingV2Preprocessor`
- `ACN_ControlNet++LoaderSingle`
- `ACN_ControlNet++LoaderSingle`
- `ACN_ControlNet++LoaderSingle`
- `PreviewBridge`
- `AV_FaceDetailer`
- `SaveImage`
- `easy promptConcat`
- `easy promptReplace`
- `easy stylesSelector`
- `easy showAnything`
- `RH_Captioner`
- `UpscaleModelLoader`
- `UltimateSDUpscale`
- `SaveImage`
- `LoraLoaderModelOnly` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `1020177553773995`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `dpmpp_sde`
- `scheduler` = `karras`
- `denoise` = `0.8`
- `controlnet_strength` = `0.08`
- `checkpoint` = `dreamshaperXL_v21TurboDPMSDE.safetensors`

## 知识

覆盖率 **89%**（33/37）

**有卡**：`KSampler`、`VAEDecode`、`VAEEncode`、`AnyLinePreprocessor`、`CLIPTextEncode`、`UltralyticsDetectorProvider`、`SAMLoader`、`PreviewBridge`、`ControlNetApplyAdvanced`、`LoadImage`、`AegisFlow/aflogo`、`ImageResize+`、`LoraLoaderModelOnly`、`CheckpointLoaderSimple`、`DepthAnythingV2Preprocessor`、`ACN_ControlNet++LoaderSingle`、`AV_FaceDetailer`、`SaveImage`、`easy promptConcat`、`easy promptReplace`、`easy stylesSelector`、`RH_Captioner`、`UpscaleModelLoader`、`UltimateSDUpscale`

**用到的条目**：KSampler、VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、ACN_ControlNet++LoaderSingle、ControlNetApplyAdvanced

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
