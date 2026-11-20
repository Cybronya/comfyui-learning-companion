---
key: 平台全量/Acestep1.5开源音乐创作_2029091777650626562.json
name: Acestep1.5开源音乐创作_2029091777650626562
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Acestep1.5开源音乐创作_2029091777650626562.json
hash: bf903650ec8498ce
coverage: 0.909091
learned_at: 2026-11-14 00:17:24
nodes: [UNETLoader, DualCLIPLoader, VAELoader, EmptyAceStep1.5LatentAudio, ConditioningZeroOut, ModelSamplingAuraFlow, VAEDecodeAudio, KSampler, SaveAudioMP3, PrimitiveNode, TextEncodeAceStepAudio1.5]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 33, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 平台全量/Acestep1.5开源音乐创作_2029091777650626562.json

> 来源文件 `comfyui_library/workflows/平台全量/Acestep1.5开源音乐创作_2029091777650626562.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（11 个）：
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `VAELoader`
- `EmptyAceStep1.5LatentAudio`
- `ConditioningZeroOut`
- `ModelSamplingAuraFlow`
- `VAEDecodeAudio` ★核心
- `KSampler` ★核心
- `SaveAudioMP3`
- `PrimitiveNode`
- `TextEncodeAceStepAudio1.5`

## 关键参数

- `seed` = `33`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **91%**（10/11）

**有卡**：`UNETLoader`、`DualCLIPLoader`、`VAELoader`、`EmptyAceStep1.5LatentAudio`、`ConditioningZeroOut`、`ModelSamplingAuraFlow`、`VAEDecodeAudio`、`KSampler`、`SaveAudioMP3`、`TextEncodeAceStepAudio1.5`

**用到的条目**：KSampler、VAELoader、ConditioningZeroOut、UNETLoader、EmptyAceStep1.5LatentAudio、TextEncodeAceStepAudio1.5、VAEDecodeAudio、SaveAudioMP3

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
