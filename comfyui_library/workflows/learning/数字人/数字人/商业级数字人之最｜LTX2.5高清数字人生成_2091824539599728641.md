---
key: 数字人/数字人/商业级数字人之最｜LTX2.5高清数字人生成_2091824539599728641.json
name: 商业级数字人之最｜LTX2.5高清数字人生成_2091824539599728641
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/商业级数字人之最｜LTX2.5高清数字人生成_2091824539599728641.json
hash: a2815c2f46fe11c2
coverage: 0.934426
learned_at: 2026-10-18 22:17:14
nodes: [LTXVLatentUpsampler, LTXVDualCFGGuider, LTXVConcatAVLatent, SamplerCustomAdvanced, KSamplerSelect, ManualSigmas, LTXVSeparateAVLatent, LTXVAudioVAEDecode, LTXVConditioning, LTXVDualCFGGuider, LTXVConcatAVLatent, RandomNoise, SamplerCustomAdvanced, KSamplerSelect, ManualSigmas, LTXVSeparateAVLatent, LTXDirectorCropGuides, LTXDirectorCropGuides, LTXDirectorGuide, SaveVideo, LTX2_NAG, CreateVideo, VAEDecodeTiled, LatentUpscaleModelLoader, LTXDirectorGuide, LTX2_NAG, VAELoader, VAELoader, LTXDirector, CLIPLoader, UNETLoader, RandomNoise, LoadVideoUI, CLIPTextEncode, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, JjkText, solarL_SaveImagesToZip, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 数字人/数字人/商业级数字人之最｜LTX2.5高清数字人生成_2091824539599728641.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/商业级数字人之最｜LTX2.5高清数字人生成_2091824539599728641.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（61 个）：
- `LTXVLatentUpsampler` ★核心
- `LTXVDualCFGGuider`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `LTXVConditioning`
- `LTXVDualCFGGuider`
- `LTXVConcatAVLatent`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LTXVSeparateAVLatent`
- `LTXDirectorCropGuides`
- `LTXDirectorCropGuides`
- `LTXDirectorGuide`
- `SaveVideo`
- `LTX2_NAG`
- `CreateVideo`
- `VAEDecodeTiled` ★核心
- `LatentUpscaleModelLoader`
- `LTXDirectorGuide`
- `LTX2_NAG`
- `VAELoader`
- `VAELoader`
- `LTXDirector`
- `CLIPLoader`
- `UNETLoader` ★核心
- `RandomNoise`
- `LoadVideoUI`
- `CLIPTextEncode` ★核心
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

覆盖率 **93%**（57/61）

**有卡**：`LTXVLatentUpsampler`、`LTXVDualCFGGuider`、`LTXVConcatAVLatent`、`SamplerCustomAdvanced`、`KSamplerSelect`、`ManualSigmas`、`LTXVSeparateAVLatent`、`LTXVAudioVAEDecode`、`LTXVConditioning`、`RandomNoise`、`LTXDirectorCropGuides`、`LTXDirectorGuide`、`SaveVideo`、`LTX2_NAG`、`CreateVideo`、`VAEDecodeTiled`、`LatentUpscaleModelLoader`、`VAELoader`、`LTXDirector`、`CLIPLoader`、`UNETLoader`、`LoadVideoUI`、`CLIPTextEncode`、`EmptyLatentImage`、`KSampler`、`VAEDecode`、`solarL_SaveImagesToZip`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
