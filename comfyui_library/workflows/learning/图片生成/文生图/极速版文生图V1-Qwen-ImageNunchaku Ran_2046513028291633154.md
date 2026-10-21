---
key: 图片生成/文生图/极速版文生图V1-Qwen-ImageNunchaku Ran_2046513028291633154.json
name: 极速版文生图V1-Qwen-ImageNunchaku Ran_2046513028291633154
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/极速版文生图V1-Qwen-ImageNunchaku Ran_2046513028291633154.json
hash: 9fdb20ef04088aac
coverage: 0.785714
learned_at: 2026-10-21 03:01:35
nodes: [VAELoader, SaveImage, EmptySD3LatentImage, CLIPTextEncode, CLIPLoader, ModelSamplingAuraFlow, Note, KSampler, NunchakuQwenImageDiTLoader, LayerUtility: PurgeVRAM, VAEDecode, Note, MarkdownNote, CLIPTextEncode]
patterns: []
missing: []
parameters: {"cfg": 2.5, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 788264225973121, "steps": 20}
---

# 图片生成/文生图/极速版文生图V1-Qwen-ImageNunchaku Ran_2046513028291633154.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/极速版文生图V1-Qwen-ImageNunchaku Ran_2046513028291633154.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（14 个）：
- `VAELoader`
- `SaveImage`
- `EmptySD3LatentImage`
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `ModelSamplingAuraFlow`
- `Note`
- `KSampler` ★核心
- `NunchakuQwenImageDiTLoader`
- `LayerUtility: PurgeVRAM`
- `VAEDecode` ★核心
- `Note`
- `MarkdownNote`
- `CLIPTextEncode` ★核心

## 关键参数

- `seed` = `788264225973121`
- `steps` = `20`
- `cfg` = `2.5`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **79%**（11/14）

**有卡**：`VAELoader`、`SaveImage`、`EmptySD3LatentImage`、`CLIPTextEncode`、`CLIPLoader`、`ModelSamplingAuraFlow`、`KSampler`、`NunchakuQwenImageDiTLoader`、`LayerUtility: PurgeVRAM`、`VAEDecode`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、SaveImage、EmptySD3LatentImage、ModelSamplingAuraFlow
