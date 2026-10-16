---
key: 视频生成/图生视频/动作模仿  角色替换  人物替换 动作迁移   wan2.2_2069298390604795905.json
name: 动作模仿  角色替换  人物替换 动作迁移   wan2.2_2069298390604795905.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2069298390604795905.json
hash: 7409c994cb2b250d
coverage: 0.974359
learned_at: 2026-10-15 22:40:27
nodes: [WanVideoTorchCompileSettings, VHS_VideoInfoLoaded, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageMaskScaleAsV2, easy int, SeCModelLoader, ImageFromBatch, ClothesSegment, SeCVideoSegmentation, CLIPVisionLoader, WanVideoVAELoader, OnnxDetectionModelLoader, GrowMask, WanVideoContextOptions, VHS_LoadVideo, LoadImage, easy showAnything, BlockifyMask, PoseAndFaceDetection, DrawMaskOnImage, WanVideoClipVisionEncode, VHS_VideoCombine, Evaluate Integers, DrawViTPose, WanVideoAnimateEmbeds, ImageBlend, ImageConcatMulti, WanVideoModelLoader, WanVideoLoraSelectMulti, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoBlockSwap, WanVideoTextEncodeCached, WanVideoSampler, WanVideoDecode, GetImageSizeAndCount, ImageConcatMulti, VHS_VideoCombine, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/动作模仿  角色替换  人物替换 动作迁移   wan2.2_2069298390604795905.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2069298390604795905.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（39 个）：
- `WanVideoTorchCompileSettings`
- `VHS_VideoInfoLoaded`
- `LayerUtility: ImageScaleByAspectRatio V2`
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
- `WanVideoContextOptions`
- `VHS_LoadVideo`
- `LoadImage`
- `easy showAnything`
- `BlockifyMask`
- `PoseAndFaceDetection`
- `DrawMaskOnImage`
- `WanVideoClipVisionEncode`
- `VHS_VideoCombine`
- `Evaluate Integers`
- `DrawViTPose`
- `WanVideoAnimateEmbeds`
- `ImageBlend`
- `ImageConcatMulti`
- `WanVideoModelLoader`
- `WanVideoLoraSelectMulti`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoTextEncodeCached`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `VHS_VideoCombine`

## 知识

覆盖率 **97%**（38/39）

**有卡**：`WanVideoTorchCompileSettings`、`VHS_VideoInfoLoaded`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageMaskScaleAsV2`、`easy int`、`SeCModelLoader`、`ImageFromBatch`、`ClothesSegment`、`SeCVideoSegmentation`、`CLIPVisionLoader`、`WanVideoVAELoader`、`OnnxDetectionModelLoader`、`GrowMask`、`WanVideoContextOptions`、`VHS_LoadVideo`、`LoadImage`、`BlockifyMask`、`PoseAndFaceDetection`、`DrawMaskOnImage`、`WanVideoClipVisionEncode`、`VHS_VideoCombine`、`Evaluate Integers`、`DrawViTPose`、`WanVideoAnimateEmbeds`、`ImageBlend`、`ImageConcatMulti`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`WanVideoTextEncodeCached`、`WanVideoSampler`、`WanVideoDecode`、`GetImageSizeAndCount`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
