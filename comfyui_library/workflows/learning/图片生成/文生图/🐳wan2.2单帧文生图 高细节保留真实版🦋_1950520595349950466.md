---
key: 图片生成/文生图/🐳wan2.2单帧文生图 高细节保留真实版🦋_1950520595349950466.json
name: 🐳wan2.2单帧文生图 高细节保留真实版🦋_1950520595349950466.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/🐳wan2.2单帧文生图 高细节保留真实版🦋_1950520595349950466.json
hash: 48c1f945ea0d974b
coverage: 0.833333
learned_at: 2026-10-07 22:58:30
nodes: [ModelSamplingSD3, ModelSamplingSD3, ImpactInt, ImpactInt, Float, VAEDecode, CLIPTextEncode, CLIPLoader, ImpactInt, ImpactInt, EmptyHunyuanLatentVideo, ImpactInt, SaveImage, CLIPTextEncode, KSamplerAdvanced, KSamplerAdvanced, Switch any [Crystools], MarkdownNote, Note Plus (mtb), UNETLoader, UNETLoader, VAELoader, RH_LLMAPI_NODE, CR Text]
patterns: []
missing: [CR Text, Note Plus (mtb), Switch any [Crystools]]
parameters: {"cfg": 25, "denoise": "beta", "sampler_name": 5, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `Note Plus (mtb)` 知识库中没有该节点类型的任何知识, 次要节点 `Switch any [Crystools]` 知识库中没有该节点类型的任何知识]
---

# 图片生成/文生图/🐳wan2.2单帧文生图 高细节保留真实版🦋_1950520595349950466.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/1950520595349950466.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（24 个）：
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `ImpactInt`
- `ImpactInt`
- `Float`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `ImpactInt`
- `ImpactInt`
- `EmptyHunyuanLatentVideo`
- `ImpactInt`
- `SaveImage`
- `CLIPTextEncode` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `Switch any [Crystools]`
- `MarkdownNote`
- `Note Plus (mtb)`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `VAELoader`
- `RH_LLMAPI_NODE`
- `CR Text`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `25`
- `sampler_name` = `5`
- `scheduler` = `euler`
- `denoise` = `beta`

## 知识

覆盖率 **83%**（20/24）

**有卡**：`ModelSamplingSD3`、`ImpactInt`、`Float`、`VAEDecode`、`CLIPTextEncode`、`CLIPLoader`、`EmptyHunyuanLatentVideo`、`SaveImage`、`KSamplerAdvanced`、`UNETLoader`、`VAELoader`、`RH_LLMAPI_NODE`

**缺卡**（3）：`CR Text`、`Note Plus (mtb)`、`Switch any [Crystools]`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、EmptyHunyuanLatentVideo、SaveImage

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `Note Plus (mtb)` 知识库中没有该节点类型的任何知识
- 次要节点 `Switch any [Crystools]` 知识库中没有该节点类型的任何知识
