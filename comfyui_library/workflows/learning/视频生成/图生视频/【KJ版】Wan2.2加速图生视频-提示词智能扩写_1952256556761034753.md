---
key: 视频生成/图生视频/【KJ版】Wan2.2加速图生视频-提示词智能扩写_1952256556761034753.json
name: 【KJ版】Wan2.2加速图生视频-提示词智能扩写_1952256556761034753.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/【KJ版】Wan2.2加速图生视频-提示词智能扩写_1952256556761034753.json
hash: d2b7fd4787182acc
coverage: 0.702703
learned_at: 2026-10-15 22:31:00
nodes: [WanVideoTorchCompileSettings, WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoBlockSwap, WanVideoLoraSelect, Reroute, WanVideoSetLoRAs, CreateCFGScheduleFloatList, WanVideoDecode, VHS_VideoCombine, WanVideoSetLoRAs, WanVideoSampler, MathExpression|pysssss, PrimitiveInt, PrimitiveInt, PrimitiveInt, Wan22PromptSelector, PrimitiveInt, Reroute, WanVideoVAELoader, MathExpression|pysssss, LayerUtility: ImageScaleByAspectRatio V2, ImageResizeKJv2, LoadWanVideoT5TextEncoder, WanVideoImageToVideoEncode, Reroute, WanVideoModelLoader, WanVideoModelLoader, Reroute, WanVideoSampler, LoadImage, ShowText|pysssss, PrimitiveStringMultiline, RH_LLMAPI_NODE, Text Concatenate, WanVideoTextEncode, ImpactSwitch]
patterns: []
missing: []
---

# 视频生成/图生视频/【KJ版】Wan2.2加速图生视频-提示词智能扩写_1952256556761034753.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1952256556761034753.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（37 个）：
- `WanVideoTorchCompileSettings`
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `Reroute`
- `WanVideoSetLoRAs`
- `CreateCFGScheduleFloatList`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `WanVideoSetLoRAs`
- `WanVideoSampler` ★核心
- `MathExpression|pysssss`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `Wan22PromptSelector`
- `PrimitiveInt`
- `Reroute`
- `WanVideoVAELoader`
- `MathExpression|pysssss`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageResizeKJv2`
- `LoadWanVideoT5TextEncoder`
- `WanVideoImageToVideoEncode`
- `Reroute`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `Reroute`
- `WanVideoSampler` ★核心
- `LoadImage`
- `ShowText|pysssss`
- `PrimitiveStringMultiline`
- `RH_LLMAPI_NODE`
- `Text Concatenate`
- `WanVideoTextEncode`
- `ImpactSwitch`

## 知识

覆盖率 **70%**（26/37）

**有卡**：`WanVideoTorchCompileSettings`、`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`WanVideoLoraSelect`、`WanVideoSetLoRAs`、`CreateCFGScheduleFloatList`、`WanVideoDecode`、`VHS_VideoCombine`、`WanVideoSampler`、`MathExpression|pysssss`、`Wan22PromptSelector`、`WanVideoVAELoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageResizeKJv2`、`LoadWanVideoT5TextEncoder`、`WanVideoImageToVideoEncode`、`WanVideoModelLoader`、`LoadImage`、`RH_LLMAPI_NODE`、`Text Concatenate`、`WanVideoTextEncode`

**用到的条目**：LoadImage、LayerUtility: ImageScaleByAspectRatio V2、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader
