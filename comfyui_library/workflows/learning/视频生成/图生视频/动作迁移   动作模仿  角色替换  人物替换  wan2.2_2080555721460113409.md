---
key: 视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2080555721460113409.json
name: 动作迁移   动作模仿  角色替换  人物替换  wan2.2_2080555721460113409.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2080555721460113409.json
hash: 16f0ffc461997d4c
coverage: 0.974359
learned_at: 2026-10-15 22:42:15
nodes: [WanVideoModelLoader, WanVideoTorchCompileSettings, WanVideoLoraSelectMulti, WanVideoSetBlockSwap, ImageConcatMulti, WanVideoDecode, WanVideoContextOptions, CLIPVisionLoader, PoseAndFaceDetection, VHS_VideoCombine, LayerUtility: ImageScaleByAspectRatio V2, WanVideoSampler, WanVideoAnimateEmbeds, Evaluate Integers, WanVideoClipVisionEncode, WanVideoSetLoRAs, DrawMaskOnImage, GetImageSizeAndCount, WanVideoBlockSwap, WanVideoTextEncodeCached, ImageBlend, DrawViTPose, ImageConcatMulti, VHS_VideoCombine, VHS_LoadVideo, LoadImage, VHS_VideoInfoLoaded, easy showAnything, LayerUtility: ImageMaskScaleAsV2, easy int, ImageFromBatch, SeCModelLoader, ClothesSegment, GrowMask, WanVideoVAELoader, OnnxDetectionModelLoader, BlockifyMask, SeCVideoSegmentation, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2080555721460113409.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2080555721460113409.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（39 个）：
- `WanVideoModelLoader`
- `WanVideoTorchCompileSettings`
- `WanVideoLoraSelectMulti`
- `WanVideoSetBlockSwap`
- `ImageConcatMulti`
- `WanVideoDecode`
- `WanVideoContextOptions`
- `CLIPVisionLoader`
- `PoseAndFaceDetection`
- `VHS_VideoCombine`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoSampler` ★核心
- `WanVideoAnimateEmbeds`
- `Evaluate Integers`
- `WanVideoClipVisionEncode`
- `WanVideoSetLoRAs`
- `DrawMaskOnImage`
- `GetImageSizeAndCount`
- `WanVideoBlockSwap`
- `WanVideoTextEncodeCached`
- `ImageBlend`
- `DrawViTPose`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `LoadImage`
- `VHS_VideoInfoLoaded`
- `easy showAnything`
- `LayerUtility: ImageMaskScaleAsV2`
- `easy int`
- `ImageFromBatch`
- `SeCModelLoader`
- `ClothesSegment`
- `GrowMask`
- `WanVideoVAELoader`
- `OnnxDetectionModelLoader`
- `BlockifyMask`
- `SeCVideoSegmentation`
- `VHS_VideoCombine`

## 知识

覆盖率 **97%**（38/39）

**有卡**：`WanVideoModelLoader`、`WanVideoTorchCompileSettings`、`WanVideoLoraSelectMulti`、`WanVideoSetBlockSwap`、`ImageConcatMulti`、`WanVideoDecode`、`WanVideoContextOptions`、`CLIPVisionLoader`、`PoseAndFaceDetection`、`VHS_VideoCombine`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoSampler`、`WanVideoAnimateEmbeds`、`Evaluate Integers`、`WanVideoClipVisionEncode`、`WanVideoSetLoRAs`、`DrawMaskOnImage`、`GetImageSizeAndCount`、`WanVideoBlockSwap`、`WanVideoTextEncodeCached`、`ImageBlend`、`DrawViTPose`、`VHS_LoadVideo`、`LoadImage`、`VHS_VideoInfoLoaded`、`LayerUtility: ImageMaskScaleAsV2`、`easy int`、`ImageFromBatch`、`SeCModelLoader`、`ClothesSegment`、`GrowMask`、`WanVideoVAELoader`、`OnnxDetectionModelLoader`、`BlockifyMask`、`SeCVideoSegmentation`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
