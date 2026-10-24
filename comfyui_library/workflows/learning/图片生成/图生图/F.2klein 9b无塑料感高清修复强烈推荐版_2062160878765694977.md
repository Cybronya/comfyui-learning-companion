---
key: 图片生成/图生图/F.2klein 9b无塑料感高清修复强烈推荐版_2062160878765694977.json
name: F.2klein 9b无塑料感高清修复强烈推荐版_2062160878765694977
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/F.2klein 9b无塑料感高清修复强烈推荐版_2062160878765694977.json
hash: 92a64bdf497bf671
coverage: 0.933333
learned_at: 2026-10-23 10:52:50
nodes: [ConditioningZeroOut, KSamplerAdvanced, VAELoader, CLIPLoader, LoadImage, ImageResizeKJv2, UNETLoader, ReferenceLatent, VAEEncode, CLIPTextEncode, Image Comparer (rgthree), LoraLoaderModelOnly, easy imageColorMatch, VAEDecode, SaveImage]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "FlowMatchEulerDiscreteScheduler", "sampler_name": 1, "scheduler": "sa_solver", "seed": "disable", "steps": "fixed"}
---

# 图片生成/图生图/F.2klein 9b无塑料感高清修复强烈推荐版_2062160878765694977.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/F.2klein 9b无塑料感高清修复强烈推荐版_2062160878765694977.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（15 个）：
- `ConditioningZeroOut`
- `KSamplerAdvanced` ★核心
- `VAELoader`
- `CLIPLoader`
- `LoadImage`
- `ImageResizeKJv2`
- `UNETLoader` ★核心
- `ReferenceLatent`
- `VAEEncode` ★核心
- `CLIPTextEncode` ★核心
- `Image Comparer (rgthree)`
- `LoraLoaderModelOnly` ★核心
- `easy imageColorMatch`
- `VAEDecode` ★核心
- `SaveImage`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `sa_solver`
- `denoise` = `FlowMatchEulerDiscreteScheduler`

## 知识

覆盖率 **93%**（14/15）

**有卡**：`ConditioningZeroOut`、`KSamplerAdvanced`、`VAELoader`、`CLIPLoader`、`LoadImage`、`ImageResizeKJv2`、`UNETLoader`、`ReferenceLatent`、`VAEEncode`、`CLIPTextEncode`、`LoraLoaderModelOnly`、`easy imageColorMatch`、`VAEDecode`、`SaveImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader
