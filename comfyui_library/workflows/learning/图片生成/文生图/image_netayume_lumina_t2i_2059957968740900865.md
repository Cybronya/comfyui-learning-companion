---
key: 图片生成/文生图/image_netayume_lumina_t2i_2059957968740900865.json
name: image_netayume_lumina_t2i_2059957968740900865
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/image_netayume_lumina_t2i_2059957968740900865.json
hash: 425cd508f781ace3
coverage: 0.642857
learned_at: 2026-10-19 23:03:20
nodes: [ModelSamplingAuraFlow, PrimitiveStringMultiline, PrimitiveStringMultiline, CheckpointLoaderSimple, EmptySD3LatentImage, StringConcatenate, CLIPTextEncode, CLIPTextEncode, KSampler, VAEDecode, SaveImage, MarkdownNote, MarkdownNote, MarkdownNote]
patterns: []
missing: []
parameters: {"cfg": 4, "checkpoint": "NetaYumev35_pretrained_all_in_one.safetensors", "denoise": 1, "sampler_name": "res_multistep", "scheduler": "simple", "seed": 717507911953308, "steps": 30}
---

# 图片生成/文生图/image_netayume_lumina_t2i_2059957968740900865.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/image_netayume_lumina_t2i_2059957968740900865.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（14 个）：
- `ModelSamplingAuraFlow`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `CheckpointLoaderSimple` ★核心
- `EmptySD3LatentImage`
- `StringConcatenate`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`

## 关键参数

- `checkpoint` = `NetaYumev35_pretrained_all_in_one.safetensors`
- `seed` = `717507911953308`
- `steps` = `30`
- `cfg` = `4`
- `sampler_name` = `res_multistep`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **64%**（9/14）

**有卡**：`ModelSamplingAuraFlow`、`CheckpointLoaderSimple`、`EmptySD3LatentImage`、`StringConcatenate`、`CLIPTextEncode`、`KSampler`、`VAEDecode`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、SaveImage、EmptySD3LatentImage、ModelSamplingAuraFlow、StringConcatenate
