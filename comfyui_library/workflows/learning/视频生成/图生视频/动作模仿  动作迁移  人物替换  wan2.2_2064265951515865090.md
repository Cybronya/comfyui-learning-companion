---
key: 视频生成/图生视频/动作模仿  动作迁移  人物替换  wan2.2_2064265951515865090.json
name: 动作模仿  动作迁移  人物替换  wan2.2_2064265951515865090.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2064265951515865090.json
hash: 2c36e75ad03b3bff
coverage: 0.926829
learned_at: 2026-10-15 22:39:22
nodes: [WanVideoLoraSelectMulti, OnnxDetectionModelLoader, WanVideoVAELoader, WanVideoBlockSwap, WanVideoModelLoader, WanVideoSetBlockSwap, CLIPVisionLoader, WanVideoSetLoRAs, WanVideoAnimateEmbeds, WanVideoContextOptions, WanVideoSampler, WanVideoTorchCompileSettings, Evaluate Integers, WanVideoClipVisionEncode, ImageBlend, VHS_VideoCombine, DrawViTPose, PoseAndFaceDetection, GetImageSizeAndCount, WanVideoDecode, VHS_VideoCombine, VHS_VideoCombine, ImageConcatMulti, ImageConcatMulti, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageMaskScaleAsV2, VHS_VideoInfoLoaded, easy showAnything, ImageFromBatch, easy int, BlockifyMask, DrawMaskOnImage, GrowMask, ClothesSegment, PreviewImage, VHS_LoadVideo, WanVideoTextEncodeCached, SeCVideoSegmentation, SeCModelLoader, PreviewImage, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/动作模仿  动作迁移  人物替换  wan2.2_2064265951515865090.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2064265951515865090.json`

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
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `ImageConcatMulti`
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
- `VHS_LoadVideo`
- `WanVideoTextEncodeCached`
- `SeCVideoSegmentation`
- `SeCModelLoader`
- `PreviewImage`
- `LoadImage`

## 知识

覆盖率 **93%**（38/41）

**有卡**：`WanVideoLoraSelectMulti`、`OnnxDetectionModelLoader`、`WanVideoVAELoader`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`WanVideoSetBlockSwap`、`CLIPVisionLoader`、`WanVideoSetLoRAs`、`WanVideoAnimateEmbeds`、`WanVideoContextOptions`、`WanVideoSampler`、`WanVideoTorchCompileSettings`、`Evaluate Integers`、`WanVideoClipVisionEncode`、`ImageBlend`、`VHS_VideoCombine`、`DrawViTPose`、`PoseAndFaceDetection`、`GetImageSizeAndCount`、`WanVideoDecode`、`ImageConcatMulti`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageMaskScaleAsV2`、`VHS_VideoInfoLoaded`、`ImageFromBatch`、`easy int`、`BlockifyMask`、`DrawMaskOnImage`、`GrowMask`、`ClothesSegment`、`VHS_LoadVideo`、`WanVideoTextEncodeCached`、`SeCVideoSegmentation`、`SeCModelLoader`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
