---
key: 视频生成/图生视频/动作迁移  动作模仿  人物替换  wan2.2_2067482504520617985.json
name: 动作迁移  动作模仿  人物替换  wan2.2_2067482504520617985.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/动作迁移  动作模仿  人物替换  wan2.2_2067482504520617985.json
hash: 294c9e5583df367a
coverage: 0.926829
learned_at: 2026-10-15 22:40:02
nodes: [OnnxDetectionModelLoader, ImageBlend, VHS_VideoCombine, DrawViTPose, PoseAndFaceDetection, ImageConcatMulti, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageMaskScaleAsV2, VHS_VideoInfoLoaded, easy showAnything, PreviewImage, ImageFromBatch, easy int, GrowMask, BlockifyMask, DrawMaskOnImage, SeCVideoSegmentation, VHS_LoadVideo, LoadImage, SeCModelLoader, PreviewImage, ClothesSegment, WanVideoTextEncodeCached, VHS_VideoCombine, ImageConcatMulti, VHS_VideoCombine, CLIPVisionLoader, GetImageSizeAndCount, WanVideoDecode, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoModelLoader, WanVideoLoraSelectMulti, WanVideoBlockSwap, WanVideoTorchCompileSettings, WanVideoAnimateEmbeds, WanVideoContextOptions, Evaluate Integers, WanVideoClipVisionEncode, WanVideoVAELoader]
patterns: []
missing: []
---

# 视频生成/图生视频/动作迁移  动作模仿  人物替换  wan2.2_2067482504520617985.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2067482504520617985.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（41 个）：
- `OnnxDetectionModelLoader`
- `ImageBlend`
- `VHS_VideoCombine`
- `DrawViTPose`
- `PoseAndFaceDetection`
- `ImageConcatMulti`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageMaskScaleAsV2`
- `VHS_VideoInfoLoaded`
- `easy showAnything`
- `PreviewImage`
- `ImageFromBatch`
- `easy int`
- `GrowMask`
- `BlockifyMask`
- `DrawMaskOnImage`
- `SeCVideoSegmentation`
- `VHS_LoadVideo`
- `LoadImage`
- `SeCModelLoader`
- `PreviewImage`
- `ClothesSegment`
- `WanVideoTextEncodeCached`
- `VHS_VideoCombine`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `CLIPVisionLoader`
- `GetImageSizeAndCount`
- `WanVideoDecode`
- `WanVideoSampler` ★核心
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoModelLoader`
- `WanVideoLoraSelectMulti`
- `WanVideoBlockSwap`
- `WanVideoTorchCompileSettings`
- `WanVideoAnimateEmbeds`
- `WanVideoContextOptions`
- `Evaluate Integers`
- `WanVideoClipVisionEncode`
- `WanVideoVAELoader`

## 知识

覆盖率 **93%**（38/41）

**有卡**：`OnnxDetectionModelLoader`、`ImageBlend`、`VHS_VideoCombine`、`DrawViTPose`、`PoseAndFaceDetection`、`ImageConcatMulti`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageMaskScaleAsV2`、`VHS_VideoInfoLoaded`、`ImageFromBatch`、`easy int`、`GrowMask`、`BlockifyMask`、`DrawMaskOnImage`、`SeCVideoSegmentation`、`VHS_LoadVideo`、`LoadImage`、`SeCModelLoader`、`ClothesSegment`、`WanVideoTextEncodeCached`、`CLIPVisionLoader`、`GetImageSizeAndCount`、`WanVideoDecode`、`WanVideoSampler`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`WanVideoBlockSwap`、`WanVideoTorchCompileSettings`、`WanVideoAnimateEmbeds`、`WanVideoContextOptions`、`Evaluate Integers`、`WanVideoClipVisionEncode`、`WanVideoVAELoader`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
