---
key: 视频生成/图生视频/MiniMax H3图生视频fastH3加速 trim latent放大增强_2110365841622659073.json
name: MiniMax H3图生视频fastH3加速 trim latent放大增强_2110365841622659073
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/MiniMax H3图生视频fastH3加速 trim latent放大增强_2110365841622659073.json
hash: 506bd820ed49f2ff
coverage: 0.875
learned_at: 2026-10-18 00:23:23
nodes: [ManualSigmas, VAEDecode, VAEDecodeAudio, VAELoader, MiniMaxH3ImageToVideo, PrimitiveFloat, CLIPLoader, ComfyMathExpression, SamplerCustomAdvanced, SamplerCustomAdvanced, KSamplerSelect, BasicGuider, BasicGuider, RandomNoise, PrimitiveStringMultiline, VAELoader, UNETLoader, MiniMaxH3SigmaShift, ModelAttentionBackend, BlockSparseAttention, MiniMaxH3ImageToVideo, BasicScheduler, ResolutionSelector, ManualSigmas, SplitSigmas, ManualSigmas, PrimitiveFloat, VHS_VideoCombine, PrimitiveNode, LoadImage, LTXVSeparateAVLatent, LTXVConcatAVLatent, ResolutionSelector, MinimaxH3LatentUpscaler3D, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPTextEncode, CLIPLoader, JjkText, VAEDecode, EmptyLatentImage, VAELoader, solarL_SaveImagesToZip, Note, SaveImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/MiniMax H3图生视频fastH3加速 trim latent放大增强_2110365841622659073.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/MiniMax H3图生视频fastH3加速 trim latent放大增强_2110365841622659073.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（64 个）：
- `ManualSigmas`
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `VAELoader`
- `MiniMaxH3ImageToVideo`
- `PrimitiveFloat`
- `CLIPLoader`
- `ComfyMathExpression`
- `SamplerCustomAdvanced` ★核心
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
- `BasicGuider`
- `BasicGuider`
- `RandomNoise`
- `PrimitiveStringMultiline`
- `VAELoader`
- `UNETLoader` ★核心
- `MiniMaxH3SigmaShift`
- `ModelAttentionBackend`
- `BlockSparseAttention`
- `MiniMaxH3ImageToVideo`
- `BasicScheduler`
- `ResolutionSelector`
- `ManualSigmas`
- `SplitSigmas`
- `ManualSigmas`
- `PrimitiveFloat`
- `VHS_VideoCombine`
- `PrimitiveNode`
- `LoadImage`
- `LTXVSeparateAVLatent`
- `LTXVConcatAVLatent`
- `ResolutionSelector`
- `MinimaxH3LatentUpscaler3D`
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
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `JjkText`
- `VAEDecode` ★核心
- `EmptyLatentImage` ★核心
- `VAELoader`
- `solarL_SaveImagesToZip`
- `Note`
- `SaveImage`

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

覆盖率 **88%**（56/64）

**有卡**：`ManualSigmas`、`VAEDecode`、`VAEDecodeAudio`、`VAELoader`、`MiniMaxH3ImageToVideo`、`CLIPLoader`、`ComfyMathExpression`、`SamplerCustomAdvanced`、`KSamplerSelect`、`BasicGuider`、`RandomNoise`、`UNETLoader`、`MiniMaxH3SigmaShift`、`ModelAttentionBackend`、`BlockSparseAttention`、`BasicScheduler`、`ResolutionSelector`、`SplitSigmas`、`VHS_VideoCombine`、`LoadImage`、`LTXVSeparateAVLatent`、`LTXVConcatAVLatent`、`MinimaxH3LatentUpscaler3D`、`LoraLoaderModelOnly`、`KSampler`、`CLIPTextEncode`、`EmptyLatentImage`、`solarL_SaveImagesToZip`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
