---
key: 图片生成/文生图/Qwen Image 2.1 加速1分35秒出2K,4K_2103662823787286529.json
name: Qwen Image 2.1 加速1分35秒出2K,4K_2103662823787286529
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1 加速1分35秒出2K,4K_2103662823787286529.json
hash: d1f6af3f9c6ac6f7
coverage: 0.580645
learned_at: 2026-10-10 20:58:51
nodes: [VAELoader, ComfySwitchNode, UNETLoader, CLIPLoader, EmptyLatentImage, PlaySound|pysssss, VAEDecode, easy cleanGpuUsed, PreviewImage, Image Remove Alpha JK, VOSR2ModelLoader, SaveImage, CLIPLoader, Note, TextEncodeQwenImage21, UNETLoader, QwenImage21SageAttentionT8, QwenImage21BlockCacheT8, QwenImage21Cache, Lora Loader Stack (rgthree), QwenImage21SpectrumT8, ResolutionSelector, PrimitiveStringMultiline, SaveImage, KSampler, easy imageChooser, ImageApplyLUT+, PreviewImage, VOSR2Upscale, PreviewImage, MarkdownNote]
patterns: []
missing: [Image Remove Alpha JK, ImageApplyLUT+, PlaySound|pysssss, easy cleanGpuUsed, easy imageChooser, Lora Loader Stack (rgthree)]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 3, "steps": 40, "width": 1024}
discoveries: [次要节点 `Image Remove Alpha JK` 知识库中没有该节点类型的任何知识, 次要节点 `ImageApplyLUT+` 知识库中没有该节点类型的任何知识, 次要节点 `PlaySound|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy imageChooser` 知识库中没有该节点类型的任何知识, 次要节点 `Lora Loader Stack (rgthree)` 仅有 LoRA 的通用知识，没有该节点自己的说明]
---

# 图片生成/文生图/Qwen Image 2.1 加速1分35秒出2K,4K_2103662823787286529.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1 加速1分35秒出2K,4K_2103662823787286529.json`

## 结构

**节点**（31 个）：
- `VAELoader`
- `ComfySwitchNode`
- `UNETLoader`
- `CLIPLoader`
- `EmptyLatentImage`
- `PlaySound|pysssss`
- `VAEDecode`
- `easy cleanGpuUsed`
- `PreviewImage`
- `Image Remove Alpha JK`
- `VOSR2ModelLoader`
- `SaveImage`
- `CLIPLoader`
- `Note`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `QwenImage21SageAttentionT8`
- `QwenImage21BlockCacheT8`
- `QwenImage21Cache`
- `Lora Loader Stack (rgthree)`
- `QwenImage21SpectrumT8`
- `ResolutionSelector`
- `PrimitiveStringMultiline`
- `SaveImage`
- `KSampler`
- `easy imageChooser`
- `ImageApplyLUT+`
- `PreviewImage`
- `VOSR2Upscale`
- `PreviewImage`
- `MarkdownNote`

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

覆盖率 **58%**（18/31）

**有卡**：`VAELoader`、`ComfySwitchNode`、`UNETLoader`、`CLIPLoader`、`EmptyLatentImage`、`PlaySound|pysssss`、`VAEDecode`、`easy cleanGpuUsed`、`PreviewImage`、`Image Remove Alpha JK`、`VOSR2ModelLoader`、`SaveImage`、`Note`、`TextEncodeQwenImage21`、`QwenImage21SageAttentionT8`、`QwenImage21BlockCacheT8`

**缺卡**（6）：`Image Remove Alpha JK`、`ImageApplyLUT+`、`PlaySound|pysssss`、`easy cleanGpuUsed`、`easy imageChooser`、`Lora Loader Stack (rgthree)`

## 学习发现

- 次要节点 `Image Remove Alpha JK` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageApplyLUT+` 知识库中没有该节点类型的任何知识
- 次要节点 `PlaySound|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy imageChooser` 知识库中没有该节点类型的任何知识
- 次要节点 `Lora Loader Stack (rgthree)` 仅有 LoRA 的通用知识，没有该节点自己的说明
