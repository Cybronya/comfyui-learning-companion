---
key: 视频生成/图生视频/动作迁移  动作模仿  人物替换  wan2.2_2062558376567066626.json
name: 动作迁移  动作模仿  人物替换  wan2.2_2062558376567066626.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/动作迁移  动作模仿  人物替换  wan2.2_2062558376567066626.json
hash: e98aa52671d9d494
coverage: 0.95
learned_at: 2026-10-15 22:39:05
nodes: [ImageConcatMulti, WanVideoDecode, VHS_LoadVideo, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, easy int, ImageFromBatch, SeCModelLoader, ClothesSegment, LayerUtility: ImageMaskScaleAsV2, PreviewImage, VHS_VideoInfoLoaded, SeCVideoSegmentation, PreviewImage, OnnxDetectionModelLoader, GrowMask, BlockifyMask, PoseAndFaceDetection, DrawMaskOnImage, VHS_VideoCombine, DrawViTPose, ImageBlend, WanVideoTextEncodeCached, WanVideoVAELoader, WanVideoTorchCompileSettings, WanVideoLoraSelectMulti, WanVideoSampler, WanVideoSetBlockSwap, GetImageSizeAndCount, VHS_VideoCombine, ImageConcatMulti, VHS_VideoCombine, WanVideoContextOptions, Evaluate Integers, WanVideoBlockSwap, CLIPVisionLoader, WanVideoClipVisionEncode, WanVideoModelLoader, WanVideoSetLoRAs, WanVideoAnimateEmbeds]
patterns: []
missing: []
---

# 视频生成/图生视频/动作迁移  动作模仿  人物替换  wan2.2_2062558376567066626.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2062558376567066626.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（40 个）：
- `ImageConcatMulti`
- `WanVideoDecode`
- `VHS_LoadVideo`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `easy int`
- `ImageFromBatch`
- `SeCModelLoader`
- `ClothesSegment`
- `LayerUtility: ImageMaskScaleAsV2`
- `PreviewImage`
- `VHS_VideoInfoLoaded`
- `SeCVideoSegmentation`
- `PreviewImage`
- `OnnxDetectionModelLoader`
- `GrowMask`
- `BlockifyMask`
- `PoseAndFaceDetection`
- `DrawMaskOnImage`
- `VHS_VideoCombine`
- `DrawViTPose`
- `ImageBlend`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`
- `WanVideoTorchCompileSettings`
- `WanVideoLoraSelectMulti`
- `WanVideoSampler` ★核心
- `WanVideoSetBlockSwap`
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `WanVideoContextOptions`
- `Evaluate Integers`
- `WanVideoBlockSwap`
- `CLIPVisionLoader`
- `WanVideoClipVisionEncode`
- `WanVideoModelLoader`
- `WanVideoSetLoRAs`
- `WanVideoAnimateEmbeds`

## 知识

覆盖率 **95%**（38/40）

**有卡**：`ImageConcatMulti`、`WanVideoDecode`、`VHS_LoadVideo`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`easy int`、`ImageFromBatch`、`SeCModelLoader`、`ClothesSegment`、`LayerUtility: ImageMaskScaleAsV2`、`VHS_VideoInfoLoaded`、`SeCVideoSegmentation`、`OnnxDetectionModelLoader`、`GrowMask`、`BlockifyMask`、`PoseAndFaceDetection`、`DrawMaskOnImage`、`VHS_VideoCombine`、`DrawViTPose`、`ImageBlend`、`WanVideoTextEncodeCached`、`WanVideoVAELoader`、`WanVideoTorchCompileSettings`、`WanVideoLoraSelectMulti`、`WanVideoSampler`、`WanVideoSetBlockSwap`、`GetImageSizeAndCount`、`WanVideoContextOptions`、`Evaluate Integers`、`WanVideoBlockSwap`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`WanVideoModelLoader`、`WanVideoSetLoRAs`、`WanVideoAnimateEmbeds`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
