---
key: 图片生成/图生图/Qwen Image 2.1 透明图层抠图改图_2108778898052968449.json
name: Qwen Image 2.1 透明图层抠图改图_2108778898052968449
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 透明图层抠图改图_2108778898052968449.json
hash: 4a71a50a6ea94a3a
coverage: 0.941176
learned_at: 2026-10-23 11:12:45
nodes: [PathchSageAttentionKJ, QwenImage21Cache, ModelAttentionBackend, TextEncodeQwenImage21, CLIPLoader, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, LoadImage, KSampler, VAELoader, VAEDecode, SaveImage, PixaromaLabel, UNETLoader, LoraLoaderModelOnly, CR Prompt Text, SaveImageAdvanced]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 742380036838239, "steps": 40}
---

# 图片生成/图生图/Qwen Image 2.1 透明图层抠图改图_2108778898052968449.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 透明图层抠图改图_2108778898052968449.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（17 个）：
- `PathchSageAttentionKJ`
- `QwenImage21Cache`
- `ModelAttentionBackend`
- `TextEncodeQwenImage21`
- `CLIPLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewImage`
- `LoadImage`
- `KSampler` ★核心
- `VAELoader`
- `VAEDecode` ★核心
- `SaveImage`
- `PixaromaLabel`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `CR Prompt Text`
- `SaveImageAdvanced`

## 关键参数

- `seed` = `742380036838239`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **94%**（16/17）

**有卡**：`PathchSageAttentionKJ`、`QwenImage21Cache`、`ModelAttentionBackend`、`TextEncodeQwenImage21`、`CLIPLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`KSampler`、`VAELoader`、`VAEDecode`、`SaveImage`、`PixaromaLabel`、`UNETLoader`、`LoraLoaderModelOnly`、`CR Prompt Text`、`SaveImageAdvanced`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、QwenImage21Cache
