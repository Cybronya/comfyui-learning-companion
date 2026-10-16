---
key: 视频生成/图生视频/wan2.2 animate 跳舞单人转绘-不带蒙版_1998969662585065474.json
name: wan2.2 animate 跳舞单人转绘-不带蒙版_1998969662585065474.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1998969662585065474.json
hash: 675fa772bba89108
coverage: 0.547619
learned_at: 2026-10-15 22:33:34
nodes: [GetNode, FaceMaskFromPoseKeypoints, ImageCropByMaskAndResize, SetNode, SetNode, GetNode, GetImageSizeAndCount, PixelPerfectResolution, DWPreprocessor, VHS_VideoCombine, VHS_VideoCombine, ImageResizeKJv2, GetNode, Reroute, SetNode, WanVideoSampler, WanVideoDecode, SetNode, JjkText, WanVideoTextEncodeCached, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, WanVideoAnimateEmbeds, LoadImage, ImpactInt, ImpactInt, WanVideoClipVisionEncode, WanVideoContextOptions, GetNode, SetNode, SetNode, CM_IntToFloat, PrimitiveFloat, ImpactInt, RHHiddenNodes, ImpactInt, VHS_LoadVideo, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.2 animate 跳舞单人转绘-不带蒙版_1998969662585065474.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1998969662585065474.json`

## 结构

**生成流程**：Sampling → Process → Other

**节点**（42 个）：
- `GetNode`
- `FaceMaskFromPoseKeypoints`
- `ImageCropByMaskAndResize`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetImageSizeAndCount`
- `PixelPerfectResolution`
- `DWPreprocessor`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `ImageResizeKJv2`
- `GetNode`
- `Reroute`
- `SetNode`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `SetNode`
- `JjkText`
- `WanVideoTextEncodeCached`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoAnimateEmbeds`
- `LoadImage`
- `ImpactInt`
- `ImpactInt`
- `WanVideoClipVisionEncode`
- `WanVideoContextOptions`
- `GetNode`
- `SetNode`
- `SetNode`
- `CM_IntToFloat`
- `PrimitiveFloat`
- `ImpactInt`
- `RHHiddenNodes`
- `ImpactInt`
- `VHS_LoadVideo`
- `VHS_VideoCombine`

## 知识

覆盖率 **55%**（23/42）

**有卡**：`FaceMaskFromPoseKeypoints`、`ImageCropByMaskAndResize`、`GetImageSizeAndCount`、`PixelPerfectResolution`、`DWPreprocessor`、`VHS_VideoCombine`、`ImageResizeKJv2`、`WanVideoSampler`、`WanVideoDecode`、`WanVideoTextEncodeCached`、`WanVideoAnimateEmbeds`、`LoadImage`、`ImpactInt`、`WanVideoClipVisionEncode`、`WanVideoContextOptions`、`CM_IntToFloat`、`RHHiddenNodes`、`VHS_LoadVideo`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoClipVisionEncode、WanVideoTextEncodeCached、GetImageSizeAndCount、ImageResizeKJv2、PixelPerfectResolution
