---
key: 视频生成/图生视频/动作模仿  动作迁移  人物替换  wan2.2_2062567605399019522.json
name: 动作模仿  动作迁移  人物替换  wan2.2_2062567605399019522.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/动作模仿  动作迁移  人物替换  wan2.2_2062567605399019522.json
hash: 64c39b8c42aacea7
coverage: 0.95
learned_at: 2026-10-15 22:39:05
nodes: [WanVideoContextOptions, Evaluate Integers, ImageConcatMulti, VHS_LoadVideo, LayerUtility: ImageMaskScaleAsV2, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, ImageFromBatch, easy int, SeCVideoSegmentation, PreviewImage, VHS_VideoInfoLoaded, DrawViTPose, WanVideoSetBlockSwap, WanVideoBlockSwap, CLIPVisionLoader, ImageBlend, LoadImage, WanVideoModelLoader, WanVideoTorchCompileSettings, WanVideoSetLoRAs, WanVideoSampler, WanVideoAnimateEmbeds, WanVideoVAELoader, VHS_VideoCombine, DrawMaskOnImage, GrowMask, BlockifyMask, PoseAndFaceDetection, OnnxDetectionModelLoader, WanVideoTextEncodeCached, SeCModelLoader, ClothesSegment, WanVideoLoraSelectMulti, WanVideoClipVisionEncode, WanVideoDecode, GetImageSizeAndCount, VHS_VideoCombine, ImageConcatMulti, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/动作模仿  动作迁移  人物替换  wan2.2_2062567605399019522.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2062567605399019522.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（40 个）：
- `WanVideoContextOptions`
- `Evaluate Integers`
- `ImageConcatMulti`
- `VHS_LoadVideo`
- `LayerUtility: ImageMaskScaleAsV2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewImage`
- `ImageFromBatch`
- `easy int`
- `SeCVideoSegmentation`
- `PreviewImage`
- `VHS_VideoInfoLoaded`
- `DrawViTPose`
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `CLIPVisionLoader`
- `ImageBlend`
- `LoadImage`
- `WanVideoModelLoader`
- `WanVideoTorchCompileSettings`
- `WanVideoSetLoRAs`
- `WanVideoSampler` ★核心
- `WanVideoAnimateEmbeds`
- `WanVideoVAELoader`
- `VHS_VideoCombine`
- `DrawMaskOnImage`
- `GrowMask`
- `BlockifyMask`
- `PoseAndFaceDetection`
- `OnnxDetectionModelLoader`
- `WanVideoTextEncodeCached`
- `SeCModelLoader`
- `ClothesSegment`
- `WanVideoLoraSelectMulti`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `ImageConcatMulti`
- `VHS_VideoCombine`

## 知识

覆盖率 **95%**（38/40）

**有卡**：`WanVideoContextOptions`、`Evaluate Integers`、`ImageConcatMulti`、`VHS_LoadVideo`、`LayerUtility: ImageMaskScaleAsV2`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageFromBatch`、`easy int`、`SeCVideoSegmentation`、`VHS_VideoInfoLoaded`、`DrawViTPose`、`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`CLIPVisionLoader`、`ImageBlend`、`LoadImage`、`WanVideoModelLoader`、`WanVideoTorchCompileSettings`、`WanVideoSetLoRAs`、`WanVideoSampler`、`WanVideoAnimateEmbeds`、`WanVideoVAELoader`、`VHS_VideoCombine`、`DrawMaskOnImage`、`GrowMask`、`BlockifyMask`、`PoseAndFaceDetection`、`OnnxDetectionModelLoader`、`WanVideoTextEncodeCached`、`SeCModelLoader`、`ClothesSegment`、`WanVideoLoraSelectMulti`、`WanVideoClipVisionEncode`、`WanVideoDecode`、`GetImageSizeAndCount`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
