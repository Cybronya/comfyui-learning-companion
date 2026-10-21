---
key: 图片生成/文生图/LH-DMT版本-2.生图片类-044.Qwen-Image-10步蒸馏-Q版3D人物_2016524825891704833.json
name: LH-DMT版本-2.生图片类-044.Qwen-Image-10步蒸馏-Q版3D人物_2016524825891704833
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/LH-DMT版本-2.生图片类-044.Qwen-Image-10步蒸馏-Q版3D人物_2016524825891704833.json
hash: bc34689dd958c9e4
coverage: 0.833333
learned_at: 2026-10-19 22:15:13
nodes: [CLIPTextEncode, CLIPTextEncode, UNETLoader, CLIPLoader, VAELoader, EmptySD3LatentImage, ModelSamplingAuraFlow, Note, KSampler, SaveImage, VAEDecode, MarkdownNote]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "res_multistep", "scheduler": "simple", "seed": 405461604411812, "steps": 10}
---

# 图片生成/文生图/LH-DMT版本-2.生图片类-044.Qwen-Image-10步蒸馏-Q版3D人物_2016524825891704833.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/LH-DMT版本-2.生图片类-044.Qwen-Image-10步蒸馏-Q版3D人物_2016524825891704833.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（12 个）：
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `EmptySD3LatentImage`
- `ModelSamplingAuraFlow`
- `Note`
- `KSampler` ★核心
- `SaveImage`
- `VAEDecode` ★核心
- `MarkdownNote`

## 关键参数

- `seed` = `405461604411812`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `res_multistep`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **83%**（10/12）

**有卡**：`CLIPTextEncode`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`EmptySD3LatentImage`、`ModelSamplingAuraFlow`、`KSampler`、`SaveImage`、`VAEDecode`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、SaveImage、EmptySD3LatentImage
