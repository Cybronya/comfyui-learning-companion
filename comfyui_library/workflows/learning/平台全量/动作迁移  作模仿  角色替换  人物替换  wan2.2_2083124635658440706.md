---
key: 平台全量/动作迁移  作模仿  角色替换  人物替换  wan2.2_2083124635658440706.json
name: 动作迁移  作模仿  角色替换  人物替换  wan2.2_2083124635658440706
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/动作迁移  作模仿  角色替换  人物替换  wan2.2_2083124635658440706.json
hash: db74b6bafac56a13
coverage: 0.906977
learned_at: 2026-11-14 01:44:41
nodes: [WanVideoModelLoader, WanVideoTorchCompileSettings, WanVideoLoraSelectMulti, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoDecode, WanVideoContextOptions, CLIPVisionLoader, PoseAndFaceDetection, VHS_VideoCombine, OnnxDetectionModelLoader, GrowMask, BlockifyMask, easy int, ImageFromBatch, SeCVideoSegmentation, LayerUtility: ImageScaleByAspectRatio V2, WanVideoSampler, WanVideoVAELoader, ClothesSegment, SeCModelLoader, LayerUtility: ImageMaskScaleAsV2, WanVideoAnimateEmbeds, WanVideoClipVisionEncode, WanVideoSetLoRAs, WanVideoTextEncodeCached, DrawMaskOnImage, LoadImage, GetImageSizeAndCount, SetNode, SetNode, VHS_LoadVideo, ImageConcatMulti, ImageBlend, Evaluate Integers, DrawViTPose, VHS_VideoCombine, ImageConcatMulti, VHS_VideoCombine, GetNode, GetNode, VHS_VideoCombine, ImageConcatMulti]
patterns: []
missing: []
---

# 平台全量/动作迁移  作模仿  角色替换  人物替换  wan2.2_2083124635658440706.json

> 来源文件 `comfyui_library/workflows/平台全量/动作迁移  作模仿  角色替换  人物替换  wan2.2_2083124635658440706.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（43 个）：
- `WanVideoModelLoader`
- `WanVideoTorchCompileSettings`
- `WanVideoLoraSelectMulti`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoDecode`
- `WanVideoContextOptions`
- `CLIPVisionLoader`
- `PoseAndFaceDetection`
- `VHS_VideoCombine`
- `OnnxDetectionModelLoader`
- `GrowMask`
- `BlockifyMask`
- `easy int`
- `ImageFromBatch`
- `SeCVideoSegmentation`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoSampler` ★核心
- `WanVideoVAELoader`
- `ClothesSegment`
- `SeCModelLoader`
- `LayerUtility: ImageMaskScaleAsV2`
- `WanVideoAnimateEmbeds`
- `WanVideoClipVisionEncode`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `DrawMaskOnImage`
- `LoadImage`
- `GetImageSizeAndCount`
- `SetNode`
- `SetNode`
- `VHS_LoadVideo`
- `ImageConcatMulti`
- `ImageBlend`
- `Evaluate Integers`
- `DrawViTPose`
- `VHS_VideoCombine`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `ImageConcatMulti`

## 知识

覆盖率 **91%**（39/43）

**有卡**：`WanVideoModelLoader`、`WanVideoTorchCompileSettings`、`WanVideoLoraSelectMulti`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`WanVideoDecode`、`WanVideoContextOptions`、`CLIPVisionLoader`、`PoseAndFaceDetection`、`VHS_VideoCombine`、`OnnxDetectionModelLoader`、`GrowMask`、`BlockifyMask`、`easy int`、`ImageFromBatch`、`SeCVideoSegmentation`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoSampler`、`WanVideoVAELoader`、`ClothesSegment`、`SeCModelLoader`、`LayerUtility: ImageMaskScaleAsV2`、`WanVideoAnimateEmbeds`、`WanVideoClipVisionEncode`、`WanVideoSetLoRAs`、`WanVideoTextEncodeCached`、`DrawMaskOnImage`、`LoadImage`、`GetImageSizeAndCount`、`VHS_LoadVideo`、`ImageConcatMulti`、`ImageBlend`、`Evaluate Integers`、`DrawViTPose`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoLoraSelectMulti、WanVideoSetLoRAs
