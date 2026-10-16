---
key: 视频生成/图生视频/动作迁移   角色替换  人物替换  动作模仿 wan2.2_2082913589769363457.json
name: 动作迁移   角色替换  人物替换  动作模仿 wan2.2_2082913589769363457
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/动作迁移   角色替换  人物替换  动作模仿 wan2.2_2082913589769363457.json
hash: 928c6090d49a3db2
coverage: 1
learned_at: 2026-10-16 01:17:14
nodes: [WanVideoModelLoader, WanVideoTorchCompileSettings, WanVideoLoraSelectMulti, WanVideoSetBlockSwap, ImageConcatMulti, WanVideoDecode, WanVideoContextOptions, VHS_VideoCombine, LayerUtility: ImageScaleByAspectRatio V2, WanVideoSampler, WanVideoAnimateEmbeds, Evaluate Integers, WanVideoClipVisionEncode, WanVideoSetLoRAs, GetImageSizeAndCount, WanVideoBlockSwap, WanVideoTextEncodeCached, VHS_VideoCombine, ImageBlend, DrawViTPose, ImageConcatMulti, VHS_VideoCombine, VHS_LoadVideo, LayerUtility: ImageMaskScaleAsV2, SeCModelLoader, ClothesSegment, SeCVideoSegmentation, GrowMask, BlockifyMask, DrawMaskOnImage, OnnxDetectionModelLoader, WanVideoVAELoader, PoseAndFaceDetection, CLIPVisionLoader, ImageFromBatch, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/动作迁移   角色替换  人物替换  动作模仿 wan2.2_2082913589769363457.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/动作迁移   角色替换  人物替换  动作模仿 wan2.2_2082913589769363457.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（36 个）：
- `WanVideoModelLoader`
- `WanVideoTorchCompileSettings`
- `WanVideoLoraSelectMulti`
- `WanVideoSetBlockSwap`
- `ImageConcatMulti`
- `WanVideoDecode`
- `WanVideoContextOptions`
- `VHS_VideoCombine`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoSampler` ★核心
- `WanVideoAnimateEmbeds`
- `Evaluate Integers`
- `WanVideoClipVisionEncode`
- `WanVideoSetLoRAs`
- `GetImageSizeAndCount`
- `WanVideoBlockSwap`
- `WanVideoTextEncodeCached`
- `VHS_VideoCombine`
- `ImageBlend`
- `DrawViTPose`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `LayerUtility: ImageMaskScaleAsV2`
- `SeCModelLoader`
- `ClothesSegment`
- `SeCVideoSegmentation`
- `GrowMask`
- `BlockifyMask`
- `DrawMaskOnImage`
- `OnnxDetectionModelLoader`
- `WanVideoVAELoader`
- `PoseAndFaceDetection`
- `CLIPVisionLoader`
- `ImageFromBatch`
- `LoadImage`

## 知识

覆盖率 **100%**（36/36）

**有卡**：`WanVideoModelLoader`、`WanVideoTorchCompileSettings`、`WanVideoLoraSelectMulti`、`WanVideoSetBlockSwap`、`ImageConcatMulti`、`WanVideoDecode`、`WanVideoContextOptions`、`VHS_VideoCombine`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoSampler`、`WanVideoAnimateEmbeds`、`Evaluate Integers`、`WanVideoClipVisionEncode`、`WanVideoSetLoRAs`、`GetImageSizeAndCount`、`WanVideoBlockSwap`、`WanVideoTextEncodeCached`、`ImageBlend`、`DrawViTPose`、`VHS_LoadVideo`、`LayerUtility: ImageMaskScaleAsV2`、`SeCModelLoader`、`ClothesSegment`、`SeCVideoSegmentation`、`GrowMask`、`BlockifyMask`、`DrawMaskOnImage`、`OnnxDetectionModelLoader`、`WanVideoVAELoader`、`PoseAndFaceDetection`、`CLIPVisionLoader`、`ImageFromBatch`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
