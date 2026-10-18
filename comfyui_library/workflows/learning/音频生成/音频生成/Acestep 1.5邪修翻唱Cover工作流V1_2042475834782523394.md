---
key: 音频生成/音频生成/Acestep 1.5邪修翻唱Cover工作流V1_2042475834782523394.json
name: Acestep 1.5邪修翻唱Cover工作流V1_2042475834782523394
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/Acestep 1.5邪修翻唱Cover工作流V1_2042475834782523394.json
hash: a3efaf45f5574c44
coverage: 0.789474
learned_at: 2026-10-18 02:28:38
nodes: [UNETLoader, DualCLIPLoader, VAELoader, ConditioningZeroOut, KSampler, ModelSamplingAuraFlow, ReferenceTimbreAudio, PrimitiveNode, VAEEncodeAudio, VAEDecodeAudio, SaveAudioMP3, CR Prompt Text, TextEncodeAceStepAudio1.5, CR Prompt Text, LoadAudio, Float, Note, Note, Note]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "denoise": 0.5, "sampler_name": "euler", "scheduler": "simple", "seed": 408778949380513, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 音频生成/音频生成/Acestep 1.5邪修翻唱Cover工作流V1_2042475834782523394.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/Acestep 1.5邪修翻唱Cover工作流V1_2042475834782523394.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Output → Other

**节点**（19 个）：
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `VAELoader`
- `ConditioningZeroOut`
- `KSampler` ★核心
- `ModelSamplingAuraFlow`
- `ReferenceTimbreAudio`
- `PrimitiveNode`
- `VAEEncodeAudio` ★核心
- `VAEDecodeAudio` ★核心
- `SaveAudioMP3`
- `CR Prompt Text`
- `TextEncodeAceStepAudio1.5`
- `CR Prompt Text`
- `LoadAudio`
- `Float`
- `Note`
- `Note`
- `Note`

## 关键参数

- `seed` = `408778949380513`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.5`

## 知识

覆盖率 **79%**（15/19）

**有卡**：`UNETLoader`、`DualCLIPLoader`、`VAELoader`、`ConditioningZeroOut`、`KSampler`、`ModelSamplingAuraFlow`、`ReferenceTimbreAudio`、`VAEEncodeAudio`、`VAEDecodeAudio`、`SaveAudioMP3`、`CR Prompt Text`、`TextEncodeAceStepAudio1.5`、`LoadAudio`、`Float`

**用到的条目**：KSampler、VAELoader、ConditioningZeroOut、UNETLoader、VAEDecodeAudio、VAEEncodeAudio、TextEncodeAceStepAudio1.5、CR Prompt Text

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
