---
key: 视频生成/图生视频/wan2.2  动作迁移   动作模仿  角色替换  人物替换_2083060698434850817.json
name: wan2.2  动作迁移   动作模仿  角色替换  人物替换_2083060698434850817
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.2  动作迁移   动作模仿  角色替换  人物替换_2083060698434850817.json
hash: 74e55f273d929a30
coverage: 1
learned_at: 2026-10-16 01:17:13
nodes: [WanVideoModelLoader, WanVideoTorchCompileSettings, WanVideoLoraSelectMulti, WanVideoSetBlockSwap, WanVideoDecode, WanVideoContextOptions, CLIPVisionLoader, PoseAndFaceDetection, VHS_VideoCombine, OnnxDetectionModelLoader, GrowMask, BlockifyMask, VHS_VideoInfoLoaded, easy int, SeCVideoSegmentation, LayerUtility: ImageScaleByAspectRatio V2, WanVideoSampler, WanVideoVAELoader, LayerUtility: ImageMaskScaleAsV2, WanVideoAnimateEmbeds, Evaluate Integers, WanVideoClipVisionEncode, WanVideoSetLoRAs, DrawMaskOnImage, WanVideoBlockSwap, WanVideoTextEncodeCached, ImageBlend, DrawViTPose, ImageConcatMulti, ClothesSegment, ImageFromBatch, SeCModelLoader, LoadImage, VHS_VideoCombine, VHS_VideoCombine, GetImageSizeAndCount, ImageConcatMulti, VHS_VideoCombine, VHS_LoadVideo, ImageConcatMulti]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.2  动作迁移   动作模仿  角色替换  人物替换_2083060698434850817.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/wan2.2  动作迁移   动作模仿  角色替换  人物替换_2083060698434850817.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（40 个）：
- `WanVideoModelLoader`
- `WanVideoTorchCompileSettings`
- `WanVideoLoraSelectMulti`
- `WanVideoSetBlockSwap`
- `WanVideoDecode`
- `WanVideoContextOptions`
- `CLIPVisionLoader`
- `PoseAndFaceDetection`
- `VHS_VideoCombine`
- `OnnxDetectionModelLoader`
- `GrowMask`
- `BlockifyMask`
- `VHS_VideoInfoLoaded`
- `easy int`
- `SeCVideoSegmentation`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoSampler` ★核心
- `WanVideoVAELoader`
- `LayerUtility: ImageMaskScaleAsV2`
- `WanVideoAnimateEmbeds`
- `Evaluate Integers`
- `WanVideoClipVisionEncode`
- `WanVideoSetLoRAs`
- `DrawMaskOnImage`
- `WanVideoBlockSwap`
- `WanVideoTextEncodeCached`
- `ImageBlend`
- `DrawViTPose`
- `ImageConcatMulti`
- `ClothesSegment`
- `ImageFromBatch`
- `SeCModelLoader`
- `LoadImage`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `GetImageSizeAndCount`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `ImageConcatMulti`

## 知识

覆盖率 **100%**（40/40）

**有卡**：`WanVideoModelLoader`、`WanVideoTorchCompileSettings`、`WanVideoLoraSelectMulti`、`WanVideoSetBlockSwap`、`WanVideoDecode`、`WanVideoContextOptions`、`CLIPVisionLoader`、`PoseAndFaceDetection`、`VHS_VideoCombine`、`OnnxDetectionModelLoader`、`GrowMask`、`BlockifyMask`、`VHS_VideoInfoLoaded`、`easy int`、`SeCVideoSegmentation`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoSampler`、`WanVideoVAELoader`、`LayerUtility: ImageMaskScaleAsV2`、`WanVideoAnimateEmbeds`、`Evaluate Integers`、`WanVideoClipVisionEncode`、`WanVideoSetLoRAs`、`DrawMaskOnImage`、`WanVideoBlockSwap`、`WanVideoTextEncodeCached`、`ImageBlend`、`DrawViTPose`、`ImageConcatMulti`、`ClothesSegment`、`ImageFromBatch`、`SeCModelLoader`、`LoadImage`、`GetImageSizeAndCount`、`VHS_LoadVideo`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
