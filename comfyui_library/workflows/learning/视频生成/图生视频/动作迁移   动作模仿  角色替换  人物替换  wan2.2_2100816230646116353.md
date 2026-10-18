---
key: 视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2100816230646116353.json
name: 动作迁移   动作模仿  角色替换  人物替换  wan2.2_2100816230646116353
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2100816230646116353.json
hash: e588812282fb720d
coverage: 1
learned_at: 2026-10-17 02:14:57
nodes: [WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoBlockSwap, LayerUtility: ImageMaskScaleAsV2, easy int, ClothesSegment, ImageFromBatch, GrowMask, WanVideoVAELoader, OnnxDetectionModelLoader, DrawMaskOnImage, CLIPVisionLoader, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoTorchCompileSettings, WanVideoModelLoader, WanVideoSampler, WanVideoDecode, ImageConcatMulti, VHS_VideoCombine, VHS_VideoCombine, WanVideoLoraSelectMulti, ImageBlend, WanVideoTextEncodeCached, ImageConcatMulti, GetImageSizeAndCount, SeCVideoSegmentation, SeCModelLoader, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, VHS_LoadVideo, Evaluate Integers, DrawViTPose, WanVideoClipVisionEncode, WanVideoContextOptions, BlockifyMask, PoseAndFaceDetection]
patterns: []
missing: []
---

# 视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2100816230646116353.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2100816230646116353.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（37 个）：
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoBlockSwap`
- `LayerUtility: ImageMaskScaleAsV2`
- `easy int`
- `ClothesSegment`
- `ImageFromBatch`
- `GrowMask`
- `WanVideoVAELoader`
- `OnnxDetectionModelLoader`
- `DrawMaskOnImage`
- `CLIPVisionLoader`
- `VHS_VideoCombine`
- `WanVideoAnimateEmbeds`
- `WanVideoTorchCompileSettings`
- `WanVideoModelLoader`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `WanVideoLoraSelectMulti`
- `ImageBlend`
- `WanVideoTextEncodeCached`
- `ImageConcatMulti`
- `GetImageSizeAndCount`
- `SeCVideoSegmentation`
- `SeCModelLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `VHS_LoadVideo`
- `Evaluate Integers`
- `DrawViTPose`
- `WanVideoClipVisionEncode`
- `WanVideoContextOptions`
- `BlockifyMask`
- `PoseAndFaceDetection`

## 知识

覆盖率 **100%**（37/37）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoBlockSwap`、`LayerUtility: ImageMaskScaleAsV2`、`easy int`、`ClothesSegment`、`ImageFromBatch`、`GrowMask`、`WanVideoVAELoader`、`OnnxDetectionModelLoader`、`DrawMaskOnImage`、`CLIPVisionLoader`、`VHS_VideoCombine`、`WanVideoAnimateEmbeds`、`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`WanVideoSampler`、`WanVideoDecode`、`ImageConcatMulti`、`WanVideoLoraSelectMulti`、`ImageBlend`、`WanVideoTextEncodeCached`、`GetImageSizeAndCount`、`SeCVideoSegmentation`、`SeCModelLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`VHS_LoadVideo`、`Evaluate Integers`、`DrawViTPose`、`WanVideoClipVisionEncode`、`WanVideoContextOptions`、`BlockifyMask`、`PoseAndFaceDetection`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
