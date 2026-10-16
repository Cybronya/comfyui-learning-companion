---
key: 视频生成/图生视频/Wan2.2_AnimateV2__SEC新版替换工作流（全身_局部）_2065864428897259522.json
name: Wan2.2_AnimateV2__SEC新版替换工作流（全身_局部）_2065864428897259522.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2065864428897259522.json
hash: 81292288e6dfbc72
coverage: 0.903226
learned_at: 2026-10-15 22:39:45
nodes: [Note, UNETLoader, UnetLoaderGGUF, CLIPTextEncode, PreviewImage, ImageResizeKJv2, CM_IntToFloat, LoadImage, easy imageSize, CLIPTextEncode, CLIPVisionLoader, Note, TrimVideoLatent, LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, PreviewImage, easy showAnything, easy int, SimpleMath+, Mute / Bypass Repeater (rgthree), CR Model Input Switch, VAELoader, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, ImageBlend, OnnxDetectionModelLoader, PoseAndFaceDetection, DrawViTPose, SeCVideoSegmentation, easy cleanGpuUsed, GrowMask, BlockifyMask, Fast Bypasser (rgthree), DrawMaskOnImage, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, SeCModelLoader, VAEDecode, easy cleanGpuUsed, CLIPVisionEncode, easy cleanGpuUsed, CLIPLoader, WanAnimateToVideo, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, KSampler, ImpactInt, PixaromaResolution, LoadImage, LoadImage, MarkdownNote, PointsEditor, VHS_VideoCombine, VHS_VideoCombine, RIFE VFI, LoadVideoUI, RHHiddenNodes]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "sa_solver", "scheduler": "beta", "seed": 1043782060985962, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/Wan2.2_AnimateV2__SEC新版替换工作流（全身_局部）_2065864428897259522.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2065864428897259522.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（62 个）：
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

## 关键参数

- `seed` = `1043782060985962`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `sa_solver`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **90%**（56/62）

**有卡**：`UNETLoader`、`UnetLoaderGGUF`、`CLIPTextEncode`、`ImageResizeKJv2`、`CM_IntToFloat`、`LoadImage`、`easy imageSize`、`CLIPVisionLoader`、`TrimVideoLatent`、`LayerUtility: PurgeVRAM V2`、`easy int`、`SimpleMath+`、`Mute / Bypass Repeater (rgthree)`、`CR Model Input Switch`、`VAELoader`、`easy cleanGpuUsed`、`ImageBlend`、`OnnxDetectionModelLoader`、`PoseAndFaceDetection`、`DrawViTPose`、`SeCVideoSegmentation`、`GrowMask`、`BlockifyMask`、`Fast Bypasser (rgthree)`、`DrawMaskOnImage`、`SeCModelLoader`、`VAEDecode`、`CLIPVisionEncode`、`CLIPLoader`、`WanAnimateToVideo`、`KSampler`、`ImpactInt`、`PixaromaResolution`、`PointsEditor`、`VHS_VideoCombine`、`RIFE VFI`、`LoadVideoUI`、`RHHiddenNodes`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、CLIPVisionEncode

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
