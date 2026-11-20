---
key: 平台全量/动作迁移_动作模仿_角色替换_人物替换_wan2.2_2101501237249265665.json
name: 动作迁移_动作模仿_角色替换_人物替换_wan2.2_2101501237249265665
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/动作迁移_动作模仿_角色替换_人物替换_wan2.2_2101501237249265665.json
hash: c223847ce2ca79cc
coverage: 1
learned_at: 2026-11-14 01:45:31
nodes: [WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoBlockSwap, VHS_VideoCombine, ClothesSegment, ImageFromBatch, SeCVideoSegmentation, GrowMask, WanVideoVAELoader, OnnxDetectionModelLoader, BlockifyMask, DrawMaskOnImage, PoseAndFaceDetection, WanVideoClipVisionEncode, VHS_VideoCombine, Evaluate Integers, DrawViTPose, WanVideoContextOptions, WanVideoAnimateEmbeds, WanVideoTorchCompileSettings, WanVideoModelLoader, WanVideoLoraSelectMulti, ImageBlend, ImageConcatMulti, WanVideoDecode, WanVideoTextEncodeCached, LoadImage, GetImageSizeAndCount, ImageConcatMulti, VHS_VideoCombine, CLIPVisionLoader, LayerUtility: ImageMaskScaleAsV2, easy int, SeCModelLoader, LayerUtility: ImageScaleByAspectRatio V2, WanVideoSampler, VHS_LoadVideo]
patterns: []
missing: []
---

# 平台全量/动作迁移_动作模仿_角色替换_人物替换_wan2.2_2101501237249265665.json

> 来源文件 `comfyui_library/workflows/平台全量/动作迁移_动作模仿_角色替换_人物替换_wan2.2_2101501237249265665.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（37 个）：
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoBlockSwap`
- `VHS_VideoCombine`
- `ClothesSegment`
- `ImageFromBatch`
- `SeCVideoSegmentation`
- `GrowMask`
- `WanVideoVAELoader`
- `OnnxDetectionModelLoader`
- `BlockifyMask`
- `DrawMaskOnImage`
- `PoseAndFaceDetection`
- `WanVideoClipVisionEncode`
- `VHS_VideoCombine`
- `Evaluate Integers`
- `DrawViTPose`
- `WanVideoContextOptions`
- `WanVideoAnimateEmbeds`
- `WanVideoTorchCompileSettings`
- `WanVideoModelLoader`
- `WanVideoLoraSelectMulti`
- `ImageBlend`
- `ImageConcatMulti`
- `WanVideoDecode`
- `WanVideoTextEncodeCached`
- `LoadImage`
- `GetImageSizeAndCount`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `CLIPVisionLoader`
- `LayerUtility: ImageMaskScaleAsV2`
- `easy int`
- `SeCModelLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoSampler` ★核心
- `VHS_LoadVideo`

## 知识

覆盖率 **100%**（37/37）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoBlockSwap`、`VHS_VideoCombine`、`ClothesSegment`、`ImageFromBatch`、`SeCVideoSegmentation`、`GrowMask`、`WanVideoVAELoader`、`OnnxDetectionModelLoader`、`BlockifyMask`、`DrawMaskOnImage`、`PoseAndFaceDetection`、`WanVideoClipVisionEncode`、`Evaluate Integers`、`DrawViTPose`、`WanVideoContextOptions`、`WanVideoAnimateEmbeds`、`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`ImageBlend`、`ImageConcatMulti`、`WanVideoDecode`、`WanVideoTextEncodeCached`、`LoadImage`、`GetImageSizeAndCount`、`CLIPVisionLoader`、`LayerUtility: ImageMaskScaleAsV2`、`easy int`、`SeCModelLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoSampler`、`VHS_LoadVideo`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoLoraSelectMulti、WanVideoSetLoRAs
