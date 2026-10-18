---
key: 视频生成/图生视频/动作迁移  动作模仿  人物替换  wan2.2_2064962652962648066.json
name: 动作迁移  动作模仿  人物替换  wan2.2_2064962652962648066.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/动作迁移  动作模仿  人物替换  wan2.2_2064962652962648066.json
hash: 814bf5923d84ce4c
coverage: 0.974359
learned_at: 2026-10-15 22:39:32
nodes: [VHS_VideoCombine, WanVideoModelLoader, GetImageSizeAndCount, WanVideoTorchCompileSettings, WanVideoLoraSelectMulti, WanVideoBlockSwap, WanVideoSetBlockSwap, ImageConcatMulti, VHS_VideoCombine, WanVideoDecode, WanVideoContextOptions, CLIPVisionLoader, ImageConcatMulti, PoseAndFaceDetection, VHS_VideoCombine, OnnxDetectionModelLoader, GrowMask, BlockifyMask, DrawMaskOnImage, VHS_VideoInfoLoaded, easy showAnything, easy int, ImageFromBatch, SeCVideoSegmentation, LayerUtility: ImageScaleByAspectRatio V2, WanVideoSampler, VHS_LoadVideo, LoadImage, WanVideoVAELoader, ClothesSegment, SeCModelLoader, LayerUtility: ImageMaskScaleAsV2, ImageBlend, DrawViTPose, WanVideoAnimateEmbeds, Evaluate Integers, WanVideoClipVisionEncode, WanVideoSetLoRAs, WanVideoTextEncodeCached]
patterns: []
missing: []
---

# 视频生成/图生视频/动作迁移  动作模仿  人物替换  wan2.2_2064962652962648066.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2064962652962648066.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（39 个）：
- `VHS_VideoCombine`
- `WanVideoModelLoader`
- `GetImageSizeAndCount`
- `WanVideoTorchCompileSettings`
- `WanVideoLoraSelectMulti`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `WanVideoContextOptions`
- `CLIPVisionLoader`
- `ImageConcatMulti`
- `PoseAndFaceDetection`
- `VHS_VideoCombine`
- `OnnxDetectionModelLoader`
- `GrowMask`
- `BlockifyMask`
- `DrawMaskOnImage`
- `VHS_VideoInfoLoaded`
- `easy showAnything`
- `easy int`
- `ImageFromBatch`
- `SeCVideoSegmentation`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoSampler` ★核心
- `VHS_LoadVideo`
- `LoadImage`
- `WanVideoVAELoader`
- `ClothesSegment`
- `SeCModelLoader`
- `LayerUtility: ImageMaskScaleAsV2`
- `ImageBlend`
- `DrawViTPose`
- `WanVideoAnimateEmbeds`
- `Evaluate Integers`
- `WanVideoClipVisionEncode`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`

## 知识

覆盖率 **97%**（38/39）

**有卡**：`VHS_VideoCombine`、`WanVideoModelLoader`、`GetImageSizeAndCount`、`WanVideoTorchCompileSettings`、`WanVideoLoraSelectMulti`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`ImageConcatMulti`、`WanVideoDecode`、`WanVideoContextOptions`、`CLIPVisionLoader`、`PoseAndFaceDetection`、`OnnxDetectionModelLoader`、`GrowMask`、`BlockifyMask`、`DrawMaskOnImage`、`VHS_VideoInfoLoaded`、`easy int`、`ImageFromBatch`、`SeCVideoSegmentation`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoSampler`、`VHS_LoadVideo`、`LoadImage`、`WanVideoVAELoader`、`ClothesSegment`、`SeCModelLoader`、`LayerUtility: ImageMaskScaleAsV2`、`ImageBlend`、`DrawViTPose`、`WanVideoAnimateEmbeds`、`Evaluate Integers`、`WanVideoClipVisionEncode`、`WanVideoSetLoRAs`、`WanVideoTextEncodeCached`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
