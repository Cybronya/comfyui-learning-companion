---
key: 视频生成/图生视频/minimax h3 r2v Latent Upscaler｜图生视频二采放大_2092058189146710017.json
name: minimax h3 r2v Latent Upscaler｜图生视频二采放大_2092058189146710017
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/minimax h3 r2v Latent Upscaler｜图生视频二采放大_2092058189146710017.json
hash: 02cc0aa82c50dda9
coverage: 0.903226
learned_at: 2026-10-16 22:59:31
nodes: [VAELoader, VAELoader, ManualSigmas, VAEDecode, VAEDecodeAudio, ModelPreviewOverrideKJ, SplitSigmas, CLIPLoader, SamplerCustomAdvanced, KSamplerSelect, SamplerCustomAdvanced, ManualSigmas, BasicScheduler, BasicGuider, UNETLoader, BasicGuider, ManualSigmas, ResolutionSelector, ComfyMathExpression, LTXVConcatAVLatent, RandomNoise, PrimitiveFloat, MinimaxH3LatentUpscaler3D, LTXVSeparateAVLatent, VAEDecode, VAEDecodeAudio, VHS_VideoCombine, MiniMaxH3SigmaShift, ModelAttentionBackend, MiniMaxH3ReferenceToVideo, PrimitiveStringMultiline, LoadImage, LoraLoaderModelOnly, 孤海注释, 孤海注释, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, KSampler, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, VAELoader, CLIPLoader, EmptyLatentImage, JjkText, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/minimax h3 r2v Latent Upscaler｜图生视频二采放大_2092058189146710017.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/minimax h3 r2v Latent Upscaler｜图生视频二采放大_2092058189146710017.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（62 个）：
- `VAELoader`
- `VAELoader`
- `ManualSigmas`
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `ModelPreviewOverrideKJ`
- `SplitSigmas`
- `CLIPLoader`
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `ManualSigmas`
- `BasicScheduler`
- `BasicGuider`
- `UNETLoader` ★核心
- `BasicGuider`
- `ManualSigmas`
- `ResolutionSelector`
- `ComfyMathExpression`
- `LTXVConcatAVLatent`
- `RandomNoise`
- `PrimitiveFloat`
- `MinimaxH3LatentUpscaler3D`
- `LTXVSeparateAVLatent`
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `VHS_VideoCombine`
- `MiniMaxH3SigmaShift`
- `ModelAttentionBackend`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveStringMultiline`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `孤海注释`
- `孤海注释`
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

覆盖率 **90%**（56/62）

**有卡**：`VAELoader`、`ManualSigmas`、`VAEDecode`、`VAEDecodeAudio`、`ModelPreviewOverrideKJ`、`SplitSigmas`、`CLIPLoader`、`SamplerCustomAdvanced`、`KSamplerSelect`、`BasicScheduler`、`BasicGuider`、`UNETLoader`、`ResolutionSelector`、`ComfyMathExpression`、`LTXVConcatAVLatent`、`RandomNoise`、`MinimaxH3LatentUpscaler3D`、`LTXVSeparateAVLatent`、`VHS_VideoCombine`、`MiniMaxH3SigmaShift`、`ModelAttentionBackend`、`MiniMaxH3ReferenceToVideo`、`LoadImage`、`LoraLoaderModelOnly`、`KSampler`、`CLIPTextEncode`、`solarL_SaveImagesToZip`、`EmptyLatentImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
