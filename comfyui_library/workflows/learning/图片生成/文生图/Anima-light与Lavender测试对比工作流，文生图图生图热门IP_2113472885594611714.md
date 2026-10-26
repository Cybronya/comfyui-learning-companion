---
key: 图片生成/文生图/Anima-light与Lavender测试对比工作流，文生图图生图热门IP_2113472885594611714.json
name: Anima-light与Lavender测试对比工作流，文生图图生图热门IP_2113472885594611714
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Anima-light与Lavender测试对比工作流，文生图图生图热门IP_2113472885594611714.json
hash: c41b9e7573456ee4
coverage: 0.886364
learned_at: 2026-10-26 22:07:11
nodes: [Reroute, LayerUtility: ImageReelComposit, CLIPLoader, EmptyLatentImage, VAELoader, VAEDecode, SaveImage, CLIPLoader, VAELoader, CLIPTextEncode, CLIPTextEncode, EmptyLatentImage, VAEDecode, easy promptList, KSampler, CLIPTextEncode, KSampler, CLIPTextEncode, Reroute, UNETLoader, Reroute, CLIPLoader, VAELoader, CLIPTextEncode, EmptyLatentImage, KSampler, easy promptList, VAEDecode, Reroute, Reroute, Reroute, UNETLoader, easy promptList, Reroute, easy promptList, easy promptList, LayerUtility: ImageReel, easy promptList, easy promptList, UNETLoader, CLIPTextEncode, TTResolutionSelector, easy anythingIndexSwitch, easy promptList, easy promptList, easy promptList, Seed (rgthree), SaveImage, easy promptList, easy anythingIndexSwitch, easy promptList, easy mathInt, easy promptList, SaveImage, SaveImage, easy promptList, easy promptList, easy promptList, PrimitiveInt, easy promptList, easy promptList, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPTextEncode, CLIPLoader, JjkText, VAEDecode, EmptyLatentImage, VAELoader, solarL_SaveImagesToZip, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Anima-light与Lavender测试对比工作流，文生图图生图热门IP_2113472885594611714.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Anima-light与Lavender测试对比工作流，文生图图生图热门IP_2113472885594611714.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（88 个）：
- `Reroute`
- `LayerUtility: ImageReelComposit`
- `CLIPLoader`
- `EmptyLatentImage` ★核心
- `VAELoader`
- `VAEDecode` ★核心
- `SaveImage`
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `easy promptList`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `Reroute`
- `UNETLoader` ★核心
- `Reroute`
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `easy promptList`
- `VAEDecode` ★核心
- `Reroute`
- `Reroute`
- `Reroute`
- `UNETLoader` ★核心
- `easy promptList`
- `Reroute`
- `easy promptList`
- `easy promptList`
- `LayerUtility: ImageReel`
- `easy promptList`
- `easy promptList`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `TTResolutionSelector`
- `easy anythingIndexSwitch`
- `easy promptList`
- `easy promptList`
- `easy promptList`
- `Seed (rgthree)`
- `SaveImage`
- `easy promptList`
- `easy anythingIndexSwitch`
- `easy promptList`
- `easy mathInt`
- `easy promptList`
- `SaveImage`
- `SaveImage`
- `easy promptList`
- `easy promptList`
- `easy promptList`
- `PrimitiveInt`
- `easy promptList`
- `easy promptList`
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
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `JjkText`
- `VAEDecode` ★核心
- `EmptyLatentImage` ★核心
- `VAELoader`
- `solarL_SaveImagesToZip`
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

覆盖率 **89%**（78/88）

**有卡**：`LayerUtility: ImageReelComposit`、`CLIPLoader`、`EmptyLatentImage`、`VAELoader`、`VAEDecode`、`SaveImage`、`CLIPTextEncode`、`easy promptList`、`KSampler`、`UNETLoader`、`LayerUtility: ImageReel`、`TTResolutionSelector`、`easy anythingIndexSwitch`、`Seed (rgthree)`、`easy mathInt`、`LoraLoaderModelOnly`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
