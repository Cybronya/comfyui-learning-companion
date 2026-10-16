---
key: 视频生成/图生视频/动作迁移  动作模仿  人物替换  wan2.2_2068225775664451586.json
name: 动作迁移  动作模仿  人物替换  wan2.2_2068225775664451586.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2068225775664451586.json
hash: b92a49a404028206
coverage: 0.95
learned_at: 2026-10-15 22:40:17
nodes: [LayerUtility: ImageScaleByAspectRatio V2, VHS_VideoInfoLoaded, easy showAnything, easy int, GrowMask, BlockifyMask, PreviewImage, ImageConcatMulti, VHS_VideoCombine, VHS_VideoCombine, GetImageSizeAndCount, WanVideoDecode, WanVideoAnimateEmbeds, WanVideoSampler, WanVideoSetBlockSwap, WanVideoBlockSwap, WanVideoClipVisionEncode, CLIPVisionLoader, Evaluate Integers, WanVideoContextOptions, ImageConcatMulti, SeCModelLoader, ClothesSegment, ImageFromBatch, PoseAndFaceDetection, DrawMaskOnImage, DrawViTPose, ImageBlend, VHS_VideoCombine, VHS_LoadVideo, LoadImage, LayerUtility: ImageMaskScaleAsV2, SeCVideoSegmentation, OnnxDetectionModelLoader, WanVideoVAELoader, WanVideoTextEncodeCached, WanVideoModelLoader, WanVideoTorchCompileSettings, WanVideoSetLoRAs, WanVideoLoraSelectMulti]
patterns: []
missing: []
---

# 视频生成/图生视频/动作迁移  动作模仿  人物替换  wan2.2_2068225775664451586.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2068225775664451586.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（40 个）：
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
- `WanVideoAnimateEmbeds`
- `WanVideoSampler` ★核心
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `CLIPVisionLoader`
- `Evaluate Integers`
- `WanVideoContextOptions`
- `ImageConcatMulti`
- `SeCModelLoader`
- `ClothesSegment`
- `ImageFromBatch`
- `PoseAndFaceDetection`
- `DrawMaskOnImage`
- `DrawViTPose`
- `ImageBlend`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `LoadImage`
- `LayerUtility: ImageMaskScaleAsV2`
- `SeCVideoSegmentation`
- `OnnxDetectionModelLoader`
- `WanVideoVAELoader`
- `WanVideoTextEncodeCached`
- `WanVideoModelLoader`
- `WanVideoTorchCompileSettings`
- `WanVideoSetLoRAs`
- `WanVideoLoraSelectMulti`

## 知识

覆盖率 **95%**（38/40）

**有卡**：`LayerUtility: ImageScaleByAspectRatio V2`、`VHS_VideoInfoLoaded`、`easy int`、`GrowMask`、`BlockifyMask`、`ImageConcatMulti`、`VHS_VideoCombine`、`GetImageSizeAndCount`、`WanVideoDecode`、`WanVideoAnimateEmbeds`、`WanVideoSampler`、`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`WanVideoClipVisionEncode`、`CLIPVisionLoader`、`Evaluate Integers`、`WanVideoContextOptions`、`SeCModelLoader`、`ClothesSegment`、`ImageFromBatch`、`PoseAndFaceDetection`、`DrawMaskOnImage`、`DrawViTPose`、`ImageBlend`、`VHS_LoadVideo`、`LoadImage`、`LayerUtility: ImageMaskScaleAsV2`、`SeCVideoSegmentation`、`OnnxDetectionModelLoader`、`WanVideoVAELoader`、`WanVideoTextEncodeCached`、`WanVideoModelLoader`、`WanVideoTorchCompileSettings`、`WanVideoSetLoRAs`、`WanVideoLoraSelectMulti`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
