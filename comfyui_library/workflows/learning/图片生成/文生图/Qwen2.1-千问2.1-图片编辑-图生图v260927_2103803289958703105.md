---
key: 图片生成/文生图/Qwen2.1-千问2.1-图片编辑-图生图v260927_2103803289958703105.json
name: Qwen2.1-千问2.1-图片编辑-图生图v260927_2103803289958703105
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen2.1-千问2.1-图片编辑-图生图v260927_2103803289958703105.json
hash: 1f75acf59771b258
coverage: 0.8
learned_at: 2026-10-07 02:26:57
nodes: [MarkdownNote, QwenPERewriteT8, ShowAnything|Mie, EmptyLatentImage, CLIPLoader, EnhancedLoadDiffusionModel, VAELoader_Any, TextEncodeQwenImage21, KSamplerCacheable, QwenImage21Cache, LoadImage, LoadImage, Fast Groups Bypasser (rgthree), LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, PreviewImage, FastGroupsBypassSwitch, ResolutionSelector, JjkText, VAEDecode, SaveImage]
patterns: []
missing: [ShowAnything|Mie]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 612469955575595, "steps": 50, "width": 1024}
discoveries: [次要节点 `ShowAnything|Mie` 知识库中没有该节点类型的任何知识]
---

# 图片生成/文生图/Qwen2.1-千问2.1-图片编辑-图生图v260927_2103803289958703105.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen2.1-千问2.1-图片编辑-图生图v260927_2103803289958703105.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（25 个）：
- `MarkdownNote`
- `QwenPERewriteT8`
- `ShowAnything|Mie`
- `EmptyLatentImage` ★核心
- `CLIPLoader`
- `EnhancedLoadDiffusionModel`
- `VAELoader_Any`
- `TextEncodeQwenImage21`
- `KSamplerCacheable` ★核心
- `QwenImage21Cache`
- `LoadImage`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `PreviewImage`
- `FastGroupsBypassSwitch`
- `ResolutionSelector`
- `JjkText`
- `VAEDecode` ★核心
- `SaveImage`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `612469955575595`
- `steps` = `50`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **80%**（20/25）

**有卡**：`QwenPERewriteT8`、`EmptyLatentImage`、`CLIPLoader`、`EnhancedLoadDiffusionModel`、`VAELoader_Any`、`TextEncodeQwenImage21`、`KSamplerCacheable`、`QwenImage21Cache`、`LoadImage`、`FastGroupsBypassSwitch`、`ResolutionSelector`、`VAEDecode`、`SaveImage`

**缺卡**（1）：`ShowAnything|Mie`

**用到的条目**：VAEDecode、TextEncodeQwenImage21、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage、QwenImage21Cache、KSamplerCacheable

## 学习发现

- 次要节点 `ShowAnything|Mie` 知识库中没有该节点类型的任何知识
