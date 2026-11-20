---
key: 平台全量/qwen image2.1-扩图_2110323479294857217.json
name: qwen image2.1-扩图_2110323479294857217
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/qwen image2.1-扩图_2110323479294857217.json
hash: 3c6e8fcc066161f2
coverage: 0.8125
learned_at: 2026-11-14 01:16:01
nodes: [CLIPLoader, SaveImage, Image Comparer (rgthree), UNETLoader, VAELoader, VAEDecode, QwenImage21Cache, LoraLoaderModelOnly, LoadImage, ImagePadForOutpaint, PreviewAny, PreviewAny, GetImageSize, KSampler, EmptyLatentImage, TextEncodeQwenImage21]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 2560, "sampler_name": "euler", "scheduler": "normal", "seed": 673376011695723, "steps": 25, "width": 2384}
---

# 平台全量/qwen image2.1-扩图_2110323479294857217.json

> 来源文件 `comfyui_library/workflows/平台全量/qwen image2.1-扩图_2110323479294857217.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（16 个）：
- `CLIPLoader`
- `SaveImage`
- `Image Comparer (rgthree)`
- `UNETLoader` ★核心
- `VAELoader`
- `VAEDecode` ★核心
- `QwenImage21Cache`
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `ImagePadForOutpaint`
- `PreviewAny`
- `PreviewAny`
- `GetImageSize`
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `TextEncodeQwenImage21`

## 关键参数

- `seed` = `673376011695723`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`
- `width` = `2384`
- `height` = `2560`
- `batch_size` = `1`

## 知识

覆盖率 **81%**（13/16）

**有卡**：`CLIPLoader`、`SaveImage`、`UNETLoader`、`VAELoader`、`VAEDecode`、`QwenImage21Cache`、`LoraLoaderModelOnly`、`LoadImage`、`ImagePadForOutpaint`、`GetImageSize`、`KSampler`、`EmptyLatentImage`、`TextEncodeQwenImage21`

**用到的条目**：KSampler、TextEncodeQwenImage21、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、LoadImage
