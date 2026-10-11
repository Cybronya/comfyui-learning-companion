---
key: 视频生成/文生视频/Anima-2.9B官方文生图｜文生视频视频生视频图生视频_2090076387519582210.json
name: Anima-2.9B官方文生图｜文生视频视频生视频图生视频_2090076387519582210
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Anima-2.9B官方文生图｜文生视频视频生视频图生视频_2090076387519582210.json
hash: 47ed7c1aca66f427
coverage: 0.863636
learned_at: 2026-10-11 21:19:36
nodes: [SaveImage, SamplerCustomAdvanced, KSamplerSelect, BasicScheduler, CFGGuider, RandomNoise, KSampler Config (rgthree), CLIPLoader, VAEDecode, ImpactSwitch, UNETLoader, CLIPTextEncode, CLIPTextEncode, VAELoaderKJ, EmptyLatentImage, EmptyLatentImage, PathchSageAttentionKJ, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, JjkText, solarL_SaveImagesToZip, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, Note]
patterns: [text_to_image]
missing: [KSampler Config (rgthree)]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [核心节点 `KSampler Config (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/Anima-2.9B官方文生图｜文生视频视频生视频图生视频_2090076387519582210.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Anima-2.9B官方文生图｜文生视频视频生视频图生视频_2090076387519582210.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（44 个）：
- `SaveImage`
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `CFGGuider`
- `RandomNoise`
- `KSampler Config (rgthree)` ★核心
- `CLIPLoader`
- `VAEDecode` ★核心
- `ImpactSwitch`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAELoaderKJ`
- `EmptyLatentImage` ★核心
- `EmptyLatentImage` ★核心
- `PathchSageAttentionKJ`
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

覆盖率 **86%**（38/44）

**有卡**：`SaveImage`、`SamplerCustomAdvanced`、`KSamplerSelect`、`BasicScheduler`、`CFGGuider`、`RandomNoise`、`CLIPLoader`、`VAEDecode`、`UNETLoader`、`CLIPTextEncode`、`VAELoaderKJ`、`EmptyLatentImage`、`PathchSageAttentionKJ`、`VAELoader`、`KSampler`、`solarL_SaveImagesToZip`、`LoraLoaderModelOnly`

**缺卡**（1）：`KSampler Config (rgthree)`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 核心节点 `KSampler Config (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
