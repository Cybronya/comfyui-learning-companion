---
key: 视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2073370111406333953.json
name: 动作迁移   动作模仿  角色替换  人物替换  wan2.2_2073370111406333953.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2073370111406333953.json
hash: 14ea0731b80876b6
coverage: 1
learned_at: 2026-10-15 22:41:06
nodes: [WanVideoModelLoader, WanVideoTorchCompileSettings, WanVideoSetBlockSwap, LayerUtility: ImageScaleByAspectRatio V2, WanVideoSampler, LayerUtility: ImageMaskScaleAsV2, WanVideoAnimateEmbeds, WanVideoSetLoRAs, GetImageSizeAndCount, WanVideoBlockSwap, WanVideoTextEncodeCached, ImageConcatMulti, LoadImage, ImageConcatMulti, VHS_VideoCombine, VHS_VideoCombine, ImageFromBatch, VHS_VideoInfoLoaded, ClothesSegment, SeCVideoSegmentation, GrowMask, BlockifyMask, OnnxDetectionModelLoader, easy int, WanVideoVAELoader, SeCModelLoader, CLIPVisionLoader, WanVideoClipVisionEncode, VHS_VideoCombine, PoseAndFaceDetection, DrawViTPose, Evaluate Integers, DrawMaskOnImage, WanVideoContextOptions, ImageBlend, WanVideoLoraSelectMulti, WanVideoDecode, VHS_LoadVideo]
patterns: []
missing: []
---

# 视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2073370111406333953.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2073370111406333953.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（38 个）：
- `WanVideoModelLoader`
- `WanVideoTorchCompileSettings`
- `WanVideoSetBlockSwap`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoSampler` ★核心
- `LayerUtility: ImageMaskScaleAsV2`
- `WanVideoAnimateEmbeds`
- `WanVideoSetLoRAs`
- `GetImageSizeAndCount`
- `WanVideoBlockSwap`
- `WanVideoTextEncodeCached`
- `ImageConcatMulti`
- `LoadImage`
- `ImageConcatMulti`
- `VHS_VideoCombine`
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
- `CLIPVisionLoader`
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
- `VHS_LoadVideo`

## 知识

覆盖率 **100%**（38/38）

**有卡**：`WanVideoModelLoader`、`WanVideoTorchCompileSettings`、`WanVideoSetBlockSwap`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoSampler`、`LayerUtility: ImageMaskScaleAsV2`、`WanVideoAnimateEmbeds`、`WanVideoSetLoRAs`、`GetImageSizeAndCount`、`WanVideoBlockSwap`、`WanVideoTextEncodeCached`、`ImageConcatMulti`、`LoadImage`、`VHS_VideoCombine`、`ImageFromBatch`、`VHS_VideoInfoLoaded`、`ClothesSegment`、`SeCVideoSegmentation`、`GrowMask`、`BlockifyMask`、`OnnxDetectionModelLoader`、`easy int`、`WanVideoVAELoader`、`SeCModelLoader`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`PoseAndFaceDetection`、`DrawViTPose`、`Evaluate Integers`、`DrawMaskOnImage`、`WanVideoContextOptions`、`ImageBlend`、`WanVideoLoraSelectMulti`、`WanVideoDecode`、`VHS_LoadVideo`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
