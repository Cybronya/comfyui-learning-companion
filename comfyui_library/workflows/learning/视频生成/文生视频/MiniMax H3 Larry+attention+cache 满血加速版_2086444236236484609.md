---
key: 视频生成/文生视频/MiniMax H3 Larry+attention+cache 满血加速版_2086444236236484609.json
name: MiniMax H3 Larry+attention+cache 满血加速版_2086444236236484609
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/MiniMax H3 Larry+attention+cache 满血加速版_2086444236236484609.json
hash: a8d596dc13cb908c
coverage: 0.873239
learned_at: 2026-10-15 22:45:32
nodes: [VAELoader, VAELoader, VAEDecodeAudio, VAEDecode, SamplerCustomAdvanced, BasicGuider, RandomNoise, CreateVideo, ImageResizeKJv2, MiniMaxH3ImageToVideo, CLIPLoader, KSamplerSelect, BasicScheduler, PrimitiveFloat, ComfyMathExpression, ResolutionSelector, UNETLoader, VAELoader, VAELoader, VAEDecodeAudio, VAEDecode, SamplerCustomAdvanced, BasicGuider, RandomNoise, CreateVideo, ImageResizeKJv2, MiniMaxH3ImageToVideo, CLIPLoader, KSamplerSelect, BasicScheduler, SaveVideo, PrimitiveFloat, ComfyMathExpression, ResolutionSelector, UNETLoader, Note, LoraLoaderModelOnly, PathchSageAttentionKJ, LoraLoaderModelOnly, PathchSageAttentionKJ, VAELoader, VAELoader, VAEDecodeAudio, VAEDecode, SamplerCustomAdvanced, BasicGuider, RandomNoise, CreateVideo, ImageResizeKJv2, MiniMaxH3ImageToVideo, CLIPLoader, KSamplerSelect, BasicScheduler, SaveVideo, PrimitiveFloat, ComfyMathExpression, ResolutionSelector, UNETLoader, LoraLoaderModelOnly, PathchSageAttentionKJ, EasyCache, SpectrumApplyMiniMaxH3, Note, LoadImage, PrimitiveStringMultiline, PrimitiveStringMultiline, LoadImage, PrimitiveStringMultiline, LoadImage, Note, SaveVideo]
patterns: []
missing: []
---

# 视频生成/文生视频/MiniMax H3 Larry+attention+cache 满血加速版_2086444236236484609.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/MiniMax H3 Larry+attention+cache 满血加速版_2086444236236484609.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Process → Output → Other

**节点**（71 个）：
- `VAELoader`
- `VAELoader`
- `VAEDecodeAudio` ★核心
- `VAEDecode` ★核心
- `SamplerCustomAdvanced` ★核心
- `BasicGuider`
- `RandomNoise`
- `CreateVideo`
- `ImageResizeKJv2`
- `MiniMaxH3ImageToVideo`
- `CLIPLoader`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `PrimitiveFloat`
- `ComfyMathExpression`
- `ResolutionSelector`
- `UNETLoader` ★核心
- `VAELoader`
- `VAELoader`
- `VAEDecodeAudio` ★核心
- `VAEDecode` ★核心
- `SamplerCustomAdvanced` ★核心
- `BasicGuider`
- `RandomNoise`
- `CreateVideo`
- `ImageResizeKJv2`
- `MiniMaxH3ImageToVideo`
- `CLIPLoader`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `SaveVideo`
- `PrimitiveFloat`
- `ComfyMathExpression`
- `ResolutionSelector`
- `UNETLoader` ★核心
- `Note`
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `VAELoader`
- `VAELoader`
- `VAEDecodeAudio` ★核心
- `VAEDecode` ★核心
- `SamplerCustomAdvanced` ★核心
- `BasicGuider`
- `RandomNoise`
- `CreateVideo`
- `ImageResizeKJv2`
- `MiniMaxH3ImageToVideo`
- `CLIPLoader`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `SaveVideo`
- `PrimitiveFloat`
- `ComfyMathExpression`
- `ResolutionSelector`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `EasyCache`
- `SpectrumApplyMiniMaxH3`
- `Note`
- `LoadImage`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `LoadImage`
- `PrimitiveStringMultiline`
- `LoadImage`
- `Note`
- `SaveVideo`

## 知识

覆盖率 **87%**（62/71）

**有卡**：`VAELoader`、`VAEDecodeAudio`、`VAEDecode`、`SamplerCustomAdvanced`、`BasicGuider`、`RandomNoise`、`CreateVideo`、`ImageResizeKJv2`、`MiniMaxH3ImageToVideo`、`CLIPLoader`、`KSamplerSelect`、`BasicScheduler`、`ComfyMathExpression`、`ResolutionSelector`、`UNETLoader`、`SaveVideo`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`EasyCache`、`SpectrumApplyMiniMaxH3`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect
