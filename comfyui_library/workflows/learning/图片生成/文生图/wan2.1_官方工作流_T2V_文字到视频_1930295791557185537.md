---
key: wan2.1_官方工作流_T2V_文字到视频_1930295791557185537.json
name: wan2.1_官方工作流_T2V_文字到视频_1930295791557185537
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/wan2.1_官方工作流_T2V_文字到视频_1930295791557185537.json
hash: 2b862362b770b7bc
coverage: 1
learned_at: 2026-10-10 20:59:26
nodes: [ModelSamplingSD3, KSampler, CLIPTextEncode, UNETLoader, CLIPTextEncode, VAELoader, EmptyHunyuanLatentVideo, CLIPLoader, SaveAnimatedWEBP, VAEDecode, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 138152422751227, "steps": 30}
---

# wan2.1_官方工作流_T2V_文字到视频_1930295791557185537.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/wan2.1_官方工作流_T2V_文字到视频_1930295791557185537.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（11 个）：
- `ModelSamplingSD3`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `VAELoader`
- `EmptyHunyuanLatentVideo`
- `CLIPLoader`
- `SaveAnimatedWEBP`
- `VAEDecode` ★核心
- `VHS_VideoCombine`

## 关键参数

- `seed` = `138152422751227`
- `steps` = `30`
- `cfg` = `6`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（11/11）

**有卡**：`ModelSamplingSD3`、`KSampler`、`CLIPTextEncode`、`UNETLoader`、`VAELoader`、`EmptyHunyuanLatentVideo`、`CLIPLoader`、`SaveAnimatedWEBP`、`VAEDecode`、`VHS_VideoCombine`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、EmptyHunyuanLatentVideo、SaveAnimatedWEBP
