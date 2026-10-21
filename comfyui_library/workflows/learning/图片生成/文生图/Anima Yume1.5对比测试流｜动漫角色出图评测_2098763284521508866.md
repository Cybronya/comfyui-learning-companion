---
key: 图片生成/文生图/Anima Yume1.5对比测试流｜动漫角色出图评测_2098763284521508866.json
name: Anima Yume1.5对比测试流｜动漫角色出图评测_2098763284521508866
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Anima Yume1.5对比测试流｜动漫角色出图评测_2098763284521508866.json
hash: 62073ec8d5cb63a9
coverage: 0.854369
learned_at: 2026-10-20 01:34:15
nodes: [Reroute, LayerUtility: ImageReelComposit, CLIPLoader, EmptyLatentImage, VAELoader, VAEDecode, SaveImage, CLIPLoader, VAELoader, CLIPTextEncode, CLIPTextEncode, EmptyLatentImage, VAEDecode, SaveImage, easy promptList, easy promptList, easy promptList, easy mathInt, KSampler, CLIPTextEncode, KSampler, CLIPTextEncode, Reroute, UNETLoader, UNETLoader, Fast Groups Bypasser (rgthree), Reroute, CLIPLoader, VAELoader, CLIPTextEncode, CLIPTextEncode, EmptyLatentImage, SaveImage, KSampler, UNETLoader, easy promptList, Reroute, CLIPLoader, VAELoader, CLIPTextEncode, CLIPTextEncode, EmptyLatentImage, SaveImage, KSampler, ImageOnlyCheckpointLoader, Reroute, Reroute, VAEDecode, VAEDecode, LayerUtility: ImageReel, SaveImage, TTResolutionSelector, Reroute, Reroute, easy promptList, Reroute, easy promptList, easy anythingIndexSwitch, PrimitiveInt, Seed (rgthree), 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, solarL_SaveImagesToZip, JjkText, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "checkpoint": "miaomiaoHarem_anima12.safetensors", "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Anima Yume1.5对比测试流｜动漫角色出图评测_2098763284521508866.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Anima Yume1.5对比测试流｜动漫角色出图评测_2098763284521508866.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（103 个）：
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
- `SaveImage`
- `easy promptList`
- `easy promptList`
- `easy promptList`
- `easy mathInt`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `Reroute`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `Fast Groups Bypasser (rgthree)`
- `Reroute`
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `EmptyLatentImage` ★核心
- `SaveImage`
- `KSampler` ★核心
- `UNETLoader` ★核心
- `easy promptList`
- `Reroute`
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `EmptyLatentImage` ★核心
- `SaveImage`
- `KSampler` ★核心
- `ImageOnlyCheckpointLoader` ★核心
- `Reroute`
- `Reroute`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `LayerUtility: ImageReel`
- `SaveImage`
- `TTResolutionSelector`
- `Reroute`
- `Reroute`
- `easy promptList`
- `Reroute`
- `easy promptList`
- `easy anythingIndexSwitch`
- `PrimitiveInt`
- `Seed (rgthree)`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `solarL_SaveImagesToZip`
- `JjkText`
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
- `CLIPTextEncode` ★核心
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
- `checkpoint` = `miaomiaoHarem_anima12.safetensors`

## 知识

覆盖率 **85%**（88/103）

**有卡**：`LayerUtility: ImageReelComposit`、`CLIPLoader`、`EmptyLatentImage`、`VAELoader`、`VAEDecode`、`SaveImage`、`CLIPTextEncode`、`easy promptList`、`easy mathInt`、`KSampler`、`UNETLoader`、`ImageOnlyCheckpointLoader`、`LayerUtility: ImageReel`、`TTResolutionSelector`、`easy anythingIndexSwitch`、`Seed (rgthree)`、`solarL_SaveImagesToZip`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
