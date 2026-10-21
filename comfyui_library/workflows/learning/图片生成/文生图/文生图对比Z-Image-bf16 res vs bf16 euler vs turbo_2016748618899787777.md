---
key: 图片生成/文生图/文生图对比Z-Image-bf16 res vs bf16 euler vs turbo_2016748618899787777.json
name: 文生图对比Z-Image-bf16 res vs bf16 euler vs turbo_2016748618899787777
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/文生图对比Z-Image-bf16 res vs bf16 euler vs turbo_2016748618899787777.json
hash: 030d365209a2c3a6
coverage: 0.622222
learned_at: 2026-10-19 22:16:01
nodes: [VAEDecode, MarkdownNote, VAEDecode, MarkdownNote, MarkdownNote, MarkdownNote, SaveImage, easy cleanGpuUsed, Reroute, easy cleanGpuUsed, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, MarkdownNote, LayerUtility: ImageReelComposit, ModelSamplingAuraFlow, UNETLoader, SaveImage, MarkdownNote, VAELoader, CLIPTextEncode, Reroute, LayerUtility: ImageReel, CLIPTextEncode, ConditioningZeroOut, EmptySD3LatentImage, KSampler, KSampler, CLIPLoader, CLIPLoader, UNETLoader, CLIPTextEncode, MarkdownNote, VAEDecode, SaveImage, SaveImage, KSampler, easy seed, MarkdownNote, MuyeTextEditOutput, MarkdownNote, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 120537002179752, "steps": 10}
---

# 图片生成/文生图/文生图对比Z-Image-bf16 res vs bf16 euler vs turbo_2016748618899787777.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/文生图对比Z-Image-bf16 res vs bf16 euler vs turbo_2016748618899787777.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（45 个）：
- `VAEDecode` ★核心
- `MarkdownNote`
- `VAEDecode` ★核心
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `SaveImage`
- `easy cleanGpuUsed`
- `Reroute`
- `easy cleanGpuUsed`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `MarkdownNote`
- `LayerUtility: ImageReelComposit`
- `ModelSamplingAuraFlow`
- `UNETLoader` ★核心
- `SaveImage`
- `MarkdownNote`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `Reroute`
- `LayerUtility: ImageReel`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `EmptySD3LatentImage`
- `KSampler` ★核心
- `KSampler` ★核心
- `CLIPLoader`
- `CLIPLoader`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `MarkdownNote`
- `VAEDecode` ★核心
- `SaveImage`
- `SaveImage`
- `KSampler` ★核心
- `easy seed`
- `MarkdownNote`
- `MuyeTextEditOutput`
- `MarkdownNote`
- `LoadImage`

## 关键参数

- `seed` = `120537002179752`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **62%**（28/45）

**有卡**：`VAEDecode`、`SaveImage`、`easy cleanGpuUsed`、`LayerUtility: ImageReelComposit`、`ModelSamplingAuraFlow`、`UNETLoader`、`VAELoader`、`CLIPTextEncode`、`LayerUtility: ImageReel`、`ConditioningZeroOut`、`EmptySD3LatentImage`、`KSampler`、`CLIPLoader`、`easy seed`、`MuyeTextEditOutput`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、SaveImage、LoadImage
