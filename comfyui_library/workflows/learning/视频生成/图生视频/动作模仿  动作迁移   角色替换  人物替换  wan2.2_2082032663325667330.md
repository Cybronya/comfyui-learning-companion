---
key: 视频生成/图生视频/动作模仿  动作迁移   角色替换  人物替换  wan2.2_2082032663325667330.json
name: 动作模仿  动作迁移   角色替换  人物替换  wan2.2_2082032663325667330.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2082032663325667330.json
hash: e17df5401e546413
coverage: 0.930233
learned_at: 2026-10-15 22:42:27
nodes: [WanVideoModelLoader, WanVideoTorchCompileSettings, WanVideoLoraSelectMulti, WanVideoSetBlockSwap, WanVideoDecode, WanVideoContextOptions, CLIPVisionLoader, PoseAndFaceDetection, VHS_VideoCombine, OnnxDetectionModelLoader, GrowMask, BlockifyMask, VHS_VideoInfoLoaded, easy int, SeCVideoSegmentation, LayerUtility: ImageScaleByAspectRatio V2, WanVideoSampler, WanVideoVAELoader, WanVideoAnimateEmbeds, Evaluate Integers, WanVideoClipVisionEncode, WanVideoSetLoRAs, DrawMaskOnImage, WanVideoBlockSwap, WanVideoTextEncodeCached, ImageBlend, DrawViTPose, ClothesSegment, ImageFromBatch, SeCModelLoader, easy showAnything, LoadImage, SetNode, LayerUtility: ImageMaskScaleAsV2, ImageConcatMulti, VHS_LoadVideo, VHS_VideoCombine, ImageConcatMulti, VHS_VideoCombine, VHS_VideoCombine, GetImageSizeAndCount, GetNode, ImageConcatMulti]
patterns: []
missing: []
---

# 视频生成/图生视频/动作模仿  动作迁移   角色替换  人物替换  wan2.2_2082032663325667330.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2082032663325667330.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（43 个）：
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
- `WanVideoAnimateEmbeds`
- `Evaluate Integers`
- `WanVideoClipVisionEncode`
- `WanVideoSetLoRAs`
- `DrawMaskOnImage`
- `WanVideoBlockSwap`
- `WanVideoTextEncodeCached`
- `ImageBlend`
- `DrawViTPose`
- `ClothesSegment`
- `ImageFromBatch`
- `SeCModelLoader`
- `easy showAnything`
- `LoadImage`
- `SetNode`
- `LayerUtility: ImageMaskScaleAsV2`
- `ImageConcatMulti`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `GetImageSizeAndCount`
- `GetNode`
- `ImageConcatMulti`

## 知识

覆盖率 **93%**（40/43）

**有卡**：`WanVideoModelLoader`、`WanVideoTorchCompileSettings`、`WanVideoLoraSelectMulti`、`WanVideoSetBlockSwap`、`WanVideoDecode`、`WanVideoContextOptions`、`CLIPVisionLoader`、`PoseAndFaceDetection`、`VHS_VideoCombine`、`OnnxDetectionModelLoader`、`GrowMask`、`BlockifyMask`、`VHS_VideoInfoLoaded`、`easy int`、`SeCVideoSegmentation`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoSampler`、`WanVideoVAELoader`、`WanVideoAnimateEmbeds`、`Evaluate Integers`、`WanVideoClipVisionEncode`、`WanVideoSetLoRAs`、`DrawMaskOnImage`、`WanVideoBlockSwap`、`WanVideoTextEncodeCached`、`ImageBlend`、`DrawViTPose`、`ClothesSegment`、`ImageFromBatch`、`SeCModelLoader`、`LoadImage`、`LayerUtility: ImageMaskScaleAsV2`、`ImageConcatMulti`、`VHS_LoadVideo`、`GetImageSizeAndCount`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
