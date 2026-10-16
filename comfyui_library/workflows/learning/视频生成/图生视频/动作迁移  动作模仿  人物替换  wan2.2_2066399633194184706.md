---
key: 视频生成/图生视频/动作迁移  动作模仿  人物替换  wan2.2_2066399633194184706.json
name: 动作迁移  动作模仿  人物替换  wan2.2_2066399633194184706.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2066399633194184706.json
hash: cdbb753eaafe763e
coverage: 0.926829
learned_at: 2026-10-15 22:39:48
nodes: [LayerUtility: ImageScaleByAspectRatio V2, VHS_VideoInfoLoaded, easy showAnything, easy int, GrowMask, BlockifyMask, PreviewImage, ImageConcatMulti, VHS_VideoCombine, VHS_VideoCombine, GetImageSizeAndCount, WanVideoDecode, WanVideoVAELoader, WanVideoAnimateEmbeds, WanVideoSampler, WanVideoSetBlockSwap, WanVideoLoraSelectMulti, WanVideoSetLoRAs, WanVideoModelLoader, WanVideoTorchCompileSettings, WanVideoBlockSwap, WanVideoTextEncodeCached, WanVideoClipVisionEncode, CLIPVisionLoader, Evaluate Integers, WanVideoContextOptions, ImageConcatMulti, OnnxDetectionModelLoader, LayerUtility: ImageMaskScaleAsV2, PreviewImage, SeCModelLoader, SeCVideoSegmentation, ClothesSegment, ImageFromBatch, PoseAndFaceDetection, DrawMaskOnImage, DrawViTPose, ImageBlend, VHS_VideoCombine, VHS_LoadVideo, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/动作迁移  动作模仿  人物替换  wan2.2_2066399633194184706.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2066399633194184706.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（41 个）：
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VHS_VideoInfoLoaded`
- `easy showAnything`
- `easy int`
- `GrowMask`
- `BlockifyMask`
- `PreviewImage`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `GetImageSizeAndCount`
- `WanVideoDecode`
- `WanVideoVAELoader`
- `WanVideoAnimateEmbeds`
- `WanVideoSampler` ★核心
- `WanVideoSetBlockSwap`
- `WanVideoLoraSelectMulti`
- `WanVideoSetLoRAs`
- `WanVideoModelLoader`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `WanVideoTextEncodeCached`
- `WanVideoClipVisionEncode`
- `CLIPVisionLoader`
- `Evaluate Integers`
- `WanVideoContextOptions`
- `ImageConcatMulti`
- `OnnxDetectionModelLoader`
- `LayerUtility: ImageMaskScaleAsV2`
- `PreviewImage`
- `SeCModelLoader`
- `SeCVideoSegmentation`
- `ClothesSegment`
- `ImageFromBatch`
- `PoseAndFaceDetection`
- `DrawMaskOnImage`
- `DrawViTPose`
- `ImageBlend`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `LoadImage`

## 知识

覆盖率 **93%**（38/41）

**有卡**：`LayerUtility: ImageScaleByAspectRatio V2`、`VHS_VideoInfoLoaded`、`easy int`、`GrowMask`、`BlockifyMask`、`ImageConcatMulti`、`VHS_VideoCombine`、`GetImageSizeAndCount`、`WanVideoDecode`、`WanVideoVAELoader`、`WanVideoAnimateEmbeds`、`WanVideoSampler`、`WanVideoSetBlockSwap`、`WanVideoLoraSelectMulti`、`WanVideoSetLoRAs`、`WanVideoModelLoader`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoTextEncodeCached`、`WanVideoClipVisionEncode`、`CLIPVisionLoader`、`Evaluate Integers`、`WanVideoContextOptions`、`OnnxDetectionModelLoader`、`LayerUtility: ImageMaskScaleAsV2`、`SeCModelLoader`、`SeCVideoSegmentation`、`ClothesSegment`、`ImageFromBatch`、`PoseAndFaceDetection`、`DrawMaskOnImage`、`DrawViTPose`、`ImageBlend`、`VHS_LoadVideo`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
