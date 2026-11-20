---
key: 平台全量/加速版-MiniMax H3｜AI Video Studio PR插件VIP专用一句话特效_2090357874504589313.json
name: 加速版-MiniMax H3｜AI Video Studio PR插件VIP专用一句话特效_2090357874504589313
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/加速版-MiniMax H3｜AI Video Studio PR插件VIP专用一句话特效_2090357874504589313.json
hash: 5e546421bfe6a624
coverage: 0.923077
learned_at: 2026-11-14 01:44:09
nodes: [LoadImage, PrimitiveFloat, UpscaleModelLoader, ComfyMathExpression, VAELoader, VAELoader, UNETLoader, CLIPLoader, RandomNoise, KSamplerSelect, BasicScheduler, BasicGuider, PathchSageAttentionKJ, EasyCache, SamplerCustomAdvanced, VAEDecode, VAEDecodeAudio, ImageUpscaleWithModel, MiniMaxH3ReferenceToVideo, CreateVideo, SaveVideo, GetVideoComponents, LoadVideo, CR Prompt Text, ResolutionSelector, PrimitiveFloat]
patterns: []
missing: []
---

# 平台全量/加速版-MiniMax H3｜AI Video Studio PR插件VIP专用一句话特效_2090357874504589313.json

> 来源文件 `comfyui_library/workflows/平台全量/加速版-MiniMax H3｜AI Video Studio PR插件VIP专用一句话特效_2090357874504589313.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Process → Output → Other

**节点**（26 个）：
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
- `GetVideoComponents`
- `LoadVideo`
- `CR Prompt Text`
- `ResolutionSelector`
- `PrimitiveFloat`

## 知识

覆盖率 **92%**（24/26）

**有卡**：`LoadImage`、`UpscaleModelLoader`、`ComfyMathExpression`、`VAELoader`、`UNETLoader`、`CLIPLoader`、`RandomNoise`、`KSamplerSelect`、`BasicScheduler`、`BasicGuider`、`PathchSageAttentionKJ`、`EasyCache`、`SamplerCustomAdvanced`、`VAEDecode`、`VAEDecodeAudio`、`ImageUpscaleWithModel`、`MiniMaxH3ReferenceToVideo`、`CreateVideo`、`SaveVideo`、`GetVideoComponents`、`LoadVideo`、`CR Prompt Text`、`ResolutionSelector`

**用到的条目**：VAEDecode、VAELoader、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced
