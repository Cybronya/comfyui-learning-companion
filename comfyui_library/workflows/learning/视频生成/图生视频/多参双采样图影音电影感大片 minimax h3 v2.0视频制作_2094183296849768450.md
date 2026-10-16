---
key: 视频生成/图生视频/多参双采样图影音电影感大片 minimax h3 v2.0视频制作_2094183296849768450.json
name: 多参双采样图影音电影感大片 minimax h3 v2.0视频制作_2094183296849768450
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/多参双采样图影音电影感大片 minimax h3 v2.0视频制作_2094183296849768450.json
hash: f2a38758eb823051
coverage: 0.911765
learned_at: 2026-10-16 23:43:00
nodes: [VAEDecodeAudio, SamplerCustomAdvanced, VAEDecode, LoraLoaderBypassModelOnly, PathchSageAttentionKJ, LoraLoaderBypassModelOnly, PathchSageAttentionKJ, MiniMaxH3BlockCacheT8, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, CreateVideo, BasicGuider, BasicScheduler, SplitSigmas, MiniMaxH3BlockCacheT8, CLIPLoader, VAELoader, VAELoader, BasicGuider, KSamplerSelect, SamplerCustomAdvanced, DisableNoise, MiniMaxH3ReferenceToVideo, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, ComfyMathExpression, PrimitiveFloat, ResolutionSelector, LoadImage, VHS_LoadVideo, SaveVideo, PrimitiveStringMultiline, H3SigmaRefiner, RandomNoise, easy anythingIndexSwitch, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPLoader, CLIPTextEncode, JjkText, EmptyLatentImage, solarL_SaveImagesToZip, VAEDecode, VAELoader, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/多参双采样图影音电影感大片 minimax h3 v2.0视频制作_2094183296849768450.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/多参双采样图影音电影感大片 minimax h3 v2.0视频制作_2094183296849768450.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（68 个）：
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
- `RandomNoise`
- `easy anythingIndexSwitch`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `JjkText`
- `EmptyLatentImage` ★核心
- `solarL_SaveImagesToZip`
- `VAEDecode` ★核心
- `VAELoader`
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`
- `width` = `80`
- `height` = `80`
- `batch_size` = `1`

## 知识

覆盖率 **91%**（62/68）

**有卡**：`VAEDecodeAudio`、`SamplerCustomAdvanced`、`VAEDecode`、`LoraLoaderBypassModelOnly`、`PathchSageAttentionKJ`、`MiniMaxH3BlockCacheT8`、`LoraLoaderModelOnly`、`UNETLoader`、`CreateVideo`、`BasicGuider`、`BasicScheduler`、`SplitSigmas`、`CLIPLoader`、`VAELoader`、`KSamplerSelect`、`DisableNoise`、`MiniMaxH3ReferenceToVideo`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadAudio`、`LoadImage`、`ComfyMathExpression`、`ResolutionSelector`、`VHS_LoadVideo`、`SaveVideo`、`H3SigmaRefiner`、`RandomNoise`、`easy anythingIndexSwitch`、`KSampler`、`CLIPTextEncode`、`EmptyLatentImage`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
