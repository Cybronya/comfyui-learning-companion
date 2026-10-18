---
key: 视频生成/图生视频/动作模仿  角色替换  人物替换 动作迁移   wan2.2_2068791565585313794.json
name: 动作模仿  角色替换  人物替换 动作迁移   wan2.2_2068791565585313794.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/动作模仿  角色替换  人物替换 动作迁移   wan2.2_2068791565585313794.json
hash: 866c680e9bf02cdc
coverage: 0.974359
learned_at: 2026-10-15 22:40:21
nodes: [WanVideoModelLoader, GetImageSizeAndCount, WanVideoTorchCompileSettings, WanVideoLoraSelectMulti, WanVideoBlockSwap, WanVideoSetBlockSwap, ImageConcatMulti, VHS_VideoCombine, WanVideoDecode, PoseAndFaceDetection, VHS_VideoCombine, VHS_VideoInfoLoaded, easy showAnything, LayerUtility: ImageScaleByAspectRatio V2, WanVideoSampler, WanVideoAnimateEmbeds, WanVideoClipVisionEncode, WanVideoSetLoRAs, WanVideoTextEncodeCached, LayerUtility: ImageMaskScaleAsV2, easy int, SeCModelLoader, ImageFromBatch, ClothesSegment, SeCVideoSegmentation, CLIPVisionLoader, WanVideoVAELoader, OnnxDetectionModelLoader, GrowMask, BlockifyMask, DrawMaskOnImage, ImageConcatMulti, WanVideoContextOptions, ImageBlend, Evaluate Integers, DrawViTPose, VHS_VideoCombine, VHS_LoadVideo, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/动作模仿  角色替换  人物替换 动作迁移   wan2.2_2068791565585313794.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2068791565585313794.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（39 个）：
- `WanVideoModelLoader`
- `GetImageSizeAndCount`
- `WanVideoTorchCompileSettings`
- `WanVideoLoraSelectMulti`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `PoseAndFaceDetection`
- `VHS_VideoCombine`
- `VHS_VideoInfoLoaded`
- `easy showAnything`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoSampler` ★核心
- `WanVideoAnimateEmbeds`
- `WanVideoClipVisionEncode`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `LayerUtility: ImageMaskScaleAsV2`
- `easy int`
- `SeCModelLoader`
- `ImageFromBatch`
- `ClothesSegment`
- `SeCVideoSegmentation`
- `CLIPVisionLoader`
- `WanVideoVAELoader`
- `OnnxDetectionModelLoader`
- `GrowMask`
- `BlockifyMask`
- `DrawMaskOnImage`
- `ImageConcatMulti`
- `WanVideoContextOptions`
- `ImageBlend`
- `Evaluate Integers`
- `DrawViTPose`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `LoadImage`

## 知识

覆盖率 **97%**（38/39）

**有卡**：`WanVideoModelLoader`、`GetImageSizeAndCount`、`WanVideoTorchCompileSettings`、`WanVideoLoraSelectMulti`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`ImageConcatMulti`、`VHS_VideoCombine`、`WanVideoDecode`、`PoseAndFaceDetection`、`VHS_VideoInfoLoaded`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoSampler`、`WanVideoAnimateEmbeds`、`WanVideoClipVisionEncode`、`WanVideoSetLoRAs`、`WanVideoTextEncodeCached`、`LayerUtility: ImageMaskScaleAsV2`、`easy int`、`SeCModelLoader`、`ImageFromBatch`、`ClothesSegment`、`SeCVideoSegmentation`、`CLIPVisionLoader`、`WanVideoVAELoader`、`OnnxDetectionModelLoader`、`GrowMask`、`BlockifyMask`、`DrawMaskOnImage`、`WanVideoContextOptions`、`ImageBlend`、`Evaluate Integers`、`DrawViTPose`、`VHS_LoadVideo`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
