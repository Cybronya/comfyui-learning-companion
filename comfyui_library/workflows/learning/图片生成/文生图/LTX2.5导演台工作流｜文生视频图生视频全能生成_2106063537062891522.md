---
key: 图片生成/文生图/LTX2.5导演台工作流｜文生视频图生视频全能生成_2106063537062891522.json
name: LTX2.5导演台工作流｜文生视频图生视频全能生成_2106063537062891522
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/LTX2.5导演台工作流｜文生视频图生视频全能生成_2106063537062891522.json
hash: 458bd87616b58e70
coverage: 0.734375
learned_at: 2026-10-10 20:58:46
nodes: [CFGGuider, LTXVConcatAVLatent, SamplerCustomAdvanced, KSamplerSelect, GetNode, GetNode, GetNode, LTXVAudioVAEDecode, GetNode, CLIPLoader, VAELoaderKJ, VAELoaderKJ, SetNode, SetNode, SetNode, SetNode, DiffusionModelLoaderKJ, ConditioningZeroOut, GetNode, BasicScheduler, GetNode, RandomNoise, GetNode, GetNode, LTXDirectorCropGuides, CreateVideo, SetNode, VAEDecodeTiled, LTXVSeparateAVLatent, LTXDirectorGuide, LTXVConditioning, SaveVideo, TTResolutionSelector, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPLoader, CLIPTextEncode, JjkText, EmptyLatentImage, solarL_SaveImagesToZip, VAEDecode, VAELoader, Note, SaveImage, LTXDirector]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/LTX2.5导演台工作流｜文生视频图生视频全能生成_2106063537062891522.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/LTX2.5导演台工作流｜文生视频图生视频全能生成_2106063537062891522.json`

## 结构

**节点**（64 个）：
- `CFGGuider`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced`
- `KSamplerSelect`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVAudioVAEDecode`
- `GetNode`
- `CLIPLoader`
- `VAELoaderKJ`
- `VAELoaderKJ`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `DiffusionModelLoaderKJ`
- `ConditioningZeroOut`
- `GetNode`
- `BasicScheduler`
- `GetNode`
- `RandomNoise`
- `GetNode`
- `GetNode`
- `LTXDirectorCropGuides`
- `CreateVideo`
- `SetNode`
- `VAEDecodeTiled`
- `LTXVSeparateAVLatent`
- `LTXDirectorGuide`
- `LTXVConditioning`
- `SaveVideo`
- `TTResolutionSelector`
- `孤海注释`
- `孤海注释`
- `UNETLoader`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `KSampler`
- `CLIPTextEncode`
- `CLIPLoader`
- `CLIPTextEncode`
- `JjkText`
- `EmptyLatentImage`
- `solarL_SaveImagesToZip`
- `VAEDecode`
- `VAELoader`
- `Note`
- `SaveImage`
- `LTXDirector`

**识别到的模式**：text_to_image

## 关键参数

- `batch_size` = `1`
- `cfg` = `4.5`
- `denoise` = `1`
- `height` = `80`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `seed` = `598626327129635`
- `steps` = `4`
- `width` = `80`

## 知识

覆盖率 **73%**（47/64）

**有卡**：`CFGGuider`、`LTXVConcatAVLatent`、`SamplerCustomAdvanced`、`KSamplerSelect`、`GetNode`、`LTXVAudioVAEDecode`、`CLIPLoader`、`VAELoaderKJ`、`SetNode`、`DiffusionModelLoaderKJ`、`ConditioningZeroOut`、`BasicScheduler`、`RandomNoise`、`LTXDirectorCropGuides`、`CreateVideo`、`VAEDecodeTiled`、`LTXVSeparateAVLatent`、`LTXDirectorGuide`、`LTXVConditioning`、`SaveVideo`、`TTResolutionSelector`、`孤海注释`、`UNETLoader`、`LoraLoaderModelOnly`

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
