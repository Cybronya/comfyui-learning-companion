---
key: 图片生成/图生图/Qwen Image 2.1 金属产品白底精修｜可自动扣图_2104383255930826754.json
name: Qwen Image 2.1 金属产品白底精修｜可自动扣图_2104383255930826754
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 金属产品白底精修｜可自动扣图_2104383255930826754.json
hash: d77ef938e483a9c9
coverage: 0.76
learned_at: 2026-10-21 00:42:16
nodes: [CLIPLoader, VAELoader, easy promptConcat, JjkText, JjkText, ComfySwitchNode, UNETLoader, LoraLoaderModelOnly, QwenImage21Cache, KSampler, VAELoader, VAEDecode, LayerMask: BiRefNetUltraV2, GrowMask, InvertMask, LayerMask: LoadBiRefNetModelV2, Any Switch (rgthree), JoinImageWithAlpha, SaveImage, LoadImage, TextEncodeQwenImage21, 忽略多组孤海, PrimitiveNode, Int, JjkText]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 376522998715178, "steps": 25}
---

# 图片生成/图生图/Qwen Image 2.1 金属产品白底精修｜可自动扣图_2104383255930826754.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 金属产品白底精修｜可自动扣图_2104383255930826754.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（25 个）：
- `CLIPLoader`
- `VAELoader`
- `easy promptConcat`
- `JjkText`
- `JjkText`
- `ComfySwitchNode`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `QwenImage21Cache`
- `KSampler` ★核心
- `VAELoader`
- `VAEDecode` ★核心
- `LayerMask: BiRefNetUltraV2`
- `GrowMask`
- `InvertMask`
- `LayerMask: LoadBiRefNetModelV2`
- `Any Switch (rgthree)`
- `JoinImageWithAlpha`
- `SaveImage`
- `LoadImage`
- `TextEncodeQwenImage21`
- `忽略多组孤海`
- `PrimitiveNode`
- `Int`
- `JjkText`

## 关键参数

- `seed` = `376522998715178`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **76%**（19/25）

**有卡**：`CLIPLoader`、`VAELoader`、`easy promptConcat`、`UNETLoader`、`LoraLoaderModelOnly`、`QwenImage21Cache`、`KSampler`、`VAEDecode`、`LayerMask: BiRefNetUltraV2`、`GrowMask`、`InvertMask`、`LayerMask: LoadBiRefNetModelV2`、`JoinImageWithAlpha`、`SaveImage`、`LoadImage`、`TextEncodeQwenImage21`、`忽略多组孤海`、`Int`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、QwenImage21Cache
