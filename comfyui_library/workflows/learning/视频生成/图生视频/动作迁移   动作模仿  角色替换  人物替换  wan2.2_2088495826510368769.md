---
key: 视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2088495826510368769.json
name: 动作迁移   动作模仿  角色替换  人物替换  wan2.2_2088495826510368769
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2088495826510368769.json
hash: 7e783ed80529abbf
coverage: 1
learned_at: 2026-10-16 21:43:48
nodes: [WanVideoTorchCompileSettings, WanVideoAnimateEmbeds, Evaluate Integers, DrawViTPose, ImageConcatMulti, ImageConcatMulti, ImageBlend, VHS_VideoCombine, WanVideoLoraSelectMulti, WanVideoTextEncodeCached, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoDecode, GetImageSizeAndCount, WanVideoSampler, WanVideoContextOptions, LayerUtility: ImageMaskScaleAsV2, easy int, ClothesSegment, ImageFromBatch, SeCModelLoader, OnnxDetectionModelLoader, WanVideoVAELoader, SeCVideoSegmentation, DrawMaskOnImage, BlockifyMask, GrowMask, CLIPVisionLoader, PoseAndFaceDetection, WanVideoClipVisionEncode, WanVideoBlockSwap, VHS_VideoCombine, LoadImage, VHS_LoadVideo, LayerUtility: ImageScaleByAspectRatio V2, WanVideoModelLoader, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2088495826510368769.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2088495826510368769.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（37 个）：
- `WanVideoTorchCompileSettings`
- `WanVideoAnimateEmbeds`
- `Evaluate Integers`
- `DrawViTPose`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `ImageBlend`
- `VHS_VideoCombine`
- `WanVideoLoraSelectMulti`
- `WanVideoTextEncodeCached`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `WanVideoSampler` ★核心
- `WanVideoContextOptions`
- `LayerUtility: ImageMaskScaleAsV2`
- `easy int`
- `ClothesSegment`
- `ImageFromBatch`
- `SeCModelLoader`
- `OnnxDetectionModelLoader`
- `WanVideoVAELoader`
- `SeCVideoSegmentation`
- `DrawMaskOnImage`
- `BlockifyMask`
- `GrowMask`
- `CLIPVisionLoader`
- `PoseAndFaceDetection`
- `WanVideoClipVisionEncode`
- `WanVideoBlockSwap`
- `VHS_VideoCombine`
- `LoadImage`
- `VHS_LoadVideo`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoModelLoader`
- `VHS_VideoCombine`

## 知识

覆盖率 **100%**（37/37）

**有卡**：`WanVideoTorchCompileSettings`、`WanVideoAnimateEmbeds`、`Evaluate Integers`、`DrawViTPose`、`ImageConcatMulti`、`ImageBlend`、`VHS_VideoCombine`、`WanVideoLoraSelectMulti`、`WanVideoTextEncodeCached`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`WanVideoDecode`、`GetImageSizeAndCount`、`WanVideoSampler`、`WanVideoContextOptions`、`LayerUtility: ImageMaskScaleAsV2`、`easy int`、`ClothesSegment`、`ImageFromBatch`、`SeCModelLoader`、`OnnxDetectionModelLoader`、`WanVideoVAELoader`、`SeCVideoSegmentation`、`DrawMaskOnImage`、`BlockifyMask`、`GrowMask`、`CLIPVisionLoader`、`PoseAndFaceDetection`、`WanVideoClipVisionEncode`、`WanVideoBlockSwap`、`LoadImage`、`VHS_LoadVideo`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoModelLoader`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
