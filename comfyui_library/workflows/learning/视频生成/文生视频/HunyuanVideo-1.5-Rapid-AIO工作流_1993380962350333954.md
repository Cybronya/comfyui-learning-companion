---
key: 视频生成/文生视频/HunyuanVideo-1.5-Rapid-AIO工作流_1993380962350333954.json
name: HunyuanVideo-1.5-Rapid-AIO工作流_1993380962350333954
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/HunyuanVideo-1.5-Rapid-AIO工作流_1993380962350333954.json
hash: 0471e0d6a73e046f
coverage: 0.916667
learned_at: 2026-10-15 22:44:28
nodes: [ModelSamplingSD3, VAEDecodeTiled, CLIPTextEncode, KSampler, LoadImage, CLIPTextEncode, CheckpointLoaderSimple, VHS_VideoCombine, HunyuanVideo15ImageToVideo, CLIPVisionLoader, CLIPVisionEncode, Note]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "checkpoint": "HV15-Rapid-AIO-v1.safetensors", "denoise": 1, "sampler_name": "er_sde", "scheduler": "beta", "seed": 85869543322327, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 视频生成/文生视频/HunyuanVideo-1.5-Rapid-AIO工作流_1993380962350333954.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/HunyuanVideo-1.5-Rapid-AIO工作流_1993380962350333954.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（12 个）：
- `ModelSamplingSD3`
- `VAEDecodeTiled` ★核心
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `LoadImage`
- `CLIPTextEncode` ★核心
- `CheckpointLoaderSimple` ★核心
- `VHS_VideoCombine`
- `HunyuanVideo15ImageToVideo`
- `CLIPVisionLoader`
- `CLIPVisionEncode`
- `Note`

## 关键参数

- `seed` = `85869543322327`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`
- `checkpoint` = `HV15-Rapid-AIO-v1.safetensors`

## 知识

覆盖率 **92%**（11/12）

**有卡**：`ModelSamplingSD3`、`VAEDecodeTiled`、`CLIPTextEncode`、`KSampler`、`LoadImage`、`CheckpointLoaderSimple`、`VHS_VideoCombine`、`HunyuanVideo15ImageToVideo`、`CLIPVisionLoader`、`CLIPVisionEncode`

**用到的条目**：KSampler、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、VAEDecodeTiled、CLIPVisionEncode、CLIPVisionLoader、ModelSamplingSD3

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
