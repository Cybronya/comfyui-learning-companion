---
key: 音频生成/音频生成/音乐生成歌曲生成最新超快ace1.5音乐生成（加速版）_2018994115257573378.json
name: 音乐生成歌曲生成最新超快ace1.5音乐生成（加速版）_2018994115257573378
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/音乐生成歌曲生成最新超快ace1.5音乐生成（加速版）_2018994115257573378.json
hash: e3949a57c6d464e0
coverage: 0.863636
learned_at: 2026-10-18 02:07:13
nodes: [UNETLoader, VAELoader, EmptyAceStep1.5LatentAudio, ModelSamplingAuraFlow, ConditioningZeroOut, VAEDecodeAudio, KSampler, PrimitiveNode, DualCLIPLoader, TextEncodeAceStepAudio1.5, MarkdownNote, MarkdownNote, LoadImage, SaveAudio, SaveAudioMP3, CR Text, DF_Int_to_Float, JWInteger, Int, CR Text, TextEncodeAceStepAudio1.5, CR Text]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 999, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 音频生成/音频生成/音乐生成歌曲生成最新超快ace1.5音乐生成（加速版）_2018994115257573378.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/音乐生成歌曲生成最新超快ace1.5音乐生成（加速版）_2018994115257573378.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（22 个）：
- `UNETLoader` ★核心
- `VAELoader`
- `EmptyAceStep1.5LatentAudio`
- `ModelSamplingAuraFlow`
- `ConditioningZeroOut`
- `VAEDecodeAudio` ★核心
- `KSampler` ★核心
- `PrimitiveNode`
- `DualCLIPLoader`
- `TextEncodeAceStepAudio1.5`
- `MarkdownNote`
- `MarkdownNote`
- `LoadImage`
- `SaveAudio`
- `SaveAudioMP3`
- `CR Text`
- `DF_Int_to_Float`
- `JWInteger`
- `Int`
- `CR Text`
- `TextEncodeAceStepAudio1.5`
- `CR Text`

## 关键参数

- `seed` = `999`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **86%**（19/22）

**有卡**：`UNETLoader`、`VAELoader`、`EmptyAceStep1.5LatentAudio`、`ModelSamplingAuraFlow`、`ConditioningZeroOut`、`VAEDecodeAudio`、`KSampler`、`DualCLIPLoader`、`TextEncodeAceStepAudio1.5`、`LoadImage`、`SaveAudio`、`SaveAudioMP3`、`CR Text`、`DF_Int_to_Float`、`JWInteger`、`Int`

**用到的条目**：KSampler、VAELoader、ConditioningZeroOut、LoadImage、UNETLoader、VAEDecodeAudio、EmptyAceStep1.5LatentAudio、TextEncodeAceStepAudio1.5

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
