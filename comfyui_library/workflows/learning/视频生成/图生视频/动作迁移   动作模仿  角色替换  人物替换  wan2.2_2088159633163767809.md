---
key: 视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2088159633163767809.json
name: 动作迁移   动作模仿  角色替换  人物替换  wan2.2_2088159633163767809
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2088159633163767809.json
hash: a435149f038ad122
coverage: 1
learned_at: 2026-10-16 21:28:03
nodes: [WanVideoModelLoader, WanVideoTorchCompileSettings, WanVideoLoraSelectMulti, WanVideoSetBlockSwap, WanVideoDecode, LayerUtility: ImageScaleByAspectRatio V2, WanVideoSampler, WanVideoAnimateEmbeds, Evaluate Integers, WanVideoClipVisionEncode, WanVideoSetLoRAs, GetImageSizeAndCount, WanVideoBlockSwap, WanVideoTextEncodeCached, DrawViTPose, LoadImage, VHS_VideoCombine, VHS_VideoCombine, ImageConcatMulti, ImageConcatMulti, WanVideoContextOptions, ImageBlend, LayerUtility: ImageMaskScaleAsV2, ImageFromBatch, VHS_LoadVideo, easy int, SeCVideoSegmentation, GrowMask, BlockifyMask, VHS_VideoInfoLoaded, SeCModelLoader, OnnxDetectionModelLoader, DrawMaskOnImage, PoseAndFaceDetection, WanVideoVAELoader, CLIPVisionLoader, VHS_VideoCombine, ClothesSegment]
patterns: []
missing: []
---

# 视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2088159633163767809.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2088159633163767809.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（38 个）：
- `WanVideoModelLoader`
- `WanVideoTorchCompileSettings`
- `WanVideoLoraSelectMulti`
- `WanVideoSetBlockSwap`
- `WanVideoDecode`
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
- `LoadImage`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `WanVideoContextOptions`
- `ImageBlend`
- `LayerUtility: ImageMaskScaleAsV2`
- `ImageFromBatch`
- `VHS_LoadVideo`
- `easy int`
- `SeCVideoSegmentation`
- `GrowMask`
- `BlockifyMask`
- `VHS_VideoInfoLoaded`
- `SeCModelLoader`
- `OnnxDetectionModelLoader`
- `DrawMaskOnImage`
- `PoseAndFaceDetection`
- `WanVideoVAELoader`
- `CLIPVisionLoader`
- `VHS_VideoCombine`
- `ClothesSegment`

## 知识

覆盖率 **100%**（38/38）

**有卡**：`WanVideoModelLoader`、`WanVideoTorchCompileSettings`、`WanVideoLoraSelectMulti`、`WanVideoSetBlockSwap`、`WanVideoDecode`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoSampler`、`WanVideoAnimateEmbeds`、`Evaluate Integers`、`WanVideoClipVisionEncode`、`WanVideoSetLoRAs`、`GetImageSizeAndCount`、`WanVideoBlockSwap`、`WanVideoTextEncodeCached`、`DrawViTPose`、`LoadImage`、`VHS_VideoCombine`、`ImageConcatMulti`、`WanVideoContextOptions`、`ImageBlend`、`LayerUtility: ImageMaskScaleAsV2`、`ImageFromBatch`、`VHS_LoadVideo`、`easy int`、`SeCVideoSegmentation`、`GrowMask`、`BlockifyMask`、`VHS_VideoInfoLoaded`、`SeCModelLoader`、`OnnxDetectionModelLoader`、`DrawMaskOnImage`、`PoseAndFaceDetection`、`WanVideoVAELoader`、`CLIPVisionLoader`、`ClothesSegment`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
