---
key: 视频生成/图生视频/【KJ版】Wan2.2最强图生视频+智能扩写提示词_1972595555933302785.json
name: 【KJ版】Wan2.2最强图生视频+智能扩写提示词_1972595555933302785.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/【KJ版】Wan2.2最强图生视频+智能扩写提示词_1972595555933302785.json
hash: e9e60d7d815edb2d
coverage: 0.741935
learned_at: 2026-10-15 22:32:00
nodes: [WanVideoModelLoader, WanVideoTorchCompileSettings, WanVideoBlockSwap, WanVideoModelLoader, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoLoraSelectMulti, WanVideoSetBlockSwap, LoadWanVideoT5TextEncoder, PrimitiveInt, MathExpression|pysssss, LayerUtility: ImageScaleByAspectRatio V2, WanVideoTextEncode, Wan22PromptSelector, CR Text Concatenate, CreateCFGScheduleFloatList, PrimitiveInt, PrimitiveInt, WanVideoSampler, WanVideoSampler, WanVideoVAELoader, WanVideoDecode, VHS_VideoCombine, RH_LLMAPI_NODE, PrimitiveInt, LoadImage, ImpactSwitch, PrimitiveStringMultiline, ShowText|pysssss, ShowText|pysssss, WanVideoImageToVideoEncode]
patterns: []
missing: []
---

# 视频生成/图生视频/【KJ版】Wan2.2最强图生视频+智能扩写提示词_1972595555933302785.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1972595555933302785.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（31 个）：
- `WanVideoModelLoader`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoLoraSelectMulti`
- `WanVideoSetBlockSwap`
- `LoadWanVideoT5TextEncoder`
- `PrimitiveInt`
- `MathExpression|pysssss`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoTextEncode`
- `Wan22PromptSelector`
- `CR Text Concatenate`
- `CreateCFGScheduleFloatList`
- `PrimitiveInt`
- `PrimitiveInt`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `WanVideoVAELoader`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `RH_LLMAPI_NODE`
- `PrimitiveInt`
- `LoadImage`
- `ImpactSwitch`
- `PrimitiveStringMultiline`
- `ShowText|pysssss`
- `ShowText|pysssss`
- `WanVideoImageToVideoEncode`

## 知识

覆盖率 **74%**（23/31）

**有卡**：`WanVideoModelLoader`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoLoraSelectMulti`、`LoadWanVideoT5TextEncoder`、`MathExpression|pysssss`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoTextEncode`、`Wan22PromptSelector`、`CR Text Concatenate`、`CreateCFGScheduleFloatList`、`WanVideoSampler`、`WanVideoVAELoader`、`WanVideoDecode`、`VHS_VideoCombine`、`RH_LLMAPI_NODE`、`LoadImage`、`WanVideoImageToVideoEncode`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode
