---
key: 平台全量/Qwen Image 2.1 单图_多图编辑工作流20261103_2117550983411752962.json
name: Qwen Image 2.1 单图_多图编辑工作流20261103_2117550983411752962
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Qwen Image 2.1 单图_多图编辑工作流20261103_2117550983411752962.json
hash: 7f3c91b406094233
coverage: 0.828571
learned_at: 2026-11-14 00:49:56
nodes: [UNETLoader, CLIPLoader, VAELoader, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, TextEncodeQwenImage21, QwenImage21Cache, KSampler, VAEDecode, GoohaiUniversalSlider, SaveImage, Image Comparer (rgthree), 孤海注释, 孤海注释, MarkdownNote, GoohaiUniversalSlider, MarkdownNote, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, SaveImage, TextEncodeQwenImage21, KSampler, VAELoader, CLIPLoader, UNETLoader, QwenImage21Cache, VAEDecode, 孤海注释, LoadImage, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, 忽略多组孤海, Text Prompt (JPS), Text Prompt (JPS)]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 54, "steps": 25}
---

# 平台全量/Qwen Image 2.1 单图_多图编辑工作流20261103_2117550983411752962.json

> 来源文件 `comfyui_library/workflows/平台全量/Qwen Image 2.1 单图_多图编辑工作流20261103_2117550983411752962.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（35 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `TextEncodeQwenImage21`
- `QwenImage21Cache`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `GoohaiUniversalSlider`
- `SaveImage`
- `Image Comparer (rgthree)`
- `孤海注释`
- `孤海注释`
- `MarkdownNote`
- `GoohaiUniversalSlider`
- `MarkdownNote`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SaveImage`
- `TextEncodeQwenImage21`
- `KSampler` ★核心
- `VAELoader`
- `CLIPLoader`
- `UNETLoader` ★核心
- `QwenImage21Cache`
- `VAEDecode` ★核心
- `孤海注释`
- `LoadImage`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `忽略多组孤海`
- `Text Prompt (JPS)`
- `Text Prompt (JPS)`

## 关键参数

- `seed` = `54`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **83%**（29/35）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`TextEncodeQwenImage21`、`QwenImage21Cache`、`KSampler`、`VAEDecode`、`GoohaiUniversalSlider`、`SaveImage`、`忽略多组孤海`、`Text Prompt (JPS)`

**用到的条目**：KSampler、TextEncodeQwenImage21、VAEDecode、VAELoader、CLIPLoader、LoadImage、QwenImage21Cache、UNETLoader
