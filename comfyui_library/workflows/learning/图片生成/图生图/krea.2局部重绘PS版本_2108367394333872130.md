---
key: 图片生成/图生图/krea.2局部重绘PS版本_2108367394333872130.json
name: krea.2局部重绘PS版本_2108367394333872130
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/krea.2局部重绘PS版本_2108367394333872130.json
hash: b7003c833b83884d
coverage: 0.928571
learned_at: 2026-10-21 00:45:43
nodes: [CLIPLoader, VAELoader, UNETLoader, Image Comparer (rgthree), SaveImage, VAEDecode, KSamplerAdvanced, LoraLoaderModelOnly, ConditioningZeroOut, VAEEncode, CLIPTextEncode, Int, CR Text, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "sgm_uniform", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "enable", "steps": "randomize"}
---

# 图片生成/图生图/krea.2局部重绘PS版本_2108367394333872130.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/krea.2局部重绘PS版本_2108367394333872130.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Output → Other

**节点**（14 个）：
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `Image Comparer (rgthree)`
- `SaveImage`
- `VAEDecode` ★核心
- `KSamplerAdvanced` ★核心
- `LoraLoaderModelOnly` ★核心
- `ConditioningZeroOut`
- `VAEEncode` ★核心
- `CLIPTextEncode` ★核心
- `Int`
- `CR Text`
- `LoadImage`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `sgm_uniform`

## 知识

覆盖率 **93%**（13/14）

**有卡**：`CLIPLoader`、`VAELoader`、`UNETLoader`、`SaveImage`、`VAEDecode`、`KSamplerAdvanced`、`LoraLoaderModelOnly`、`ConditioningZeroOut`、`VAEEncode`、`CLIPTextEncode`、`Int`、`CR Text`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader
