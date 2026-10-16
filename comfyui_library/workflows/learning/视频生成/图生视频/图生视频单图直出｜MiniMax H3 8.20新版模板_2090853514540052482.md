---
key: 视频生成/图生视频/图生视频单图直出｜MiniMax H3 8.20新版模板_2090853514540052482.json
name: 图生视频单图直出｜MiniMax H3 8.20新版模板_2090853514540052482
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/图生视频单图直出｜MiniMax H3 8.20新版模板_2090853514540052482.json
hash: f97bce9751083396
coverage: 0.925373
learned_at: 2026-10-16 22:31:04
nodes: [MiniMaxH3MemoryEfficientSageAttentionPatch, LoadImage, LoadImage, LoadAudio, LoadAudio, UNETLoader, PrimitiveFloat, SigmasToFloat, KSamplerSelect, VAELoader, ComfyMathExpression, BasicGuider, VAEDecode, VAEDecodeAudio, CLIPLoader, RandomNoise, LoadImage, Lora Loader Stack (rgthree), LoadImage, PixaromaSaveMp4, BasicScheduler, VAELoader, LoadImage, LoadImage, ResolutionSelector, LoadAudio, MiniMaxH3SigmaShift, SplitSigmas, SamplerCustomAdvanced, LTXVSeparateAVLatent, MinimaxH3LatentUpscalerNode3D, LTXVConcatAVLatent, SamplerCustomAdvanced, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, MiniMaxH3ReferenceToVideo, LoadImage, LoadImage, LoadImage, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, JjkText, solarL_SaveImagesToZip, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/图生视频单图直出｜MiniMax H3 8.20新版模板_2090853514540052482.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/图生视频单图直出｜MiniMax H3 8.20新版模板_2090853514540052482.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（67 个）：
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `LoadImage`
- `LoadImage`
- `LoadAudio`
- `LoadAudio`
- `UNETLoader` ★核心
- `PrimitiveFloat`
- `SigmasToFloat`
- `KSamplerSelect` ★核心
- `VAELoader`
- `ComfyMathExpression`
- `BasicGuider`
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `CLIPLoader`
- `RandomNoise`
- `LoadImage`
- `Lora Loader Stack (rgthree)`
- `LoadImage`
- `PixaromaSaveMp4`
- `BasicScheduler`
- `VAELoader`
- `LoadImage`
- `LoadImage`
- `ResolutionSelector`
- `LoadAudio`
- `MiniMaxH3SigmaShift`
- `SplitSigmas`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `MinimaxH3LatentUpscalerNode3D`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `MiniMaxH3ReferenceToVideo`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `JjkText`
- `solarL_SaveImagesToZip`
- `CLIPTextEncode` ★核心
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
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `80`
- `height` = `80`
- `batch_size` = `1`
- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **93%**（62/67）

**有卡**：`MiniMaxH3MemoryEfficientSageAttentionPatch`、`LoadImage`、`LoadAudio`、`UNETLoader`、`SigmasToFloat`、`KSamplerSelect`、`VAELoader`、`ComfyMathExpression`、`BasicGuider`、`VAEDecode`、`VAEDecodeAudio`、`CLIPLoader`、`RandomNoise`、`Lora Loader Stack (rgthree)`、`PixaromaSaveMp4`、`BasicScheduler`、`ResolutionSelector`、`MiniMaxH3SigmaShift`、`SplitSigmas`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`MinimaxH3LatentUpscalerNode3D`、`LTXVConcatAVLatent`、`easy cleanGpuUsed`、`MiniMaxH3ReferenceToVideo`、`CLIPTextEncode`、`EmptyLatentImage`、`KSampler`、`solarL_SaveImagesToZip`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
