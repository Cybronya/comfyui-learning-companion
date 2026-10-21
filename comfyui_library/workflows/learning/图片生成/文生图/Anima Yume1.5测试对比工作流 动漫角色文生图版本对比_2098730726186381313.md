---
key: 图片生成/文生图/Anima Yume1.5测试对比工作流 动漫角色文生图版本对比_2098730726186381313.json
name: Anima Yume1.5测试对比工作流 动漫角色文生图版本对比_2098730726186381313
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Anima Yume1.5测试对比工作流 动漫角色文生图版本对比_2098730726186381313.json
hash: 0f0379182fc0971e
coverage: 0.831461
learned_at: 2026-10-20 01:34:15
nodes: [Reroute, LayerUtility: ImageReelComposit, CLIPLoader, EmptyLatentImage, VAELoader, VAEDecode, SaveImage, CLIPLoader, VAELoader, CLIPTextEncode, CLIPTextEncode, EmptyLatentImage, VAEDecode, SaveImage, easy promptList, easy promptList, easy promptList, easy mathInt, KSampler, CLIPTextEncode, KSampler, CLIPTextEncode, Reroute, UNETLoader, UNETLoader, Fast Groups Bypasser (rgthree), Reroute, CLIPLoader, VAELoader, CLIPTextEncode, CLIPTextEncode, EmptyLatentImage, SaveImage, KSampler, UNETLoader, easy promptList, Reroute, CLIPLoader, VAELoader, CLIPTextEncode, CLIPTextEncode, EmptyLatentImage, SaveImage, KSampler, ImageOnlyCheckpointLoader, Reroute, Reroute, VAEDecode, VAEDecode, LayerUtility: ImageReel, SaveImage, TTResolutionSelector, Reroute, Reroute, easy promptList, Reroute, easy promptList, easy anythingIndexSwitch, PrimitiveInt, Seed (rgthree), 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPLoader, CLIPTextEncode, JjkText, EmptyLatentImage, solarL_SaveImagesToZip, VAEDecode, VAELoader, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "checkpoint": "miaomiaoHarem_anima12.safetensors", "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Anima Yume1.5测试对比工作流 动漫角色文生图版本对比_2098730726186381313.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Anima Yume1.5测试对比工作流 动漫角色文生图版本对比_2098730726186381313.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（89 个）：
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

覆盖率 **83%**（74/89）

**有卡**：`LayerUtility: ImageReelComposit`、`CLIPLoader`、`EmptyLatentImage`、`VAELoader`、`VAEDecode`、`SaveImage`、`CLIPTextEncode`、`easy promptList`、`easy mathInt`、`KSampler`、`UNETLoader`、`ImageOnlyCheckpointLoader`、`LayerUtility: ImageReel`、`TTResolutionSelector`、`easy anythingIndexSwitch`、`Seed (rgthree)`、`LoraLoaderModelOnly`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
