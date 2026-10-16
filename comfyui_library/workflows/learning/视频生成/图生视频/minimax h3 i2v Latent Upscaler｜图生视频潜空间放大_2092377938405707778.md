---
key: 视频生成/图生视频/minimax h3 i2v Latent Upscaler｜图生视频潜空间放大_2092377938405707778.json
name: minimax h3 i2v Latent Upscaler｜图生视频潜空间放大_2092377938405707778
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/minimax h3 i2v Latent Upscaler｜图生视频潜空间放大_2092377938405707778.json
hash: 0a4a4f85c4909ccb
coverage: 0.912088
learned_at: 2026-10-16 22:59:31
nodes: [VAEDecodeAudio, VAELoader, VAEDecode, VAELoader, LTXVConcatAVLatent, ManualSigmas, KSamplerSelect, ManualSigmas, BasicGuider, BasicGuider, MiniMaxH3SigmaShift, UNETLoader, CLIPLoader, VAEDecodeAudio, SamplerCustomAdvanced, ComfyMathExpression, BasicScheduler, SplitSigmas, ManualSigmas, VHS_VideoCombine, PrimitiveFloat, PrimitiveFloat, RandomNoise, MiniMaxH3ImageToVideo, MiniMaxH3ImageToVideo, LoraLoaderModelOnly, ModelPreviewOverrideKJ, ImageResizeKJv2, LTXVSeparateAVLatent, SamplerCustomAdvanced, MinimaxH3LatentUpscaler3D, ModelAttentionBackend, ResolutionSelector, ResolutionSelector, PrimitiveStringMultiline, LoadImage, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, KSampler, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, VAELoader, CLIPLoader, EmptyLatentImage, JjkText, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPLoader, CLIPTextEncode, JjkText, EmptyLatentImage, solarL_SaveImagesToZip, VAEDecode, VAELoader, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/minimax h3 i2v Latent Upscaler｜图生视频潜空间放大_2092377938405707778.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/minimax h3 i2v Latent Upscaler｜图生视频潜空间放大_2092377938405707778.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（91 个）：
- `VAEDecodeAudio` ★核心
- `VAELoader`
- `VAEDecode` ★核心
- `VAELoader`
- `LTXVConcatAVLatent`
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `BasicGuider`
- `BasicGuider`
- `MiniMaxH3SigmaShift`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAEDecodeAudio` ★核心
- `SamplerCustomAdvanced` ★核心
- `ComfyMathExpression`
- `BasicScheduler`
- `SplitSigmas`
- `ManualSigmas`
- `VHS_VideoCombine`
- `PrimitiveFloat`
- `PrimitiveFloat`
- `RandomNoise`
- `MiniMaxH3ImageToVideo`
- `MiniMaxH3ImageToVideo`
- `LoraLoaderModelOnly` ★核心
- `ModelPreviewOverrideKJ`
- `ImageResizeKJv2`
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `MinimaxH3LatentUpscaler3D`
- `ModelAttentionBackend`
- `ResolutionSelector`
- `ResolutionSelector`
- `PrimitiveStringMultiline`
- `LoadImage`
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
- `UNETLoader` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `solarL_SaveImagesToZip`
- `VAEDecode` ★核心
- `VAELoader`
- `CLIPLoader`
- `EmptyLatentImage` ★核心
- `JjkText`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
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

覆盖率 **91%**（83/91）

**有卡**：`VAEDecodeAudio`、`VAELoader`、`VAEDecode`、`LTXVConcatAVLatent`、`ManualSigmas`、`KSamplerSelect`、`BasicGuider`、`MiniMaxH3SigmaShift`、`UNETLoader`、`CLIPLoader`、`SamplerCustomAdvanced`、`ComfyMathExpression`、`BasicScheduler`、`SplitSigmas`、`VHS_VideoCombine`、`RandomNoise`、`MiniMaxH3ImageToVideo`、`LoraLoaderModelOnly`、`ModelPreviewOverrideKJ`、`ImageResizeKJv2`、`LTXVSeparateAVLatent`、`MinimaxH3LatentUpscaler3D`、`ModelAttentionBackend`、`ResolutionSelector`、`LoadImage`、`KSampler`、`CLIPTextEncode`、`solarL_SaveImagesToZip`、`EmptyLatentImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
