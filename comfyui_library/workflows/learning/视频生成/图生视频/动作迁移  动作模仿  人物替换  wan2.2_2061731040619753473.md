---
key: 视频生成/图生视频/动作迁移  动作模仿  人物替换  wan2.2_2061731040619753473.json
name: 动作迁移  动作模仿  人物替换  wan2.2_2061731040619753473.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/动作迁移  动作模仿  人物替换  wan2.2_2061731040619753473.json
hash: d628ed4fe3a194d6
coverage: 0.931818
learned_at: 2026-10-15 22:38:56
nodes: [easy int, easy int, Evaluate Integers, LayerUtility: ImageScaleByAspectRatio V2, VHS_VideoInfoLoaded, easy int, easy showAnything, ImageConcatMulti, ImageFromBatch, ClothesSegment, SeCModelLoader, SeCVideoSegmentation, VHS_VideoCombine, LayerUtility: ImageMaskScaleAsV2, PreviewImage, PreviewImage, WanVideoDecode, GetImageSizeAndCount, VHS_VideoCombine, LoadImage, VHS_VideoCombine, PoseAndFaceDetection, OnnxDetectionModelLoader, WanVideoTorchCompileSettings, WanVideoModelLoader, WanVideoLoraSelectMulti, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoSampler, WanVideoContextOptions, WanVideoBlockSwap, WanVideoTextEncodeCached, WanVideoVAELoader, DrawViTPose, CLIPVisionLoader, WanVideoClipVisionEncode, WanVideoAnimateEmbeds, ImageConcatMulti, GrowMask, BlockifyMask, DrawMaskOnImage, Evaluate Integers, ImageBlend, VHS_LoadVideo]
patterns: []
missing: []
---

# 视频生成/图生视频/动作迁移  动作模仿  人物替换  wan2.2_2061731040619753473.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2061731040619753473.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（44 个）：
- `easy int`
- `easy int`
- `Evaluate Integers`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VHS_VideoInfoLoaded`
- `easy int`
- `easy showAnything`
- `ImageConcatMulti`
- `ImageFromBatch`
- `ClothesSegment`
- `SeCModelLoader`
- `SeCVideoSegmentation`
- `VHS_VideoCombine`
- `LayerUtility: ImageMaskScaleAsV2`
- `PreviewImage`
- `PreviewImage`
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `LoadImage`
- `VHS_VideoCombine`
- `PoseAndFaceDetection`
- `OnnxDetectionModelLoader`
- `WanVideoTorchCompileSettings`
- `WanVideoModelLoader`
- `WanVideoLoraSelectMulti`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoSampler` ★核心
- `WanVideoContextOptions`
- `WanVideoBlockSwap`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`
- `DrawViTPose`
- `CLIPVisionLoader`
- `WanVideoClipVisionEncode`
- `WanVideoAnimateEmbeds`
- `ImageConcatMulti`
- `GrowMask`
- `BlockifyMask`
- `DrawMaskOnImage`
- `Evaluate Integers`
- `ImageBlend`
- `VHS_LoadVideo`

## 知识

覆盖率 **93%**（41/44）

**有卡**：`easy int`、`Evaluate Integers`、`LayerUtility: ImageScaleByAspectRatio V2`、`VHS_VideoInfoLoaded`、`ImageConcatMulti`、`ImageFromBatch`、`ClothesSegment`、`SeCModelLoader`、`SeCVideoSegmentation`、`VHS_VideoCombine`、`LayerUtility: ImageMaskScaleAsV2`、`WanVideoDecode`、`GetImageSizeAndCount`、`LoadImage`、`PoseAndFaceDetection`、`OnnxDetectionModelLoader`、`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`WanVideoSampler`、`WanVideoContextOptions`、`WanVideoBlockSwap`、`WanVideoTextEncodeCached`、`WanVideoVAELoader`、`DrawViTPose`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`WanVideoAnimateEmbeds`、`GrowMask`、`BlockifyMask`、`DrawMaskOnImage`、`ImageBlend`、`VHS_LoadVideo`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
