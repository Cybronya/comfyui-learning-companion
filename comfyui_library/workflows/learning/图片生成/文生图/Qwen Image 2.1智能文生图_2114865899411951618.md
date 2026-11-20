---
key: 图片生成/文生图/Qwen Image 2.1智能文生图_2114865899411951618.json
name: Qwen Image 2.1智能文生图_2114865899411951618
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1智能文生图_2114865899411951618.json
hash: 2f62d9a0b80d3e1e
coverage: 0.727273
learned_at: 2026-11-02 19:15:47
nodes: [ResolutionSelector, UNETLoader, TextEncodeQwenImage21, CLIPLoader, VAELoader, EmptyLatentImage, VAEDecode, KSampler, TextGenerate, PreviewAny, CLIPLoader, PrimitiveStringMultiline, QwenImage21Cache, Display Int (rgthree), Display Int (rgthree), 孤海注释, Text Prompt (JPS), GoohaiUniversalSlider, 孤海注释, 孤海注释, MarkdownNote, SaveImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 30, "steps": 25, "width": 1024}
---

# 图片生成/文生图/Qwen Image 2.1智能文生图_2114865899411951618.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1智能文生图_2114865899411951618.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（22 个）：
- `ResolutionSelector`
- `UNETLoader` ★核心
- `TextEncodeQwenImage21`
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `KSampler` ★核心
- `TextGenerate`
- `PreviewAny`
- `CLIPLoader`
- `PrimitiveStringMultiline`
- `QwenImage21Cache`
- `Display Int (rgthree)`
- `Display Int (rgthree)`
- `孤海注释`
- `Text Prompt (JPS)`
- `GoohaiUniversalSlider`
- `孤海注释`
- `孤海注释`
- `MarkdownNote`
- `SaveImage`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `30`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **73%**（16/22）

**有卡**：`ResolutionSelector`、`UNETLoader`、`TextEncodeQwenImage21`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`VAEDecode`、`KSampler`、`TextGenerate`、`QwenImage21Cache`、`Display Int (rgthree)`、`Text Prompt (JPS)`、`GoohaiUniversalSlider`、`SaveImage`

**用到的条目**：KSampler、TextEncodeQwenImage21、VAEDecode、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、QwenImage21Cache
