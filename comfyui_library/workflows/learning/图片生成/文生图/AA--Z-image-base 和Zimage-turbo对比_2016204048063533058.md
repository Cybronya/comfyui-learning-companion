---
key: 图片生成/文生图/AA--Z-image-base 和Zimage-turbo对比_2016204048063533058.json
name: AA--Z-image-base 和Zimage-turbo对比_2016204048063533058
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/AA--Z-image-base 和Zimage-turbo对比_2016204048063533058.json
hash: 9abb41c3ca7b00c9
coverage: 0.833333
learned_at: 2026-10-19 22:14:52
nodes: [LayerUtility: PurgeVRAM, CLIPLoader, VAELoader, Note, CLIPTextEncode, ModelSamplingAuraFlow, EmptySD3LatentImage, UNETLoader, VAELoader, CLIPLoader, KSampler, CLIPTextEncode, CLIPTextEncode, EmptyLatentImage, ConditioningZeroOut, UNETLoader, KSampler, Note, Fast Groups Bypasser (rgthree), VAEDecode, VAEDecode, SaveImage, SaveImage, Image Comparer (rgthree)]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4, "denoise": 1, "height": 1920, "sampler_name": "dpmpp_2m_sde", "scheduler": "sgm_uniform", "seed": 166281393569696, "steps": 30, "width": 1080}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/AA--Z-image-base 和Zimage-turbo对比_2016204048063533058.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/AA--Z-image-base 和Zimage-turbo对比_2016204048063533058.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（24 个）：
- `LayerUtility: PurgeVRAM`
- `CLIPLoader`
- `VAELoader`
- `Note`
- `CLIPTextEncode` ★核心
- `ModelSamplingAuraFlow`
- `EmptySD3LatentImage`
- `UNETLoader` ★核心
- `VAELoader`
- `CLIPLoader`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `EmptyLatentImage` ★核心
- `ConditioningZeroOut`
- `UNETLoader` ★核心
- `KSampler` ★核心
- `Note`
- `Fast Groups Bypasser (rgthree)`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `SaveImage`
- `Image Comparer (rgthree)`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `166281393569696`
- `steps` = `30`
- `cfg` = `4`
- `sampler_name` = `dpmpp_2m_sde`
- `scheduler` = `sgm_uniform`
- `denoise` = `1`
- `width` = `1080`
- `height` = `1920`
- `batch_size` = `1`

## 知识

覆盖率 **83%**（20/24）

**有卡**：`LayerUtility: PurgeVRAM`、`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`ModelSamplingAuraFlow`、`EmptySD3LatentImage`、`UNETLoader`、`KSampler`、`EmptyLatentImage`、`ConditioningZeroOut`、`VAEDecode`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
