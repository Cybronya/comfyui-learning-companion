---
key: 视频生成/图生视频/wan3.0 换人换音色_2101582598848991234.json
name: wan3.0 换人换音色_2101582598848991234
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan3.0 换人换音色_2101582598848991234.json
hash: b3805d1ff0652233
coverage: 0.95122
learned_at: 2026-10-17 02:14:50
nodes: [UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, JjkText, solarL_SaveImagesToZip, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, AudioSeparation, AudioSeparation, RH_AlibabaWan30ReferenceToVideo, Note, LoraLoaderModelOnly, SeedVCRun, LoadImage, AudioMerge, AudioMerge, AudioMerge, CreateVideo, LoadVideo, VHS_LoadVideo, VHS_VideoInfo, SaveVideo, LoadAudio, SaveVideo, LazySwitchKJ]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/wan3.0 换人换音色_2101582598848991234.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/wan3.0 换人换音色_2101582598848991234.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（41 个）：
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
- `AudioSeparation`
- `AudioSeparation`
- `RH_AlibabaWan30ReferenceToVideo`
- `Note`
- `LoraLoaderModelOnly` ★核心
- `SeedVCRun`
- `LoadImage`
- `AudioMerge`
- `AudioMerge`
- `AudioMerge`
- `CreateVideo`
- `LoadVideo`
- `VHS_LoadVideo`
- `VHS_VideoInfo`
- `SaveVideo`
- `LoadAudio`
- `SaveVideo`
- `LazySwitchKJ`

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

覆盖率 **95%**（39/41）

**有卡**：`UNETLoader`、`CLIPLoader`、`CLIPTextEncode`、`VAELoader`、`EmptyLatentImage`、`KSampler`、`VAEDecode`、`solarL_SaveImagesToZip`、`LoraLoaderModelOnly`、`AudioSeparation`、`RH_AlibabaWan30ReferenceToVideo`、`SeedVCRun`、`LoadImage`、`AudioMerge`、`CreateVideo`、`LoadVideo`、`VHS_LoadVideo`、`VHS_VideoInfo`、`SaveVideo`、`LoadAudio`、`LazySwitchKJ`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
