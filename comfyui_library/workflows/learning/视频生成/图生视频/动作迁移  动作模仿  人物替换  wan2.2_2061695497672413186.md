---
key: 视频生成/图生视频/动作迁移  动作模仿  人物替换  wan2.2_2061695497672413186.json
name: 动作迁移  动作模仿  人物替换  wan2.2_2061695497672413186.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2061695497672413186.json
hash: e8fcbb9755e2e4f2
coverage: 0.931818
learned_at: 2026-10-15 22:38:55
nodes: [VHS_LoadVideo, easy int, easy int, Evaluate Integers, LayerUtility: ImageScaleByAspectRatio V2, VHS_VideoInfoLoaded, easy int, easy showAnything, ImageConcatMulti, ImageFromBatch, ClothesSegment, SeCModelLoader, SeCVideoSegmentation, VHS_VideoCombine, LoadImage, LayerUtility: ImageMaskScaleAsV2, PreviewImage, PreviewImage, VHS_VideoCombine, DrawViTPose, PoseAndFaceDetection, OnnxDetectionModelLoader, GrowMask, BlockifyMask, DrawMaskOnImage, Evaluate Integers, ImageBlend, ImageConcatMulti, CLIPVisionLoader, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoAnimateEmbeds, WanVideoVAELoader, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoModelLoader, WanVideoLoraSelectMulti, WanVideoSetLoRAs, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoSampler, WanVideoDecode, GetImageSizeAndCount, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/动作迁移  动作模仿  人物替换  wan2.2_2061695497672413186.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2061695497672413186.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（44 个）：
- `VHS_LoadVideo`
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
- `LoadImage`
- `LayerUtility: ImageMaskScaleAsV2`
- `PreviewImage`
- `PreviewImage`
- `VHS_VideoCombine`
- `DrawViTPose`
- `PoseAndFaceDetection`
- `OnnxDetectionModelLoader`
- `GrowMask`
- `BlockifyMask`
- `DrawMaskOnImage`
- `Evaluate Integers`
- `ImageBlend`
- `ImageConcatMulti`
- `CLIPVisionLoader`
- `WanVideoClipVisionEncode`
- `WanVideoContextOptions`
- `WanVideoAnimateEmbeds`
- `WanVideoVAELoader`
- `WanVideoTextEncodeCached`
- `WanVideoTorchCompileSettings`
- `WanVideoModelLoader`
- `WanVideoLoraSelectMulti`
- `WanVideoSetLoRAs`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `VHS_VideoCombine`

## 知识

覆盖率 **93%**（41/44）

**有卡**：`VHS_LoadVideo`、`easy int`、`Evaluate Integers`、`LayerUtility: ImageScaleByAspectRatio V2`、`VHS_VideoInfoLoaded`、`ImageConcatMulti`、`ImageFromBatch`、`ClothesSegment`、`SeCModelLoader`、`SeCVideoSegmentation`、`VHS_VideoCombine`、`LoadImage`、`LayerUtility: ImageMaskScaleAsV2`、`DrawViTPose`、`PoseAndFaceDetection`、`OnnxDetectionModelLoader`、`GrowMask`、`BlockifyMask`、`DrawMaskOnImage`、`ImageBlend`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`WanVideoContextOptions`、`WanVideoAnimateEmbeds`、`WanVideoVAELoader`、`WanVideoTextEncodeCached`、`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`WanVideoSetLoRAs`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`WanVideoSampler`、`WanVideoDecode`、`GetImageSizeAndCount`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
