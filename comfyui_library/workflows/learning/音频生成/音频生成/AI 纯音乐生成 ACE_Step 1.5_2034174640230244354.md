---
key: 音频生成/音频生成/AI 纯音乐生成 ACE_Step 1.5_2034174640230244354.json
name: AI 纯音乐生成 ACE_Step 1.5_2034174640230244354
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/AI 纯音乐生成 ACE_Step 1.5_2034174640230244354.json
hash: ffa2d03257c31a96
coverage: 0.625
learned_at: 2026-10-18 02:28:38
nodes: [UNETLoader, DualCLIPLoader, VAELoader, PrimitiveNode, PrimitiveNode, ModelSamplingAuraFlow, KSampler, VAEDecodeAudio, JjkText, SaveAudioMP3, Note, TextEncodeAceStepAudio1.5, EmptyAceStep1.5LatentAudio, ConditioningZeroOut, Note, Note]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 159497992887294, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 音频生成/音频生成/AI 纯音乐生成 ACE_Step 1.5_2034174640230244354.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/AI 纯音乐生成 ACE_Step 1.5_2034174640230244354.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（16 个）：
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `VAELoader`
- `PrimitiveNode`
- `PrimitiveNode`
- `ModelSamplingAuraFlow`
- `KSampler` ★核心
- `VAEDecodeAudio` ★核心
- `JjkText`
- `SaveAudioMP3`
- `Note`
- `TextEncodeAceStepAudio1.5`
- `EmptyAceStep1.5LatentAudio`
- `ConditioningZeroOut`
- `Note`
- `Note`

## 关键参数

- `seed` = `159497992887294`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **62%**（10/16）

**有卡**：`UNETLoader`、`DualCLIPLoader`、`VAELoader`、`ModelSamplingAuraFlow`、`KSampler`、`VAEDecodeAudio`、`SaveAudioMP3`、`TextEncodeAceStepAudio1.5`、`EmptyAceStep1.5LatentAudio`、`ConditioningZeroOut`

**用到的条目**：KSampler、VAELoader、ConditioningZeroOut、UNETLoader、VAEDecodeAudio、EmptyAceStep1.5LatentAudio、TextEncodeAceStepAudio1.5、SaveAudioMP3

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
