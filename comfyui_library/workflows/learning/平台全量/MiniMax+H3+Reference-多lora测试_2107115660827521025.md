---
key: 平台全量/MiniMax+H3+Reference-多lora测试_2107115660827521025.json
name: MiniMax+H3+Reference-多lora测试_2107115660827521025
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/MiniMax+H3+Reference-多lora测试_2107115660827521025.json
hash: a432e796d52524ef
coverage: 0.882353
learned_at: 2026-11-14 00:41:59
nodes: [VAEDecodeAudio, VAEDecode, SamplerCustomAdvanced, BasicGuider, RandomNoise, CreateVideo, ImageResizeKJv2, PrimitiveFloat, EasyCache, Note, SaveVideo, CLIPLoader, VAELoader, LoadVideo, GetVideoComponents, LoadAudio, VAELoader, ComfyMathExpression, ImageResizeKJv2, ImageResizeKJv2, Note, KSamplerSelect, BasicScheduler, LoadImage, LoadImage, LoadImage, UNETLoader, MiniMaxH3ReferenceToVideo, LoadImage, ResolutionSelector, PathchSageAttentionKJ, PrimitiveStringMultiline, LoraLoaderModelOnly, LoraLoaderModelOnly]
patterns: []
missing: []
---

# 平台全量/MiniMax+H3+Reference-多lora测试_2107115660827521025.json

> 来源文件 `comfyui_library/workflows/平台全量/MiniMax+H3+Reference-多lora测试_2107115660827521025.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Process → Output → Other

**节点**（34 个）：
- `VAEDecodeAudio` ★核心
- `VAEDecode` ★核心
- `SamplerCustomAdvanced` ★核心
- `BasicGuider`
- `RandomNoise`
- `CreateVideo`
- `ImageResizeKJv2`
- `PrimitiveFloat`
- `EasyCache`
- `Note`
- `SaveVideo`
- `CLIPLoader`
- `VAELoader`
- `LoadVideo`
- `GetVideoComponents`
- `LoadAudio`
- `VAELoader`
- `ComfyMathExpression`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `Note`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `UNETLoader` ★核心
- `MiniMaxH3ReferenceToVideo`
- `LoadImage`
- `ResolutionSelector`
- `PathchSageAttentionKJ`
- `PrimitiveStringMultiline`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心

## 知识

覆盖率 **88%**（30/34）

**有卡**：`VAEDecodeAudio`、`VAEDecode`、`SamplerCustomAdvanced`、`BasicGuider`、`RandomNoise`、`CreateVideo`、`ImageResizeKJv2`、`EasyCache`、`SaveVideo`、`CLIPLoader`、`VAELoader`、`LoadVideo`、`GetVideoComponents`、`LoadAudio`、`ComfyMathExpression`、`KSamplerSelect`、`BasicScheduler`、`LoadImage`、`UNETLoader`、`MiniMaxH3ReferenceToVideo`、`ResolutionSelector`、`PathchSageAttentionKJ`、`LoraLoaderModelOnly`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect
