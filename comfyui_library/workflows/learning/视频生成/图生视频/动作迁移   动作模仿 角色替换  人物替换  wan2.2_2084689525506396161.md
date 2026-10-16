---
key: 视频生成/图生视频/动作迁移   动作模仿 角色替换  人物替换  wan2.2_2084689525506396161.json
name: 动作迁移   动作模仿 角色替换  人物替换  wan2.2_2084689525506396161
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/动作迁移   动作模仿 角色替换  人物替换  wan2.2_2084689525506396161.json
hash: 9037213490fcaf39
coverage: 1
learned_at: 2026-10-16 20:35:50
nodes: [WanVideoModelLoader, WanVideoTorchCompileSettings, WanVideoLoraSelectMulti, WanVideoSetBlockSwap, ImageConcatMulti, WanVideoDecode, WanVideoContextOptions, CLIPVisionLoader, LayerUtility: ImageScaleByAspectRatio V2, WanVideoSampler, WanVideoAnimateEmbeds, Evaluate Integers, WanVideoClipVisionEncode, WanVideoSetLoRAs, GetImageSizeAndCount, WanVideoBlockSwap, WanVideoTextEncodeCached, VHS_VideoCombine, ImageBlend, DrawViTPose, ImageConcatMulti, VHS_VideoCombine, LayerUtility: ImageMaskScaleAsV2, SeCModelLoader, ImageFromBatch, WanVideoVAELoader, OnnxDetectionModelLoader, PoseAndFaceDetection, GrowMask, BlockifyMask, DrawMaskOnImage, VHS_VideoCombine, ClothesSegment, SeCVideoSegmentation, VHS_LoadVideo, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/动作迁移   动作模仿 角色替换  人物替换  wan2.2_2084689525506396161.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/动作迁移   动作模仿 角色替换  人物替换  wan2.2_2084689525506396161.json`

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
- `CLIPVisionLoader`
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
- `LayerUtility: ImageMaskScaleAsV2`
- `SeCModelLoader`
- `ImageFromBatch`
- `WanVideoVAELoader`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `GrowMask`
- `BlockifyMask`
- `DrawMaskOnImage`
- `VHS_VideoCombine`
- `ClothesSegment`
- `SeCVideoSegmentation`
- `VHS_LoadVideo`
- `LoadImage`

## 知识

覆盖率 **100%**（36/36）

**有卡**：`WanVideoModelLoader`、`WanVideoTorchCompileSettings`、`WanVideoLoraSelectMulti`、`WanVideoSetBlockSwap`、`ImageConcatMulti`、`WanVideoDecode`、`WanVideoContextOptions`、`CLIPVisionLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoSampler`、`WanVideoAnimateEmbeds`、`Evaluate Integers`、`WanVideoClipVisionEncode`、`WanVideoSetLoRAs`、`GetImageSizeAndCount`、`WanVideoBlockSwap`、`WanVideoTextEncodeCached`、`VHS_VideoCombine`、`ImageBlend`、`DrawViTPose`、`LayerUtility: ImageMaskScaleAsV2`、`SeCModelLoader`、`ImageFromBatch`、`WanVideoVAELoader`、`OnnxDetectionModelLoader`、`PoseAndFaceDetection`、`GrowMask`、`BlockifyMask`、`DrawMaskOnImage`、`ClothesSegment`、`SeCVideoSegmentation`、`VHS_LoadVideo`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
