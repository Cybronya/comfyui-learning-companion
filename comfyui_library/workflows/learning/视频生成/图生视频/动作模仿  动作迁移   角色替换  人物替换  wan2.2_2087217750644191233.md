---
key: 视频生成/图生视频/动作模仿  动作迁移   角色替换  人物替换  wan2.2_2087217750644191233.json
name: 动作模仿  动作迁移   角色替换  人物替换  wan2.2_2087217750644191233
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/动作模仿  动作迁移   角色替换  人物替换  wan2.2_2087217750644191233.json
hash: 29798fe989d4d53e
coverage: 1
learned_at: 2026-10-16 21:28:02
nodes: [WanVideoModelLoader, WanVideoTorchCompileSettings, WanVideoLoraSelectMulti, WanVideoSetBlockSwap, ImageConcatMulti, WanVideoDecode, WanVideoContextOptions, VHS_VideoCombine, LayerUtility: ImageScaleByAspectRatio V2, WanVideoSampler, WanVideoAnimateEmbeds, Evaluate Integers, WanVideoClipVisionEncode, WanVideoSetLoRAs, GetImageSizeAndCount, WanVideoBlockSwap, WanVideoTextEncodeCached, DrawViTPose, ImageConcatMulti, VHS_VideoCombine, SeCModelLoader, LayerUtility: ImageMaskScaleAsV2, ImageFromBatch, easy int, ClothesSegment, SeCVideoSegmentation, GrowMask, OnnxDetectionModelLoader, WanVideoVAELoader, CLIPVisionLoader, BlockifyMask, PoseAndFaceDetection, DrawMaskOnImage, ImageBlend, VHS_VideoCombine, VHS_LoadVideo, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/动作模仿  动作迁移   角色替换  人物替换  wan2.2_2087217750644191233.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/动作模仿  动作迁移   角色替换  人物替换  wan2.2_2087217750644191233.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（37 个）：
- `WanVideoModelLoader`
- `WanVideoTorchCompileSettings`
- `WanVideoLoraSelectMulti`
- `WanVideoSetBlockSwap`
- `ImageConcatMulti`
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
- `DrawViTPose`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `SeCModelLoader`
- `LayerUtility: ImageMaskScaleAsV2`
- `ImageFromBatch`
- `easy int`
- `ClothesSegment`
- `SeCVideoSegmentation`
- `GrowMask`
- `OnnxDetectionModelLoader`
- `WanVideoVAELoader`
- `CLIPVisionLoader`
- `BlockifyMask`
- `PoseAndFaceDetection`
- `DrawMaskOnImage`
- `ImageBlend`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `LoadImage`

## 知识

覆盖率 **100%**（37/37）

**有卡**：`WanVideoModelLoader`、`WanVideoTorchCompileSettings`、`WanVideoLoraSelectMulti`、`WanVideoSetBlockSwap`、`ImageConcatMulti`、`WanVideoDecode`、`WanVideoContextOptions`、`VHS_VideoCombine`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoSampler`、`WanVideoAnimateEmbeds`、`Evaluate Integers`、`WanVideoClipVisionEncode`、`WanVideoSetLoRAs`、`GetImageSizeAndCount`、`WanVideoBlockSwap`、`WanVideoTextEncodeCached`、`DrawViTPose`、`SeCModelLoader`、`LayerUtility: ImageMaskScaleAsV2`、`ImageFromBatch`、`easy int`、`ClothesSegment`、`SeCVideoSegmentation`、`GrowMask`、`OnnxDetectionModelLoader`、`WanVideoVAELoader`、`CLIPVisionLoader`、`BlockifyMask`、`PoseAndFaceDetection`、`DrawMaskOnImage`、`ImageBlend`、`VHS_LoadVideo`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
