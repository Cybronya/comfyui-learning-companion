---
key: 音频生成/音频生成/Acestep1.5-XL满血版&turbo版_2046207480346189825.json
name: Acestep1.5-XL满血版&turbo版_2046207480346189825
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/Acestep1.5-XL满血版&turbo版_2046207480346189825.json
hash: 7ef6f393282d31db
coverage: 0.923077
learned_at: 2026-10-18 03:04:47
nodes: [UNETLoader, CR Text, CR Text, SaveAudioMP3, VAELoader, ModelSamplingAuraFlow, VAEDecodeAudio, ConditioningZeroOut, EmptyAceStep1.5LatentAudio, DualCLIPLoader, CR Text, CR Text, UNETLoader, KSampler, VAELoader, ModelSamplingAuraFlow, Note, DualCLIPLoader, CLIPTextEncode, KSampler, VAEDecodeAudio, SaveAudioMP3, Fast Groups Muter (rgthree), EmptyAceStep1.5LatentAudio, TextEncodeAceStepAudio1.5, TextEncodeAceStepAudio1.5]
patterns: []
missing: []
problems: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 490890465182902, "steps": 50}
discoveries: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 音频生成/音频生成/Acestep1.5-XL满血版&turbo版_2046207480346189825.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/Acestep1.5-XL满血版&turbo版_2046207480346189825.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（26 个）：
- `UNETLoader` ★核心
- `CR Text`
- `CR Text`
- `SaveAudioMP3`
- `VAELoader`
- `ModelSamplingAuraFlow`
- `VAEDecodeAudio` ★核心
- `ConditioningZeroOut`
- `EmptyAceStep1.5LatentAudio`
- `DualCLIPLoader`
- `CR Text`
- `CR Text`
- `UNETLoader` ★核心
- `KSampler` ★核心
- `VAELoader`
- `ModelSamplingAuraFlow`
- `Note`
- `DualCLIPLoader`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `VAEDecodeAudio` ★核心
- `SaveAudioMP3`
- `Fast Groups Muter (rgthree)`
- `EmptyAceStep1.5LatentAudio`
- `TextEncodeAceStepAudio1.5`
- `TextEncodeAceStepAudio1.5`

## 关键参数

- `seed` = `490890465182902`
- `steps` = `50`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **92%**（24/26）

**有卡**：`UNETLoader`、`CR Text`、`SaveAudioMP3`、`VAELoader`、`ModelSamplingAuraFlow`、`VAEDecodeAudio`、`ConditioningZeroOut`、`EmptyAceStep1.5LatentAudio`、`DualCLIPLoader`、`KSampler`、`CLIPTextEncode`、`TextEncodeAceStepAudio1.5`

**用到的条目**：KSampler、VAELoader、CLIPTextEncode、ConditioningZeroOut、UNETLoader、VAEDecodeAudio、EmptyAceStep1.5LatentAudio、TextEncodeAceStepAudio1.5

## 参数体检

发现 1 个问题：
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
