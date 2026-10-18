---
key: 音频生成/音频生成/ACE-STEP 1.5XL turbo-文生音乐_2077369725973254146.json
name: ACE-STEP 1.5XL turbo-文生音乐_2077369725973254146
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/ACE-STEP 1.5XL turbo-文生音乐_2077369725973254146.json
hash: a0493d3d95591c8c
coverage: 0.769231
learned_at: 2026-10-18 03:04:46
nodes: [PrimitiveNode, ConditioningZeroOut, KSampler, VAEDecodeAudio, MarkdownNote, TextEncodeAceStepAudio1.5, UNETLoader, DualCLIPLoader, VAELoader, ModelSamplingAuraFlow, SaveAudioMP3, EmptyAceStep1.5LatentAudio, PrimitiveInt]
patterns: []
missing: []
problems: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 6, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 0, "steps": 50}
discoveries: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 音频生成/音频生成/ACE-STEP 1.5XL turbo-文生音乐_2077369725973254146.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/ACE-STEP 1.5XL turbo-文生音乐_2077369725973254146.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（13 个）：
- `PrimitiveNode`
- `ConditioningZeroOut`
- `KSampler` ★核心
- `VAEDecodeAudio` ★核心
- `MarkdownNote`
- `TextEncodeAceStepAudio1.5`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `VAELoader`
- `ModelSamplingAuraFlow`
- `SaveAudioMP3`
- `EmptyAceStep1.5LatentAudio`
- `PrimitiveInt`

## 关键参数

- `seed` = `0`
- `steps` = `50`
- `cfg` = `6`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **77%**（10/13）

**有卡**：`ConditioningZeroOut`、`KSampler`、`VAEDecodeAudio`、`TextEncodeAceStepAudio1.5`、`UNETLoader`、`DualCLIPLoader`、`VAELoader`、`ModelSamplingAuraFlow`、`SaveAudioMP3`、`EmptyAceStep1.5LatentAudio`

**用到的条目**：KSampler、VAELoader、ConditioningZeroOut、UNETLoader、VAEDecodeAudio、EmptyAceStep1.5LatentAudio、TextEncodeAceStepAudio1.5、SaveAudioMP3

## 参数体检

发现 1 个问题：
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
