---
key: 视频生成/文生视频/H3提示词Skills V2.5优化台词多合一极简版，文生视频图生视频方案_2103960622621872129.json
name: H3提示词Skills V2.5优化台词多合一极简版，文生视频图生视频方案_2103960622621872129
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/H3提示词Skills V2.5优化台词多合一极简版，文生视频图生视频方案_2103960622621872129.json
hash: eaa331fbf413a460
coverage: 0.892857
learned_at: 2026-10-15 22:44:21
nodes: [BasicGuider, RandomNoise, KSamplerSelect, MiniMaxH3EasyOutput, LoadVideo, SamplerCustomAdvanced, MiniMaxH3EasyLoader, BasicScheduler, VAEDecode, VAEDecodeAudio, LoraLoaderModelOnly, ModelAttentionBackend, SamplerCustomAdvanced, ModelPreviewOverrideKJ, VHS_VideoCombine, MiniMaxH3EasyMediaLoader, PrimitiveStringMultiline, SplitSigmas, VAEDecodeAudio, VAEDecode, VHS_VideoCombine, LTXVSeparateAVLatent, LTXVConcatAVLatent, MinimaxH3LatentUpscaler3D, PrimitiveStringMultiline, MiniMaxH3Easy, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note, SaveImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/H3提示词Skills V2.5优化台词多合一极简版，文生视频图生视频方案_2103960622621872129.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/H3提示词Skills V2.5优化台词多合一极简版，文生视频图生视频方案_2103960622621872129.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（56 个）：
- `BasicGuider`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `MiniMaxH3EasyOutput`
- `LoadVideo`
- `SamplerCustomAdvanced` ★核心
- `MiniMaxH3EasyLoader`
- `BasicScheduler`
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelAttentionBackend`
- `SamplerCustomAdvanced` ★核心
- `ModelPreviewOverrideKJ`
- `VHS_VideoCombine`
- `MiniMaxH3EasyMediaLoader`
- `PrimitiveStringMultiline`
- `SplitSigmas`
- `VAEDecodeAudio` ★核心
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `LTXVSeparateAVLatent`
- `LTXVConcatAVLatent`
- `MinimaxH3LatentUpscaler3D`
- `PrimitiveStringMultiline`
- `MiniMaxH3Easy`
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
- `EmptyLatentImage` ★核心
- `JjkText`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `solarL_SaveImagesToZip`
- `VAEDecode` ★核心
- `CLIPLoader`
- `VAELoader`
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

覆盖率 **89%**（50/56）

**有卡**：`BasicGuider`、`RandomNoise`、`KSamplerSelect`、`MiniMaxH3EasyOutput`、`LoadVideo`、`SamplerCustomAdvanced`、`MiniMaxH3EasyLoader`、`BasicScheduler`、`VAEDecode`、`VAEDecodeAudio`、`LoraLoaderModelOnly`、`ModelAttentionBackend`、`ModelPreviewOverrideKJ`、`VHS_VideoCombine`、`MiniMaxH3EasyMediaLoader`、`SplitSigmas`、`LTXVSeparateAVLatent`、`LTXVConcatAVLatent`、`MinimaxH3LatentUpscaler3D`、`MiniMaxH3Easy`、`UNETLoader`、`KSampler`、`EmptyLatentImage`、`CLIPTextEncode`、`solarL_SaveImagesToZip`、`CLIPLoader`、`VAELoader`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、SaveImage、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
