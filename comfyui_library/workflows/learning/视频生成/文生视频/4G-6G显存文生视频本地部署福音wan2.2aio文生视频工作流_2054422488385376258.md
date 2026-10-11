---
key: 视频生成/文生视频/4G-6G显存文生视频本地部署福音wan2.2aio文生视频工作流_2054422488385376258.json
name: 4G-6G显存文生视频本地部署福音wan2.2aio文生视频工作流_2054422488385376258
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/4G-6G显存文生视频本地部署福音wan2.2aio文生视频工作流_2054422488385376258.json
hash: 5c92d14b99713fca
coverage: 0.909091
learned_at: 2026-10-11 19:49:33
nodes: [ConditioningZeroOut, ModelSamplingSD3, CLIPTextEncode, EmptyHunyuanLatentVideo, VHS_VideoCombine, KSampler, VAEDecode, UnetLoaderGGUF, ClipLoaderGGUF, VaeGGUF, 孤海注释]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler_ancestral", "scheduler": "beta", "seed": 190741495803443, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/4G-6G显存文生视频本地部署福音wan2.2aio文生视频工作流_2054422488385376258.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/4G-6G显存文生视频本地部署福音wan2.2aio文生视频工作流_2054422488385376258.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（11 个）：
- `ConditioningZeroOut`
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `EmptyHunyuanLatentVideo`
- `VHS_VideoCombine`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `UnetLoaderGGUF` ★核心
- `ClipLoaderGGUF`
- `VaeGGUF`
- `孤海注释`

## 关键参数

- `seed` = `190741495803443`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **91%**（10/11）

**有卡**：`ConditioningZeroOut`、`ModelSamplingSD3`、`CLIPTextEncode`、`EmptyHunyuanLatentVideo`、`VHS_VideoCombine`、`KSampler`、`VAEDecode`、`UnetLoaderGGUF`、`ClipLoaderGGUF`、`VaeGGUF`

**用到的条目**：KSampler、VAEDecode、CLIPTextEncode、ConditioningZeroOut、EmptyHunyuanLatentVideo、VaeGGUF、CLIPLoaderGGUF、ClipLoaderGGUF

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
