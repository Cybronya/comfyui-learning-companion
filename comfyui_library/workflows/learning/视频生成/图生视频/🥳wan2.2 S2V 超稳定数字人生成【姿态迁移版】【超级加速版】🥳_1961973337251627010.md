---
key: 视频生成/图生视频/🥳wan2.2 S2V 超稳定数字人生成【姿态迁移版】【超级加速版】🥳_1961973337251627010.json
name: 🥳wan2.2 S2V 超稳定数字人生成【姿态迁移版】【超级加速版】🥳_1961973337251627010.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/🥳wan2.2 S2V 超稳定数字人生成【姿态迁移版】【超级加速版】🥳_1961973337251627010.json
hash: 6d9cf4f266ee8967
coverage: 0.93617
learned_at: 2026-10-15 22:31:29
nodes: [ModelSamplingSD3, CLIPTextEncode, CLIPLoader, CLIPTextEncode, AudioEncoderEncode, SimpleMath+, ImpactInt, PathchSageAttentionKJ, ImpactInt, Float, ImpactInt, PreviewImage, AIO_Preprocessor, Audio Duration (mtb), ImageConcanate, ImageConcanate, AudioSeparation, JWIntegerToString, JWIntegerToString, SimpleMath+, VAELoader, WanSoundImageToVideo, easy showAnything, AudioEncoderLoader, easy convertAnything, ImageResizeKJv2, CR Text, MarkdownNote, Note Plus (mtb), VHS_VideoCombine, GIMMVFI_interpolate, DownloadAndLoadGIMMVFIModel, UpscaleModelLoader, LoadImage, VHS_LoadVideo, VHS_VideoCombine, VAEDecode, VHS_VideoCombine, VHS_VideoCombine, ImageScaleToMegapixels, AudioCrop, VHS_VideoCombine, LoadAudio, LoraLoaderModelOnly, UNETLoader, KSampler, ImpactInt]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 666, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/🥳wan2.2 S2V 超稳定数字人生成【姿态迁移版】【超级加速版】🥳_1961973337251627010.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1961973337251627010.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（47 个）：
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `AudioEncoderEncode`
- `SimpleMath+`
- `ImpactInt`
- `PathchSageAttentionKJ`
- `ImpactInt`
- `Float`
- `ImpactInt`
- `PreviewImage`
- `AIO_Preprocessor`
- `Audio Duration (mtb)`
- `ImageConcanate`
- `ImageConcanate`
- `AudioSeparation`
- `JWIntegerToString`
- `JWIntegerToString`
- `SimpleMath+`
- `VAELoader`
- `WanSoundImageToVideo`
- `easy showAnything`
- `AudioEncoderLoader`
- `easy convertAnything`
- `ImageResizeKJv2`
- `CR Text`
- `MarkdownNote`
- `Note Plus (mtb)`
- `VHS_VideoCombine`
- `GIMMVFI_interpolate`
- `DownloadAndLoadGIMMVFIModel`
- `UpscaleModelLoader`
- `LoadImage`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `ImageScaleToMegapixels`
- `AudioCrop`
- `VHS_VideoCombine`
- `LoadAudio`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `KSampler` ★核心
- `ImpactInt`

## 关键参数

- `seed` = `666`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **94%**（44/47）

**有卡**：`ModelSamplingSD3`、`CLIPTextEncode`、`CLIPLoader`、`AudioEncoderEncode`、`SimpleMath+`、`ImpactInt`、`PathchSageAttentionKJ`、`Float`、`AIO_Preprocessor`、`Audio Duration (mtb)`、`ImageConcanate`、`AudioSeparation`、`JWIntegerToString`、`VAELoader`、`WanSoundImageToVideo`、`AudioEncoderLoader`、`easy convertAnything`、`ImageResizeKJv2`、`CR Text`、`Note Plus (mtb)`、`VHS_VideoCombine`、`GIMMVFI_interpolate`、`DownloadAndLoadGIMMVFIModel`、`UpscaleModelLoader`、`LoadImage`、`VHS_LoadVideo`、`VAEDecode`、`ImageScaleToMegapixels`、`AudioCrop`、`LoadAudio`、`LoraLoaderModelOnly`、`UNETLoader`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
