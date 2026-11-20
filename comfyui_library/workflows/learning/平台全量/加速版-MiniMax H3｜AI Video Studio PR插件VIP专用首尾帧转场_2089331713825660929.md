---
key: 平台全量/加速版-MiniMax H3｜AI Video Studio PR插件VIP专用首尾帧转场_2089331713825660929.json
name: 加速版-MiniMax H3｜AI Video Studio PR插件VIP专用首尾帧转场_2089331713825660929
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/加速版-MiniMax H3｜AI Video Studio PR插件VIP专用首尾帧转场_2089331713825660929.json
hash: 56ef3c9f05c3c029
coverage: 0.92
learned_at: 2026-11-14 01:44:09
nodes: [PrimitiveFloat, UpscaleModelLoader, ComfyMathExpression, VAELoader, VAELoader, UNETLoader, CLIPLoader, RandomNoise, KSamplerSelect, BasicScheduler, BasicGuider, PathchSageAttentionKJ, EasyCache, SamplerCustomAdvanced, VAEDecode, VAEDecodeAudio, ImageUpscaleWithModel, MiniMaxH3ReferenceToVideo, CreateVideo, SaveVideo, LoadImage, LoadImage, CR Prompt Text, PrimitiveFloat, ResolutionSelector]
patterns: []
missing: []
---

# 平台全量/加速版-MiniMax H3｜AI Video Studio PR插件VIP专用首尾帧转场_2089331713825660929.json

> 来源文件 `comfyui_library/workflows/平台全量/加速版-MiniMax H3｜AI Video Studio PR插件VIP专用首尾帧转场_2089331713825660929.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Process → Output → Other

**节点**（25 个）：
- `PrimitiveFloat`
- `UpscaleModelLoader`
- `ComfyMathExpression`
- `VAELoader`
- `VAELoader`
- `UNETLoader` ★核心
- `CLIPLoader`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `BasicGuider`
- `PathchSageAttentionKJ`
- `EasyCache`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `ImageUpscaleWithModel`
- `MiniMaxH3ReferenceToVideo`
- `CreateVideo`
- `SaveVideo`
- `LoadImage`
- `LoadImage`
- `CR Prompt Text`
- `PrimitiveFloat`
- `ResolutionSelector`

## 知识

覆盖率 **92%**（23/25）

**有卡**：`UpscaleModelLoader`、`ComfyMathExpression`、`VAELoader`、`UNETLoader`、`CLIPLoader`、`RandomNoise`、`KSamplerSelect`、`BasicScheduler`、`BasicGuider`、`PathchSageAttentionKJ`、`EasyCache`、`SamplerCustomAdvanced`、`VAEDecode`、`VAEDecodeAudio`、`ImageUpscaleWithModel`、`MiniMaxH3ReferenceToVideo`、`CreateVideo`、`SaveVideo`、`LoadImage`、`CR Prompt Text`、`ResolutionSelector`

**用到的条目**：VAEDecode、VAELoader、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced
