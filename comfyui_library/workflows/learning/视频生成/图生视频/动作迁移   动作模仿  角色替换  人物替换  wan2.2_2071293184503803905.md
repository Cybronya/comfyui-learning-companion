---
key: 视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2071293184503803905.json
name: 动作迁移   动作模仿  角色替换  人物替换  wan2.2_2071293184503803905.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2071293184503803905.json
hash: bfc00597cdc7bdfa
coverage: 0.974359
learned_at: 2026-10-15 22:40:44
nodes: [WanVideoModelLoader, WanVideoTorchCompileSettings, WanVideoSetBlockSwap, ImageConcatMulti, WanVideoDecode, LayerUtility: ImageScaleByAspectRatio V2, WanVideoSampler, WanVideoAnimateEmbeds, WanVideoClipVisionEncode, WanVideoSetLoRAs, GetImageSizeAndCount, WanVideoBlockSwap, WanVideoTextEncodeCached, VHS_VideoCombine, DrawViTPose, VHS_VideoCombine, LoadImage, LayerUtility: ImageMaskScaleAsV2, ImageFromBatch, easy int, easy showAnything, VHS_LoadVideo, VHS_VideoInfoLoaded, ClothesSegment, SeCModelLoader, SeCVideoSegmentation, WanVideoVAELoader, CLIPVisionLoader, OnnxDetectionModelLoader, PoseAndFaceDetection, GrowMask, BlockifyMask, DrawMaskOnImage, VHS_VideoCombine, Evaluate Integers, WanVideoContextOptions, ImageBlend, ImageConcatMulti, WanVideoLoraSelectMulti]
patterns: []
missing: []
---

# 视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2071293184503803905.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2071293184503803905.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（39 个）：
- `WanVideoModelLoader`
- `WanVideoTorchCompileSettings`
- `WanVideoSetBlockSwap`
- `ImageConcatMulti`
- `WanVideoDecode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoSampler` ★核心
- `WanVideoAnimateEmbeds`
- `WanVideoClipVisionEncode`
- `WanVideoSetLoRAs`
- `GetImageSizeAndCount`
- `WanVideoBlockSwap`
- `WanVideoTextEncodeCached`
- `VHS_VideoCombine`
- `DrawViTPose`
- `VHS_VideoCombine`
- `LoadImage`
- `LayerUtility: ImageMaskScaleAsV2`
- `ImageFromBatch`
- `easy int`
- `easy showAnything`
- `VHS_LoadVideo`
- `VHS_VideoInfoLoaded`
- `ClothesSegment`
- `SeCModelLoader`
- `SeCVideoSegmentation`
- `WanVideoVAELoader`
- `CLIPVisionLoader`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `GrowMask`
- `BlockifyMask`
- `DrawMaskOnImage`
- `VHS_VideoCombine`
- `Evaluate Integers`
- `WanVideoContextOptions`
- `ImageBlend`
- `ImageConcatMulti`
- `WanVideoLoraSelectMulti`

## 知识

覆盖率 **97%**（38/39）

**有卡**：`WanVideoModelLoader`、`WanVideoTorchCompileSettings`、`WanVideoSetBlockSwap`、`ImageConcatMulti`、`WanVideoDecode`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoSampler`、`WanVideoAnimateEmbeds`、`WanVideoClipVisionEncode`、`WanVideoSetLoRAs`、`GetImageSizeAndCount`、`WanVideoBlockSwap`、`WanVideoTextEncodeCached`、`VHS_VideoCombine`、`DrawViTPose`、`LoadImage`、`LayerUtility: ImageMaskScaleAsV2`、`ImageFromBatch`、`easy int`、`VHS_LoadVideo`、`VHS_VideoInfoLoaded`、`ClothesSegment`、`SeCModelLoader`、`SeCVideoSegmentation`、`WanVideoVAELoader`、`CLIPVisionLoader`、`OnnxDetectionModelLoader`、`PoseAndFaceDetection`、`GrowMask`、`BlockifyMask`、`DrawMaskOnImage`、`Evaluate Integers`、`WanVideoContextOptions`、`ImageBlend`、`WanVideoLoraSelectMulti`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
