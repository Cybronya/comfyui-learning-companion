---
key: 视频生成/图生视频/Wan2.2_原图加两套换装_带货视频_2075861551701127169.json
name: Wan2.2_原图加两套换装_带货视频_2075861551701127169.json
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2075861551701127169.json
hash: f58c0ff4abdc5f0f
coverage: 0.988889
learned_at: 2026-10-15 22:41:26
nodes: [INTConstant, INTConstant, SimpleMath+, LayerUtility: ImageScaleByAspectRatio V2, CR Text, CR Text, CR Text, CR Text, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelPatchTorchSettings, ModelSamplingSD3, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelPatchTorchSettings, ModelSamplingSD3, CLIPLoader, CLIPVisionLoader, VAELoader, CLIPTextEncode, CLIPTextEncode, CLIPVisionEncode, WanImageToVideo, KSamplerAdvanced, KSamplerAdvanced, VAEDecode, ImageScaleBy, easy cleanGpuUsed, RIFE VFI, VHS_VideoCombine, LayerUtility: ImageScaleByAspectRatio V2, CLIPTextEncode, CLIPVisionEncode, WanImageToVideo, KSamplerAdvanced, KSamplerAdvanced, VAEDecode, ImageScaleBy, easy cleanGpuUsed, RIFE VFI, VHS_VideoCombine, LayerUtility: ImageScaleByAspectRatio V2, CLIPTextEncode, CLIPVisionEncode, WanImageToVideo, KSamplerAdvanced, KSamplerAdvanced, VAEDecode, ImageScaleBy, easy cleanGpuUsed, RIFE VFI, VHS_VideoCombine, ImageBatchExtendWithOverlap, ImageBatchExtendWithOverlap, VHS_VideoCombine, CR Text, CR Text, VAELoader, CLIPLoader, UNETLoader, LoraLoaderModelOnly, CLIPTextEncode, PrimitiveNode, ImageScaleToTotalPixels, GetImageSize, EmptyLatentImage, TextEncodeQwenImageEditPlus, KSampler, VAEDecode, easy cleanGpuUsed, SeedVR2, SaveImage, ImageScaleToTotalPixels, GetImageSize, EmptyLatentImage, TextEncodeQwenImageEditPlus, KSampler, VAEDecode, easy cleanGpuUsed, SeedVR2, SaveImage, ImageScale, ImageScale, LoadImage, LoadImage, LoadImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1280, "sampler_name": "euler", "scheduler": "simple", "seed": 166609105414396, "steps": 8, "width": 720}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/Wan2.2_原图加两套换装_带货视频_2075861551701127169.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2075861551701127169.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（90 个）：
- `INTConstant`
- `INTConstant`
- `SimpleMath+`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CR Text`
- `CR Text`
- `CR Text`
- `CR Text`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `CLIPLoader`
- `CLIPVisionLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPVisionEncode`
- `WanImageToVideo`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `ImageScaleBy`
- `easy cleanGpuUsed`
- `RIFE VFI`
- `VHS_VideoCombine`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPTextEncode` ★核心
- `CLIPVisionEncode`
- `WanImageToVideo`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `ImageScaleBy`
- `easy cleanGpuUsed`
- `RIFE VFI`
- `VHS_VideoCombine`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPTextEncode` ★核心
- `CLIPVisionEncode`
- `WanImageToVideo`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `ImageScaleBy`
- `easy cleanGpuUsed`
- `RIFE VFI`
- `VHS_VideoCombine`
- `ImageBatchExtendWithOverlap`
- `ImageBatchExtendWithOverlap`
- `VHS_VideoCombine`
- `CR Text`
- `CR Text`
- `VAELoader`
- `CLIPLoader`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `PrimitiveNode`
- `ImageScaleToTotalPixels`
- `GetImageSize`
- `EmptyLatentImage` ★核心
- `TextEncodeQwenImageEditPlus`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `SeedVR2`
- `SaveImage`
- `ImageScaleToTotalPixels`
- `GetImageSize`
- `EmptyLatentImage` ★核心
- `TextEncodeQwenImageEditPlus`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `SeedVR2`
- `SaveImage`
- `ImageScale`
- `ImageScale`
- `LoadImage`
- `LoadImage`
- `LoadImage`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `166609105414396`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `720`
- `height` = `1280`
- `batch_size` = `1`

## 知识

覆盖率 **99%**（89/90）

**有卡**：`INTConstant`、`SimpleMath+`、`LayerUtility: ImageScaleByAspectRatio V2`、`CR Text`、`UNETLoader`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`ModelSamplingSD3`、`CLIPLoader`、`CLIPVisionLoader`、`VAELoader`、`CLIPTextEncode`、`CLIPVisionEncode`、`WanImageToVideo`、`KSamplerAdvanced`、`VAEDecode`、`ImageScaleBy`、`easy cleanGpuUsed`、`RIFE VFI`、`VHS_VideoCombine`、`ImageBatchExtendWithOverlap`、`ImageScaleToTotalPixels`、`GetImageSize`、`EmptyLatentImage`、`TextEncodeQwenImageEditPlus`、`KSampler`、`SeedVR2`、`SaveImage`、`ImageScale`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
