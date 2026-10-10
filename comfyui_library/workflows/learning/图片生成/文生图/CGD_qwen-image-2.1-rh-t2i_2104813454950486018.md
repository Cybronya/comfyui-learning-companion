---
key: CGD_qwen-image-2.1-rh-t2i_2104813454950486018.json
name: CGD_qwen-image-2.1-rh-t2i_2104813454950486018
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/CGD_qwen-image-2.1-rh-t2i_2104813454950486018.json
hash: fa595e4f2e84158d
coverage: 0.722222
learned_at: 2026-10-10 21:26:34
nodes: [MarkdownNote, CLIPLoader, VAELoader, QwenImage21Cache, UNETLoader, KSampler, EmptyLatentImage, ResolutionSelector, MarkdownNote, PrimitiveStringMultiline, CLIPLoader, TextGenerate, VAEDecode, SaveImageAdvanced, SaveImage, ComfySwitchNode, PreviewAny, TextEncodeQwenImage21]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 447606998181262, "steps": 25, "width": 1024}
---

# CGD_qwen-image-2.1-rh-t2i_2104813454950486018.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/CGD_qwen-image-2.1-rh-t2i_2104813454950486018.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（18 个）：
- `MarkdownNote`
- `CLIPLoader`
- `VAELoader`
- `QwenImage21Cache`
- `UNETLoader` ★核心
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `ResolutionSelector`
- `MarkdownNote`
- `PrimitiveStringMultiline`
- `CLIPLoader`
- `TextGenerate`
- `VAEDecode` ★核心
- `SaveImageAdvanced`
- `SaveImage`
- `ComfySwitchNode`
- `PreviewAny`
- `TextEncodeQwenImage21`

## 关键参数

- `seed` = `447606998181262`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **72%**（13/18）

**有卡**：`CLIPLoader`、`VAELoader`、`QwenImage21Cache`、`UNETLoader`、`KSampler`、`EmptyLatentImage`、`ResolutionSelector`、`TextGenerate`、`VAEDecode`、`SaveImageAdvanced`、`SaveImage`、`TextEncodeQwenImage21`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、QwenImage21Cache
