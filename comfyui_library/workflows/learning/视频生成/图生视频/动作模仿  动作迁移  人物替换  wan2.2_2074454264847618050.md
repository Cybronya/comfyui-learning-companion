---
key: 视频生成/图生视频/动作模仿  动作迁移  人物替换  wan2.2_2074454264847618050.json
name: 动作模仿  动作迁移  人物替换  wan2.2_2074454264847618050.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/动作模仿  动作迁移  人物替换  wan2.2_2074454264847618050.json
hash: cd5b7d0a17591a49
coverage: 0.926829
learned_at: 2026-10-15 22:41:15
nodes: [WanVideoLoraSelectMulti, OnnxDetectionModelLoader, WanVideoVAELoader, WanVideoBlockSwap, WanVideoModelLoader, WanVideoSetBlockSwap, CLIPVisionLoader, WanVideoSetLoRAs, WanVideoAnimateEmbeds, WanVideoContextOptions, WanVideoSampler, WanVideoTorchCompileSettings, Evaluate Integers, WanVideoClipVisionEncode, ImageBlend, VHS_VideoCombine, DrawViTPose, PoseAndFaceDetection, GetImageSizeAndCount, WanVideoDecode, ImageConcatMulti, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageMaskScaleAsV2, VHS_VideoInfoLoaded, easy showAnything, ImageFromBatch, easy int, BlockifyMask, DrawMaskOnImage, GrowMask, ClothesSegment, PreviewImage, WanVideoTextEncodeCached, SeCVideoSegmentation, SeCModelLoader, PreviewImage, ImageConcatMulti, VHS_VideoCombine, VHS_VideoCombine, VHS_LoadVideo, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/动作模仿  动作迁移  人物替换  wan2.2_2074454264847618050.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2074454264847618050.json`

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
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `LoadImage`

## 知识

覆盖率 **93%**（38/41）

**有卡**：`WanVideoLoraSelectMulti`、`OnnxDetectionModelLoader`、`WanVideoVAELoader`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`WanVideoSetBlockSwap`、`CLIPVisionLoader`、`WanVideoSetLoRAs`、`WanVideoAnimateEmbeds`、`WanVideoContextOptions`、`WanVideoSampler`、`WanVideoTorchCompileSettings`、`Evaluate Integers`、`WanVideoClipVisionEncode`、`ImageBlend`、`VHS_VideoCombine`、`DrawViTPose`、`PoseAndFaceDetection`、`GetImageSizeAndCount`、`WanVideoDecode`、`ImageConcatMulti`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageMaskScaleAsV2`、`VHS_VideoInfoLoaded`、`ImageFromBatch`、`easy int`、`BlockifyMask`、`DrawMaskOnImage`、`GrowMask`、`ClothesSegment`、`WanVideoTextEncodeCached`、`SeCVideoSegmentation`、`SeCModelLoader`、`VHS_LoadVideo`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
