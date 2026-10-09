---
key: 图片生成/图生图/Qwen Image 2.1｜文生图图生图二合一整合流｜抠图也能一键搞定_2102568018860666881.json
name: Qwen Image 2.1｜文生图图生图二合一整合流｜抠图也能一键搞定_2102568018860666881.json
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1｜文生图图生图二合一整合流｜抠图也能一键搞定_2102568018860666881.json
hash: 70a9400cd97d59e5
coverage: 0.788235
learned_at: 2026-10-09 22:19:29
nodes: [LoadImage, LoadImage, SaveImage, PreviewImage, VAELoader, CLIPLoader, EmptyLatentImage, PlaySound|pysssss, VAEDecode, TextEncodeQwenImage21, KSampler, JjkText, JjkText, ResolutionSelector, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, KSampler, CLIPLoader, VAELoader, EmptyLatentImage, UNETLoader, QwenImage21Cache, PlaySound|pysssss, ComfySwitchNode, UNETLoader, ResolutionSelector, TextEncodeQwenImage21, VAEDecode, easy int, easy int, LoadImage, JjkText, JjkText, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), PreviewImage, SaveImage, Image Comparer (rgthree), 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, solarL_SaveImagesToZip, JjkText, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note]
patterns: [text_to_image]
missing: [PlaySound|pysssss, PlaySound|pysssss, easy int, easy int]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `PlaySound|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `PlaySound|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen Image 2.1｜文生图图生图二合一整合流｜抠图也能一键搞定_2102568018860666881.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/2102568018860666881.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（85 个）：
- `LoadImage`
- `LoadImage`
- `SaveImage`
- `PreviewImage`
- `VAELoader`
- `CLIPLoader`
- `EmptyLatentImage` ★核心
- `PlaySound|pysssss`
- `VAEDecode` ★核心
- `TextEncodeQwenImage21`
- `KSampler` ★核心
- `JjkText`
- `JjkText`
- `ResolutionSelector`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `KSampler` ★核心
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `UNETLoader` ★核心
- `QwenImage21Cache`
- `PlaySound|pysssss`
- `ComfySwitchNode`
- `UNETLoader` ★核心
- `ResolutionSelector`
- `TextEncodeQwenImage21`
- `VAEDecode` ★核心
- `easy int`
- `easy int`
- `LoadImage`
- `JjkText`
- `JjkText`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `PreviewImage`
- `SaveImage`
- `Image Comparer (rgthree)`
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

## 知识

覆盖率 **79%**（67/85）

**有卡**：`LoadImage`、`SaveImage`、`VAELoader`、`CLIPLoader`、`EmptyLatentImage`、`VAEDecode`、`TextEncodeQwenImage21`、`KSampler`、`ResolutionSelector`、`UNETLoader`、`QwenImage21Cache`、`CLIPTextEncode`、`solarL_SaveImagesToZip`、`LoraLoaderModelOnly`

**缺卡**（4）：`PlaySound|pysssss`、`PlaySound|pysssss`、`easy int`、`easy int`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `PlaySound|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `PlaySound|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
