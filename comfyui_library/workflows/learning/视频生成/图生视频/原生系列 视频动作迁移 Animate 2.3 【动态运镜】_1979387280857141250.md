---
key: 视频生成/图生视频/原生系列 视频动作迁移 Animate 2.3 【动态运镜】_1979387280857141250.json
name: 原生系列 视频动作迁移 Animate 2.3 【动态运镜】_1979387280857141250.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/原生系列 视频动作迁移 Animate 2.3 【动态运镜】_1979387280857141250.json
hash: 1ff9b32f29c8845e
coverage: 0.535714
learned_at: 2026-10-15 22:32:23
nodes: [ImpactSwitch, Primitive integer [Crystools], SetNode, SetNode, ImageResizeKJv2, SetNode, Primitive integer [Crystools], WanVideoSetBlockSwap, SetNode, GetNode, WanVideoVAELoader, SetNode, WanVideoAnimateEmbeds, GetNode, GetNode, GetNode, WanVideoClipVisionEncode, CLIPVisionLoader, GetNode, DWPreprocessor, SetNode, PoseAndFaceDetection, SetNode, GetNode, GetNode, GetNode, ImpactSwitch, Primitive integer [Crystools], WanVideoTextEncodeCached, SetNode, WanVideoDecode, SetNode, LoadImage, WanVideoSampler, GetImageSizeAndCount, FaceMaskFromPoseKeypoints, GetNode, GetNode, LoadImage, GetNode, VHS_VideoCombine, VHS_VideoCombine, Primitive integer [Crystools], VHS_LoadVideo, GetNode, SetNode, easy showAnything, easy showAnything, easy showAnything, easy showAnything, easy showAnything, SetNode, SetNode, SetNode, VHS_VideoInfoSource, VHS_VideoCombine, WanVideoSetLoRAs, Primitive integer [Crystools], GetNode, GetNode, GetNode, ImageConcatMulti, ImageConcatMulti, Primitive integer [Crystools], JjkText, JjkText, VHS_LoadVideo, SimpleMath+, SimpleMath+, SimpleMath+, SimpleMath+, ImageResizeKJv2, GetNode, WanVideoEncode, SetNode, GetImageSizeAndCount, RHHiddenNodes, RHHiddenNodes, RHHiddenNodes, RHHiddenNodes, RHHiddenNodes, RHHiddenNodes, RHHiddenNodes, RHHiddenNodes]
patterns: []
missing: []
---

# 视频生成/图生视频/原生系列 视频动作迁移 Animate 2.3 【动态运镜】_1979387280857141250.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1979387280857141250.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（84 个）：
- `ImpactSwitch`
- `Primitive integer [Crystools]`
- `SetNode`
- `SetNode`
- `ImageResizeKJv2`
- `SetNode`
- `Primitive integer [Crystools]`
- `WanVideoSetBlockSwap`
- `SetNode`
- `GetNode`
- `WanVideoVAELoader`
- `SetNode`
- `WanVideoAnimateEmbeds`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoClipVisionEncode`
- `CLIPVisionLoader`
- `GetNode`
- `DWPreprocessor`
- `SetNode`
- `PoseAndFaceDetection`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImpactSwitch`
- `Primitive integer [Crystools]`
- `WanVideoTextEncodeCached`
- `SetNode`
- `WanVideoDecode`
- `SetNode`
- `LoadImage`
- `WanVideoSampler` ★核心
- `GetImageSizeAndCount`
- `FaceMaskFromPoseKeypoints`
- `GetNode`
- `GetNode`
- `LoadImage`
- `GetNode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `Primitive integer [Crystools]`
- `VHS_LoadVideo`
- `GetNode`
- `SetNode`
- `easy showAnything`
- `easy showAnything`
- `easy showAnything`
- `easy showAnything`
- `easy showAnything`
- `SetNode`
- `SetNode`
- `SetNode`
- `VHS_VideoInfoSource`
- `VHS_VideoCombine`
- `WanVideoSetLoRAs`
- `Primitive integer [Crystools]`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `Primitive integer [Crystools]`
- `JjkText`
- `JjkText`
- `VHS_LoadVideo`
- `SimpleMath+`
- `SimpleMath+`
- `SimpleMath+`
- `SimpleMath+`
- `ImageResizeKJv2`
- `GetNode`
- `WanVideoEncode`
- `SetNode`
- `GetImageSizeAndCount`
- `RHHiddenNodes`
- `RHHiddenNodes`
- `RHHiddenNodes`
- `RHHiddenNodes`
- `RHHiddenNodes`
- `RHHiddenNodes`
- `RHHiddenNodes`
- `RHHiddenNodes`

## 知识

覆盖率 **54%**（45/84）

**有卡**：`Primitive integer [Crystools]`、`ImageResizeKJv2`、`WanVideoSetBlockSwap`、`WanVideoVAELoader`、`WanVideoAnimateEmbeds`、`WanVideoClipVisionEncode`、`CLIPVisionLoader`、`DWPreprocessor`、`PoseAndFaceDetection`、`WanVideoTextEncodeCached`、`WanVideoDecode`、`LoadImage`、`WanVideoSampler`、`GetImageSizeAndCount`、`FaceMaskFromPoseKeypoints`、`VHS_VideoCombine`、`VHS_LoadVideo`、`VHS_VideoInfoSource`、`WanVideoSetLoRAs`、`ImageConcatMulti`、`SimpleMath+`、`WanVideoEncode`、`RHHiddenNodes`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoEncode、WanVideoSetLoRAs
