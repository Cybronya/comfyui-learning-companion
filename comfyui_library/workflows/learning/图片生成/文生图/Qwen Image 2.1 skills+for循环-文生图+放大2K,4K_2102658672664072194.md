---
key: Qwen Image 2.1 skills+for循环-文生图+放大2K,4K_2102658672664072194.json
name: Qwen Image 2.1 skills+for循环-文生图+放大2K,4K_2102658672664072194
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1 skills+for循环-文生图+放大2K,4K_2102658672664072194.json
hash: 192c308b106c4513
coverage: 0.466667
learned_at: 2026-10-10 20:58:51
nodes: [UNETLoader, CLIPLoader, Image Remove Alpha JK, VOSR2Upscale, VOSR2ModelLoader, UNETLoader, CLIPLoader, TextEncodeQwenImage21, QwenImage21Cache, ComfySwitchNode, EmptyLatentImage, VAELoader, ResolutionSelector, PlaySound|pysssss, Lora Loader Stack (rgthree), MarkdownNote, PrimitiveStringMultiline, VAEDecode, easy cleanGpuUsed, GetItemFromList, easy promptList, easy forLoopEnd, easy showAnything, easy batchAnything, Note, SaveImage, KSampler, PreviewImage, easy forLoopStart, easy lengthAnything]
patterns: []
missing: [GetItemFromList, Image Remove Alpha JK, PlaySound|pysssss, easy batchAnything, easy cleanGpuUsed, easy forLoopEnd, easy forLoopStart, easy lengthAnything, Lora Loader Stack (rgthree), easy promptList]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 3, "steps": 40, "width": 1024}
discoveries: [次要节点 `GetItemFromList` 知识库中没有该节点类型的任何知识, 次要节点 `Image Remove Alpha JK` 知识库中没有该节点类型的任何知识, 次要节点 `PlaySound|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `easy batchAnything` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy forLoopEnd` 知识库中没有该节点类型的任何知识, 次要节点 `easy forLoopStart` 知识库中没有该节点类型的任何知识, 次要节点 `easy lengthAnything` 知识库中没有该节点类型的任何知识, 次要节点 `Lora Loader Stack (rgthree)` 仅有 LoRA 的通用知识，没有该节点自己的说明, 次要节点 `easy promptList` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# Qwen Image 2.1 skills+for循环-文生图+放大2K,4K_2102658672664072194.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1 skills+for循环-文生图+放大2K,4K_2102658672664072194.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（30 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `Image Remove Alpha JK`
- `VOSR2Upscale`
- `VOSR2ModelLoader`
- `UNETLoader` ★核心
- `CLIPLoader`
- `TextEncodeQwenImage21`
- `QwenImage21Cache`
- `ComfySwitchNode`
- `EmptyLatentImage` ★核心
- `VAELoader`
- `ResolutionSelector`
- `PlaySound|pysssss`
- `Lora Loader Stack (rgthree)`
- `MarkdownNote`
- `PrimitiveStringMultiline`
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `GetItemFromList`
- `easy promptList`
- `easy forLoopEnd`
- `easy showAnything`
- `easy batchAnything`
- `Note`
- `SaveImage`
- `KSampler` ★核心
- `PreviewImage`
- `easy forLoopStart`
- `easy lengthAnything`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `3`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **47%**（14/30）

**有卡**：`UNETLoader`、`CLIPLoader`、`VOSR2Upscale`、`VOSR2ModelLoader`、`TextEncodeQwenImage21`、`QwenImage21Cache`、`EmptyLatentImage`、`VAELoader`、`ResolutionSelector`、`VAEDecode`、`SaveImage`、`KSampler`

**缺卡**（10）：`GetItemFromList`、`Image Remove Alpha JK`、`PlaySound|pysssss`、`easy batchAnything`、`easy cleanGpuUsed`、`easy forLoopEnd`、`easy forLoopStart`、`easy lengthAnything`、`Lora Loader Stack (rgthree)`、`easy promptList`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、QwenImage21Cache

## 学习发现

- 次要节点 `GetItemFromList` 知识库中没有该节点类型的任何知识
- 次要节点 `Image Remove Alpha JK` 知识库中没有该节点类型的任何知识
- 次要节点 `PlaySound|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `easy batchAnything` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy forLoopEnd` 知识库中没有该节点类型的任何知识
- 次要节点 `easy forLoopStart` 知识库中没有该节点类型的任何知识
- 次要节点 `easy lengthAnything` 知识库中没有该节点类型的任何知识
- 次要节点 `Lora Loader Stack (rgthree)` 仅有 LoRA 的通用知识，没有该节点自己的说明
- 次要节点 `easy promptList` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
