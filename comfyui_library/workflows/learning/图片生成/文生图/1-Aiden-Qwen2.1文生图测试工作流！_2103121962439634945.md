---
key: 图片生成/文生图/1-Aiden-Qwen2.1文生图测试工作流！_2103121962439634945.json
name: 1-Aiden-Qwen2.1文生图测试工作流！_2103121962439634945
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/1-Aiden-Qwen2.1文生图测试工作流！_2103121962439634945.json
hash: 5b4796eaac96c805
coverage: 0.607143
learned_at: 2026-10-07 02:04:28
nodes: [TextEncodeQwenImage21, KSampler, VAEDecode, EmptyLatentImage, ResolutionSelector, 孤海注释, MarkdownNote, 孤海注释, PreviewImage, ModelPreviewOverrideKJ, 孤海注释, VOSR2Upscale, SaveImage, VOSR2ModelLoader, SplitImageWithAlpha, 忽略多组孤海, UNETLoader, CLIPLoader, VAELoader, easy positive, LayerUtility: PurgeVRAM V2, ShowText|pysssss, CLIPLoader, easy positive, JoinStrings, StringFormat, Image Comparer (rgthree), TextGenerate]
patterns: []
missing: [LayerUtility: PurgeVRAM V2, easy positive, easy positive, 忽略多组孤海]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 210, "steps": 25, "width": 1024}
discoveries: [次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识, 次要节点 `easy positive` 知识库中没有该节点类型的任何知识, 次要节点 `easy positive` 知识库中没有该节点类型的任何知识, 次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识]
---

# 图片生成/文生图/1-Aiden-Qwen2.1文生图测试工作流！_2103121962439634945.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/1-Aiden-Qwen2.1文生图测试工作流！_2103121962439634945.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（28 个）：
- `TextEncodeQwenImage21`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `EmptyLatentImage` ★核心
- `ResolutionSelector`
- `孤海注释`
- `MarkdownNote`
- `孤海注释`
- `PreviewImage`
- `ModelPreviewOverrideKJ`
- `孤海注释`
- `VOSR2Upscale`
- `SaveImage`
- `VOSR2ModelLoader`
- `SplitImageWithAlpha`
- `忽略多组孤海`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `easy positive`
- `LayerUtility: PurgeVRAM V2`
- `ShowText|pysssss`
- `CLIPLoader`
- `easy positive`
- `JoinStrings`
- `StringFormat`
- `Image Comparer (rgthree)`
- `TextGenerate`

## 关键参数

- `seed` = `210`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **61%**（17/28）

**有卡**：`TextEncodeQwenImage21`、`KSampler`、`VAEDecode`、`EmptyLatentImage`、`ResolutionSelector`、`ModelPreviewOverrideKJ`、`VOSR2Upscale`、`SaveImage`、`VOSR2ModelLoader`、`SplitImageWithAlpha`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`JoinStrings`、`StringFormat`、`TextGenerate`

**缺卡**（4）：`LayerUtility: PurgeVRAM V2`、`easy positive`、`easy positive`、`忽略多组孤海`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、UNETLoader

## 学习发现

- 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识
- 次要节点 `easy positive` 知识库中没有该节点类型的任何知识
- 次要节点 `easy positive` 知识库中没有该节点类型的任何知识
- 次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识
