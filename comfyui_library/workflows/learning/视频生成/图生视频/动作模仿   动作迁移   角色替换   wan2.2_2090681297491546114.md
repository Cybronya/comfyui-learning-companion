---
key: 视频生成/图生视频/动作模仿   动作迁移   角色替换   wan2.2_2090681297491546114.json
name: 动作模仿   动作迁移   角色替换   wan2.2_2090681297491546114
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/动作模仿   动作迁移   角色替换   wan2.2_2090681297491546114.json
hash: 4e47aacbb7b0b691
coverage: 1
learned_at: 2026-10-16 22:30:59
nodes: [WanVideoSetBlockSwap, LayerUtility: ImageScaleByAspectRatio V2, WanVideoSetLoRAs, WanVideoBlockSwap, VHS_LoadVideo, LoadImage, LayerUtility: ImageMaskScaleAsV2, ClothesSegment, SeCVideoSegmentation, GrowMask, ImageFromBatch, WanVideoVAELoader, VHS_VideoInfoLoaded, easy int, SeCModelLoader, OnnxDetectionModelLoader, PoseAndFaceDetection, BlockifyMask, DrawMaskOnImage, CLIPVisionLoader, WanVideoClipVisionEncode, VHS_VideoCombine, Evaluate Integers, DrawViTPose, WanVideoAnimateEmbeds, WanVideoTorchCompileSettings, WanVideoModelLoader, WanVideoContextOptions, WanVideoLoraSelectMulti, WanVideoTextEncodeCached, WanVideoSampler, WanVideoDecode, GetImageSizeAndCount, ImageConcatMulti, ImageBlend, ImageConcatMulti, VHS_VideoCombine, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/动作模仿   动作迁移   角色替换   wan2.2_2090681297491546114.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/动作模仿   动作迁移   角色替换   wan2.2_2090681297491546114.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（38 个）：
- `WanVideoSetBlockSwap`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoSetLoRAs`
- `WanVideoBlockSwap`
- `VHS_LoadVideo`
- `LoadImage`
- `LayerUtility: ImageMaskScaleAsV2`
- `ClothesSegment`
- `SeCVideoSegmentation`
- `GrowMask`
- `ImageFromBatch`
- `WanVideoVAELoader`
- `VHS_VideoInfoLoaded`
- `easy int`
- `SeCModelLoader`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `BlockifyMask`
- `DrawMaskOnImage`
- `CLIPVisionLoader`
- `WanVideoClipVisionEncode`
- `VHS_VideoCombine`
- `Evaluate Integers`
- `DrawViTPose`
- `WanVideoAnimateEmbeds`
- `WanVideoTorchCompileSettings`
- `WanVideoModelLoader`
- `WanVideoContextOptions`
- `WanVideoLoraSelectMulti`
- `WanVideoTextEncodeCached`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `ImageConcatMulti`
- `ImageBlend`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `VHS_VideoCombine`

## 知识

覆盖率 **100%**（38/38）

**有卡**：`WanVideoSetBlockSwap`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoSetLoRAs`、`WanVideoBlockSwap`、`VHS_LoadVideo`、`LoadImage`、`LayerUtility: ImageMaskScaleAsV2`、`ClothesSegment`、`SeCVideoSegmentation`、`GrowMask`、`ImageFromBatch`、`WanVideoVAELoader`、`VHS_VideoInfoLoaded`、`easy int`、`SeCModelLoader`、`OnnxDetectionModelLoader`、`PoseAndFaceDetection`、`BlockifyMask`、`DrawMaskOnImage`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`VHS_VideoCombine`、`Evaluate Integers`、`DrawViTPose`、`WanVideoAnimateEmbeds`、`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`WanVideoContextOptions`、`WanVideoLoraSelectMulti`、`WanVideoTextEncodeCached`、`WanVideoSampler`、`WanVideoDecode`、`GetImageSizeAndCount`、`ImageConcatMulti`、`ImageBlend`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
