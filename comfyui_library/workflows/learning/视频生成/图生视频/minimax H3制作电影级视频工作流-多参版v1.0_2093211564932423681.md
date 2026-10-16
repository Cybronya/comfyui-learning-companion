---
key: 视频生成/图生视频/minimax H3制作电影级视频工作流-多参版v1.0_2093211564932423681.json
name: minimax H3制作电影级视频工作流-多参版v1.0_2093211564932423681
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/minimax H3制作电影级视频工作流-多参版v1.0_2093211564932423681.json
hash: f5d2acbf3d38f32a
coverage: 0.935484
learned_at: 2026-10-16 23:42:35
nodes: [BasicGuider, VAEDecode, RandomNoise, VAELoader, LoadAudio, CLIPLoader, UNETLoader, ComfyMathExpression, PixaromaLabel, VAELoader, LoraLoaderModelOnly, ResolutionSelector, VAEDecodeAudio, CreateVideo, SamplerCustomAdvanced, KSamplerSelect, BasicScheduler, PathchSageAttentionKJ, MiniMaxH3BlockCacheT8, LoraLoaderModelOnly, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, easy anythingIndexSwitch, VHS_LoadVideo, PrimitiveFloat, PrimitiveStringMultiline, LoadImage, MiniMaxH3ReferenceToVideo, SaveVideo]
patterns: []
missing: []
---

# 视频生成/图生视频/minimax H3制作电影级视频工作流-多参版v1.0_2093211564932423681.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/minimax H3制作电影级视频工作流-多参版v1.0_2093211564932423681.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Process → Output → Other

**节点**（31 个）：
- `BasicGuider`
- `VAEDecode` ★核心
- `RandomNoise`
- `VAELoader`
- `LoadAudio`
- `CLIPLoader`
- `UNETLoader` ★核心
- `ComfyMathExpression`
- `PixaromaLabel`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `ResolutionSelector`
- `VAEDecodeAudio` ★核心
- `CreateVideo`
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `PathchSageAttentionKJ`
- `MiniMaxH3BlockCacheT8`
- `LoraLoaderModelOnly` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `easy anythingIndexSwitch`
- `VHS_LoadVideo`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `LoadImage`
- `MiniMaxH3ReferenceToVideo`
- `SaveVideo`

## 知识

覆盖率 **94%**（29/31）

**有卡**：`BasicGuider`、`VAEDecode`、`RandomNoise`、`VAELoader`、`LoadAudio`、`CLIPLoader`、`UNETLoader`、`ComfyMathExpression`、`PixaromaLabel`、`LoraLoaderModelOnly`、`ResolutionSelector`、`VAEDecodeAudio`、`CreateVideo`、`SamplerCustomAdvanced`、`KSamplerSelect`、`BasicScheduler`、`PathchSageAttentionKJ`、`MiniMaxH3BlockCacheT8`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`easy anythingIndexSwitch`、`VHS_LoadVideo`、`MiniMaxH3ReferenceToVideo`、`SaveVideo`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect
