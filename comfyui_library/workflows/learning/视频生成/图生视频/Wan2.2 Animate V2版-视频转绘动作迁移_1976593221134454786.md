---
key: 视频生成/图生视频/Wan2.2 Animate V2版-视频转绘动作迁移_1976593221134454786.json
name: Wan2.2 Animate V2版-视频转绘动作迁移_1976593221134454786.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1976593221134454786.json
hash: 33d9851296c6dd8a
coverage: 0.565217
learned_at: 2026-10-15 22:32:11
nodes: [OnnxDetectionModelLoader, GetNode, GetNode, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoModelLoader, WanVideoAnimateEmbeds, CLIPVisionLoader, PreviewImage, SetNode, ImageResize+, DrawViTPose, SetNode, VHS_VideoCombine, PoseAndFaceDetection, SetNode, WanVideoClipVisionEncode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, VHS_VideoCombine, WanVideoVAELoader, Reroute, WanVideoSampler, WanVideoDecode, LayerUtility: ImageScaleByAspectRatio V2, SetNode, SetNode, SetNode, easy showAnything, WanVideoTextEncodeCached, LoadImage, Reroute, LoadImage, WanVideoLoraSelectMulti, VHS_LoadVideo, ImageFromBatch, SaveImage, RH_Nano_Banana_Image2Image, PreviewImage, VHS_VideoCombine, MarkdownNote]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2 Animate V2版-视频转绘动作迁移_1976593221134454786.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1976593221134454786.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（46 个）：
- `OnnxDetectionModelLoader`
- `GetNode`
- `GetNode`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoModelLoader`
- `WanVideoAnimateEmbeds`
- `CLIPVisionLoader`
- `PreviewImage`
- `SetNode`
- `ImageResize+`
- `DrawViTPose`
- `SetNode`
- `VHS_VideoCombine`
- `PoseAndFaceDetection`
- `SetNode`
- `WanVideoClipVisionEncode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `WanVideoVAELoader`
- `Reroute`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `SetNode`
- `SetNode`
- `easy showAnything`
- `WanVideoTextEncodeCached`
- `LoadImage`
- `Reroute`
- `LoadImage`
- `WanVideoLoraSelectMulti`
- `VHS_LoadVideo`
- `ImageFromBatch`
- `SaveImage`
- `RH_Nano_Banana_Image2Image`
- `PreviewImage`
- `VHS_VideoCombine`
- `MarkdownNote`

## 知识

覆盖率 **57%**（26/46）

**有卡**：`OnnxDetectionModelLoader`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoModelLoader`、`WanVideoAnimateEmbeds`、`CLIPVisionLoader`、`ImageResize+`、`DrawViTPose`、`VHS_VideoCombine`、`PoseAndFaceDetection`、`WanVideoClipVisionEncode`、`WanVideoVAELoader`、`WanVideoSampler`、`WanVideoDecode`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoTextEncodeCached`、`LoadImage`、`WanVideoLoraSelectMulti`、`VHS_LoadVideo`、`ImageFromBatch`、`SaveImage`、`RH_Nano_Banana_Image2Image`

**用到的条目**：LoadImage、LayerUtility: ImageScaleByAspectRatio V2、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs
