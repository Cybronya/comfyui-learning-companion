---
key: 平台全量/Qwen Image2.1 精准抠图 移除遮挡_2105662821404073986.json
name: Qwen Image2.1 精准抠图 移除遮挡_2105662821404073986
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Qwen Image2.1 精准抠图 移除遮挡_2105662821404073986.json
hash: 68a5df801d049289
coverage: 0.9
learned_at: 2026-11-14 00:50:18
nodes: [LoadImage, ComfySwitchNode, Seed (rgthree), Text Multiline, XinbaoImageStandardizer, ResolutionSelector, EmptyLatentImage, VAELoader, CLIPLoader, LoraLoaderModelOnly, UNETLoader, VAEDecode, ImageConcanate, SaveImageAdvanced, TextEncodeQwenImage21, QwenImage21Cache, KSampler, Image Comparer (rgthree), SaveImage, SaveImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 863456957738568, "steps": 25, "width": 1024}
---

# 平台全量/Qwen Image2.1 精准抠图 移除遮挡_2105662821404073986.json

> 来源文件 `comfyui_library/workflows/平台全量/Qwen Image2.1 精准抠图 移除遮挡_2105662821404073986.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（20 个）：
- `LoadImage`
- `ComfySwitchNode`
- `Seed (rgthree)`
- `Text Multiline`
- `XinbaoImageStandardizer`
- `ResolutionSelector`
- `EmptyLatentImage` ★核心
- `VAELoader`
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `ImageConcanate`
- `SaveImageAdvanced`
- `TextEncodeQwenImage21`
- `QwenImage21Cache`
- `KSampler` ★核心
- `Image Comparer (rgthree)`
- `SaveImage`
- `SaveImage`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `863456957738568`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **90%**（18/20）

**有卡**：`LoadImage`、`Seed (rgthree)`、`Text Multiline`、`XinbaoImageStandardizer`、`ResolutionSelector`、`EmptyLatentImage`、`VAELoader`、`CLIPLoader`、`LoraLoaderModelOnly`、`UNETLoader`、`VAEDecode`、`ImageConcanate`、`SaveImageAdvanced`、`TextEncodeQwenImage21`、`QwenImage21Cache`、`KSampler`、`SaveImage`

**用到的条目**：KSampler、TextEncodeQwenImage21、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、ResolutionSelector
