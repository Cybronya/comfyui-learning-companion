---
key: 图片生成/图生图/krea.2局部重绘（PS版本）_2070875464536776706.json
name: krea.2局部重绘（PS版本）_2070875464536776706.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/krea.2局部重绘（PS版本）_2070875464536776706.json
hash: c77ea1d3535a13da
coverage: 0.857143
learned_at: 2026-10-09 22:19:25
nodes: [CLIPLoader, VAELoader, UNETLoader, Image Comparer (rgthree), SaveImage, VAEDecode, KSamplerAdvanced, LoraLoaderModelOnly, ConditioningZeroOut, VAEEncode, CLIPTextEncode, LoadImage, Int, CR Text]
patterns: []
missing: [CR Text]
parameters: {"cfg": 8, "denoise": "sgm_uniform", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "enable", "steps": "randomize"}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识]
---

# 图片生成/图生图/krea.2局部重绘（PS版本）_2070875464536776706.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/2070875464536776706.json`

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
- `LoadImage`
- `Int`
- `CR Text`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `sgm_uniform`

## 知识

覆盖率 **86%**（12/14）

**有卡**：`CLIPLoader`、`VAELoader`、`UNETLoader`、`SaveImage`、`VAEDecode`、`KSamplerAdvanced`、`LoraLoaderModelOnly`、`ConditioningZeroOut`、`VAEEncode`、`CLIPTextEncode`、`LoadImage`、`Int`

**缺卡**（1）：`CR Text`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
