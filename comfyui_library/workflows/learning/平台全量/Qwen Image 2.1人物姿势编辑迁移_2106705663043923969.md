---
key: 平台全量/Qwen Image 2.1人物姿势编辑迁移_2106705663043923969.json
name: Qwen Image 2.1人物姿势编辑迁移_2106705663043923969
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Qwen Image 2.1人物姿势编辑迁移_2106705663043923969.json
hash: 3c66119ecdfd8e3b
coverage: 0.710526
learned_at: 2026-11-14 00:50:02
nodes: [UNETLoader, VAELoader, EmptyLatentImage, VAEDecode, ComfySwitchNode, QwenImage21Cache, CLIPLoader, easy showAnything, SaveImageAdvanced, AnyLineArtPreprocessor_aux, LoadDepthPro, LoadImage, DepthPro, MetricDepthToRelative, DWPreprocessor, LoadImage, 孤海注释, ImageResizeKJv2, TTResolutionSelector, PreviewImage, PreviewImage, PreviewImage, TextEncodeQwenImage21, PreviewImage, PreviewImage, PreviewImage, PreviewImage, MuyeTextEditOutput, BatchImagesNode, ResolutionSelector, KSampler, CLIPLoader, SaveImage, easy cleanGpuUsed, Fast Groups Bypasser (rgthree), PoseForge3D.PoseEditor, CR Prompt Text, TextGenerate]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 294541098258124, "steps": 40, "width": 1024}
---

# 平台全量/Qwen Image 2.1人物姿势编辑迁移_2106705663043923969.json

> 来源文件 `comfyui_library/workflows/平台全量/Qwen Image 2.1人物姿势编辑迁移_2106705663043923969.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（38 个）：
- `UNETLoader` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `ComfySwitchNode`
- `QwenImage21Cache`
- `CLIPLoader`
- `easy showAnything`
- `SaveImageAdvanced`
- `AnyLineArtPreprocessor_aux`
- `LoadDepthPro`
- `LoadImage`
- `DepthPro`
- `MetricDepthToRelative`
- `DWPreprocessor`
- `LoadImage`
- `孤海注释`
- `ImageResizeKJv2`
- `TTResolutionSelector`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `TextEncodeQwenImage21`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `MuyeTextEditOutput`
- `BatchImagesNode`
- `ResolutionSelector`
- `KSampler` ★核心
- `CLIPLoader`
- `SaveImage`
- `easy cleanGpuUsed`
- `Fast Groups Bypasser (rgthree)`
- `PoseForge3D.PoseEditor`
- `CR Prompt Text`
- `TextGenerate`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `294541098258124`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **71%**（27/38）

**有卡**：`UNETLoader`、`VAELoader`、`EmptyLatentImage`、`VAEDecode`、`QwenImage21Cache`、`CLIPLoader`、`SaveImageAdvanced`、`AnyLineArtPreprocessor_aux`、`LoadDepthPro`、`LoadImage`、`DepthPro`、`MetricDepthToRelative`、`DWPreprocessor`、`ImageResizeKJv2`、`TTResolutionSelector`、`TextEncodeQwenImage21`、`MuyeTextEditOutput`、`BatchImagesNode`、`ResolutionSelector`、`KSampler`、`SaveImage`、`easy cleanGpuUsed`、`PoseForge3D.PoseEditor`、`CR Prompt Text`、`TextGenerate`

**用到的条目**：KSampler、TextEncodeQwenImage21、VAEDecode、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、SaveImage
