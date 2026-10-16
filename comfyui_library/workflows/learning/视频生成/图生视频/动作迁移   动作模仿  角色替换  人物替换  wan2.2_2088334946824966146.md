---
key: 视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2088334946824966146.json
name: 动作迁移   动作模仿  角色替换  人物替换  wan2.2_2088334946824966146
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2088334946824966146.json
hash: 569fa76dcc6c9c95
coverage: 1
learned_at: 2026-10-16 21:43:47
nodes: [WanVideoModelLoader, WanVideoTorchCompileSettings, WanVideoLoraSelectMulti, WanVideoSetBlockSwap, WanVideoDecode, VHS_VideoCombine, WanVideoSampler, WanVideoAnimateEmbeds, Evaluate Integers, WanVideoClipVisionEncode, WanVideoSetLoRAs, GetImageSizeAndCount, WanVideoBlockSwap, WanVideoTextEncodeCached, DrawViTPose, VHS_VideoCombine, VHS_VideoCombine, WanVideoContextOptions, ImageConcatMulti, ImageConcatMulti, ImageBlend, easy int, ImageFromBatch, SeCModelLoader, LayerUtility: ImageScaleByAspectRatio V2, VHS_VideoInfoLoaded, ClothesSegment, SeCVideoSegmentation, GrowMask, BlockifyMask, WanVideoVAELoader, OnnxDetectionModelLoader, DrawMaskOnImage, PoseAndFaceDetection, CLIPVisionLoader, LayerUtility: ImageMaskScaleAsV2, LoadImage, VHS_LoadVideo]
patterns: []
missing: []
---

# 视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2088334946824966146.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2088334946824966146.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（38 个）：
- `WanVideoModelLoader`
- `WanVideoTorchCompileSettings`
- `WanVideoLoraSelectMulti`
- `WanVideoSetBlockSwap`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `WanVideoSampler` ★核心
- `WanVideoAnimateEmbeds`
- `Evaluate Integers`
- `WanVideoClipVisionEncode`
- `WanVideoSetLoRAs`
- `GetImageSizeAndCount`
- `WanVideoBlockSwap`
- `WanVideoTextEncodeCached`
- `DrawViTPose`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `WanVideoContextOptions`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `ImageBlend`
- `easy int`
- `ImageFromBatch`
- `SeCModelLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VHS_VideoInfoLoaded`
- `ClothesSegment`
- `SeCVideoSegmentation`
- `GrowMask`
- `BlockifyMask`
- `WanVideoVAELoader`
- `OnnxDetectionModelLoader`
- `DrawMaskOnImage`
- `PoseAndFaceDetection`
- `CLIPVisionLoader`
- `LayerUtility: ImageMaskScaleAsV2`
- `LoadImage`
- `VHS_LoadVideo`

## 知识

覆盖率 **100%**（38/38）

**有卡**：`WanVideoModelLoader`、`WanVideoTorchCompileSettings`、`WanVideoLoraSelectMulti`、`WanVideoSetBlockSwap`、`WanVideoDecode`、`VHS_VideoCombine`、`WanVideoSampler`、`WanVideoAnimateEmbeds`、`Evaluate Integers`、`WanVideoClipVisionEncode`、`WanVideoSetLoRAs`、`GetImageSizeAndCount`、`WanVideoBlockSwap`、`WanVideoTextEncodeCached`、`DrawViTPose`、`WanVideoContextOptions`、`ImageConcatMulti`、`ImageBlend`、`easy int`、`ImageFromBatch`、`SeCModelLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`VHS_VideoInfoLoaded`、`ClothesSegment`、`SeCVideoSegmentation`、`GrowMask`、`BlockifyMask`、`WanVideoVAELoader`、`OnnxDetectionModelLoader`、`DrawMaskOnImage`、`PoseAndFaceDetection`、`CLIPVisionLoader`、`LayerUtility: ImageMaskScaleAsV2`、`LoadImage`、`VHS_LoadVideo`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
