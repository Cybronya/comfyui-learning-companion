---
key: 视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2069395904876081153.json
name: 动作迁移   动作模仿  角色替换  人物替换  wan2.2_2069395904876081153.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2069395904876081153.json
hash: 4af904bec19d342c
coverage: 0.974359
learned_at: 2026-10-15 22:40:28
nodes: [ImageConcatMulti, PoseAndFaceDetection, easy int, WanVideoVAELoader, LayerUtility: ImageMaskScaleAsV2, VHS_VideoCombine, LoadImage, VHS_VideoCombine, ClothesSegment, ImageFromBatch, SeCModelLoader, easy showAnything, VHS_LoadVideo, VHS_VideoInfoLoaded, LayerUtility: ImageScaleByAspectRatio V2, SeCVideoSegmentation, OnnxDetectionModelLoader, CLIPVisionLoader, DrawMaskOnImage, BlockifyMask, GrowMask, WanVideoClipVisionEncode, VHS_VideoCombine, Evaluate Integers, DrawViTPose, WanVideoAnimateEmbeds, WanVideoTorchCompileSettings, WanVideoContextOptions, ImageBlend, WanVideoModelLoader, WanVideoLoraSelectMulti, WanVideoSampler, WanVideoSetBlockSwap, WanVideoBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, ImageConcatMulti, WanVideoDecode, GetImageSizeAndCount]
patterns: []
missing: []
---

# 视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2069395904876081153.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2069395904876081153.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（39 个）：
- `ImageConcatMulti`
- `PoseAndFaceDetection`
- `easy int`
- `WanVideoVAELoader`
- `LayerUtility: ImageMaskScaleAsV2`
- `VHS_VideoCombine`
- `LoadImage`
- `VHS_VideoCombine`
- `ClothesSegment`
- `ImageFromBatch`
- `SeCModelLoader`
- `easy showAnything`
- `VHS_LoadVideo`
- `VHS_VideoInfoLoaded`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SeCVideoSegmentation`
- `OnnxDetectionModelLoader`
- `CLIPVisionLoader`
- `DrawMaskOnImage`
- `BlockifyMask`
- `GrowMask`
- `WanVideoClipVisionEncode`
- `VHS_VideoCombine`
- `Evaluate Integers`
- `DrawViTPose`
- `WanVideoAnimateEmbeds`
- `WanVideoTorchCompileSettings`
- `WanVideoContextOptions`
- `ImageBlend`
- `WanVideoModelLoader`
- `WanVideoLoraSelectMulti`
- `WanVideoSampler` ★核心
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `ImageConcatMulti`
- `WanVideoDecode`
- `GetImageSizeAndCount`

## 知识

覆盖率 **97%**（38/39）

**有卡**：`ImageConcatMulti`、`PoseAndFaceDetection`、`easy int`、`WanVideoVAELoader`、`LayerUtility: ImageMaskScaleAsV2`、`VHS_VideoCombine`、`LoadImage`、`ClothesSegment`、`ImageFromBatch`、`SeCModelLoader`、`VHS_LoadVideo`、`VHS_VideoInfoLoaded`、`LayerUtility: ImageScaleByAspectRatio V2`、`SeCVideoSegmentation`、`OnnxDetectionModelLoader`、`CLIPVisionLoader`、`DrawMaskOnImage`、`BlockifyMask`、`GrowMask`、`WanVideoClipVisionEncode`、`Evaluate Integers`、`DrawViTPose`、`WanVideoAnimateEmbeds`、`WanVideoTorchCompileSettings`、`WanVideoContextOptions`、`ImageBlend`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`WanVideoSampler`、`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`WanVideoSetLoRAs`、`WanVideoTextEncodeCached`、`WanVideoDecode`、`GetImageSizeAndCount`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
