---
key: 视频生成/文生视频/Qwen-Image-2.1_T2I文生图｜人像写真级出图质感｜写实人像一步生成_2104043820429176833.json
name: Qwen-Image-2.1_T2I文生图｜人像写真级出图质感｜写实人像一步生成_2104043820429176833
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Qwen-Image-2.1_T2I文生图｜人像写真级出图质感｜写实人像一步生成_2104043820429176833.json
hash: e5d21ba1419326b4
coverage: 0.772727
learned_at: 2026-10-11 22:12:46
nodes: [CLIPLoader, TextGenerate, PrimitiveStringMultiline, easy showAnything, EmptyLatentImage, TextEncodeQwenImage21, KSampler, Seed (rgthree), VAEDecode, SaveImage, Fast Groups Bypasser (rgthree), easy promptList, easy promptList, easy promptList, easy promptList, easy promptList, easy promptList, easy promptList, easy promptList, VAELoader, UNETLoader, CLIPLoader, ResolutionSelector, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, solarL_SaveImagesToZip, JjkText, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note, EmptyImage, PreviewImage]
patterns: [text_to_image]
missing: [Seed (rgthree), easy promptList, easy promptList, easy promptList, easy promptList, easy promptList, easy promptList, easy promptList, easy promptList]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明, 次要节点 `easy promptList` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `easy promptList` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `easy promptList` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `easy promptList` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `easy promptList` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `easy promptList` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `easy promptList` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `easy promptList` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/Qwen-Image-2.1_T2I文生图｜人像写真级出图质感｜写实人像一步生成_2104043820429176833.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Qwen-Image-2.1_T2I文生图｜人像写真级出图质感｜写实人像一步生成_2104043820429176833.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（66 个）：
- `CLIPLoader`
- `TextGenerate`
- `PrimitiveStringMultiline`
- `easy showAnything`
- `EmptyLatentImage` ★核心
- `TextEncodeQwenImage21`
- `KSampler` ★核心
- `Seed (rgthree)`
- `VAEDecode` ★核心
- `SaveImage`
- `Fast Groups Bypasser (rgthree)`
- `easy promptList`
- `easy promptList`
- `easy promptList`
- `easy promptList`
- `easy promptList`
- `easy promptList`
- `easy promptList`
- `easy promptList`
- `VAELoader`
- `UNETLoader` ★核心
- `CLIPLoader`
- `ResolutionSelector`
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
- `EmptyImage`
- `PreviewImage`

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

覆盖率 **77%**（51/66）

**有卡**：`CLIPLoader`、`TextGenerate`、`EmptyLatentImage`、`TextEncodeQwenImage21`、`KSampler`、`VAEDecode`、`SaveImage`、`VAELoader`、`UNETLoader`、`ResolutionSelector`、`CLIPTextEncode`、`solarL_SaveImagesToZip`、`LoraLoaderModelOnly`、`EmptyImage`

**缺卡**（9）：`Seed (rgthree)`、`easy promptList`、`easy promptList`、`easy promptList`、`easy promptList`、`easy promptList`、`easy promptList`、`easy promptList`、`easy promptList`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明
- 次要节点 `easy promptList` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `easy promptList` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `easy promptList` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `easy promptList` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `easy promptList` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `easy promptList` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `easy promptList` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `easy promptList` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
