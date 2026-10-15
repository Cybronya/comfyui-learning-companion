---
key: 图片生成/文生图/Qwen Image 2.1 skills文生图+放大2K,4K_2102657150928642049.json
name: Qwen Image 2.1 skills文生图+放大2K,4K_2102657150928642049
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1 skills文生图+放大2K,4K_2102657150928642049.json
hash: 27b85149986677fa
coverage: 0.576923
learned_at: 2026-10-10 20:58:51
nodes: [UNETLoader, CLIPLoader, VAEDecode, easy cleanGpuUsed, PreviewImage, Image Remove Alpha JK, VOSR2Upscale, VOSR2ModelLoader, ImageApplyLUT+, SaveImage, UNETLoader, CLIPLoader, TextEncodeQwenImage21, SaveImage, QwenImage21Cache, KSampler, Note, ComfySwitchNode, EmptyLatentImage, VAELoader, ResolutionSelector, PlaySound|pysssss, Lora Loader Stack (rgthree), MarkdownNote, PrimitiveStringMultiline, easy imageChooser]
patterns: []
missing: [Image Remove Alpha JK, ImageApplyLUT+, PlaySound|pysssss, easy cleanGpuUsed, easy imageChooser, Lora Loader Stack (rgthree)]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 3, "steps": 40, "width": 1024}
discoveries: [次要节点 `Image Remove Alpha JK` 知识库中没有该节点类型的任何知识, 次要节点 `ImageApplyLUT+` 知识库中没有该节点类型的任何知识, 次要节点 `PlaySound|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy imageChooser` 知识库中没有该节点类型的任何知识, 次要节点 `Lora Loader Stack (rgthree)` 仅有 LoRA 的通用知识，没有该节点自己的说明]
---

# 图片生成/文生图/Qwen Image 2.1 skills文生图+放大2K,4K_2102657150928642049.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1 skills文生图+放大2K,4K_2102657150928642049.json`

## 结构

**节点**（26 个）：
- `UNETLoader`
- `CLIPLoader`
- `VAEDecode`
- `easy cleanGpuUsed`
- `PreviewImage`
- `Image Remove Alpha JK`
- `VOSR2Upscale`
- `VOSR2ModelLoader`
- `ImageApplyLUT+`
- `SaveImage`
- `UNETLoader`
- `CLIPLoader`
- `TextEncodeQwenImage21`
- `SaveImage`
- `QwenImage21Cache`
- `KSampler`
- `Note`
- `ComfySwitchNode`
- `EmptyLatentImage`
- `VAELoader`
- `ResolutionSelector`
- `PlaySound|pysssss`
- `Lora Loader Stack (rgthree)`
- `MarkdownNote`
- `PrimitiveStringMultiline`
- `easy imageChooser`

## 关键参数

- `batch_size` = `1`
- `cfg` = `1`
- `denoise` = `1`
- `height` = `1024`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `seed` = `3`
- `steps` = `40`
- `width` = `1024`

## 知识

覆盖率 **58%**（15/26）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAEDecode`、`easy cleanGpuUsed`、`PreviewImage`、`Image Remove Alpha JK`、`VOSR2Upscale`、`VOSR2ModelLoader`、`ImageApplyLUT+`、`SaveImage`、`TextEncodeQwenImage21`、`QwenImage21Cache`

**缺卡**（6）：`Image Remove Alpha JK`、`ImageApplyLUT+`、`PlaySound|pysssss`、`easy cleanGpuUsed`、`easy imageChooser`、`Lora Loader Stack (rgthree)`

## 学习发现

- 次要节点 `Image Remove Alpha JK` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageApplyLUT+` 知识库中没有该节点类型的任何知识
- 次要节点 `PlaySound|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy imageChooser` 知识库中没有该节点类型的任何知识
- 次要节点 `Lora Loader Stack (rgthree)` 仅有 LoRA 的通用知识，没有该节点自己的说明
