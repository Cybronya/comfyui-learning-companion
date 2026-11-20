---
key: 平台全量/WAN2.2视频处理+动作模仿+动作迁移+人物替换_2073971277534158850.json
name: WAN2.2视频处理+动作模仿+动作迁移+人物替换_2073971277534158850
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/WAN2.2视频处理+动作模仿+动作迁移+人物替换_2073971277534158850.json
hash: d5bfbdeafe8ebaae
coverage: 0.931818
learned_at: 2026-11-14 01:03:45
nodes: [WanVideoDecode, GetImageSizeAndCount, VHS_VideoCombine, PoseAndFaceDetection, OnnxDetectionModelLoader, WanVideoTorchCompileSettings, WanVideoModelLoader, WanVideoLoraSelectMulti, WanVideoSetLoRAs, WanVideoSampler, WanVideoContextOptions, WanVideoBlockSwap, DrawViTPose, CLIPVisionLoader, WanVideoClipVisionEncode, WanVideoAnimateEmbeds, ImageConcatMulti, GrowMask, BlockifyMask, ImageBlend, VHS_VideoInfoLoaded, easy showAnything, Evaluate Integers, Evaluate Integers, LayerUtility: ImageMaskScaleAsV2, ImageFromBatch, ClothesSegment, SeCVideoSegmentation, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, SeCModelLoader, easy int, PreviewImage, DrawMaskOnImage, WanVideoVAELoader, WanVideoSetBlockSwap, ImageConcatMulti, LoadImage, easy int, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoCombine, easy int, WanVideoTextEncodeCached]
patterns: []
missing: []
---

# 平台全量/WAN2.2视频处理+动作模仿+动作迁移+人物替换_2073971277534158850.json

> 来源文件 `comfyui_library/workflows/平台全量/WAN2.2视频处理+动作模仿+动作迁移+人物替换_2073971277534158850.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（44 个）：
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `PoseAndFaceDetection`
- `OnnxDetectionModelLoader`
- `WanVideoTorchCompileSettings`
- `WanVideoModelLoader`
- `WanVideoLoraSelectMulti`
- `WanVideoSetLoRAs`
- `WanVideoSampler` ★核心
- `WanVideoContextOptions`
- `WanVideoBlockSwap`
- `DrawViTPose`
- `CLIPVisionLoader`
- `WanVideoClipVisionEncode`
- `WanVideoAnimateEmbeds`
- `ImageConcatMulti`
- `GrowMask`
- `BlockifyMask`
- `ImageBlend`
- `VHS_VideoInfoLoaded`
- `easy showAnything`
- `Evaluate Integers`
- `Evaluate Integers`
- `LayerUtility: ImageMaskScaleAsV2`
- `ImageFromBatch`
- `ClothesSegment`
- `SeCVideoSegmentation`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewImage`
- `SeCModelLoader`
- `easy int`
- `PreviewImage`
- `DrawMaskOnImage`
- `WanVideoVAELoader`
- `WanVideoSetBlockSwap`
- `ImageConcatMulti`
- `LoadImage`
- `easy int`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `easy int`
- `WanVideoTextEncodeCached`

## 知识

覆盖率 **93%**（41/44）

**有卡**：`WanVideoDecode`、`GetImageSizeAndCount`、`VHS_VideoCombine`、`PoseAndFaceDetection`、`OnnxDetectionModelLoader`、`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`WanVideoSetLoRAs`、`WanVideoSampler`、`WanVideoContextOptions`、`WanVideoBlockSwap`、`DrawViTPose`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`WanVideoAnimateEmbeds`、`ImageConcatMulti`、`GrowMask`、`BlockifyMask`、`ImageBlend`、`VHS_VideoInfoLoaded`、`Evaluate Integers`、`LayerUtility: ImageMaskScaleAsV2`、`ImageFromBatch`、`ClothesSegment`、`SeCVideoSegmentation`、`LayerUtility: ImageScaleByAspectRatio V2`、`SeCModelLoader`、`easy int`、`DrawMaskOnImage`、`WanVideoVAELoader`、`WanVideoSetBlockSwap`、`LoadImage`、`VHS_LoadVideo`、`WanVideoTextEncodeCached`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoLoraSelectMulti、WanVideoSetLoRAs
