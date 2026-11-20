---
key: 平台全量/SDXL漫画转真人：Manga to Real Photo_1840089269988708353.json
name: SDXL漫画转真人：Manga to Real Photo_1840089269988708353
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/SDXL漫画转真人：Manga to Real Photo_1840089269988708353.json
hash: ec24ae7f21cd186f
coverage: 0.888889
learned_at: 2026-11-14 00:56:27
nodes: [KSampler, ACN_ControlNet++LoaderSingle, DepthAnythingV2Preprocessor, VAEDecode, VAEEncode, easy showAnything, AnyLinePreprocessor, CLIPTextEncode, UpscaleModelLoader, PreviewImage, CLIPTextEncode, CLIPTextEncode, PreviewBridge, UltralyticsDetectorProvider, SAMLoader, AV_FaceDetailer, easy promptReplace, easy promptConcat, LoraLoaderModelOnly, ControlNetApplyAdvanced, ControlNetApplyAdvanced, ControlNetApplyAdvanced, LoraLoaderModelOnly, Note, Note, UltimateSDUpscale, ACN_ControlNet++LoaderSingle, ACN_ControlNet++LoaderSingle, Joy_caption_load, Joy_caption, PreviewBridge, SaveImage, easy stylesSelector, ImageResize+, CheckpointLoaderSimple, LoadImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "dreamshaperXL_v21TurboDPMSDE.safetensors", "controlnet_strength": 0.08, "denoise": 0.8, "sampler_name": "dpmpp_sde", "scheduler": "karras", "seed": 505516836074868, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/SDXL漫画转真人：Manga to Real Photo_1840089269988708353.json

> 来源文件 `comfyui_library/workflows/平台全量/SDXL漫画转真人：Manga to Real Photo_1840089269988708353.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（36 个）：
- `KSampler` ★核心
- `ACN_ControlNet++LoaderSingle`
- `DepthAnythingV2Preprocessor`
- `VAEDecode` ★核心
- `VAEEncode` ★核心
- `easy showAnything`
- `AnyLinePreprocessor`
- `CLIPTextEncode` ★核心
- `UpscaleModelLoader`
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `PreviewBridge`
- `UltralyticsDetectorProvider`
- `SAMLoader`
- `AV_FaceDetailer`
- `easy promptReplace`
- `easy promptConcat`
- `LoraLoaderModelOnly` ★核心
- `ControlNetApplyAdvanced` ★核心
- `ControlNetApplyAdvanced` ★核心
- `ControlNetApplyAdvanced` ★核心
- `LoraLoaderModelOnly` ★核心
- `Note`
- `Note`
- `UltimateSDUpscale`
- `ACN_ControlNet++LoaderSingle`
- `ACN_ControlNet++LoaderSingle`
- `Joy_caption_load`
- `Joy_caption`
- `PreviewBridge`
- `SaveImage`
- `easy stylesSelector`
- `ImageResize+`
- `CheckpointLoaderSimple` ★核心
- `LoadImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `505516836074868`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `dpmpp_sde`
- `scheduler` = `karras`
- `denoise` = `0.8`
- `controlnet_strength` = `0.08`
- `checkpoint` = `dreamshaperXL_v21TurboDPMSDE.safetensors`

## 知识

覆盖率 **89%**（32/36）

**有卡**：`KSampler`、`ACN_ControlNet++LoaderSingle`、`DepthAnythingV2Preprocessor`、`VAEDecode`、`VAEEncode`、`AnyLinePreprocessor`、`CLIPTextEncode`、`UpscaleModelLoader`、`PreviewBridge`、`UltralyticsDetectorProvider`、`SAMLoader`、`AV_FaceDetailer`、`easy promptReplace`、`easy promptConcat`、`LoraLoaderModelOnly`、`ControlNetApplyAdvanced`、`UltimateSDUpscale`、`Joy_caption_load`、`Joy_caption`、`SaveImage`、`easy stylesSelector`、`ImageResize+`、`CheckpointLoaderSimple`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、ACN_ControlNet++LoaderSingle、ControlNetApplyAdvanced

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
