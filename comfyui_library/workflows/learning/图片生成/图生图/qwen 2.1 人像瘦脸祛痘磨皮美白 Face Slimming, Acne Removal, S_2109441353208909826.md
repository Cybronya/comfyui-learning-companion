---
key: 图片生成/图生图/qwen 2.1 人像瘦脸祛痘磨皮美白 Face Slimming, Acne Removal, S_2109441353208909826.json
name: qwen 2.1 人像瘦脸祛痘磨皮美白 Face Slimming, Acne Removal, S_2109441353208909826
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/qwen 2.1 人像瘦脸祛痘磨皮美白 Face Slimming, Acne Removal, S_2109441353208909826.json
hash: bcd805d373adabd1
coverage: 0.733333
learned_at: 2026-10-23 11:41:44
nodes: [CLIPLoader, QwenImage21Cache, VAEDecode, UNETLoader, CR Text Concatenate, JjkText, ShowText|pysssss, TextEncodeQwenImage21, VAELoader, KSampler, LoraLoaderModelOnly, SaveImage, Image Comparer (rgthree), LoadImage, JjkText]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 924224481403961, "steps": 40}
---

# 图片生成/图生图/qwen 2.1 人像瘦脸祛痘磨皮美白 Face Slimming, Acne Removal, S_2109441353208909826.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/qwen 2.1 人像瘦脸祛痘磨皮美白 Face Slimming, Acne Removal, S_2109441353208909826.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（15 个）：
- `CLIPLoader`
- `QwenImage21Cache`
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `CR Text Concatenate`
- `JjkText`
- `ShowText|pysssss`
- `TextEncodeQwenImage21`
- `VAELoader`
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `SaveImage`
- `Image Comparer (rgthree)`
- `LoadImage`
- `JjkText`

## 关键参数

- `seed` = `924224481403961`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **73%**（11/15）

**有卡**：`CLIPLoader`、`QwenImage21Cache`、`VAEDecode`、`UNETLoader`、`CR Text Concatenate`、`TextEncodeQwenImage21`、`VAELoader`、`KSampler`、`LoraLoaderModelOnly`、`SaveImage`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、QwenImage21Cache
