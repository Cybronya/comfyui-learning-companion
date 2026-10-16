---
key: 视频生成/图生视频/Wan2.2+14B 4步加速图生视频KJ_1954023918736855041.json
name: Wan2.2+14B 4步加速图生视频KJ_1954023918736855041.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1954023918736855041.json
hash: 0683d068e5df5d63
coverage: 0.7
learned_at: 2026-10-15 22:31:06
nodes: [WanVideoSetBlockSwap, WanVideoSetBlockSwap, ImpactSwitch, WanVideoLoraSelect, Reroute, FloatToSigmas, PrimitiveInt, WanVideoSampler, MathExpression|pysssss, Reroute, LoadWanVideoT5TextEncoder, WanVideoBlockSwap, StringToFloatList, Text Concatenate, WanVideoTorchCompileSettings, WanVideoTextEncode, WanVideoSampler, WanVideoVAELoader, PrimitiveInt, PrimitiveInt, LayerUtility: ImageScaleByAspectRatio V2, ImageResizeKJv2, MathExpression|pysssss, CLIPVisionLoader, RH_LLMAPI_NODE, WanVideoClipVisionEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoModelLoader, WanVideoImageToVideoEncode, Reroute, WanVideoDecode, VHS_VideoCombine, DF_Int_to_Float, Reroute, PrimitiveInt, Note, Wan22PromptSelector, GetImageRangeFromBatch, PreviewImage, PrimitiveInt, VHS_LoadVideo, Reroute, WanVideoSetLoRAs, easy cleanGpuUsed, PrimitiveStringMultiline, WanVideoSetLoRAs, easy cleanGpuUsed, LoadImage, ShowText|pysssss]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2+14B 4步加速图生视频KJ_1954023918736855041.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1954023918736855041.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（50 个）：
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `ImpactSwitch`
- `WanVideoLoraSelect`
- `Reroute`
- `FloatToSigmas`
- `PrimitiveInt`
- `WanVideoSampler` ★核心
- `MathExpression|pysssss`
- `Reroute`
- `LoadWanVideoT5TextEncoder`
- `WanVideoBlockSwap`
- `StringToFloatList`
- `Text Concatenate`
- `WanVideoTorchCompileSettings`
- `WanVideoTextEncode`
- `WanVideoSampler` ★核心
- `WanVideoVAELoader`
- `PrimitiveInt`
- `PrimitiveInt`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageResizeKJv2`
- `MathExpression|pysssss`
- `CLIPVisionLoader`
- `RH_LLMAPI_NODE`
- `WanVideoClipVisionEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoImageToVideoEncode`
- `Reroute`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `DF_Int_to_Float`
- `Reroute`
- `PrimitiveInt`
- `Note`
- `Wan22PromptSelector`
- `GetImageRangeFromBatch`
- `PreviewImage`
- `PrimitiveInt`
- `VHS_LoadVideo`
- `Reroute`
- `WanVideoSetLoRAs`
- `easy cleanGpuUsed`
- `PrimitiveStringMultiline`
- `WanVideoSetLoRAs`
- `easy cleanGpuUsed`
- `LoadImage`
- `ShowText|pysssss`

## 知识

覆盖率 **70%**（35/50）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoLoraSelect`、`FloatToSigmas`、`WanVideoSampler`、`MathExpression|pysssss`、`LoadWanVideoT5TextEncoder`、`WanVideoBlockSwap`、`StringToFloatList`、`Text Concatenate`、`WanVideoTorchCompileSettings`、`WanVideoTextEncode`、`WanVideoVAELoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageResizeKJv2`、`CLIPVisionLoader`、`RH_LLMAPI_NODE`、`WanVideoClipVisionEncode`、`WanVideoModelLoader`、`WanVideoImageToVideoEncode`、`WanVideoDecode`、`VHS_VideoCombine`、`DF_Int_to_Float`、`Wan22PromptSelector`、`GetImageRangeFromBatch`、`VHS_LoadVideo`、`WanVideoSetLoRAs`、`easy cleanGpuUsed`、`LoadImage`

**用到的条目**：LoadImage、LayerUtility: ImageScaleByAspectRatio V2、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode
