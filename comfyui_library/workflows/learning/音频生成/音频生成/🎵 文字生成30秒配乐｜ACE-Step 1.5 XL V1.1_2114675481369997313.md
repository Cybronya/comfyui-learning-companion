---
key: 音频生成/音频生成/🎵 文字生成30秒配乐｜ACE-Step 1.5 XL V1.1_2114675481369997313.json
name: 🎵 文字生成30秒配乐｜ACE-Step 1.5 XL V1.1_2114675481369997313
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/🎵 文字生成30秒配乐｜ACE-Step 1.5 XL V1.1_2114675481369997313.json
hash: 0b63e8e9fa215934
coverage: 1
learned_at: 2026-10-26 22:17:37
nodes: [UNETLoader, DualCLIPLoader, VAELoader, ModelSamplingAuraFlow, TextEncodeAceStepAudio1.5, EmptyAceStep1.5LatentAudio, ConditioningZeroOut, KSampler, VAEDecodeAudio, SaveAudio]
patterns: []
missing: []
problems: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 7, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 244405449511853, "steps": 50}
discoveries: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 音频生成/音频生成/🎵 文字生成30秒配乐｜ACE-Step 1.5 XL V1.1_2114675481369997313.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/🎵 文字生成30秒配乐｜ACE-Step 1.5 XL V1.1_2114675481369997313.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（10 个）：
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `VAELoader`
- `ModelSamplingAuraFlow`
- `TextEncodeAceStepAudio1.5`
- `EmptyAceStep1.5LatentAudio`
- `ConditioningZeroOut`
- `KSampler` ★核心
- `VAEDecodeAudio` ★核心
- `SaveAudio`

## 关键参数

- `seed` = `244405449511853`
- `steps` = `50`
- `cfg` = `7`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（10/10）

**有卡**：`UNETLoader`、`DualCLIPLoader`、`VAELoader`、`ModelSamplingAuraFlow`、`TextEncodeAceStepAudio1.5`、`EmptyAceStep1.5LatentAudio`、`ConditioningZeroOut`、`KSampler`、`VAEDecodeAudio`、`SaveAudio`

**用到的条目**：KSampler、VAELoader、ConditioningZeroOut、UNETLoader、VAEDecodeAudio、EmptyAceStep1.5LatentAudio、TextEncodeAceStepAudio1.5、SaveAudio

## 参数体检

发现 1 个问题：
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
