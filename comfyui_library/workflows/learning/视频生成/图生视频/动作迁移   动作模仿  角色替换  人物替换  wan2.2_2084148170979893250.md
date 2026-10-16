---
key: 视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2084148170979893250.json
name: 动作迁移   动作模仿  角色替换  人物替换  wan2.2_2084148170979893250
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2084148170979893250.json
hash: b7b6815197c66290
coverage: 1
learned_at: 2026-10-16 19:52:29
nodes: [WanVideoModelLoader, WanVideoTorchCompileSettings, WanVideoSetBlockSwap, LayerUtility: ImageScaleByAspectRatio V2, WanVideoSampler, LayerUtility: ImageMaskScaleAsV2, WanVideoAnimateEmbeds, WanVideoSetLoRAs, WanVideoBlockSwap, WanVideoTextEncodeCached, ImageConcatMulti, VHS_VideoCombine, ImageFromBatch, VHS_VideoInfoLoaded, ClothesSegment, SeCVideoSegmentation, GrowMask, BlockifyMask, OnnxDetectionModelLoader, easy int, WanVideoVAELoader, SeCModelLoader, WanVideoClipVisionEncode, VHS_VideoCombine, PoseAndFaceDetection, DrawViTPose, Evaluate Integers, DrawMaskOnImage, WanVideoContextOptions, ImageBlend, WanVideoLoraSelectMulti, WanVideoDecode, LoadImage, CLIPVisionLoader, VHS_VideoCombine, VHS_VideoCombine, ImageConcatMulti, GetImageSizeAndCount, ImageConcatMulti, VHS_LoadVideo]
patterns: []
missing: []
---

# 视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2084148170979893250.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2084148170979893250.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（40 个）：
- `WanVideoModelLoader`
- `WanVideoTorchCompileSettings`
- `WanVideoSetBlockSwap`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoSampler` ★核心
- `LayerUtility: ImageMaskScaleAsV2`
- `WanVideoAnimateEmbeds`
- `WanVideoSetLoRAs`
- `WanVideoBlockSwap`
- `WanVideoTextEncodeCached`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `ImageFromBatch`
- `VHS_VideoInfoLoaded`
- `ClothesSegment`
- `SeCVideoSegmentation`
- `GrowMask`
- `BlockifyMask`
- `OnnxDetectionModelLoader`
- `easy int`
- `WanVideoVAELoader`
- `SeCModelLoader`
- `WanVideoClipVisionEncode`
- `VHS_VideoCombine`
- `PoseAndFaceDetection`
- `DrawViTPose`
- `Evaluate Integers`
- `DrawMaskOnImage`
- `WanVideoContextOptions`
- `ImageBlend`
- `WanVideoLoraSelectMulti`
- `WanVideoDecode`
- `LoadImage`
- `CLIPVisionLoader`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `ImageConcatMulti`
- `GetImageSizeAndCount`
- `ImageConcatMulti`
- `VHS_LoadVideo`

## 知识

覆盖率 **100%**（40/40）

**有卡**：`WanVideoModelLoader`、`WanVideoTorchCompileSettings`、`WanVideoSetBlockSwap`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoSampler`、`LayerUtility: ImageMaskScaleAsV2`、`WanVideoAnimateEmbeds`、`WanVideoSetLoRAs`、`WanVideoBlockSwap`、`WanVideoTextEncodeCached`、`ImageConcatMulti`、`VHS_VideoCombine`、`ImageFromBatch`、`VHS_VideoInfoLoaded`、`ClothesSegment`、`SeCVideoSegmentation`、`GrowMask`、`BlockifyMask`、`OnnxDetectionModelLoader`、`easy int`、`WanVideoVAELoader`、`SeCModelLoader`、`WanVideoClipVisionEncode`、`PoseAndFaceDetection`、`DrawViTPose`、`Evaluate Integers`、`DrawMaskOnImage`、`WanVideoContextOptions`、`ImageBlend`、`WanVideoLoraSelectMulti`、`WanVideoDecode`、`LoadImage`、`CLIPVisionLoader`、`GetImageSizeAndCount`、`VHS_LoadVideo`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
