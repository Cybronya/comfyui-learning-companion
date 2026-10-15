---
key: 视频生成/文生视频/latent upscale潜空间放大｜Minimax H3 FL2VA版_2091024845919313921.json
name: latent upscale潜空间放大｜Minimax H3 FL2VA版_2091024845919313921
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/latent upscale潜空间放大｜Minimax H3 FL2VA版_2091024845919313921.json
hash: 0324e6bd6a406caa
coverage: 0.920635
learned_at: 2026-10-15 22:47:20
nodes: [VAEDecodeAudio, VAEDecodeAudio, ComfyMathExpression, VAEDecode, KSamplerSelect, BasicGuider, CreateVideo, LTXVConcatAVLatent, BasicGuider, LTXVSeparateAVLatent, RandomNoise, RandomNoise, ManualSigmas, ManualSigmas, VAEDecode, SamplerCustomAdvanced, ModelAttentionBackend, SplitSigmas, BasicScheduler, ManualSigmas, SamplerCustomAdvanced, MiniMaxH3ImageToVideo, ResolutionSelector, MiniMaxH3SigmaShift, PrimitiveFloat, VHS_VideoCombine, LoadImage, LoadImage, UNETLoader, CLIPLoader, VAELoader, VAELoader, LoraLoaderModelOnly, SaveVideo, 孤海注释, 孤海注释, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, KSampler, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, VAELoader, CLIPLoader, EmptyLatentImage, JjkText, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/latent upscale潜空间放大｜Minimax H3 FL2VA版_2091024845919313921.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/latent upscale潜空间放大｜Minimax H3 FL2VA版_2091024845919313921.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（63 个）：
- `VAEDecodeAudio` ★核心
- `VAEDecodeAudio` ★核心
- `ComfyMathExpression`
- `VAEDecode` ★核心
- `KSamplerSelect` ★核心
- `BasicGuider`
- `CreateVideo`
- `LTXVConcatAVLatent`
- `BasicGuider`
- `LTXVSeparateAVLatent`
- `RandomNoise`
- `RandomNoise`
- `ManualSigmas`
- `ManualSigmas`
- `VAEDecode` ★核心
- `SamplerCustomAdvanced` ★核心
- `ModelAttentionBackend`
- `SplitSigmas`
- `BasicScheduler`
- `ManualSigmas`
- `SamplerCustomAdvanced` ★核心
- `MiniMaxH3ImageToVideo`
- `ResolutionSelector`
- `MiniMaxH3SigmaShift`
- `PrimitiveFloat`
- `VHS_VideoCombine`
- `LoadImage`
- `LoadImage`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `SaveVideo`
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

覆盖率 **92%**（58/63）

**有卡**：`VAEDecodeAudio`、`ComfyMathExpression`、`VAEDecode`、`KSamplerSelect`、`BasicGuider`、`CreateVideo`、`LTXVConcatAVLatent`、`LTXVSeparateAVLatent`、`RandomNoise`、`ManualSigmas`、`SamplerCustomAdvanced`、`ModelAttentionBackend`、`SplitSigmas`、`BasicScheduler`、`MiniMaxH3ImageToVideo`、`ResolutionSelector`、`MiniMaxH3SigmaShift`、`VHS_VideoCombine`、`LoadImage`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`、`SaveVideo`、`KSampler`、`CLIPTextEncode`、`solarL_SaveImagesToZip`、`EmptyLatentImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
