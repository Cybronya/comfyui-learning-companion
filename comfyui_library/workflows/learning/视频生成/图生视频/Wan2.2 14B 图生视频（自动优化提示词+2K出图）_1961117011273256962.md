---
key: 视频生成/图生视频/Wan2.2 14B 图生视频（自动优化提示词+2K出图）_1961117011273256962.json
name: Wan2.2 14B 图生视频（自动优化提示词+2K出图）_1961117011273256962.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1961117011273256962.json
hash: 873607c87a16d091
coverage: 0.811321
learned_at: 2026-10-15 22:31:28
nodes: [SetNode, SetNode, GetNode, GetNode, JWInteger, JWInteger, JjkText, ttN concat, CR Text Concatenate, RH_Prompter, RH_Captioner, easy showAnything, WanVideoBlockSwap, WanVideoSetBlockSwap, SetNode, SetNode, ImageResizeKJv2, MathExpression|pysssss, JWInteger, Seed_, LoadImage, VHS_VideoCombine, LoadImage, SimpleMath+, SimpleMath+, ImageUpscaleWithModel, easy cleanGpuUsed, CreateCFGScheduleFloatList, WanVideoSetLoRAs, WanVideoSetLoRAs, GetNode, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, easy cleanGpuUsed, WanVideoLoraSelect, WanVideoModelLoader, WanVideoTorchCompileSettings, WanVideoVAELoader, GetNode, WanVideoImageToVideoEncode, WanVideoSetBlockSwap, WanVideoTextEncode, LoadWanVideoT5TextEncoder, WanVideoSampler, INTConstant, INTConstant, RHHiddenNodes, RHHiddenNodes, easy cleanGpuUsed, VHS_VideoCombine, CR Text, WanVideoSampler]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2 14B 图生视频（自动优化提示词+2K出图）_1961117011273256962.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1961117011273256962.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（53 个）：
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `JWInteger`
- `JWInteger`
- `JjkText`
- `ttN concat`
- `CR Text Concatenate`
- `RH_Prompter`
- `RH_Captioner`
- `easy showAnything`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `SetNode`
- `SetNode`
- `ImageResizeKJv2`
- `MathExpression|pysssss`
- `JWInteger`
- `Seed_`
- `LoadImage`
- `VHS_VideoCombine`
- `LoadImage`
- `SimpleMath+`
- `SimpleMath+`
- `ImageUpscaleWithModel`
- `easy cleanGpuUsed`
- `CreateCFGScheduleFloatList`
- `WanVideoSetLoRAs`
- `WanVideoSetLoRAs`
- `GetNode`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `easy cleanGpuUsed`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `GetNode`
- `WanVideoImageToVideoEncode`
- `WanVideoSetBlockSwap`
- `WanVideoTextEncode`
- `LoadWanVideoT5TextEncoder`
- `WanVideoSampler` ★核心
- `INTConstant`
- `INTConstant`
- `RHHiddenNodes`
- `RHHiddenNodes`
- `easy cleanGpuUsed`
- `VHS_VideoCombine`
- `CR Text`
- `WanVideoSampler` ★核心

## 知识

覆盖率 **81%**（43/53）

**有卡**：`JWInteger`、`ttN concat`、`CR Text Concatenate`、`RH_Prompter`、`RH_Captioner`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`ImageResizeKJv2`、`MathExpression|pysssss`、`Seed_`、`LoadImage`、`VHS_VideoCombine`、`SimpleMath+`、`ImageUpscaleWithModel`、`easy cleanGpuUsed`、`CreateCFGScheduleFloatList`、`WanVideoSetLoRAs`、`WanVideoDecode`、`WanVideoLoraSelect`、`WanVideoModelLoader`、`WanVideoTorchCompileSettings`、`WanVideoVAELoader`、`WanVideoImageToVideoEncode`、`WanVideoTextEncode`、`LoadWanVideoT5TextEncoder`、`WanVideoSampler`、`INTConstant`、`RHHiddenNodes`、`CR Text`

**用到的条目**：LoadImage、Seed_、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader
