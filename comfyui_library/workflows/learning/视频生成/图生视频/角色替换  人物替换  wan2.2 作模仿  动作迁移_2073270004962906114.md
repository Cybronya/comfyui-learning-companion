---
key: 视频生成/图生视频/角色替换  人物替换  wan2.2 作模仿  动作迁移_2073270004962906114.json
name: 角色替换  人物替换  wan2.2 作模仿  动作迁移_2073270004962906114.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/角色替换  人物替换  wan2.2 作模仿  动作迁移_2073270004962906114.json
hash: 9ad6d07b16a2dffd
coverage: 1
learned_at: 2026-10-15 22:41:01
nodes: [LayerUtility: ImageScaleByAspectRatio V2, LoadImage, VHS_LoadVideo, LayerUtility: ImageMaskScaleAsV2, VHS_VideoInfoLoaded, easy int, SeCModelLoader, ImageFromBatch, ClothesSegment, SeCVideoSegmentation, GrowMask, BlockifyMask, WanVideoVAELoader, OnnxDetectionModelLoader, PoseAndFaceDetection, DrawMaskOnImage, CLIPVisionLoader, WanVideoClipVisionEncode, VHS_VideoCombine, DrawViTPose, Evaluate Integers, WanVideoAnimateEmbeds, WanVideoContextOptions, ImageBlend, WanVideoTorchCompileSettings, WanVideoLoraSelectMulti, ImageConcatMulti, WanVideoModelLoader, WanVideoSetLoRAs, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoTextEncodeCached, WanVideoSampler, WanVideoDecode, ImageConcatMulti, VHS_VideoCombine, GetImageSizeAndCount, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/角色替换  人物替换  wan2.2 作模仿  动作迁移_2073270004962906114.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2073270004962906114.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（38 个）：
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `VHS_LoadVideo`
- `LayerUtility: ImageMaskScaleAsV2`
- `VHS_VideoInfoLoaded`
- `easy int`
- `SeCModelLoader`
- `ImageFromBatch`
- `ClothesSegment`
- `SeCVideoSegmentation`
- `GrowMask`
- `BlockifyMask`
- `WanVideoVAELoader`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `DrawMaskOnImage`
- `CLIPVisionLoader`
- `WanVideoClipVisionEncode`
- `VHS_VideoCombine`
- `DrawViTPose`
- `Evaluate Integers`
- `WanVideoAnimateEmbeds`
- `WanVideoContextOptions`
- `ImageBlend`
- `WanVideoTorchCompileSettings`
- `WanVideoLoraSelectMulti`
- `ImageConcatMulti`
- `WanVideoModelLoader`
- `WanVideoSetLoRAs`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoTextEncodeCached`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `GetImageSizeAndCount`
- `VHS_VideoCombine`

## 知识

覆盖率 **100%**（38/38）

**有卡**：`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`VHS_LoadVideo`、`LayerUtility: ImageMaskScaleAsV2`、`VHS_VideoInfoLoaded`、`easy int`、`SeCModelLoader`、`ImageFromBatch`、`ClothesSegment`、`SeCVideoSegmentation`、`GrowMask`、`BlockifyMask`、`WanVideoVAELoader`、`OnnxDetectionModelLoader`、`PoseAndFaceDetection`、`DrawMaskOnImage`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`VHS_VideoCombine`、`DrawViTPose`、`Evaluate Integers`、`WanVideoAnimateEmbeds`、`WanVideoContextOptions`、`ImageBlend`、`WanVideoTorchCompileSettings`、`WanVideoLoraSelectMulti`、`ImageConcatMulti`、`WanVideoModelLoader`、`WanVideoSetLoRAs`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`WanVideoTextEncodeCached`、`WanVideoSampler`、`WanVideoDecode`、`GetImageSizeAndCount`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
