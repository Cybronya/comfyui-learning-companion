---
key: 视频生成/图生视频/动作模仿  动作迁移   角色替换  人物替换  wan2.2_2081662918516629505.json
name: 动作模仿  动作迁移   角色替换  人物替换  wan2.2_2081662918516629505.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2081662918516629505.json
hash: bda2aefdb3dbf112
coverage: 1
learned_at: 2026-10-15 22:42:24
nodes: [WanVideoModelLoader, WanVideoTorchCompileSettings, WanVideoLoraSelectMulti, WanVideoSetBlockSwap, ImageConcatMulti, WanVideoDecode, WanVideoContextOptions, CLIPVisionLoader, PoseAndFaceDetection, VHS_VideoCombine, OnnxDetectionModelLoader, GrowMask, BlockifyMask, LayerUtility: ImageScaleByAspectRatio V2, WanVideoSampler, WanVideoVAELoader, WanVideoAnimateEmbeds, Evaluate Integers, WanVideoClipVisionEncode, WanVideoSetLoRAs, DrawMaskOnImage, GetImageSizeAndCount, WanVideoBlockSwap, WanVideoTextEncodeCached, VHS_VideoCombine, ImageBlend, DrawViTPose, ImageConcatMulti, VHS_VideoCombine, VHS_LoadVideo, LayerUtility: ImageMaskScaleAsV2, ClothesSegment, SeCModelLoader, SeCVideoSegmentation, ImageFromBatch, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/动作模仿  动作迁移   角色替换  人物替换  wan2.2_2081662918516629505.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2081662918516629505.json`

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
- `PoseAndFaceDetection`
- `VHS_VideoCombine`
- `OnnxDetectionModelLoader`
- `GrowMask`
- `BlockifyMask`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoSampler` ★核心
- `WanVideoVAELoader`
- `WanVideoAnimateEmbeds`
- `Evaluate Integers`
- `WanVideoClipVisionEncode`
- `WanVideoSetLoRAs`
- `DrawMaskOnImage`
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
- `ClothesSegment`
- `SeCModelLoader`
- `SeCVideoSegmentation`
- `ImageFromBatch`
- `LoadImage`

## 知识

覆盖率 **100%**（36/36）

**有卡**：`WanVideoModelLoader`、`WanVideoTorchCompileSettings`、`WanVideoLoraSelectMulti`、`WanVideoSetBlockSwap`、`ImageConcatMulti`、`WanVideoDecode`、`WanVideoContextOptions`、`CLIPVisionLoader`、`PoseAndFaceDetection`、`VHS_VideoCombine`、`OnnxDetectionModelLoader`、`GrowMask`、`BlockifyMask`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoSampler`、`WanVideoVAELoader`、`WanVideoAnimateEmbeds`、`Evaluate Integers`、`WanVideoClipVisionEncode`、`WanVideoSetLoRAs`、`DrawMaskOnImage`、`GetImageSizeAndCount`、`WanVideoBlockSwap`、`WanVideoTextEncodeCached`、`ImageBlend`、`DrawViTPose`、`VHS_LoadVideo`、`LayerUtility: ImageMaskScaleAsV2`、`ClothesSegment`、`SeCModelLoader`、`SeCVideoSegmentation`、`ImageFromBatch`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
