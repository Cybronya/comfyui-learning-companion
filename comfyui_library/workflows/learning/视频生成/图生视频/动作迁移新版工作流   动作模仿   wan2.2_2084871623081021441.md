---
key: 视频生成/图生视频/动作迁移新版工作流   动作模仿   wan2.2_2084871623081021441.json
name: 动作迁移新版工作流   动作模仿   wan2.2_2084871623081021441
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/动作迁移新版工作流   动作模仿   wan2.2_2084871623081021441.json
hash: ea80592ae9f0b766
coverage: 1
learned_at: 2026-10-16 20:35:51
nodes: [WanVideoAnimateEmbeds, ImageConcatMulti, VHS_VideoCombine, ImageConcatMulti, WanVideoDecode, WanVideoSampler, WanVideoTextEncodeCached, WanVideoModelLoader, WanVideoSetLoRAs, WanVideoBlockSwap, WanVideoSetBlockSwap, Evaluate Integers, DrawViTPose, WanVideoClipVisionEncode, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageMaskScaleAsV2, easy int, ImageFromBatch, SeCModelLoader, ClothesSegment, SeCVideoSegmentation, GrowMask, BlockifyMask, WanVideoVAELoader, OnnxDetectionModelLoader, CLIPVisionLoader, PoseAndFaceDetection, VHS_VideoCombine, GetImageSizeAndCount, WanVideoTorchCompileSettings, WanVideoContextOptions, WanVideoLoraSelectMulti, VHS_VideoCombine, DrawMaskOnImage, LoadImage, VHS_LoadVideo]
patterns: []
missing: []
---

# 视频生成/图生视频/动作迁移新版工作流   动作模仿   wan2.2_2084871623081021441.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/动作迁移新版工作流   动作模仿   wan2.2_2084871623081021441.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（36 个）：
- `WanVideoAnimateEmbeds`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `ImageConcatMulti`
- `WanVideoDecode`
- `WanVideoSampler` ★核心
- `WanVideoTextEncodeCached`
- `WanVideoModelLoader`
- `WanVideoSetLoRAs`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `Evaluate Integers`
- `DrawViTPose`
- `WanVideoClipVisionEncode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageMaskScaleAsV2`
- `easy int`
- `ImageFromBatch`
- `SeCModelLoader`
- `ClothesSegment`
- `SeCVideoSegmentation`
- `GrowMask`
- `BlockifyMask`
- `WanVideoVAELoader`
- `OnnxDetectionModelLoader`
- `CLIPVisionLoader`
- `PoseAndFaceDetection`
- `VHS_VideoCombine`
- `GetImageSizeAndCount`
- `WanVideoTorchCompileSettings`
- `WanVideoContextOptions`
- `WanVideoLoraSelectMulti`
- `VHS_VideoCombine`
- `DrawMaskOnImage`
- `LoadImage`
- `VHS_LoadVideo`

## 知识

覆盖率 **100%**（36/36）

**有卡**：`WanVideoAnimateEmbeds`、`ImageConcatMulti`、`VHS_VideoCombine`、`WanVideoDecode`、`WanVideoSampler`、`WanVideoTextEncodeCached`、`WanVideoModelLoader`、`WanVideoSetLoRAs`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`Evaluate Integers`、`DrawViTPose`、`WanVideoClipVisionEncode`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageMaskScaleAsV2`、`easy int`、`ImageFromBatch`、`SeCModelLoader`、`ClothesSegment`、`SeCVideoSegmentation`、`GrowMask`、`BlockifyMask`、`WanVideoVAELoader`、`OnnxDetectionModelLoader`、`CLIPVisionLoader`、`PoseAndFaceDetection`、`GetImageSizeAndCount`、`WanVideoTorchCompileSettings`、`WanVideoContextOptions`、`WanVideoLoraSelectMulti`、`DrawMaskOnImage`、`LoadImage`、`VHS_LoadVideo`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
