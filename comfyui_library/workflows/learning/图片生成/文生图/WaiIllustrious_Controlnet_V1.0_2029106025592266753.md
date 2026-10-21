---
key: 图片生成/文生图/WaiIllustrious_Controlnet_V1.0_2029106025592266753.json
name: WaiIllustrious_Controlnet_V1.0_2029106025592266753
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/WaiIllustrious_Controlnet_V1.0_2029106025592266753.json
hash: f9055833545cf9da
coverage: 0.619048
learned_at: 2026-10-20 23:21:47
nodes: [Image Comparer (rgthree), LatentUpscaleBy, SaveImage, Image Comparer (rgthree), KSampler, PreviewImage, PreviewImage, PreviewImage, PreviewImage, UltralyticsDetectorProvider, VAEDecode, UltralyticsDetectorProvider, SaveImage, FaceDetailer, VAEDecode, PreviewImage, EmptyLatentImage, ImageResizeKJv2, Note, KSampler, Reroute, PrimitiveInt, PreviewImage, Note, Reroute (rgthree), OpenposePreprocessor, PreviewImage, Note, Image Comparer (rgthree), FaceDetailer, CLIPTextEncode, CLIPTextEncode, GridLoras, LoadImage, ControlNetApplyAdvanced, CheckpointLoaderSimple, ControlNetLoader, ControlNetLoader, ControlNetApplyAdvanced, PreviewBridge, DepthAnythingV2Preprocessor, DWPreprocessor]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 7, "checkpoint": "new_waiIllustriousSDXL_v160.safetensors", "controlnet_strength": 0.33, "denoise": 1, "height": 1280, "sampler_name": "euler_ancestral", "scheduler": "normal", "seed": 629841344968569, "steps": 27, "width": 960}
---

# 图片生成/文生图/WaiIllustrious_Controlnet_V1.0_2029106025592266753.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/WaiIllustrious_Controlnet_V1.0_2029106025592266753.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（42 个）：
- `Image Comparer (rgthree)`
- `LatentUpscaleBy`
- `SaveImage`
- `Image Comparer (rgthree)`
- `KSampler` ★核心
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `UltralyticsDetectorProvider`
- `VAEDecode` ★核心
- `UltralyticsDetectorProvider`
- `SaveImage`
- `FaceDetailer`
- `VAEDecode` ★核心
- `PreviewImage`
- `EmptyLatentImage` ★核心
- `ImageResizeKJv2`
- `Note`
- `KSampler` ★核心
- `Reroute`
- `PrimitiveInt`
- `PreviewImage`
- `Note`
- `Reroute (rgthree)`
- `OpenposePreprocessor`
- `PreviewImage`
- `Note`
- `Image Comparer (rgthree)`
- `FaceDetailer`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `GridLoras`
- `LoadImage`
- `ControlNetApplyAdvanced` ★核心
- `CheckpointLoaderSimple` ★核心
- `ControlNetLoader`
- `ControlNetLoader`
- `ControlNetApplyAdvanced` ★核心
- `PreviewBridge`
- `DepthAnythingV2Preprocessor`
- `DWPreprocessor`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `629841344968569`
- `steps` = `27`
- `cfg` = `7`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `normal`
- `denoise` = `1`
- `width` = `960`
- `height` = `1280`
- `batch_size` = `1`
- `controlnet_strength` = `0.33`
- `checkpoint` = `new_waiIllustriousSDXL_v160.safetensors`

## 知识

覆盖率 **62%**（26/42）

**有卡**：`LatentUpscaleBy`、`SaveImage`、`KSampler`、`UltralyticsDetectorProvider`、`VAEDecode`、`FaceDetailer`、`EmptyLatentImage`、`ImageResizeKJv2`、`OpenposePreprocessor`、`CLIPTextEncode`、`GridLoras`、`LoadImage`、`ControlNetApplyAdvanced`、`CheckpointLoaderSimple`、`ControlNetLoader`、`PreviewBridge`、`DepthAnythingV2Preprocessor`、`DWPreprocessor`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、EmptyLatentImage、LoadImage、ControlNetApplyAdvanced、ControlNetLoader
