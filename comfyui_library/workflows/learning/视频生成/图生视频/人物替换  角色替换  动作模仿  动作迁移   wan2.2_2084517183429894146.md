---
key: 视频生成/图生视频/人物替换  角色替换  动作模仿  动作迁移   wan2.2_2084517183429894146.json
name: 人物替换  角色替换  动作模仿  动作迁移   wan2.2_2084517183429894146
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/人物替换  角色替换  动作模仿  动作迁移   wan2.2_2084517183429894146.json
hash: 7ba1b3d44f313b31
coverage: 0.95122
learned_at: 2026-10-16 20:35:48
nodes: [WanVideoModelLoader, WanVideoTorchCompileSettings, WanVideoSetBlockSwap, WanVideoDecode, LayerUtility: ImageScaleByAspectRatio V2, WanVideoSampler, WanVideoVAELoader, WanVideoAnimateEmbeds, WanVideoSetLoRAs, WanVideoBlockSwap, WanVideoTextEncodeCached, VHS_VideoCombine, ImageConcatMulti, ImageConcatMulti, GetImageSizeAndCount, VHS_VideoCombine, VHS_VideoCombine, LayerUtility: ImageMaskScaleAsV2, easy int, SeCModelLoader, ImageFromBatch, ClothesSegment, SetNode, GetNode, ImageConcatMulti, GrowMask, CLIPVisionLoader, OnnxDetectionModelLoader, PoseAndFaceDetection, BlockifyMask, DrawMaskOnImage, WanVideoClipVisionEncode, DrawViTPose, Evaluate Integers, WanVideoContextOptions, ImageBlend, WanVideoLoraSelectMulti, SeCVideoSegmentation, VHS_VideoCombine, VHS_LoadVideo, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/人物替换  角色替换  动作模仿  动作迁移   wan2.2_2084517183429894146.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/人物替换  角色替换  动作模仿  动作迁移   wan2.2_2084517183429894146.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（41 个）：
- `WanVideoModelLoader`
- `WanVideoTorchCompileSettings`
- `WanVideoSetBlockSwap`
- `WanVideoDecode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoSampler` ★核心
- `WanVideoVAELoader`
- `WanVideoAnimateEmbeds`
- `WanVideoSetLoRAs`
- `WanVideoBlockSwap`
- `WanVideoTextEncodeCached`
- `VHS_VideoCombine`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `LayerUtility: ImageMaskScaleAsV2`
- `easy int`
- `SeCModelLoader`
- `ImageFromBatch`
- `ClothesSegment`
- `SetNode`
- `GetNode`
- `ImageConcatMulti`
- `GrowMask`
- `CLIPVisionLoader`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `BlockifyMask`
- `DrawMaskOnImage`
- `WanVideoClipVisionEncode`
- `DrawViTPose`
- `Evaluate Integers`
- `WanVideoContextOptions`
- `ImageBlend`
- `WanVideoLoraSelectMulti`
- `SeCVideoSegmentation`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `LoadImage`

## 知识

覆盖率 **95%**（39/41）

**有卡**：`WanVideoModelLoader`、`WanVideoTorchCompileSettings`、`WanVideoSetBlockSwap`、`WanVideoDecode`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoSampler`、`WanVideoVAELoader`、`WanVideoAnimateEmbeds`、`WanVideoSetLoRAs`、`WanVideoBlockSwap`、`WanVideoTextEncodeCached`、`VHS_VideoCombine`、`ImageConcatMulti`、`GetImageSizeAndCount`、`LayerUtility: ImageMaskScaleAsV2`、`easy int`、`SeCModelLoader`、`ImageFromBatch`、`ClothesSegment`、`GrowMask`、`CLIPVisionLoader`、`OnnxDetectionModelLoader`、`PoseAndFaceDetection`、`BlockifyMask`、`DrawMaskOnImage`、`WanVideoClipVisionEncode`、`DrawViTPose`、`Evaluate Integers`、`WanVideoContextOptions`、`ImageBlend`、`WanVideoLoraSelectMulti`、`SeCVideoSegmentation`、`VHS_LoadVideo`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
