---
key: 平台全量/角色替换  人物替换  wan2.2 动作模仿  动作迁移_2073575264243773442.json
name: 角色替换  人物替换  wan2.2 动作模仿  动作迁移_2073575264243773442
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/角色替换  人物替换  wan2.2 动作模仿  动作迁移_2073575264243773442.json
hash: d5e3af6d2ff6933f
coverage: 0.975
learned_at: 2026-11-14 02:43:41
nodes: [WanVideoModelLoader, WanVideoTorchCompileSettings, WanVideoLoraSelectMulti, WanVideoSetBlockSwap, ImageConcatMulti, WanVideoDecode, CLIPVisionLoader, PoseAndFaceDetection, BlockifyMask, SeCVideoSegmentation, LayerUtility: ImageScaleByAspectRatio V2, WanVideoSampler, LayerUtility: ImageMaskScaleAsV2, WanVideoAnimateEmbeds, WanVideoClipVisionEncode, WanVideoSetLoRAs, DrawMaskOnImage, GetImageSizeAndCount, WanVideoBlockSwap, WanVideoTextEncodeCached, DrawViTPose, ImageConcatMulti, VHS_VideoCombine, LoadImage, ImageFromBatch, easy int, SeCModelLoader, ClothesSegment, GrowMask, OnnxDetectionModelLoader, WanVideoVAELoader, Evaluate Integers, WanVideoContextOptions, VHS_VideoCombine, easy showAnything, VHS_VideoInfoLoaded, VHS_VideoCombine, ImageBlend, LoadImage, VHS_LoadVideo]
patterns: []
missing: []
---

# 平台全量/角色替换  人物替换  wan2.2 动作模仿  动作迁移_2073575264243773442.json

> 来源文件 `comfyui_library/workflows/平台全量/角色替换  人物替换  wan2.2 动作模仿  动作迁移_2073575264243773442.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（40 个）：
- `WanVideoModelLoader`
- `WanVideoTorchCompileSettings`
- `WanVideoLoraSelectMulti`
- `WanVideoSetBlockSwap`
- `ImageConcatMulti`
- `WanVideoDecode`
- `CLIPVisionLoader`
- `PoseAndFaceDetection`
- `BlockifyMask`
- `SeCVideoSegmentation`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoSampler` ★核心
- `LayerUtility: ImageMaskScaleAsV2`
- `WanVideoAnimateEmbeds`
- `WanVideoClipVisionEncode`
- `WanVideoSetLoRAs`
- `DrawMaskOnImage`
- `GetImageSizeAndCount`
- `WanVideoBlockSwap`
- `WanVideoTextEncodeCached`
- `DrawViTPose`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `LoadImage`
- `ImageFromBatch`
- `easy int`
- `SeCModelLoader`
- `ClothesSegment`
- `GrowMask`
- `OnnxDetectionModelLoader`
- `WanVideoVAELoader`
- `Evaluate Integers`
- `WanVideoContextOptions`
- `VHS_VideoCombine`
- `easy showAnything`
- `VHS_VideoInfoLoaded`
- `VHS_VideoCombine`
- `ImageBlend`
- `LoadImage`
- `VHS_LoadVideo`

## 知识

覆盖率 **98%**（39/40）

**有卡**：`WanVideoModelLoader`、`WanVideoTorchCompileSettings`、`WanVideoLoraSelectMulti`、`WanVideoSetBlockSwap`、`ImageConcatMulti`、`WanVideoDecode`、`CLIPVisionLoader`、`PoseAndFaceDetection`、`BlockifyMask`、`SeCVideoSegmentation`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoSampler`、`LayerUtility: ImageMaskScaleAsV2`、`WanVideoAnimateEmbeds`、`WanVideoClipVisionEncode`、`WanVideoSetLoRAs`、`DrawMaskOnImage`、`GetImageSizeAndCount`、`WanVideoBlockSwap`、`WanVideoTextEncodeCached`、`DrawViTPose`、`VHS_VideoCombine`、`LoadImage`、`ImageFromBatch`、`easy int`、`SeCModelLoader`、`ClothesSegment`、`GrowMask`、`OnnxDetectionModelLoader`、`WanVideoVAELoader`、`Evaluate Integers`、`WanVideoContextOptions`、`VHS_VideoInfoLoaded`、`ImageBlend`、`VHS_LoadVideo`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoLoraSelectMulti、WanVideoSetLoRAs
