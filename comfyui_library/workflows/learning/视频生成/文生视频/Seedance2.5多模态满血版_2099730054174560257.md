---
key: 视频生成/文生视频/Seedance2.5多模态满血版_2099730054174560257.json
name: Seedance2.5多模态满血版_2099730054174560257
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Seedance2.5多模态满血版_2099730054174560257.json
hash: 9a5aa8661f97f863
coverage: 0.892857
learned_at: 2026-10-11 22:12:47
nodes: [PreviewAny, PreviewAny, SaveVideo, LoadVideo, LoadVideo, LoadVideo, LoadAudio, LoadAudio, Fast Groups Bypasser (rgthree), UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPLoader, CLIPTextEncode, JjkText, EmptyLatentImage, solarL_SaveImagesToZip, VAEDecode, VAELoader, Note, SaveImage, LoadImage, LoadImage, LoadAudio, RH_BytedanceSeedance25GlobalTokenMultimodalVideo, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadVideo, LoadAudio, LoadImage, LoadVideo, LoadAudio, CR Prompt Text, LoadImage, LoadImage, LoadImage]
patterns: [text_to_image]
missing: [CR Prompt Text]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/Seedance2.5多模态满血版_2099730054174560257.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Seedance2.5多模态满血版_2099730054174560257.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（56 个）：
- `PreviewAny`
- `PreviewAny`
- `SaveVideo`
- `LoadVideo`
- `LoadVideo`
- `LoadVideo`
- `LoadAudio`
- `LoadAudio`
- `Fast Groups Bypasser (rgthree)`
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
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `JjkText`
- `EmptyLatentImage` ★核心
- `solarL_SaveImagesToZip`
- `VAEDecode` ★核心
- `VAELoader`
- `Note`
- `SaveImage`
- `LoadImage`
- `LoadImage`
- `LoadAudio`
- `RH_BytedanceSeedance25GlobalTokenMultimodalVideo`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadVideo`
- `LoadAudio`
- `LoadImage`
- `LoadVideo`
- `LoadAudio`
- `CR Prompt Text`
- `LoadImage`
- `LoadImage`
- `LoadImage`

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

**有卡**：`SaveVideo`、`LoadVideo`、`LoadAudio`、`UNETLoader`、`LoraLoaderModelOnly`、`KSampler`、`CLIPTextEncode`、`CLIPLoader`、`EmptyLatentImage`、`solarL_SaveImagesToZip`、`VAEDecode`、`VAELoader`、`SaveImage`、`LoadImage`、`RH_BytedanceSeedance25GlobalTokenMultimodalVideo`

**缺卡**（1）：`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
