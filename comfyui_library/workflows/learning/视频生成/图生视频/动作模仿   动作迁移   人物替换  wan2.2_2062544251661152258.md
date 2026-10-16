---
key: 视频生成/图生视频/动作模仿   动作迁移   人物替换  wan2.2_2062544251661152258.json
name: 动作模仿   动作迁移   人物替换  wan2.2_2062544251661152258.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2062544251661152258.json
hash: 9f3e7df7796b94ba
coverage: 0.95
learned_at: 2026-10-15 22:39:05
nodes: [easy int, PoseAndFaceDetection, DrawViTPose, VHS_LoadVideo, LoadImage, WanVideoDecode, GetImageSizeAndCount, ImageConcatMulti, VHS_VideoCombine, WanVideoTorchCompileSettings, WanVideoModelLoader, WanVideoBlockSwap, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoTextEncodeCached, WanVideoAnimateEmbeds, VHS_VideoCombine, ImageBlend, DrawMaskOnImage, WanVideoClipVisionEncode, CLIPVisionLoader, BlockifyMask, GrowMask, OnnxDetectionModelLoader, LayerUtility: ImageScaleByAspectRatio V2, ImageFromBatch, LayerUtility: ImageMaskScaleAsV2, PreviewImage, ClothesSegment, SeCVideoSegmentation, PreviewImage, VHS_VideoInfoLoaded, SeCModelLoader, WanVideoSampler, ImageConcatMulti, WanVideoContextOptions, Evaluate Integers, WanVideoVAELoader, WanVideoLoraSelectMulti, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/动作模仿   动作迁移   人物替换  wan2.2_2062544251661152258.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2062544251661152258.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（40 个）：
- `easy int`
- `PoseAndFaceDetection`
- `DrawViTPose`
- `VHS_LoadVideo`
- `LoadImage`
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `WanVideoTorchCompileSettings`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoTextEncodeCached`
- `WanVideoAnimateEmbeds`
- `VHS_VideoCombine`
- `ImageBlend`
- `DrawMaskOnImage`
- `WanVideoClipVisionEncode`
- `CLIPVisionLoader`
- `BlockifyMask`
- `GrowMask`
- `OnnxDetectionModelLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageFromBatch`
- `LayerUtility: ImageMaskScaleAsV2`
- `PreviewImage`
- `ClothesSegment`
- `SeCVideoSegmentation`
- `PreviewImage`
- `VHS_VideoInfoLoaded`
- `SeCModelLoader`
- `WanVideoSampler` ★核心
- `ImageConcatMulti`
- `WanVideoContextOptions`
- `Evaluate Integers`
- `WanVideoVAELoader`
- `WanVideoLoraSelectMulti`
- `VHS_VideoCombine`

## 知识

覆盖率 **95%**（38/40）

**有卡**：`easy int`、`PoseAndFaceDetection`、`DrawViTPose`、`VHS_LoadVideo`、`LoadImage`、`WanVideoDecode`、`GetImageSizeAndCount`、`ImageConcatMulti`、`VHS_VideoCombine`、`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`WanVideoBlockSwap`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`WanVideoTextEncodeCached`、`WanVideoAnimateEmbeds`、`ImageBlend`、`DrawMaskOnImage`、`WanVideoClipVisionEncode`、`CLIPVisionLoader`、`BlockifyMask`、`GrowMask`、`OnnxDetectionModelLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageFromBatch`、`LayerUtility: ImageMaskScaleAsV2`、`ClothesSegment`、`SeCVideoSegmentation`、`VHS_VideoInfoLoaded`、`SeCModelLoader`、`WanVideoSampler`、`WanVideoContextOptions`、`Evaluate Integers`、`WanVideoVAELoader`、`WanVideoLoraSelectMulti`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
