---
key: 视频生成/图生视频/wan2.2动作迁移 角色替换  人物替换  动作模仿 复刻舞蹈_2082053141582929922.json
name: wan2.2动作迁移 角色替换  人物替换  动作模仿 复刻舞蹈_2082053141582929922.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.2动作迁移 角色替换  人物替换  动作模仿 复刻舞蹈_2082053141582929922.json
hash: fd4ff035a6043de4
coverage: 1
learned_at: 2026-10-15 22:42:27
nodes: [WanVideoModelLoader, WanVideoTorchCompileSettings, WanVideoLoraSelectMulti, WanVideoSetBlockSwap, WanVideoDecode, WanVideoContextOptions, VHS_VideoCombine, LayerUtility: ImageScaleByAspectRatio V2, WanVideoSampler, WanVideoAnimateEmbeds, Evaluate Integers, WanVideoClipVisionEncode, WanVideoSetLoRAs, GetImageSizeAndCount, WanVideoBlockSwap, WanVideoTextEncodeCached, ImageBlend, DrawViTPose, ImageConcatMulti, VHS_LoadVideo, LayerUtility: ImageMaskScaleAsV2, easy int, ImageFromBatch, VHS_VideoCombine, VHS_VideoCombine, ImageConcatMulti, ClothesSegment, SeCModelLoader, SeCVideoSegmentation, GrowMask, BlockifyMask, WanVideoVAELoader, OnnxDetectionModelLoader, DrawMaskOnImage, CLIPVisionLoader, PoseAndFaceDetection, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.2动作迁移 角色替换  人物替换  动作模仿 复刻舞蹈_2082053141582929922.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2082053141582929922.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（37 个）：
- `WanVideoModelLoader`
- `WanVideoTorchCompileSettings`
- `WanVideoLoraSelectMulti`
- `WanVideoSetBlockSwap`
- `WanVideoDecode`
- `WanVideoContextOptions`
- `VHS_VideoCombine`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoSampler` ★核心
- `WanVideoAnimateEmbeds`
- `Evaluate Integers`
- `WanVideoClipVisionEncode`
- `WanVideoSetLoRAs`
- `GetImageSizeAndCount`
- `WanVideoBlockSwap`
- `WanVideoTextEncodeCached`
- `ImageBlend`
- `DrawViTPose`
- `ImageConcatMulti`
- `VHS_LoadVideo`
- `LayerUtility: ImageMaskScaleAsV2`
- `easy int`
- `ImageFromBatch`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `ImageConcatMulti`
- `ClothesSegment`
- `SeCModelLoader`
- `SeCVideoSegmentation`
- `GrowMask`
- `BlockifyMask`
- `WanVideoVAELoader`
- `OnnxDetectionModelLoader`
- `DrawMaskOnImage`
- `CLIPVisionLoader`
- `PoseAndFaceDetection`
- `LoadImage`

## 知识

覆盖率 **100%**（37/37）

**有卡**：`WanVideoModelLoader`、`WanVideoTorchCompileSettings`、`WanVideoLoraSelectMulti`、`WanVideoSetBlockSwap`、`WanVideoDecode`、`WanVideoContextOptions`、`VHS_VideoCombine`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoSampler`、`WanVideoAnimateEmbeds`、`Evaluate Integers`、`WanVideoClipVisionEncode`、`WanVideoSetLoRAs`、`GetImageSizeAndCount`、`WanVideoBlockSwap`、`WanVideoTextEncodeCached`、`ImageBlend`、`DrawViTPose`、`ImageConcatMulti`、`VHS_LoadVideo`、`LayerUtility: ImageMaskScaleAsV2`、`easy int`、`ImageFromBatch`、`ClothesSegment`、`SeCModelLoader`、`SeCVideoSegmentation`、`GrowMask`、`BlockifyMask`、`WanVideoVAELoader`、`OnnxDetectionModelLoader`、`DrawMaskOnImage`、`CLIPVisionLoader`、`PoseAndFaceDetection`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
