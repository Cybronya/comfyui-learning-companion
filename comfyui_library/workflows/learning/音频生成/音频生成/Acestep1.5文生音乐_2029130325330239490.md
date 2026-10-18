---
key: 音频生成/音频生成/Acestep1.5文生音乐_2029130325330239490.json
name: Acestep1.5文生音乐_2029130325330239490
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/Acestep1.5文生音乐_2029130325330239490.json
hash: b1974ff9c54a1c46
coverage: 0.647059
learned_at: 2026-10-18 02:28:38
nodes: [ConditioningZeroOut, KSampler, ModelSamplingAuraFlow, VAEDecodeAudio, PrimitiveNode, Any Switch (rgthree), Any Switch (rgthree), Any Switch (rgthree), Fast Groups Muter (rgthree), UNETLoader, VAELoader, CheckpointLoaderSimple, PrimitiveNode, EmptyAceStep1.5LatentAudio, DualCLIPLoader, SaveAudioMP3, TextEncodeAceStepAudio1.5]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "checkpoint": "ace_step_1.5_turbo_aio.safetensors", "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 33, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 音频生成/音频生成/Acestep1.5文生音乐_2029130325330239490.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/Acestep1.5文生音乐_2029130325330239490.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（17 个）：
- `ConditioningZeroOut`
- `KSampler` ★核心
- `ModelSamplingAuraFlow`
- `VAEDecodeAudio` ★核心
- `PrimitiveNode`
- `Any Switch (rgthree)`
- `Any Switch (rgthree)`
- `Any Switch (rgthree)`
- `Fast Groups Muter (rgthree)`
- `UNETLoader` ★核心
- `VAELoader`
- `CheckpointLoaderSimple` ★核心
- `PrimitiveNode`
- `EmptyAceStep1.5LatentAudio`
- `DualCLIPLoader`
- `SaveAudioMP3`
- `TextEncodeAceStepAudio1.5`

## 关键参数

- `seed` = `33`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `checkpoint` = `ace_step_1.5_turbo_aio.safetensors`

## 知识

覆盖率 **65%**（11/17）

**有卡**：`ConditioningZeroOut`、`KSampler`、`ModelSamplingAuraFlow`、`VAEDecodeAudio`、`UNETLoader`、`VAELoader`、`CheckpointLoaderSimple`、`EmptyAceStep1.5LatentAudio`、`DualCLIPLoader`、`SaveAudioMP3`、`TextEncodeAceStepAudio1.5`

**用到的条目**：KSampler、VAELoader、CheckpointLoaderSimple、UNETLoader、ConditioningZeroOut、VAEDecodeAudio、EmptyAceStep1.5LatentAudio、TextEncodeAceStepAudio1.5

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
