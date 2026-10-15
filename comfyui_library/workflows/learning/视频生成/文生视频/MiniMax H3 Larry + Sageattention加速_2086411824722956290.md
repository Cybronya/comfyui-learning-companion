---
key: 视频生成/文生视频/MiniMax H3 Larry + Sageattention加速_2086411824722956290.json
name: MiniMax H3 Larry + Sageattention加速_2086411824722956290
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/MiniMax H3 Larry + Sageattention加速_2086411824722956290.json
hash: 111703a6c16c355d
coverage: 0.868132
learned_at: 2026-10-15 22:45:32
nodes: [VAELoader, VAELoader, VAEDecodeAudio, VAEDecode, SamplerCustomAdvanced, BasicGuider, RandomNoise, CreateVideo, ComfyMathExpression, PrimitiveFloat, ImageResizeKJv2, MiniMaxH3ImageToVideo, CLIPLoader, ResolutionSelector, LoadImage, PrimitiveStringMultiline, UNETLoader, KSamplerSelect, BasicScheduler, SaveVideo, VAELoader, VAELoader, VAEDecodeAudio, VAEDecode, SamplerCustomAdvanced, BasicGuider, RandomNoise, CreateVideo, ImageResizeKJv2, MiniMaxH3ImageToVideo, CLIPLoader, LoadImage, KSamplerSelect, BasicScheduler, SaveVideo, LoraLoaderModelOnly, PrimitiveFloat, ComfyMathExpression, ResolutionSelector, PrimitiveStringMultiline, UNETLoader, LoraLoaderModelOnly, VAELoader, VAELoader, VAEDecodeAudio, VAEDecode, SamplerCustomAdvanced, BasicGuider, RandomNoise, CreateVideo, ImageResizeKJv2, MiniMaxH3ImageToVideo, CLIPLoader, LoadImage, KSamplerSelect, BasicScheduler, SaveVideo, PrimitiveFloat, ComfyMathExpression, ResolutionSelector, PrimitiveStringMultiline, UNETLoader, VAELoader, VAELoader, VAEDecodeAudio, VAEDecode, SamplerCustomAdvanced, BasicGuider, RandomNoise, CreateVideo, ImageResizeKJv2, MiniMaxH3ImageToVideo, CLIPLoader, LoadImage, KSamplerSelect, BasicScheduler, SaveVideo, PrimitiveFloat, ComfyMathExpression, ResolutionSelector, PrimitiveStringMultiline, UNETLoader, LoraLoaderModelOnly, PatchFlashAttentionKJ, LoraLoaderModelOnly, PathchSageAttentionKJ, SolAttnPatch, Note, Note, Note, Note]
patterns: []
missing: []
---

# 视频生成/文生视频/MiniMax H3 Larry + Sageattention加速_2086411824722956290.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/MiniMax H3 Larry + Sageattention加速_2086411824722956290.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Process → Output → Other

**节点**（91 个）：
- `VAELoader`
- `VAELoader`
- `VAEDecodeAudio` ★核心
- `VAEDecode` ★核心
- `SamplerCustomAdvanced` ★核心
- `BasicGuider`
- `RandomNoise`
- `CreateVideo`
- `ComfyMathExpression`
- `PrimitiveFloat`
- `ImageResizeKJv2`
- `MiniMaxH3ImageToVideo`
- `CLIPLoader`
- `ResolutionSelector`
- `LoadImage`
- `PrimitiveStringMultiline`
- `UNETLoader` ★核心
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `SaveVideo`
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
- `LoadImage`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `SaveVideo`
- `LoraLoaderModelOnly` ★核心
- `PrimitiveFloat`
- `ComfyMathExpression`
- `ResolutionSelector`
- `PrimitiveStringMultiline`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
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
- `LoadImage`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `SaveVideo`
- `PrimitiveFloat`
- `ComfyMathExpression`
- `ResolutionSelector`
- `PrimitiveStringMultiline`
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
- `LoadImage`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `SaveVideo`
- `PrimitiveFloat`
- `ComfyMathExpression`
- `ResolutionSelector`
- `PrimitiveStringMultiline`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `PatchFlashAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `SolAttnPatch`
- `Note`
- `Note`
- `Note`
- `Note`

## 知识

覆盖率 **87%**（79/91）

**有卡**：`VAELoader`、`VAEDecodeAudio`、`VAEDecode`、`SamplerCustomAdvanced`、`BasicGuider`、`RandomNoise`、`CreateVideo`、`ComfyMathExpression`、`ImageResizeKJv2`、`MiniMaxH3ImageToVideo`、`CLIPLoader`、`ResolutionSelector`、`LoadImage`、`UNETLoader`、`KSamplerSelect`、`BasicScheduler`、`SaveVideo`、`LoraLoaderModelOnly`、`PatchFlashAttentionKJ`、`PathchSageAttentionKJ`、`SolAttnPatch`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect
