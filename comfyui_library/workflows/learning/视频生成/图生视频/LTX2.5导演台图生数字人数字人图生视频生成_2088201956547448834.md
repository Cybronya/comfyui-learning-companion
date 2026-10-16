---
key: 视频生成/图生视频/LTX2.5导演台图生数字人数字人图生视频生成_2088201956547448834.json
name: LTX2.5导演台图生数字人数字人图生视频生成_2088201956547448834
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.5导演台图生数字人数字人图生视频生成_2088201956547448834.json
hash: 44e445cb025a06ef
coverage: 0.921569
learned_at: 2026-10-16 21:43:22
nodes: [RandomNoise, BasicScheduler, KSamplerSelect, VAELoaderKJ, DiffusionModelLoaderKJ, VAELoaderKJ, LTXVConcatAVLatent, VAEDecodeTiled, LTXVSeparateAVLatent, YusuLTXDirectorCropGuides, SamplerCustomAdvanced, CFGGuider, YusuLTXDirectorGuide, LTXVConditioning, CLIPLoader, SaveVideo, LTXVAudioVAEDecode, CreateVideo, CLIPTextEncode, Label (rgthree), TTResolutionSelector, YusuLTXDirector, 孤海注释, 孤海注释, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, KSampler, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, VAELoader, CLIPLoader, EmptyLatentImage, JjkText, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/LTX2.5导演台图生数字人数字人图生视频生成_2088201956547448834.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/LTX2.5导演台图生数字人数字人图生视频生成_2088201956547448834.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（51 个）：
- `RandomNoise`
- `BasicScheduler`
- `KSamplerSelect` ★核心
- `VAELoaderKJ`
- `DiffusionModelLoaderKJ`
- `VAELoaderKJ`
- `LTXVConcatAVLatent`
- `VAEDecodeTiled` ★核心
- `LTXVSeparateAVLatent`
- `YusuLTXDirectorCropGuides`
- `SamplerCustomAdvanced` ★核心
- `CFGGuider`
- `YusuLTXDirectorGuide`
- `LTXVConditioning`
- `CLIPLoader`
- `SaveVideo`
- `LTXVAudioVAEDecode` ★核心
- `CreateVideo`
- `CLIPTextEncode` ★核心
- `Label (rgthree)`
- `TTResolutionSelector`
- `YusuLTXDirector`
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

覆盖率 **92%**（47/51）

**有卡**：`RandomNoise`、`BasicScheduler`、`KSamplerSelect`、`VAELoaderKJ`、`DiffusionModelLoaderKJ`、`LTXVConcatAVLatent`、`VAEDecodeTiled`、`LTXVSeparateAVLatent`、`YusuLTXDirectorCropGuides`、`SamplerCustomAdvanced`、`CFGGuider`、`YusuLTXDirectorGuide`、`LTXVConditioning`、`CLIPLoader`、`SaveVideo`、`LTXVAudioVAEDecode`、`CreateVideo`、`CLIPTextEncode`、`Label (rgthree)`、`TTResolutionSelector`、`YusuLTXDirector`、`LoraLoaderModelOnly`、`UNETLoader`、`KSampler`、`solarL_SaveImagesToZip`、`VAEDecode`、`VAELoader`、`EmptyLatentImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
