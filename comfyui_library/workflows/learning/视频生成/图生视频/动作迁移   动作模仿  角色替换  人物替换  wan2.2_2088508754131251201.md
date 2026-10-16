---
key: 视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2088508754131251201.json
name: 动作迁移   动作模仿  角色替换  人物替换  wan2.2_2088508754131251201
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2088508754131251201.json
hash: d5566a1d2f08c0e4
coverage: 1
learned_at: 2026-10-16 21:43:48
nodes: [WanVideoModelLoader, WanVideoTorchCompileSettings, WanVideoLoraSelectMulti, WanVideoSetBlockSwap, WanVideoDecode, WanVideoContextOptions, PoseAndFaceDetection, VHS_VideoCombine, OnnxDetectionModelLoader, WanVideoSampler, WanVideoVAELoader, WanVideoAnimateEmbeds, Evaluate Integers, WanVideoClipVisionEncode, WanVideoSetLoRAs, GetImageSizeAndCount, WanVideoBlockSwap, WanVideoTextEncodeCached, DrawViTPose, VHS_VideoCombine, ImageConcatMulti, ImageConcatMulti, ImageBlend, VHS_VideoCombine, SeCVideoSegmentation, SeCModelLoader, GrowMask, ClothesSegment, LayerUtility: ImageScaleByAspectRatio V2, VHS_VideoInfoLoaded, LayerUtility: ImageMaskScaleAsV2, easy int, ImageFromBatch, BlockifyMask, DrawMaskOnImage, CLIPVisionLoader, VHS_LoadVideo, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2088508754131251201.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2088508754131251201.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（38 个）：
- `WanVideoModelLoader`
- `WanVideoTorchCompileSettings`
- `WanVideoLoraSelectMulti`
- `WanVideoSetBlockSwap`
- `WanVideoDecode`
- `WanVideoContextOptions`
- `PoseAndFaceDetection`
- `VHS_VideoCombine`
- `OnnxDetectionModelLoader`
- `WanVideoSampler` ★核心
- `WanVideoVAELoader`
- `WanVideoAnimateEmbeds`
- `Evaluate Integers`
- `WanVideoClipVisionEncode`
- `WanVideoSetLoRAs`
- `GetImageSizeAndCount`
- `WanVideoBlockSwap`
- `WanVideoTextEncodeCached`
- `DrawViTPose`
- `VHS_VideoCombine`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `ImageBlend`
- `VHS_VideoCombine`
- `SeCVideoSegmentation`
- `SeCModelLoader`
- `GrowMask`
- `ClothesSegment`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VHS_VideoInfoLoaded`
- `LayerUtility: ImageMaskScaleAsV2`
- `easy int`
- `ImageFromBatch`
- `BlockifyMask`
- `DrawMaskOnImage`
- `CLIPVisionLoader`
- `VHS_LoadVideo`
- `LoadImage`

## 知识

覆盖率 **100%**（38/38）

**有卡**：`WanVideoModelLoader`、`WanVideoTorchCompileSettings`、`WanVideoLoraSelectMulti`、`WanVideoSetBlockSwap`、`WanVideoDecode`、`WanVideoContextOptions`、`PoseAndFaceDetection`、`VHS_VideoCombine`、`OnnxDetectionModelLoader`、`WanVideoSampler`、`WanVideoVAELoader`、`WanVideoAnimateEmbeds`、`Evaluate Integers`、`WanVideoClipVisionEncode`、`WanVideoSetLoRAs`、`GetImageSizeAndCount`、`WanVideoBlockSwap`、`WanVideoTextEncodeCached`、`DrawViTPose`、`ImageConcatMulti`、`ImageBlend`、`SeCVideoSegmentation`、`SeCModelLoader`、`GrowMask`、`ClothesSegment`、`LayerUtility: ImageScaleByAspectRatio V2`、`VHS_VideoInfoLoaded`、`LayerUtility: ImageMaskScaleAsV2`、`easy int`、`ImageFromBatch`、`BlockifyMask`、`DrawMaskOnImage`、`CLIPVisionLoader`、`VHS_LoadVideo`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
