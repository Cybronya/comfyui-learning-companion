---
key: 视频生成/文生视频/Anima-2.9B官方文生图_2089581532066443265.json
name: Anima-2.9B官方文生图_2089581532066443265
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Anima-2.9B官方文生图_2089581532066443265.json
hash: f59156a88f1669c3
coverage: 0.941176
learned_at: 2026-10-15 22:44:02
nodes: [SaveImage, SamplerCustomAdvanced, KSamplerSelect, BasicScheduler, CFGGuider, RandomNoise, KSampler Config (rgthree), CLIPLoader, VAEDecode, ImpactSwitch, UNETLoader, CLIPTextEncode, CLIPTextEncode, VAELoaderKJ, EmptyLatentImage, EmptyLatentImage, PathchSageAttentionKJ]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 1536, "width": 1152}
---

# 视频生成/文生视频/Anima-2.9B官方文生图_2089581532066443265.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Anima-2.9B官方文生图_2089581532066443265.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（17 个）：
- `SaveImage`
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `CFGGuider`
- `RandomNoise`
- `KSampler Config (rgthree)` ★核心
- `CLIPLoader`
- `VAEDecode` ★核心
- `ImpactSwitch`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAELoaderKJ`
- `EmptyLatentImage` ★核心
- `EmptyLatentImage` ★核心
- `PathchSageAttentionKJ`

## 关键参数

- `width` = `1152`
- `height` = `1536`
- `batch_size` = `1`

## 知识

覆盖率 **94%**（16/17）

**有卡**：`SaveImage`、`SamplerCustomAdvanced`、`KSamplerSelect`、`BasicScheduler`、`CFGGuider`、`RandomNoise`、`KSampler Config (rgthree)`、`CLIPLoader`、`VAEDecode`、`UNETLoader`、`CLIPTextEncode`、`VAELoaderKJ`、`EmptyLatentImage`、`PathchSageAttentionKJ`

**用到的条目**：VAEDecode、CLIPTextEncode、CLIPLoader、EmptyLatentImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
