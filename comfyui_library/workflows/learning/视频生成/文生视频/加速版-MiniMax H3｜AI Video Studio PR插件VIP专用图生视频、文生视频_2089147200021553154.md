---
key: 视频生成/文生视频/加速版-MiniMax H3｜AI Video Studio PR插件VIP专用图生视频、文生视频_2089147200021553154.json
name: 加速版-MiniMax H3｜AI Video Studio PR插件VIP专用图生视频、文生视频_2089147200021553154
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/加速版-MiniMax H3｜AI Video Studio PR插件VIP专用图生视频、文生视频_2089147200021553154.json
hash: 5425a85cf161f4fa
coverage: 0.875
learned_at: 2026-10-11 21:19:54
nodes: [LoadImage, PrimitiveFloat, UpscaleModelLoader, ComfyMathExpression, VAELoader, VAELoader, UNETLoader, CLIPLoader, RandomNoise, KSamplerSelect, BasicScheduler, BasicGuider, PathchSageAttentionKJ, EasyCache, SamplerCustomAdvanced, VAEDecode, VAEDecodeAudio, ImageUpscaleWithModel, MiniMaxH3ReferenceToVideo, CreateVideo, SaveVideo, CR Prompt Text, ResolutionSelector, PrimitiveFloat]
patterns: []
missing: [CR Prompt Text]
discoveries: [次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/加速版-MiniMax H3｜AI Video Studio PR插件VIP专用图生视频、文生视频_2089147200021553154.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/加速版-MiniMax H3｜AI Video Studio PR插件VIP专用图生视频、文生视频_2089147200021553154.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Process → Output → Other

**节点**（24 个）：
- `LoadImage`
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
- `CR Prompt Text`
- `ResolutionSelector`
- `PrimitiveFloat`

## 知识

覆盖率 **88%**（21/24）

**有卡**：`LoadImage`、`UpscaleModelLoader`、`ComfyMathExpression`、`VAELoader`、`UNETLoader`、`CLIPLoader`、`RandomNoise`、`KSamplerSelect`、`BasicScheduler`、`BasicGuider`、`PathchSageAttentionKJ`、`EasyCache`、`SamplerCustomAdvanced`、`VAEDecode`、`VAEDecodeAudio`、`ImageUpscaleWithModel`、`MiniMaxH3ReferenceToVideo`、`CreateVideo`、`SaveVideo`、`ResolutionSelector`

**缺卡**（1）：`CR Prompt Text`

**用到的条目**：VAEDecode、VAELoader、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced

## 学习发现

- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
