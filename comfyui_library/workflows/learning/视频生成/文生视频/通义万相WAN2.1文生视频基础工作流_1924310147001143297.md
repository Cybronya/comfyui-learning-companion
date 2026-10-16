---
key: 视频生成/文生视频/通义万相WAN2.1文生视频基础工作流_1924310147001143297.json
name: 通义万相WAN2.1文生视频基础工作流_1924310147001143297.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1924310147001143297.json
hash: f7e6a38cf31eed78
coverage: 1
learned_at: 2026-10-15 22:43:24
nodes: [VAELoader, CLIPTextEncode, CLIPLoader, KSampler, ModelSamplingSD3, EmptyHunyuanLatentVideo, UNETLoader, CLIPTextEncode, VAEDecode, SaveAnimatedWEBP, SaveWEBM, SaveImage]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 778349617105379, "steps": 30}
---

# 视频生成/文生视频/通义万相WAN2.1文生视频基础工作流_1924310147001143297.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1924310147001143297.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（12 个）：
- `VAELoader`
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `KSampler` ★核心
- `ModelSamplingSD3`
- `EmptyHunyuanLatentVideo`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `SaveAnimatedWEBP`
- `SaveWEBM`
- `SaveImage`

## 关键参数

- `seed` = `778349617105379`
- `steps` = `30`
- `cfg` = `6`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（12/12）

**有卡**：`VAELoader`、`CLIPTextEncode`、`CLIPLoader`、`KSampler`、`ModelSamplingSD3`、`EmptyHunyuanLatentVideo`、`UNETLoader`、`VAEDecode`、`SaveAnimatedWEBP`、`SaveWEBM`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、EmptyHunyuanLatentVideo、SaveImage
