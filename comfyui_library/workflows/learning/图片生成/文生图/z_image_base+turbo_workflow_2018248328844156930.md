---
key: 图片生成/文生图/z_image_base+turbo_workflow_2018248328844156930.json
name: z_image_base+turbo_workflow_2018248328844156930
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/z_image_base+turbo_workflow_2018248328844156930.json
hash: c5404b01a237a745
coverage: 0.8125
learned_at: 2026-10-19 22:30:15
nodes: [CLIPLoader, VAELoader, UNETLoader, PrimitiveNode, ModelSamplingAuraFlow, PrimitiveNode, EmptySD3LatentImage, PrimitiveNode, UNETLoader, ModelSamplingAuraFlow, KSamplerAdvanced, CLIPTextEncode, CLIPTextEncode, KSamplerAdvanced, SaveImage, VAEDecode]
patterns: []
missing: []
parameters: {"cfg": 20, "denoise": "simple", "sampler_name": 4, "scheduler": "res_multistep", "seed": "enable", "steps": "randomize"}
---

# 图片生成/文生图/z_image_base+turbo_workflow_2018248328844156930.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/z_image_base+turbo_workflow_2018248328844156930.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（16 个）：
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `PrimitiveNode`
- `ModelSamplingAuraFlow`
- `PrimitiveNode`
- `EmptySD3LatentImage`
- `PrimitiveNode`
- `UNETLoader` ★核心
- `ModelSamplingAuraFlow`
- `KSamplerAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `KSamplerAdvanced` ★核心
- `SaveImage`
- `VAEDecode` ★核心

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `20`
- `sampler_name` = `4`
- `scheduler` = `res_multistep`
- `denoise` = `simple`

## 知识

覆盖率 **81%**（13/16）

**有卡**：`CLIPLoader`、`VAELoader`、`UNETLoader`、`ModelSamplingAuraFlow`、`EmptySD3LatentImage`、`KSamplerAdvanced`、`CLIPTextEncode`、`SaveImage`、`VAEDecode`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、SaveImage、EmptySD3LatentImage
