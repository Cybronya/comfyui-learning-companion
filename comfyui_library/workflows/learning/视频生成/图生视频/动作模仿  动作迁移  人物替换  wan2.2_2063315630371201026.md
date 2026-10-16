---
key: 视频生成/图生视频/动作模仿  动作迁移  人物替换  wan2.2_2063315630371201026.json
name: 动作模仿  动作迁移  人物替换  wan2.2_2063315630371201026.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2063315630371201026.json
hash: 9918932cc09e14e0
coverage: 0.95
learned_at: 2026-10-15 22:39:13
nodes: [LoadImage, VHS_LoadVideo, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageMaskScaleAsV2, VHS_VideoInfoLoaded, SeCModelLoader, PreviewImage, ImageFromBatch, easy int, ClothesSegment, SeCVideoSegmentation, PreviewImage, BlockifyMask, GrowMask, OnnxDetectionModelLoader, PoseAndFaceDetection, DrawViTPose, WanVideoTextEncodeCached, CLIPVisionLoader, WanVideoVAELoader, WanVideoTorchCompileSettings, WanVideoModelLoader, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoLoraSelectMulti, GetImageSizeAndCount, WanVideoDecode, WanVideoSampler, WanVideoAnimateEmbeds, WanVideoContextOptions, Evaluate Integers, WanVideoClipVisionEncode, VHS_VideoCombine, ImageBlend, DrawMaskOnImage, ImageConcatMulti, VHS_VideoCombine, ImageConcatMulti, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/动作模仿  动作迁移  人物替换  wan2.2_2063315630371201026.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2063315630371201026.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（40 个）：
- `LoadImage`
- `VHS_LoadVideo`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageMaskScaleAsV2`
- `VHS_VideoInfoLoaded`
- `SeCModelLoader`
- `PreviewImage`
- `ImageFromBatch`
- `easy int`
- `ClothesSegment`
- `SeCVideoSegmentation`
- `PreviewImage`
- `BlockifyMask`
- `GrowMask`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `DrawViTPose`
- `WanVideoTextEncodeCached`
- `CLIPVisionLoader`
- `WanVideoVAELoader`
- `WanVideoTorchCompileSettings`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoLoraSelectMulti`
- `GetImageSizeAndCount`
- `WanVideoDecode`
- `WanVideoSampler` ★核心
- `WanVideoAnimateEmbeds`
- `WanVideoContextOptions`
- `Evaluate Integers`
- `WanVideoClipVisionEncode`
- `VHS_VideoCombine`
- `ImageBlend`
- `DrawMaskOnImage`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `ImageConcatMulti`
- `VHS_VideoCombine`

## 知识

覆盖率 **95%**（38/40）

**有卡**：`LoadImage`、`VHS_LoadVideo`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageMaskScaleAsV2`、`VHS_VideoInfoLoaded`、`SeCModelLoader`、`ImageFromBatch`、`easy int`、`ClothesSegment`、`SeCVideoSegmentation`、`BlockifyMask`、`GrowMask`、`OnnxDetectionModelLoader`、`PoseAndFaceDetection`、`DrawViTPose`、`WanVideoTextEncodeCached`、`CLIPVisionLoader`、`WanVideoVAELoader`、`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoLoraSelectMulti`、`GetImageSizeAndCount`、`WanVideoDecode`、`WanVideoSampler`、`WanVideoAnimateEmbeds`、`WanVideoContextOptions`、`Evaluate Integers`、`WanVideoClipVisionEncode`、`VHS_VideoCombine`、`ImageBlend`、`DrawMaskOnImage`、`ImageConcatMulti`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
