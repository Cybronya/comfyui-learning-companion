---
key: 视频生成/文生视频/导演台工作流｜LTX2.5文生图生视频生视频工作流_2088104395111231490.json
name: 导演台工作流｜LTX2.5文生图生视频生视频工作流_2088104395111231490
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/导演台工作流｜LTX2.5文生图生视频生视频工作流_2088104395111231490.json
hash: 4e107af585e99bf8
coverage: 0.921875
learned_at: 2026-10-15 22:48:33
nodes: [AudioCrop, MelBandRoFormerModelLoader, LoadImage, LoadImage, LiconMSR, LoadImage, CFGGuider, RandomNoise, LoadImage, VHS_VideoCombine, TTResolutionSelector, LTXVConcatAVLatent, LoadAudio, PreviewAudio, MelBandRoFormerSampler, YusuLTXDirectorGuide, ConditioningZeroOut, LTXVConditioning, LTXVSeparateAVLatent, YusuLTXDirectorCropGuides, BasicScheduler, CreateVideo, LTXVAudioVAEDecode, VAEDecodeTiled, YusuLTXDirector, CLIPLoader, VAELoaderKJ, VAELoaderKJ, TTResolutionSelector, SamplerCustomAdvanced, KSamplerSelect, Label (rgthree), Label (rgthree), Label (rgthree), DiffusionModelLoaderKJ, Fast Groups Bypasser (rgthree), SaveVideo, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, JjkText, solarL_SaveImagesToZip, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/导演台工作流｜LTX2.5文生图生视频生视频工作流_2088104395111231490.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/导演台工作流｜LTX2.5文生图生视频生视频工作流_2088104395111231490.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（64 个）：
- `AudioCrop`
- `MelBandRoFormerModelLoader`
- `LoadImage`
- `LoadImage`
- `LiconMSR`
- `LoadImage`
- `CFGGuider`
- `RandomNoise`
- `LoadImage`
- `VHS_VideoCombine`
- `TTResolutionSelector`
- `LTXVConcatAVLatent`
- `LoadAudio`
- `PreviewAudio`
- `MelBandRoFormerSampler` ★核心
- `YusuLTXDirectorGuide`
- `ConditioningZeroOut`
- `LTXVConditioning`
- `LTXVSeparateAVLatent`
- `YusuLTXDirectorCropGuides`
- `BasicScheduler`
- `CreateVideo`
- `LTXVAudioVAEDecode` ★核心
- `VAEDecodeTiled` ★核心
- `YusuLTXDirector`
- `CLIPLoader`
- `VAELoaderKJ`
- `VAELoaderKJ`
- `TTResolutionSelector`
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `DiffusionModelLoaderKJ`
- `Fast Groups Bypasser (rgthree)`
- `SaveVideo`
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

覆盖率 **92%**（59/64）

**有卡**：`AudioCrop`、`MelBandRoFormerModelLoader`、`LoadImage`、`LiconMSR`、`CFGGuider`、`RandomNoise`、`VHS_VideoCombine`、`TTResolutionSelector`、`LTXVConcatAVLatent`、`LoadAudio`、`PreviewAudio`、`MelBandRoFormerSampler`、`YusuLTXDirectorGuide`、`ConditioningZeroOut`、`LTXVConditioning`、`LTXVSeparateAVLatent`、`YusuLTXDirectorCropGuides`、`BasicScheduler`、`CreateVideo`、`LTXVAudioVAEDecode`、`VAEDecodeTiled`、`YusuLTXDirector`、`CLIPLoader`、`VAELoaderKJ`、`SamplerCustomAdvanced`、`KSamplerSelect`、`Label (rgthree)`、`DiffusionModelLoaderKJ`、`SaveVideo`、`UNETLoader`、`CLIPTextEncode`、`VAELoader`、`EmptyLatentImage`、`KSampler`、`VAEDecode`、`solarL_SaveImagesToZip`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
