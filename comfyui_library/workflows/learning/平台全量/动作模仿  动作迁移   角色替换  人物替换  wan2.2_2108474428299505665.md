---
key: 平台全量/动作模仿  动作迁移   角色替换  人物替换  wan2.2_2108474428299505665.json
name: 动作模仿  动作迁移   角色替换  人物替换  wan2.2_2108474428299505665
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/动作模仿  动作迁移   角色替换  人物替换  wan2.2_2108474428299505665.json
hash: fafca4f62bbf819e
coverage: 0.972973
learned_at: 2026-11-14 01:44:17
nodes: [WanVideoModelLoader, WanVideoTorchCompileSettings, WanVideoLoraSelectMulti, WanVideoSetBlockSwap, WanVideoDecode, WanVideoContextOptions, VHS_VideoCombine, VHS_VideoInfoLoaded, easy int, SeCVideoSegmentation, LayerUtility: ImageScaleByAspectRatio V2, WanVideoSampler, LayerUtility: ImageMaskScaleAsV2, WanVideoAnimateEmbeds, WanVideoClipVisionEncode, WanVideoSetLoRAs, WanVideoBlockSwap, WanVideoTextEncodeCached, DrawViTPose, ImageFromBatch, SeCModelLoader, easy showAnything, VHS_VideoCombine, LoadImage, GetImageSizeAndCount, VHS_LoadVideo, ClothesSegment, WanVideoVAELoader, CLIPVisionLoader, OnnxDetectionModelLoader, PoseAndFaceDetection, DrawMaskOnImage, GrowMask, BlockifyMask, Evaluate Integers, ImageConcatMulti, VHS_VideoCombine]
patterns: []
missing: []
---

# 平台全量/动作模仿  动作迁移   角色替换  人物替换  wan2.2_2108474428299505665.json

> 来源文件 `comfyui_library/workflows/平台全量/动作模仿  动作迁移   角色替换  人物替换  wan2.2_2108474428299505665.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（37 个）：
- `WanVideoModelLoader`
- `WanVideoTorchCompileSettings`
- `WanVideoLoraSelectMulti`
- `WanVideoSetBlockSwap`
- `WanVideoDecode`
- `WanVideoContextOptions`
- `VHS_VideoCombine`
- `VHS_VideoInfoLoaded`
- `easy int`
- `SeCVideoSegmentation`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoSampler` ★核心
- `LayerUtility: ImageMaskScaleAsV2`
- `WanVideoAnimateEmbeds`
- `WanVideoClipVisionEncode`
- `WanVideoSetLoRAs`
- `WanVideoBlockSwap`
- `WanVideoTextEncodeCached`
- `DrawViTPose`
- `ImageFromBatch`
- `SeCModelLoader`
- `easy showAnything`
- `VHS_VideoCombine`
- `LoadImage`
- `GetImageSizeAndCount`
- `VHS_LoadVideo`
- `ClothesSegment`
- `WanVideoVAELoader`
- `CLIPVisionLoader`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `DrawMaskOnImage`
- `GrowMask`
- `BlockifyMask`
- `Evaluate Integers`
- `ImageConcatMulti`
- `VHS_VideoCombine`

## 知识

覆盖率 **97%**（36/37）

**有卡**：`WanVideoModelLoader`、`WanVideoTorchCompileSettings`、`WanVideoLoraSelectMulti`、`WanVideoSetBlockSwap`、`WanVideoDecode`、`WanVideoContextOptions`、`VHS_VideoCombine`、`VHS_VideoInfoLoaded`、`easy int`、`SeCVideoSegmentation`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoSampler`、`LayerUtility: ImageMaskScaleAsV2`、`WanVideoAnimateEmbeds`、`WanVideoClipVisionEncode`、`WanVideoSetLoRAs`、`WanVideoBlockSwap`、`WanVideoTextEncodeCached`、`DrawViTPose`、`ImageFromBatch`、`SeCModelLoader`、`LoadImage`、`GetImageSizeAndCount`、`VHS_LoadVideo`、`ClothesSegment`、`WanVideoVAELoader`、`CLIPVisionLoader`、`OnnxDetectionModelLoader`、`PoseAndFaceDetection`、`DrawMaskOnImage`、`GrowMask`、`BlockifyMask`、`Evaluate Integers`、`ImageConcatMulti`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoLoraSelectMulti、WanVideoSetLoRAs
