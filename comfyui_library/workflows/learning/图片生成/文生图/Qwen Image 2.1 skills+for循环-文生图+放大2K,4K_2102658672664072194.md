---
key: 图片生成/文生图/Qwen Image 2.1 skills+for循环-文生图+放大2K,4K_2102658672664072194.json
name: Qwen Image 2.1 skills+for循环-文生图+放大2K,4K_2102658672664072194
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1 skills+for循环-文生图+放大2K,4K_2102658672664072194.json
hash: 192c308b106c4513
coverage: 0.8
learned_at: 2026-10-15 23:00:36
nodes: [UNETLoader, CLIPLoader, Image Remove Alpha JK, VOSR2Upscale, VOSR2ModelLoader, UNETLoader, CLIPLoader, TextEncodeQwenImage21, QwenImage21Cache, ComfySwitchNode, EmptyLatentImage, VAELoader, ResolutionSelector, PlaySound|pysssss, Lora Loader Stack (rgthree), MarkdownNote, PrimitiveStringMultiline, VAEDecode, easy cleanGpuUsed, GetItemFromList, easy promptList, easy forLoopEnd, easy showAnything, easy batchAnything, Note, SaveImage, KSampler, PreviewImage, easy forLoopStart, easy lengthAnything]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 3, "steps": 40, "width": 1024}
---

# 图片生成/文生图/Qwen Image 2.1 skills+for循环-文生图+放大2K,4K_2102658672664072194.json

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

覆盖率 **80%**（24/30）

**有卡**：`UNETLoader`、`CLIPLoader`、`Image Remove Alpha JK`、`VOSR2Upscale`、`VOSR2ModelLoader`、`TextEncodeQwenImage21`、`QwenImage21Cache`、`EmptyLatentImage`、`VAELoader`、`ResolutionSelector`、`PlaySound|pysssss`、`Lora Loader Stack (rgthree)`、`VAEDecode`、`easy cleanGpuUsed`、`GetItemFromList`、`easy promptList`、`easy forLoopEnd`、`easy batchAnything`、`SaveImage`、`KSampler`、`easy forLoopStart`、`easy lengthAnything`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、QwenImage21Cache
