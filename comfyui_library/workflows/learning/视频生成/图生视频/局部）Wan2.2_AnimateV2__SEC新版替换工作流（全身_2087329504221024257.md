---
key: 视频生成/图生视频/局部）Wan2.2_AnimateV2__SEC新版替换工作流（全身_2087329504221024257.json
name: 局部）Wan2.2_AnimateV2__SEC新版替换工作流（全身_2087329504221024257
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/局部）Wan2.2_AnimateV2__SEC新版替换工作流（全身_2087329504221024257.json
hash: ef477c94f6fcfbf1
coverage: 0.852632
learned_at: 2026-10-16 21:28:10
nodes: [Note, UNETLoader, UnetLoaderGGUF, CLIPTextEncode, PreviewImage, ImageResizeKJv2, CM_IntToFloat, LoadImage, easy imageSize, CLIPTextEncode, CLIPVisionLoader, Note, TrimVideoLatent, LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, PreviewImage, easy showAnything, easy int, SimpleMath+, Mute / Bypass Repeater (rgthree), CR Model Input Switch, VAELoader, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, ImageBlend, OnnxDetectionModelLoader, PoseAndFaceDetection, DrawViTPose, SeCVideoSegmentation, easy cleanGpuUsed, GrowMask, BlockifyMask, Fast Bypasser (rgthree), DrawMaskOnImage, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, SeCModelLoader, VAEDecode, easy cleanGpuUsed, CLIPVisionEncode, easy cleanGpuUsed, CLIPLoader, WanAnimateToVideo, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, KSampler, ImpactInt, PixaromaResolution, LoadImage, LoadImage, MarkdownNote, PointsEditor, VHS_VideoCombine, VHS_VideoCombine, RIFE VFI, LoadVideoUI, RHHiddenNodes, MarkdownNote, Note, Note, Note, 孤海注释, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, KSampler, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, VAELoader, CLIPLoader, EmptyLatentImage, JjkText, CLIPTextEncode, Note, 孤海注释]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/局部）Wan2.2_AnimateV2__SEC新版替换工作流（全身_2087329504221024257.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/局部）Wan2.2_AnimateV2__SEC新版替换工作流（全身_2087329504221024257.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（95 个）：
- `Note`
- `UNETLoader` ★核心
- `UnetLoaderGGUF` ★核心
- `CLIPTextEncode` ★核心
- `PreviewImage`
- `ImageResizeKJv2`
- `CM_IntToFloat`
- `LoadImage`
- `easy imageSize`
- `CLIPTextEncode` ★核心
- `CLIPVisionLoader`
- `Note`
- `TrimVideoLatent`
- `LayerUtility: PurgeVRAM V2`
- `LayerUtility: PurgeVRAM V2`
- `PreviewImage`
- `easy showAnything`
- `easy int`
- `SimpleMath+`
- `Mute / Bypass Repeater (rgthree)`
- `CR Model Input Switch`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `ImageBlend`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `DrawViTPose`
- `SeCVideoSegmentation`
- `easy cleanGpuUsed`
- `GrowMask`
- `BlockifyMask`
- `Fast Bypasser (rgthree)`
- `DrawMaskOnImage`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `SeCModelLoader`
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `CLIPVisionEncode`
- `easy cleanGpuUsed`
- `CLIPLoader`
- `WanAnimateToVideo`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `KSampler` ★核心
- `ImpactInt`
- `PixaromaResolution`
- `LoadImage`
- `LoadImage`
- `MarkdownNote`
- `PointsEditor`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `RIFE VFI`
- `LoadVideoUI`
- `RHHiddenNodes`
- `MarkdownNote`
- `Note`
- `Note`
- `Note`
- `孤海注释`
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
- `UNETLoader` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `solarL_SaveImagesToZip`
- `VAEDecode` ★核心
- `VAELoader`
- `CLIPLoader`
- `EmptyLatentImage` ★核心
- `JjkText`
- `CLIPTextEncode` ★核心
- `Note`
- `孤海注释`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`
- `width` = `80`
- `height` = `80`
- `batch_size` = `1`

## 知识

覆盖率 **85%**（81/95）

**有卡**：`UNETLoader`、`UnetLoaderGGUF`、`CLIPTextEncode`、`ImageResizeKJv2`、`CM_IntToFloat`、`LoadImage`、`easy imageSize`、`CLIPVisionLoader`、`TrimVideoLatent`、`LayerUtility: PurgeVRAM V2`、`easy int`、`SimpleMath+`、`Mute / Bypass Repeater (rgthree)`、`CR Model Input Switch`、`VAELoader`、`easy cleanGpuUsed`、`ImageBlend`、`OnnxDetectionModelLoader`、`PoseAndFaceDetection`、`DrawViTPose`、`SeCVideoSegmentation`、`GrowMask`、`BlockifyMask`、`Fast Bypasser (rgthree)`、`DrawMaskOnImage`、`SeCModelLoader`、`VAEDecode`、`CLIPVisionEncode`、`CLIPLoader`、`WanAnimateToVideo`、`KSampler`、`ImpactInt`、`PixaromaResolution`、`PointsEditor`、`VHS_VideoCombine`、`RIFE VFI`、`LoadVideoUI`、`RHHiddenNodes`、`LoraLoaderModelOnly`、`solarL_SaveImagesToZip`、`EmptyLatentImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
