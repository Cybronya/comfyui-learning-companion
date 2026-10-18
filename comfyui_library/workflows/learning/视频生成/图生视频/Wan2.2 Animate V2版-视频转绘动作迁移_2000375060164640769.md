---
key: 视频生成/图生视频/Wan2.2 Animate V2版-视频转绘动作迁移_2000375060164640769.json
name: Wan2.2 Animate V2版-视频转绘动作迁移_2000375060164640769.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2 Animate V2版-视频转绘动作迁移_2000375060164640769.json
hash: ae5a6b2cde0f6aaf
coverage: 0.577778
learned_at: 2026-10-15 22:33:40
nodes: [WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoModelLoader, WanVideoAnimateEmbeds, PreviewImage, SetNode, ImageResize+, GetNode, GetNode, GetNode, GetNode, WanVideoSampler, WanVideoDecode, LoadImage, Reroute, LoadImage, WanVideoLoraSelectMulti, LayerUtility: ImageScaleByAspectRatio V2, ImageFromBatch, SetNode, easy showAnything, SetNode, SetNode, OnnxDetectionModelLoader, GetNode, GetNode, PoseAndFaceDetection, VHS_VideoCombine, SetNode, SetNode, DrawViTPose, VHS_VideoCombine, CLIPVisionLoader, GetNode, WanVideoVAELoader, WanVideoClipVisionEncode, GetNode, WanVideoTextEncodeCached, VHS_LoadVideo, PreviewImage, SaveImage, RH_Nano_Banana_Image2Image, VHS_VideoCombine, Reroute]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2 Animate V2版-视频转绘动作迁移_2000375060164640769.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2000375060164640769.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（45 个）：
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoModelLoader`
- `WanVideoAnimateEmbeds`
- `PreviewImage`
- `SetNode`
- `ImageResize+`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `LoadImage`
- `Reroute`
- `LoadImage`
- `WanVideoLoraSelectMulti`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageFromBatch`
- `SetNode`
- `easy showAnything`
- `SetNode`
- `SetNode`
- `OnnxDetectionModelLoader`
- `GetNode`
- `GetNode`
- `PoseAndFaceDetection`
- `VHS_VideoCombine`
- `SetNode`
- `SetNode`
- `DrawViTPose`
- `VHS_VideoCombine`
- `CLIPVisionLoader`
- `GetNode`
- `WanVideoVAELoader`
- `WanVideoClipVisionEncode`
- `GetNode`
- `WanVideoTextEncodeCached`
- `VHS_LoadVideo`
- `PreviewImage`
- `SaveImage`
- `RH_Nano_Banana_Image2Image`
- `VHS_VideoCombine`
- `Reroute`

## 知识

覆盖率 **58%**（26/45）

**有卡**：`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoModelLoader`、`WanVideoAnimateEmbeds`、`ImageResize+`、`WanVideoSampler`、`WanVideoDecode`、`LoadImage`、`WanVideoLoraSelectMulti`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageFromBatch`、`OnnxDetectionModelLoader`、`PoseAndFaceDetection`、`VHS_VideoCombine`、`DrawViTPose`、`CLIPVisionLoader`、`WanVideoVAELoader`、`WanVideoClipVisionEncode`、`WanVideoTextEncodeCached`、`VHS_LoadVideo`、`SaveImage`、`RH_Nano_Banana_Image2Image`

**用到的条目**：LoadImage、LayerUtility: ImageScaleByAspectRatio V2、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs
