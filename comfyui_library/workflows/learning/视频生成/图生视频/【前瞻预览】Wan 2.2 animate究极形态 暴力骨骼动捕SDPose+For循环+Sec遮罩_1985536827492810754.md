---
key: 视频生成/图生视频/【前瞻预览】Wan 2.2 animate究极形态 暴力骨骼动捕SDPose+For循环+Sec遮罩_1985536827492810754.json
name: 【前瞻预览】Wan 2.2 animate究极形态 暴力骨骼动捕SDPose+For循环+Sec遮罩_1985536827492810754.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1985536827492810754.json
hash: 13ee9e406633a727
coverage: 0.496183
learned_at: 2026-10-15 22:32:51
nodes: [SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, MarkdownNote, GetNode, GetNode, CLIPVisionEncode, SetNode, SetNode, GetNode, GetNode, TrimVideoLatent, GetNode, GetNode, MarkdownNote, easy forLoopEnd, TrimVideoLatent, VAEDecode, ImageFromBatch, GetNode, VHS_VideoInfo, PoseAndFaceDetection, easy indexAnything, ImageFromBatch, easy indexAnything, easy indexAnything, ImageBatch, easy indexAnything, PreviewImage, VHS_VideoCombine, GetNode, VHS_VideoCombine, YOLOModelLoader, OnnxDetectionModelLoader, Reroute, GetNode, VAEDecode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, Reroute, SetNode, easy indexAnything, MaskPreview+, GetImageSizeAndCount, Reroute, SetNode, WanAnimateToVideo, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SDPoseOODLoader, GroundingDinoModelLoader_SDPose, VHS_VideoCombine, GetNode, GetNode, SetNode, MarkdownNote, MarkdownNote, KSampler, KSampler, SDPoseOODProcessor, GetNode, VHS_LoadVideo, InvertMask, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPLoader, CLIPVisionLoader, VAELoader, UNETLoader, ModelSamplingSD3, SetNode, LoraLoaderModelOnly, LoraLoaderModelOnly, MarkdownNote, GetNode, DrawMaskOnImage, VHS_VideoCombine, SetNode, SeCModelLoader, SeCVideoSegmentation, CLIPTextEncode, PreviewImage, CLIPTextEncode, CLIPTextEncode, VHS_LoadVideo, easy forLoopStart, GetNode, GetNode, PreviewImage, LoadImage, PointsEditor, Reroute, Reroute, SetNode, INTConstant, INTConstant, INTConstant, PreviewImage, WanAnimateToVideo, BlockifyMask, GrowMask, VHS_VideoCombine, LoadImage, SaveImage, Note]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "dpmpp_sde_gpu", "scheduler": "beta", "seed": 111798074041675, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/【前瞻预览】Wan 2.2 animate究极形态 暴力骨骼动捕SDPose+For循环+Sec遮罩_1985536827492810754.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1985536827492810754.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（131 个）：
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `MarkdownNote`
- `GetNode`
- `GetNode`
- `CLIPVisionEncode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `TrimVideoLatent`
- `GetNode`
- `GetNode`
- `MarkdownNote`
- `easy forLoopEnd`
- `TrimVideoLatent`
- `VAEDecode` ★核心
- `ImageFromBatch`
- `GetNode`
- `VHS_VideoInfo`
- `PoseAndFaceDetection`
- `easy indexAnything`
- `ImageFromBatch`
- `easy indexAnything`
- `easy indexAnything`
- `ImageBatch`
- `easy indexAnything`
- `PreviewImage`
- `VHS_VideoCombine`
- `GetNode`
- `VHS_VideoCombine`
- `YOLOModelLoader`
- `OnnxDetectionModelLoader`
- `Reroute`
- `GetNode`
- `VAEDecode` ★核心
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `Reroute`
- `SetNode`
- `easy indexAnything`
- `MaskPreview+`
- `GetImageSizeAndCount`
- `Reroute`
- `SetNode`
- `WanAnimateToVideo`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SDPoseOODLoader`
- `GroundingDinoModelLoader_SDPose`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `SetNode`
- `MarkdownNote`
- `MarkdownNote`
- `KSampler` ★核心
- `KSampler` ★核心
- `SDPoseOODProcessor`
- `GetNode`
- `VHS_LoadVideo`
- `InvertMask`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `CLIPVisionLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `MarkdownNote`
- `GetNode`
- `DrawMaskOnImage`
- `VHS_VideoCombine`
- `SetNode`
- `SeCModelLoader`
- `SeCVideoSegmentation`
- `CLIPTextEncode` ★核心
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VHS_LoadVideo`
- `easy forLoopStart`
- `GetNode`
- `GetNode`
- `PreviewImage`
- `LoadImage`
- `PointsEditor`
- `Reroute`
- `Reroute`
- `SetNode`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `PreviewImage`
- `WanAnimateToVideo`
- `BlockifyMask`
- `GrowMask`
- `VHS_VideoCombine`
- `LoadImage`
- `SaveImage`
- `Note`

## 关键参数

- `seed` = `111798074041675`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `dpmpp_sde_gpu`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **50%**（65/131）

**有卡**：`CLIPVisionEncode`、`TrimVideoLatent`、`easy forLoopEnd`、`VAEDecode`、`ImageFromBatch`、`VHS_VideoInfo`、`PoseAndFaceDetection`、`easy indexAnything`、`ImageBatch`、`VHS_VideoCombine`、`YOLOModelLoader`、`OnnxDetectionModelLoader`、`MaskPreview+`、`GetImageSizeAndCount`、`WanAnimateToVideo`、`SDPoseOODLoader`、`GroundingDinoModelLoader_SDPose`、`KSampler`、`SDPoseOODProcessor`、`VHS_LoadVideo`、`InvertMask`、`LoraLoaderModelOnly`、`CLIPLoader`、`CLIPVisionLoader`、`VAELoader`、`UNETLoader`、`ModelSamplingSD3`、`DrawMaskOnImage`、`SeCModelLoader`、`SeCVideoSegmentation`、`CLIPTextEncode`、`easy forLoopStart`、`LoadImage`、`PointsEditor`、`INTConstant`、`BlockifyMask`、`GrowMask`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
