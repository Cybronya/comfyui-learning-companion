---
key: 视频生成/图生视频/wan2.2动作参考，vace_1966553431391580161.json
name: wan2.2动作参考，vace_1966553431391580161.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1966553431391580161.json
hash: 9722af03fea4ca7d
coverage: 0.878049
learned_at: 2026-10-15 22:31:38
nodes: [RH_Captioner, ImageResizeKJv2, GetImageSizeAndCount, ImageResizeKJv2, ApplyFaceProcessor, FaceProcessorLoader, Int, DWPreprocessor, INTConstant, CreateCFGScheduleFloatList, Text Multiline, Reroute, easy cleanGpuUsed, VHS_LoadVideo, WanVideoBlockSwap, WanVideoTorchCompileSettings, WanVideoVAELoader, WanVideoTeaCache, WanVideoSLG, Anything Everywhere3, Anything Everywhere3, RHHiddenNodes, WanVideoTextEncode, Text Concatenate, easy showAnything, LoadWanVideoT5TextEncoder, Anything Everywhere3, VHS_LoadVideo, VHS_VideoCombine, SimpleMath+, WanVideoEncode, LayerUtility: ImageScaleByAspectRatio V2, WanVideoAddStandInLatent, WanVideoVACEEncode, WanVideoSampler, WanVideoSampler, INTConstant, RHHiddenNodes, WanVideoDecode, ImageFromBatch+, Int]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.2动作参考，vace_1966553431391580161.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1966553431391580161.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（41 个）：
- `RH_Captioner`
- `ImageResizeKJv2`
- `GetImageSizeAndCount`
- `ImageResizeKJv2`
- `ApplyFaceProcessor`
- `FaceProcessorLoader`
- `Int`
- `DWPreprocessor`
- `INTConstant`
- `CreateCFGScheduleFloatList`
- `Text Multiline`
- `Reroute`
- `easy cleanGpuUsed`
- `VHS_LoadVideo`
- `WanVideoBlockSwap`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `WanVideoTeaCache`
- `WanVideoSLG`
- `Anything Everywhere3`
- `Anything Everywhere3`
- `RHHiddenNodes`
- `WanVideoTextEncode`
- `Text Concatenate`
- `easy showAnything`
- `LoadWanVideoT5TextEncoder`
- `Anything Everywhere3`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `SimpleMath+`
- `WanVideoEncode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoAddStandInLatent`
- `WanVideoVACEEncode`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `INTConstant`
- `RHHiddenNodes`
- `WanVideoDecode`
- `ImageFromBatch+`
- `Int`

## 知识

覆盖率 **88%**（36/41）

**有卡**：`RH_Captioner`、`ImageResizeKJv2`、`GetImageSizeAndCount`、`ApplyFaceProcessor`、`FaceProcessorLoader`、`Int`、`DWPreprocessor`、`INTConstant`、`CreateCFGScheduleFloatList`、`Text Multiline`、`easy cleanGpuUsed`、`VHS_LoadVideo`、`WanVideoBlockSwap`、`WanVideoTorchCompileSettings`、`WanVideoVAELoader`、`WanVideoTeaCache`、`WanVideoSLG`、`RHHiddenNodes`、`WanVideoTextEncode`、`Text Concatenate`、`LoadWanVideoT5TextEncoder`、`VHS_VideoCombine`、`SimpleMath+`、`WanVideoEncode`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoAddStandInLatent`、`WanVideoVACEEncode`、`WanVideoSampler`、`WanVideoDecode`、`ImageFromBatch+`

**用到的条目**：LayerUtility: ImageScaleByAspectRatio V2、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoVACEEncode
