---
key: 视频生成/图生视频/动作迁移  动作模仿  人物替换  wan2.2_2064236113023295490.json
name: 动作迁移  动作模仿  人物替换  wan2.2_2064236113023295490.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2064236113023295490.json
hash: 7ba29dad05e2df10
coverage: 0.95
learned_at: 2026-10-15 22:39:21
nodes: [LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageMaskScaleAsV2, VHS_VideoInfoLoaded, SeCModelLoader, PreviewImage, ImageFromBatch, easy int, ClothesSegment, SeCVideoSegmentation, PreviewImage, BlockifyMask, GrowMask, OnnxDetectionModelLoader, PoseAndFaceDetection, DrawViTPose, CLIPVisionLoader, WanVideoVAELoader, WanVideoTorchCompileSettings, WanVideoModelLoader, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoLoraSelectMulti, GetImageSizeAndCount, WanVideoDecode, WanVideoSampler, WanVideoAnimateEmbeds, WanVideoContextOptions, Evaluate Integers, WanVideoClipVisionEncode, VHS_VideoCombine, ImageBlend, DrawMaskOnImage, ImageConcatMulti, VHS_VideoCombine, ImageConcatMulti, VHS_VideoCombine, WanVideoTextEncodeCached, VHS_LoadVideo, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/动作迁移  动作模仿  人物替换  wan2.2_2064236113023295490.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2064236113023295490.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（40 个）：
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
- `WanVideoTextEncodeCached`
- `VHS_LoadVideo`
- `LoadImage`

## 知识

覆盖率 **95%**（38/40）

**有卡**：`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageMaskScaleAsV2`、`VHS_VideoInfoLoaded`、`SeCModelLoader`、`ImageFromBatch`、`easy int`、`ClothesSegment`、`SeCVideoSegmentation`、`BlockifyMask`、`GrowMask`、`OnnxDetectionModelLoader`、`PoseAndFaceDetection`、`DrawViTPose`、`CLIPVisionLoader`、`WanVideoVAELoader`、`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoLoraSelectMulti`、`GetImageSizeAndCount`、`WanVideoDecode`、`WanVideoSampler`、`WanVideoAnimateEmbeds`、`WanVideoContextOptions`、`Evaluate Integers`、`WanVideoClipVisionEncode`、`VHS_VideoCombine`、`ImageBlend`、`DrawMaskOnImage`、`ImageConcatMulti`、`WanVideoTextEncodeCached`、`VHS_LoadVideo`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
