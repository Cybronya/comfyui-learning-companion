---
key: Wan2.2文生图最优实现_1950849465034940417.json
name: Wan2.2文生图最优实现_1950849465034940417
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Wan2.2文生图最优实现_1950849465034940417.json
hash: 7a625dd4050db5b8
coverage: 0.823529
learned_at: 2026-10-10 20:59:14
nodes: [easy seed, VAEDecode, UNETLoader, CLIPLoader, VAELoader, UNETLoader, ModelSamplingSD3, ModelSamplingSD3, CLIPTextEncode, CLIPTextEncode, EmptyHunyuanLatentVideo, VAEDecode, PreviewImage, KSampler, KSampler, String Literal, SaveImage]
patterns: []
missing: [String Literal, easy seed]
parameters: {"cfg": 3.5, "denoise": 0.5000000000000001, "sampler_name": "euler", "scheduler": "simple", "seed": 489343023618309, "steps": 20}
discoveries: [次要节点 `String Literal` 知识库中没有该节点类型的任何知识, 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明]
---

# Wan2.2文生图最优实现_1950849465034940417.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Wan2.2文生图最优实现_1950849465034940417.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（17 个）：
- `easy seed`
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `EmptyHunyuanLatentVideo`
- `VAEDecode` ★核心
- `PreviewImage`
- `KSampler` ★核心
- `KSampler` ★核心
- `String Literal`
- `SaveImage`

## 关键参数

- `seed` = `489343023618309`
- `steps` = `20`
- `cfg` = `3.5`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.5000000000000001`

## 知识

覆盖率 **82%**（14/17）

**有卡**：`VAEDecode`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`ModelSamplingSD3`、`CLIPTextEncode`、`EmptyHunyuanLatentVideo`、`KSampler`、`SaveImage`

**缺卡**（2）：`String Literal`、`easy seed`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、EmptyHunyuanLatentVideo、SaveImage

## 学习发现

- 次要节点 `String Literal` 知识库中没有该节点类型的任何知识
- 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明
