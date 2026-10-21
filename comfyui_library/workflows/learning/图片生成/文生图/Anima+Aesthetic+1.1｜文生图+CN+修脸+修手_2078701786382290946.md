---
key: 图片生成/文生图/Anima+Aesthetic+1.1｜文生图+CN+修脸+修手_2078701786382290946.json
name: Anima+Aesthetic+1.1｜文生图+CN+修脸+修手_2078701786382290946
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Anima+Aesthetic+1.1｜文生图+CN+修脸+修手_2078701786382290946.json
hash: 6fbf5493ccc5cedd
coverage: 0.766667
learned_at: 2026-10-20 00:18:47
nodes: [CLIPSetLastLayer, CLIPLoader, CLIPTextEncode, EmptyLatentImage, LatentUpscaleBy, PreviewImage, PreviewImage, PreviewImage, Seed (rgthree), AIO_Preprocessor, UltralyticsDetectorProvider, UltralyticsDetectorProvider, PreviewImage, NAGuidance, UltralyticsDetectorProvider, SAMLoader, AnimaLLLiteApply, ImageScale, LoadImage, ClownsharKSampler_Beta, RH_LLMAPI_Pro_Node, easy showAnything, FluxResolutionNode, LoraLoaderModelOnly, PreviewImage, Text, LoraLoaderModelOnly, UNETLoader, XB_UNetNameBroadcaster, VAELoader, VAEDecode, CLIPTextEncode, FaceDetailer, PreviewImage, ClownsharKSampler_Beta, VAEDecode, VAEDecode, LatentUpscaleBy, PreviewImage, PreviewImage, PreviewImage, Seed (rgthree), UltralyticsDetectorProvider, UltralyticsDetectorProvider, UltralyticsDetectorProvider, SAMLoader, PreviewImage, SaveImage, FaceDetailer, PreviewImage, FaceDetailer, SaveImage, PreviewImage, FaceDetailer, SaveImage, KSampler, SaveImage, KSampler, PreviewImage, VAEDecode]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 2.88, "denoise": 0.5500000000000002, "height": 512, "sampler_name": "euler", "scheduler": "simple", "seed": 426731920633172, "steps": 30, "width": 512}
---

# 图片生成/文生图/Anima+Aesthetic+1.1｜文生图+CN+修脸+修手_2078701786382290946.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Anima+Aesthetic+1.1｜文生图+CN+修脸+修手_2078701786382290946.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（60 个）：
- `CLIPSetLastLayer`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `EmptyLatentImage` ★核心
- `LatentUpscaleBy`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `Seed (rgthree)`
- `AIO_Preprocessor`
- `UltralyticsDetectorProvider`
- `UltralyticsDetectorProvider`
- `PreviewImage`
- `NAGuidance`
- `UltralyticsDetectorProvider`
- `SAMLoader`
- `AnimaLLLiteApply`
- `ImageScale`
- `LoadImage`
- `ClownsharKSampler_Beta` ★核心
- `RH_LLMAPI_Pro_Node`
- `easy showAnything`
- `FluxResolutionNode`
- `LoraLoaderModelOnly` ★核心
- `PreviewImage`
- `Text`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `XB_UNetNameBroadcaster`
- `VAELoader`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `FaceDetailer`
- `PreviewImage`
- `ClownsharKSampler_Beta` ★核心
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `LatentUpscaleBy`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `Seed (rgthree)`
- `UltralyticsDetectorProvider`
- `UltralyticsDetectorProvider`
- `UltralyticsDetectorProvider`
- `SAMLoader`
- `PreviewImage`
- `SaveImage`
- `FaceDetailer`
- `PreviewImage`
- `FaceDetailer`
- `SaveImage`
- `PreviewImage`
- `FaceDetailer`
- `SaveImage`
- `KSampler` ★核心
- `SaveImage`
- `KSampler` ★核心
- `PreviewImage`
- `VAEDecode` ★核心

**识别到的模式**：text_to_image

## 关键参数

- `width` = `512`
- `height` = `512`
- `batch_size` = `1`
- `seed` = `426731920633172`
- `steps` = `30`
- `cfg` = `2.88`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.5500000000000002`

## 知识

覆盖率 **77%**（46/60）

**有卡**：`CLIPSetLastLayer`、`CLIPLoader`、`CLIPTextEncode`、`EmptyLatentImage`、`LatentUpscaleBy`、`Seed (rgthree)`、`AIO_Preprocessor`、`UltralyticsDetectorProvider`、`NAGuidance`、`SAMLoader`、`AnimaLLLiteApply`、`ImageScale`、`LoadImage`、`ClownsharKSampler_Beta`、`RH_LLMAPI_Pro_Node`、`FluxResolutionNode`、`LoraLoaderModelOnly`、`Text`、`UNETLoader`、`XB_UNetNameBroadcaster`、`VAELoader`、`VAEDecode`、`FaceDetailer`、`SaveImage`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、EmptyLatentImage
