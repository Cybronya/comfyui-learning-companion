---
key: 音频生成/音频生成/ACE-Step 1.5 XL 音乐制作 SFT版_2064539276913762305.json
name: ACE-Step 1.5 XL 音乐制作 SFT版_2064539276913762305
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/ACE-Step 1.5 XL 音乐制作 SFT版_2064539276913762305.json
hash: faa3b597ab7418e2
coverage: 0.833333
learned_at: 2026-10-18 03:04:46
nodes: [UNETLoader, VAELoader, PrimitiveNode, EmptyAceStep1.5LatentAudio, ConditioningZeroOut, DualCLIPLoader, PrimitiveInt, TextEncodeAceStepAudio1.5, KSampler, VAEDecodeAudio, SaveAudioMP3, ModelSamplingAuraFlow]
patterns: []
missing: []
problems: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 7, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 0, "steps": 50}
discoveries: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 音频生成/音频生成/ACE-Step 1.5 XL 音乐制作 SFT版_2064539276913762305.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/ACE-Step 1.5 XL 音乐制作 SFT版_2064539276913762305.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（12 个）：
- `UNETLoader` ★核心
- `VAELoader`
- `PrimitiveNode`
- `EmptyAceStep1.5LatentAudio`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `PrimitiveInt`
- `TextEncodeAceStepAudio1.5`
- `KSampler` ★核心
- `VAEDecodeAudio` ★核心
- `SaveAudioMP3`
- `ModelSamplingAuraFlow`

## 关键参数

- `seed` = `0`
- `steps` = `50`
- `cfg` = `7`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **83%**（10/12）

**有卡**：`UNETLoader`、`VAELoader`、`EmptyAceStep1.5LatentAudio`、`ConditioningZeroOut`、`DualCLIPLoader`、`TextEncodeAceStepAudio1.5`、`KSampler`、`VAEDecodeAudio`、`SaveAudioMP3`、`ModelSamplingAuraFlow`

**用到的条目**：KSampler、VAELoader、ConditioningZeroOut、UNETLoader、VAEDecodeAudio、EmptyAceStep1.5LatentAudio、TextEncodeAceStepAudio1.5、SaveAudioMP3

## 参数体检

发现 1 个问题：
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
