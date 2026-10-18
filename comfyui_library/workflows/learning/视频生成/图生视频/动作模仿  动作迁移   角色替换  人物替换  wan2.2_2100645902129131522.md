---
key: 视频生成/图生视频/动作模仿  动作迁移   角色替换  人物替换  wan2.2_2100645902129131522.json
name: 动作模仿  动作迁移   角色替换  人物替换  wan2.2_2100645902129131522
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/动作模仿  动作迁移   角色替换  人物替换  wan2.2_2100645902129131522.json
hash: d8a1a3da229ab0c8
coverage: 1
learned_at: 2026-10-17 02:14:56
nodes: [WanVideoSetBlockSwap, WanVideoDecode, LayerUtility: ImageScaleByAspectRatio V2, WanVideoSetLoRAs, GetImageSizeAndCount, WanVideoBlockSwap, WanVideoTextEncodeCached, DrawViTPose, VHS_VideoCombine, easy int, SeCModelLoader, LayerUtility: ImageMaskScaleAsV2, ClothesSegment, ImageFromBatch, SeCVideoSegmentation, GrowMask, BlockifyMask, DrawMaskOnImage, WanVideoVAELoader, OnnxDetectionModelLoader, PoseAndFaceDetection, VHS_VideoCombine, CLIPVisionLoader, WanVideoClipVisionEncode, Evaluate Integers, ImageBlend, WanVideoContextOptions, WanVideoAnimateEmbeds, WanVideoTorchCompileSettings, WanVideoModelLoader, WanVideoLoraSelectMulti, ImageConcatMulti, ImageConcatMulti, WanVideoSampler, VHS_VideoCombine, LoadImage, VHS_LoadVideo]
patterns: []
missing: []
---

# 视频生成/图生视频/动作模仿  动作迁移   角色替换  人物替换  wan2.2_2100645902129131522.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/动作模仿  动作迁移   角色替换  人物替换  wan2.2_2100645902129131522.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（37 个）：
- `WanVideoSetBlockSwap`
- `WanVideoDecode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoSetLoRAs`
- `GetImageSizeAndCount`
- `WanVideoBlockSwap`
- `WanVideoTextEncodeCached`
- `DrawViTPose`
- `VHS_VideoCombine`
- `easy int`
- `SeCModelLoader`
- `LayerUtility: ImageMaskScaleAsV2`
- `ClothesSegment`
- `ImageFromBatch`
- `SeCVideoSegmentation`
- `GrowMask`
- `BlockifyMask`
- `DrawMaskOnImage`
- `WanVideoVAELoader`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `VHS_VideoCombine`
- `CLIPVisionLoader`
- `WanVideoClipVisionEncode`
- `Evaluate Integers`
- `ImageBlend`
- `WanVideoContextOptions`
- `WanVideoAnimateEmbeds`
- `WanVideoTorchCompileSettings`
- `WanVideoModelLoader`
- `WanVideoLoraSelectMulti`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `WanVideoSampler` ★核心
- `VHS_VideoCombine`
- `LoadImage`
- `VHS_LoadVideo`

## 知识

覆盖率 **100%**（37/37）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoDecode`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoSetLoRAs`、`GetImageSizeAndCount`、`WanVideoBlockSwap`、`WanVideoTextEncodeCached`、`DrawViTPose`、`VHS_VideoCombine`、`easy int`、`SeCModelLoader`、`LayerUtility: ImageMaskScaleAsV2`、`ClothesSegment`、`ImageFromBatch`、`SeCVideoSegmentation`、`GrowMask`、`BlockifyMask`、`DrawMaskOnImage`、`WanVideoVAELoader`、`OnnxDetectionModelLoader`、`PoseAndFaceDetection`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`Evaluate Integers`、`ImageBlend`、`WanVideoContextOptions`、`WanVideoAnimateEmbeds`、`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`ImageConcatMulti`、`WanVideoSampler`、`LoadImage`、`VHS_LoadVideo`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
