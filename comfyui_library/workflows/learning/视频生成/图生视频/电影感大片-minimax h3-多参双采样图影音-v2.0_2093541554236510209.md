---
key: 视频生成/图生视频/电影感大片-minimax h3-多参双采样图影音-v2.0_2093541554236510209.json
name: 电影感大片-minimax h3-多参双采样图影音-v2.0_2093541554236510209
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/电影感大片-minimax h3-多参双采样图影音-v2.0_2093541554236510209.json
hash: 1c25dc746b75a3b5
coverage: 0.787234
learned_at: 2026-10-16 23:43:12
nodes: [VAEDecodeAudio, SamplerCustomAdvanced, VAEDecode, LoraLoaderBypassModelOnly, PathchSageAttentionKJ, LoraLoaderBypassModelOnly, PathchSageAttentionKJ, MiniMaxH3BlockCacheT8, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, Note, CreateVideo, BasicGuider, BasicScheduler, SplitSigmas, MiniMaxH3BlockCacheT8, CLIPLoader, VAELoader, VAELoader, BasicGuider, KSamplerSelect, SamplerCustomAdvanced, DisableNoise, MiniMaxH3ReferenceToVideo, 孤海注释, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, ComfyMathExpression, PrimitiveFloat, ResolutionSelector, LoadImage, VHS_LoadVideo, SaveVideo, PrimitiveStringMultiline, H3SigmaRefiner, Note, 孤海注释, 孤海注释, 孤海注释, 孤海注释, RandomNoise, Note, easy anythingIndexSwitch]
patterns: []
missing: []
---

# 视频生成/图生视频/电影感大片-minimax h3-多参双采样图影音-v2.0_2093541554236510209.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/电影感大片-minimax h3-多参双采样图影音-v2.0_2093541554236510209.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Process → Output → Other

**节点**（47 个）：
- `VAEDecodeAudio` ★核心
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `LoraLoaderBypassModelOnly` ★核心
- `PathchSageAttentionKJ`
- `LoraLoaderBypassModelOnly` ★核心
- `PathchSageAttentionKJ`
- `MiniMaxH3BlockCacheT8`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `Note`
- `CreateVideo`
- `BasicGuider`
- `BasicScheduler`
- `SplitSigmas`
- `MiniMaxH3BlockCacheT8`
- `CLIPLoader`
- `VAELoader`
- `VAELoader`
- `BasicGuider`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `DisableNoise`
- `MiniMaxH3ReferenceToVideo`
- `孤海注释`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadAudio`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `ComfyMathExpression`
- `PrimitiveFloat`
- `ResolutionSelector`
- `LoadImage`
- `VHS_LoadVideo`
- `SaveVideo`
- `PrimitiveStringMultiline`
- `H3SigmaRefiner`
- `Note`
- `孤海注释`
- `孤海注释`
- `孤海注释`
- `孤海注释`
- `RandomNoise`
- `Note`
- `easy anythingIndexSwitch`

## 知识

覆盖率 **79%**（37/47）

**有卡**：`VAEDecodeAudio`、`SamplerCustomAdvanced`、`VAEDecode`、`LoraLoaderBypassModelOnly`、`PathchSageAttentionKJ`、`MiniMaxH3BlockCacheT8`、`LoraLoaderModelOnly`、`UNETLoader`、`CreateVideo`、`BasicGuider`、`BasicScheduler`、`SplitSigmas`、`CLIPLoader`、`VAELoader`、`KSamplerSelect`、`DisableNoise`、`MiniMaxH3ReferenceToVideo`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadAudio`、`LoadImage`、`ComfyMathExpression`、`ResolutionSelector`、`VHS_LoadVideo`、`SaveVideo`、`H3SigmaRefiner`、`RandomNoise`、`easy anythingIndexSwitch`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect
