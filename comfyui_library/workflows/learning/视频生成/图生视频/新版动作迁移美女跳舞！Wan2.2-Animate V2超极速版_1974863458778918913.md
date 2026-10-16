---
key: 视频生成/图生视频/新版动作迁移美女跳舞！Wan2.2-Animate V2超极速版_1974863458778918913.json
name: 新版动作迁移美女跳舞！Wan2.2-Animate V2超极速版_1974863458778918913.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1974863458778918913.json
hash: ceac9325ff67d0ce
coverage: 0.828571
learned_at: 2026-10-15 22:32:06
nodes: [WanVideoDecode, WanVideoSetBlockSwap, WanVideoSetLoRAs, ImageResizeKJv2, CLIPVisionLoader, WanVideoVAELoader, ImageCropByMaskAndResize, CLIPVisionLoader, Note, SimpleMath+, LoadImage, WanVideoBlockSwap, Note, DWPreprocessor, JWInteger, JWInteger, PrimitiveStringMultiline, VHS_LoadVideo, WanVideoClipVisionEncode, WanVideoClipVisionEncode, WanVideoAnimateEmbeds, WanVideoSampler, easy cleanGpuUsed, MarkdownNote, LoadImage, PixelPerfectResolution, FaceMaskFromPoseKeypoints, WanVideoModelLoader, RHHiddenNodes, WanVideoTextEncodeCached, SetNode, VHS_VideoInfo, GetNode, VHS_VideoCombine, ImpactInt]
patterns: []
missing: []
---

# 视频生成/图生视频/新版动作迁移美女跳舞！Wan2.2-Animate V2超极速版_1974863458778918913.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1974863458778918913.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（35 个）：
- `WanVideoDecode`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `ImageResizeKJv2`
- `CLIPVisionLoader`
- `WanVideoVAELoader`
- `ImageCropByMaskAndResize`
- `CLIPVisionLoader`
- `Note`
- `SimpleMath+`
- `LoadImage`
- `WanVideoBlockSwap`
- `Note`
- `DWPreprocessor`
- `JWInteger`
- `JWInteger`
- `PrimitiveStringMultiline`
- `VHS_LoadVideo`
- `WanVideoClipVisionEncode`
- `WanVideoClipVisionEncode`
- `WanVideoAnimateEmbeds`
- `WanVideoSampler` ★核心
- `easy cleanGpuUsed`
- `MarkdownNote`
- `LoadImage`
- `PixelPerfectResolution`
- `FaceMaskFromPoseKeypoints`
- `WanVideoModelLoader`
- `RHHiddenNodes`
- `WanVideoTextEncodeCached`
- `SetNode`
- `VHS_VideoInfo`
- `GetNode`
- `VHS_VideoCombine`
- `ImpactInt`

## 知识

覆盖率 **83%**（29/35）

**有卡**：`WanVideoDecode`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`ImageResizeKJv2`、`CLIPVisionLoader`、`WanVideoVAELoader`、`ImageCropByMaskAndResize`、`SimpleMath+`、`LoadImage`、`WanVideoBlockSwap`、`DWPreprocessor`、`JWInteger`、`VHS_LoadVideo`、`WanVideoClipVisionEncode`、`WanVideoAnimateEmbeds`、`WanVideoSampler`、`easy cleanGpuUsed`、`PixelPerfectResolution`、`FaceMaskFromPoseKeypoints`、`WanVideoModelLoader`、`RHHiddenNodes`、`WanVideoTextEncodeCached`、`VHS_VideoInfo`、`VHS_VideoCombine`、`ImpactInt`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、CLIPVisionLoader
