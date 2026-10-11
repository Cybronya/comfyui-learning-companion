---
key: 视频生成/文生视频/Seedance2.0 Fast全能参考视频 图片音频视频三参考输入_2104694435845070849.json
name: Seedance2.0 Fast全能参考视频 图片音频视频三参考输入_2104694435845070849
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Seedance2.0 Fast全能参考视频 图片音频视频三参考输入_2104694435845070849.json
hash: 483e7b5af11425a3
coverage: 0.902439
learned_at: 2026-10-11 22:12:46
nodes: [SaveVideo, RH_RhartVideoSparkvideo20FastMultimodalVideo, LoadImage, LoadVideo, LoadAudio, LoadAudio, LoadAudio, LoadImage, LoadImage, LoadImage, LoadVideo, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note, SaveImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/Seedance2.0 Fast全能参考视频 图片音频视频三参考输入_2104694435845070849.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Seedance2.0 Fast全能参考视频 图片音频视频三参考输入_2104694435845070849.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（41 个）：
- `SaveVideo`
- `RH_RhartVideoSparkvideo20FastMultimodalVideo`
- `LoadImage`
- `LoadVideo`
- `LoadAudio`
- `LoadAudio`
- `LoadAudio`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadVideo`
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

覆盖率 **90%**（37/41）

**有卡**：`SaveVideo`、`RH_RhartVideoSparkvideo20FastMultimodalVideo`、`LoadImage`、`LoadVideo`、`LoadAudio`、`UNETLoader`、`LoraLoaderModelOnly`、`KSampler`、`EmptyLatentImage`、`CLIPTextEncode`、`solarL_SaveImagesToZip`、`VAEDecode`、`CLIPLoader`、`VAELoader`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
