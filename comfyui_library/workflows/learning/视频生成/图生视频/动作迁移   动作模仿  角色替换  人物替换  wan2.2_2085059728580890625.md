---
key: 视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2085059728580890625.json
name: 动作迁移   动作模仿  角色替换  人物替换  wan2.2_2085059728580890625
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2085059728580890625.json
hash: c2a610f3f3f97f0c
coverage: 1
learned_at: 2026-10-16 20:50:50
nodes: [WanVideoModelLoader, WanVideoSetBlockSwap, WanVideoDecode, LayerUtility: ImageScaleByAspectRatio V2, WanVideoSampler, WanVideoSetLoRAs, GetImageSizeAndCount, WanVideoBlockSwap, WanVideoTextEncodeCached, ImageConcatMulti, ImageFromBatch, SeCVideoSegmentation, ClothesSegment, GrowMask, BlockifyMask, WanVideoVAELoader, OnnxDetectionModelLoader, PoseAndFaceDetection, DrawMaskOnImage, CLIPVisionLoader, VHS_VideoCombine, WanVideoClipVisionEncode, Evaluate Integers, DrawViTPose, ImageBlend, WanVideoContextOptions, WanVideoLoraSelectMulti, WanVideoAnimateEmbeds, WanVideoTorchCompileSettings, ImageConcatMulti, VHS_VideoCombine, VHS_VideoCombine, SeCModelLoader, LayerUtility: ImageMaskScaleAsV2, LoadImage, VHS_LoadVideo]
patterns: []
missing: []
---

# 视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2085059728580890625.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2085059728580890625.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（36 个）：
- `WanVideoModelLoader`
- `WanVideoSetBlockSwap`
- `WanVideoDecode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoSampler` ★核心
- `WanVideoSetLoRAs`
- `GetImageSizeAndCount`
- `WanVideoBlockSwap`
- `WanVideoTextEncodeCached`
- `ImageConcatMulti`
- `ImageFromBatch`
- `SeCVideoSegmentation`
- `ClothesSegment`
- `GrowMask`
- `BlockifyMask`
- `WanVideoVAELoader`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `DrawMaskOnImage`
- `CLIPVisionLoader`
- `VHS_VideoCombine`
- `WanVideoClipVisionEncode`
- `Evaluate Integers`
- `DrawViTPose`
- `ImageBlend`
- `WanVideoContextOptions`
- `WanVideoLoraSelectMulti`
- `WanVideoAnimateEmbeds`
- `WanVideoTorchCompileSettings`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `SeCModelLoader`
- `LayerUtility: ImageMaskScaleAsV2`
- `LoadImage`
- `VHS_LoadVideo`

## 知识

覆盖率 **100%**（36/36）

**有卡**：`WanVideoModelLoader`、`WanVideoSetBlockSwap`、`WanVideoDecode`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoSampler`、`WanVideoSetLoRAs`、`GetImageSizeAndCount`、`WanVideoBlockSwap`、`WanVideoTextEncodeCached`、`ImageConcatMulti`、`ImageFromBatch`、`SeCVideoSegmentation`、`ClothesSegment`、`GrowMask`、`BlockifyMask`、`WanVideoVAELoader`、`OnnxDetectionModelLoader`、`PoseAndFaceDetection`、`DrawMaskOnImage`、`CLIPVisionLoader`、`VHS_VideoCombine`、`WanVideoClipVisionEncode`、`Evaluate Integers`、`DrawViTPose`、`ImageBlend`、`WanVideoContextOptions`、`WanVideoLoraSelectMulti`、`WanVideoAnimateEmbeds`、`WanVideoTorchCompileSettings`、`SeCModelLoader`、`LayerUtility: ImageMaskScaleAsV2`、`LoadImage`、`VHS_LoadVideo`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
