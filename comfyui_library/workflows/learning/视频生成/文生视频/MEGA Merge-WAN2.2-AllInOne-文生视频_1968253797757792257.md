---
key: 视频生成/文生视频/MEGA Merge-WAN2.2-AllInOne-文生视频_1968253797757792257.json
name: MEGA Merge-WAN2.2-AllInOne-文生视频_1968253797757792257
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/MEGA Merge-WAN2.2-AllInOne-文生视频_1968253797757792257.json
hash: 594d5a1094b648a5
coverage: 1
learned_at: 2026-10-10 23:00:44
nodes: [TrimVideoLatent, VAEDecode, KSampler, ModelSamplingSD3, CheckpointLoaderSimple, VHS_VideoCombine, CLIPTextEncode, CLIPTextEncode, INTConstant, INTConstant, INTConstant, WanVaceToVideo]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "wan2.2-rapid-mega-aio-v1.safetensors", "denoise": 1, "sampler_name": "euler", "scheduler": "beta", "seed": 192054346835137, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/MEGA Merge-WAN2.2-AllInOne-文生视频_1968253797757792257.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/MEGA Merge-WAN2.2-AllInOne-文生视频_1968253797757792257.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（12 个）：
- `TrimVideoLatent`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `ModelSamplingSD3`
- `CheckpointLoaderSimple` ★核心
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `WanVaceToVideo`

## 关键参数

- `seed` = `192054346835137`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `1`
- `checkpoint` = `wan2.2-rapid-mega-aio-v1.safetensors`

## 知识

覆盖率 **100%**（12/12）

**有卡**：`TrimVideoLatent`、`VAEDecode`、`KSampler`、`ModelSamplingSD3`、`CheckpointLoaderSimple`、`VHS_VideoCombine`、`CLIPTextEncode`、`INTConstant`、`WanVaceToVideo`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、TrimVideoLatent、INTConstant、ModelSamplingSD3、VHS_VideoCombine

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
