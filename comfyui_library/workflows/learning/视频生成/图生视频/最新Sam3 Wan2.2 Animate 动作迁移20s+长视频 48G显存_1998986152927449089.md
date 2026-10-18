---
key: 视频生成/图生视频/最新Sam3 Wan2.2 Animate 动作迁移20s+长视频 48G显存_1998986152927449089.json
name: 最新Sam3 Wan2.2 Animate 动作迁移20s+长视频 48G显存_1998986152927449089.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/最新Sam3 Wan2.2 Animate 动作迁移20s+长视频 48G显存_1998986152927449089.json
hash: 9e25e47937f8ac60
coverage: 0.525641
learned_at: 2026-10-15 22:33:35
nodes: [SetNode, SetNode, SetNode, WanVideoVAELoader, GetNode, GetNode, ImageResizeKJv2, GetNode, GetNode, SetNode, CLIPVisionLoader, WanVideoClipVisionEncode, SetNode, GetNode, SetNode, GetNode, GetNode, GetNode, GetImageSizeAndCount, easy cleanGpuUsed, GetNode, WanVideoLoraSelectMulti, WanVideoSetLoRAs, WanVideoSetBlockSwap, GetNode, GetNode, SetNode, OnnxDetectionModelLoader, GetNode, ImageResizeKJv2, GetNode, easy cleanGpuUsed, easy cleanGpuUsed, LoadImage, SetNode, GetNode, ImpactImageBatchToImageList, GetNode, Int, VHS_VideoInfoLoaded, WanVideoTorchCompileSettings, easy cleanGpuUsed, LoadSAM3Model, WanVideoTeaCache, WanVideoModelLoader, WanVideoTextEncodeCached, GetNode, SetNode, DrawMaskOnImage, SetNode, SAM3Segmentation, SetNode, JjkText, SetNode, SetNode, SetNode, GetImageSizeAndCount, SetNode, PoseAndFaceDetection, SetNode, SetNode, GetNode, GetNode, LayerUtility: ImageScaleByAspectRatio V2, Int, Int, DrawViTPose, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoDecode, ACE_TextGoogleTranslate, MaskListToMaskBatch, VHS_VideoCombine, GetNode, easy cleanGpuUsed, WanVideoSampler, VHS_LoadVideo, MuyeLoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/最新Sam3 Wan2.2 Animate 动作迁移20s+长视频 48G显存_1998986152927449089.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1998986152927449089.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（78 个）：
- `SetNode`
- `SetNode`
- `SetNode`
- `WanVideoVAELoader`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `GetNode`
- `GetNode`
- `SetNode`
- `CLIPVisionLoader`
- `WanVideoClipVisionEncode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetImageSizeAndCount`
- `easy cleanGpuUsed`
- `GetNode`
- `WanVideoLoraSelectMulti`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `GetNode`
- `GetNode`
- `SetNode`
- `OnnxDetectionModelLoader`
- `GetNode`
- `ImageResizeKJv2`
- `GetNode`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `LoadImage`
- `SetNode`
- `GetNode`
- `ImpactImageBatchToImageList`
- `GetNode`
- `Int`
- `VHS_VideoInfoLoaded`
- `WanVideoTorchCompileSettings`
- `easy cleanGpuUsed`
- `LoadSAM3Model`
- `WanVideoTeaCache`
- `WanVideoModelLoader`
- `WanVideoTextEncodeCached`
- `GetNode`
- `SetNode`
- `DrawMaskOnImage`
- `SetNode`
- `SAM3Segmentation`
- `SetNode`
- `JjkText`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetImageSizeAndCount`
- `SetNode`
- `PoseAndFaceDetection`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Int`
- `Int`
- `DrawViTPose`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `ACE_TextGoogleTranslate`
- `MaskListToMaskBatch`
- `VHS_VideoCombine`
- `GetNode`
- `easy cleanGpuUsed`
- `WanVideoSampler` ★核心
- `VHS_LoadVideo`
- `MuyeLoadImage`

## 知识

覆盖率 **53%**（41/78）

**有卡**：`WanVideoVAELoader`、`ImageResizeKJv2`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`GetImageSizeAndCount`、`easy cleanGpuUsed`、`WanVideoLoraSelectMulti`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`OnnxDetectionModelLoader`、`LoadImage`、`ImpactImageBatchToImageList`、`Int`、`VHS_VideoInfoLoaded`、`WanVideoTorchCompileSettings`、`LoadSAM3Model`、`WanVideoTeaCache`、`WanVideoModelLoader`、`WanVideoTextEncodeCached`、`DrawMaskOnImage`、`SAM3Segmentation`、`PoseAndFaceDetection`、`LayerUtility: ImageScaleByAspectRatio V2`、`DrawViTPose`、`WanVideoAnimateEmbeds`、`WanVideoBlockSwap`、`WanVideoDecode`、`ACE_TextGoogleTranslate`、`MaskListToMaskBatch`、`VHS_VideoCombine`、`WanVideoSampler`、`VHS_LoadVideo`、`MuyeLoadImage`

**用到的条目**：LoadImage、LayerUtility: ImageScaleByAspectRatio V2、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs
