---
key: 视频生成/图生视频/超简单--Wan2.2 All-in-on 目前最快2.2文生视频+图生视频工作流_2043862678724157442.json
name: 超简单--Wan2.2 All-in-on 目前最快2.2文生视频+图生视频工作流_2043862678724157442.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2043862678724157442.json
hash: 39a592714ebc8002
coverage: 1
learned_at: 2026-10-15 22:36:34
nodes: [CLIPTextEncode, CLIPTextEncode, ModelSamplingSD3, EmptyHunyuanLatentVideo, KSampler, CLIPTextEncode, VHS_VideoCombine, VHS_VideoCombine, ModelSamplingSD3, WanImageToVideo, KSampler, VAEDecode, UNETLoader, VAELoader, CLIPLoader, UNETLoader, VAELoader, CLIPLoader, VAEDecode, VHS_VideoCombine, CLIPTextEncode, LoadImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "sa_solver", "scheduler": "beta", "seed": 1, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/超简单--Wan2.2 All-in-on 目前最快2.2文生视频+图生视频工作流_2043862678724157442.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2043862678724157442.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（22 个）：
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `EmptyHunyuanLatentVideo`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `ModelSamplingSD3`
- `WanImageToVideo`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `VAELoader`
- `CLIPLoader`
- `UNETLoader` ★核心
- `VAELoader`
- `CLIPLoader`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `LoadImage`

## 关键参数

- `seed` = `1`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `sa_solver`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **100%**（22/22）

**有卡**：`CLIPTextEncode`、`ModelSamplingSD3`、`EmptyHunyuanLatentVideo`、`KSampler`、`VHS_VideoCombine`、`WanImageToVideo`、`VAEDecode`、`UNETLoader`、`VAELoader`、`CLIPLoader`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、EmptyHunyuanLatentVideo

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
