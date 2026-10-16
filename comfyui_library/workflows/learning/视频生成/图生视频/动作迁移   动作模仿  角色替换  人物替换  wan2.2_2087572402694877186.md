---
key: 视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2087572402694877186.json
name: 动作迁移   动作模仿  角色替换  人物替换  wan2.2_2087572402694877186
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2087572402694877186.json
hash: d21380a2c90470b4
coverage: 1
learned_at: 2026-10-16 21:28:03
nodes: [WanVideoModelLoader, WanVideoTorchCompileSettings, WanVideoSetBlockSwap, LayerUtility: ImageScaleByAspectRatio V2, WanVideoSampler, LayerUtility: ImageMaskScaleAsV2, WanVideoAnimateEmbeds, WanVideoSetLoRAs, WanVideoBlockSwap, WanVideoTextEncodeCached, ImageConcatMulti, VHS_VideoCombine, ImageFromBatch, VHS_VideoInfoLoaded, ClothesSegment, SeCVideoSegmentation, GrowMask, BlockifyMask, OnnxDetectionModelLoader, easy int, SeCModelLoader, WanVideoClipVisionEncode, VHS_VideoCombine, PoseAndFaceDetection, DrawViTPose, Evaluate Integers, DrawMaskOnImage, WanVideoLoraSelectMulti, WanVideoDecode, VHS_VideoCombine, GetImageSizeAndCount, VHS_LoadVideo, LoadImage, ImageConcatMulti, ImageConcatMulti, WanVideoVAELoader, CLIPVisionLoader, WanVideoContextOptions, ImageBlend, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2087572402694877186.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2087572402694877186.json`

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
- `SeCModelLoader`
- `WanVideoClipVisionEncode`
- `VHS_VideoCombine`
- `PoseAndFaceDetection`
- `DrawViTPose`
- `Evaluate Integers`
- `DrawMaskOnImage`
- `WanVideoLoraSelectMulti`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `GetImageSizeAndCount`
- `VHS_LoadVideo`
- `LoadImage`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `WanVideoVAELoader`
- `CLIPVisionLoader`
- `WanVideoContextOptions`
- `ImageBlend`
- `VHS_VideoCombine`

## 知识

覆盖率 **100%**（40/40）

**有卡**：`WanVideoModelLoader`、`WanVideoTorchCompileSettings`、`WanVideoSetBlockSwap`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoSampler`、`LayerUtility: ImageMaskScaleAsV2`、`WanVideoAnimateEmbeds`、`WanVideoSetLoRAs`、`WanVideoBlockSwap`、`WanVideoTextEncodeCached`、`ImageConcatMulti`、`VHS_VideoCombine`、`ImageFromBatch`、`VHS_VideoInfoLoaded`、`ClothesSegment`、`SeCVideoSegmentation`、`GrowMask`、`BlockifyMask`、`OnnxDetectionModelLoader`、`easy int`、`SeCModelLoader`、`WanVideoClipVisionEncode`、`PoseAndFaceDetection`、`DrawViTPose`、`Evaluate Integers`、`DrawMaskOnImage`、`WanVideoLoraSelectMulti`、`WanVideoDecode`、`GetImageSizeAndCount`、`VHS_LoadVideo`、`LoadImage`、`WanVideoVAELoader`、`CLIPVisionLoader`、`WanVideoContextOptions`、`ImageBlend`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
