---
key: 图片生成/文生图/Qwen Image 2.1-mxlz- skills文生图+放大2K,4K_2102952303706857474.json
name: Qwen Image 2.1-mxlz- skills文生图+放大2K,4K_2102952303706857474
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1-mxlz- skills文生图+放大2K,4K_2102952303706857474.json
hash: 9c31e987f2d91c67
coverage: 0.807692
learned_at: 2026-10-15 22:26:58
nodes: [VAELoader, ComfySwitchNode, UNETLoader, CLIPLoader, EmptyLatentImage, PlaySound|pysssss, VAEDecode, easy cleanGpuUsed, PreviewImage, Image Remove Alpha JK, VOSR2Upscale, VOSR2ModelLoader, ImageApplyLUT+, SaveImage, UNETLoader, CLIPLoader, TextEncodeQwenImage21, SaveImage, ResolutionSelector, QwenImage21Cache, KSampler, easy imageChooser, Note, MarkdownNote, PrimitiveStringMultiline, Lora Loader Stack (rgthree)]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 3, "steps": 40, "width": 1024}
---

# 图片生成/文生图/Qwen Image 2.1-mxlz- skills文生图+放大2K,4K_2102952303706857474.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1-mxlz- skills文生图+放大2K,4K_2102952303706857474.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（26 个）：
- `VAELoader`
- `ComfySwitchNode`
- `UNETLoader` ★核心
- `CLIPLoader`
- `EmptyLatentImage` ★核心
- `PlaySound|pysssss`
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `PreviewImage`
- `Image Remove Alpha JK`
- `VOSR2Upscale`
- `VOSR2ModelLoader`
- `ImageApplyLUT+`
- `SaveImage`
- `UNETLoader` ★核心
- `CLIPLoader`
- `TextEncodeQwenImage21`
- `SaveImage`
- `ResolutionSelector`
- `QwenImage21Cache`
- `KSampler` ★核心
- `easy imageChooser`
- `Note`
- `MarkdownNote`
- `PrimitiveStringMultiline`
- `Lora Loader Stack (rgthree)`

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

覆盖率 **81%**（21/26）

**有卡**：`VAELoader`、`UNETLoader`、`CLIPLoader`、`EmptyLatentImage`、`PlaySound|pysssss`、`VAEDecode`、`easy cleanGpuUsed`、`Image Remove Alpha JK`、`VOSR2Upscale`、`VOSR2ModelLoader`、`ImageApplyLUT+`、`SaveImage`、`TextEncodeQwenImage21`、`ResolutionSelector`、`QwenImage21Cache`、`KSampler`、`easy imageChooser`、`Lora Loader Stack (rgthree)`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、QwenImage21Cache
