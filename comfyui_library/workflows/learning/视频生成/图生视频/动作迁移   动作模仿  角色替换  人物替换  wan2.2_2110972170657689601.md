---
key: 视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2110972170657689601.json
name: 动作迁移   动作模仿  角色替换  人物替换  wan2.2_2110972170657689601
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2110972170657689601.json
hash: 5e12011ba8b36307
coverage: 1
learned_at: 2026-10-18 00:24:24
nodes: [WanVideoModelLoader, WanVideoTorchCompileSettings, WanVideoLoraSelectMulti, WanVideoSetBlockSwap, WanVideoDecode, WanVideoContextOptions, VHS_VideoCombine, LayerUtility: ImageScaleByAspectRatio V2, WanVideoSampler, WanVideoAnimateEmbeds, Evaluate Integers, WanVideoClipVisionEncode, WanVideoSetLoRAs, GetImageSizeAndCount, WanVideoBlockSwap, WanVideoTextEncodeCached, DrawViTPose, ImageConcatMulti, VHS_VideoCombine, VHS_VideoCombine, ImageConcatMulti, ImageBlend, VHS_LoadVideo, LoadImage, VHS_VideoInfoLoaded, SeCModelLoader, easy int, LayerUtility: ImageMaskScaleAsV2, ImageFromBatch, ClothesSegment, GrowMask, BlockifyMask, WanVideoVAELoader, DrawMaskOnImage, OnnxDetectionModelLoader, PoseAndFaceDetection, CLIPVisionLoader, SeCVideoSegmentation]
patterns: []
missing: []
---

# 视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2110972170657689601.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2110972170657689601.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（38 个）：
- `WanVideoModelLoader`
- `WanVideoTorchCompileSettings`
- `WanVideoLoraSelectMulti`
- `WanVideoSetBlockSwap`
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
- `VHS_VideoCombine`
- `ImageConcatMulti`
- `ImageBlend`
- `VHS_LoadVideo`
- `LoadImage`
- `VHS_VideoInfoLoaded`
- `SeCModelLoader`
- `easy int`
- `LayerUtility: ImageMaskScaleAsV2`
- `ImageFromBatch`
- `ClothesSegment`
- `GrowMask`
- `BlockifyMask`
- `WanVideoVAELoader`
- `DrawMaskOnImage`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `CLIPVisionLoader`
- `SeCVideoSegmentation`

## 知识

覆盖率 **100%**（38/38）

**有卡**：`WanVideoModelLoader`、`WanVideoTorchCompileSettings`、`WanVideoLoraSelectMulti`、`WanVideoSetBlockSwap`、`WanVideoDecode`、`WanVideoContextOptions`、`VHS_VideoCombine`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoSampler`、`WanVideoAnimateEmbeds`、`Evaluate Integers`、`WanVideoClipVisionEncode`、`WanVideoSetLoRAs`、`GetImageSizeAndCount`、`WanVideoBlockSwap`、`WanVideoTextEncodeCached`、`DrawViTPose`、`ImageConcatMulti`、`ImageBlend`、`VHS_LoadVideo`、`LoadImage`、`VHS_VideoInfoLoaded`、`SeCModelLoader`、`easy int`、`LayerUtility: ImageMaskScaleAsV2`、`ImageFromBatch`、`ClothesSegment`、`GrowMask`、`BlockifyMask`、`WanVideoVAELoader`、`DrawMaskOnImage`、`OnnxDetectionModelLoader`、`PoseAndFaceDetection`、`CLIPVisionLoader`、`SeCVideoSegmentation`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
