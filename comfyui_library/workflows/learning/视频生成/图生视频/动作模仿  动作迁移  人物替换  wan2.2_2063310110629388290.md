---
key: 视频生成/图生视频/动作模仿  动作迁移  人物替换  wan2.2_2063310110629388290.json
name: 动作模仿  动作迁移  人物替换  wan2.2_2063310110629388290.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2063310110629388290.json
hash: 57f6f207a51aff86
coverage: 0.926829
learned_at: 2026-10-15 22:39:12
nodes: [WanVideoLoraSelectMulti, OnnxDetectionModelLoader, WanVideoVAELoader, WanVideoBlockSwap, WanVideoModelLoader, WanVideoSetBlockSwap, CLIPVisionLoader, WanVideoSetLoRAs, WanVideoAnimateEmbeds, WanVideoContextOptions, WanVideoSampler, WanVideoTorchCompileSettings, Evaluate Integers, WanVideoClipVisionEncode, ImageBlend, VHS_VideoCombine, DrawViTPose, PoseAndFaceDetection, GetImageSizeAndCount, WanVideoDecode, ImageConcatMulti, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageMaskScaleAsV2, VHS_VideoInfoLoaded, easy showAnything, ImageFromBatch, easy int, BlockifyMask, DrawMaskOnImage, GrowMask, ClothesSegment, PreviewImage, WanVideoTextEncodeCached, SeCVideoSegmentation, SeCModelLoader, PreviewImage, VHS_LoadVideo, LoadImage, ImageConcatMulti, VHS_VideoCombine, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/动作模仿  动作迁移  人物替换  wan2.2_2063310110629388290.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2063310110629388290.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（41 个）：
- `WanVideoLoraSelectMulti`
- `OnnxDetectionModelLoader`
- `WanVideoVAELoader`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `WanVideoSetBlockSwap`
- `CLIPVisionLoader`
- `WanVideoSetLoRAs`
- `WanVideoAnimateEmbeds`
- `WanVideoContextOptions`
- `WanVideoSampler` ★核心
- `WanVideoTorchCompileSettings`
- `Evaluate Integers`
- `WanVideoClipVisionEncode`
- `ImageBlend`
- `VHS_VideoCombine`
- `DrawViTPose`
- `PoseAndFaceDetection`
- `GetImageSizeAndCount`
- `WanVideoDecode`
- `ImageConcatMulti`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageMaskScaleAsV2`
- `VHS_VideoInfoLoaded`
- `easy showAnything`
- `ImageFromBatch`
- `easy int`
- `BlockifyMask`
- `DrawMaskOnImage`
- `GrowMask`
- `ClothesSegment`
- `PreviewImage`
- `WanVideoTextEncodeCached`
- `SeCVideoSegmentation`
- `SeCModelLoader`
- `PreviewImage`
- `VHS_LoadVideo`
- `LoadImage`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `VHS_VideoCombine`

## 知识

覆盖率 **93%**（38/41）

**有卡**：`WanVideoLoraSelectMulti`、`OnnxDetectionModelLoader`、`WanVideoVAELoader`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`WanVideoSetBlockSwap`、`CLIPVisionLoader`、`WanVideoSetLoRAs`、`WanVideoAnimateEmbeds`、`WanVideoContextOptions`、`WanVideoSampler`、`WanVideoTorchCompileSettings`、`Evaluate Integers`、`WanVideoClipVisionEncode`、`ImageBlend`、`VHS_VideoCombine`、`DrawViTPose`、`PoseAndFaceDetection`、`GetImageSizeAndCount`、`WanVideoDecode`、`ImageConcatMulti`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageMaskScaleAsV2`、`VHS_VideoInfoLoaded`、`ImageFromBatch`、`easy int`、`BlockifyMask`、`DrawMaskOnImage`、`GrowMask`、`ClothesSegment`、`WanVideoTextEncodeCached`、`SeCVideoSegmentation`、`SeCModelLoader`、`VHS_LoadVideo`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
