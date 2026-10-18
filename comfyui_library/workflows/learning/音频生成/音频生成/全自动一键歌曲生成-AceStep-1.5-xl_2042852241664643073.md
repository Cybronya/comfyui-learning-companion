---
key: 音频生成/音频生成/全自动一键歌曲生成-AceStep-1.5-xl_2042852241664643073.json
name: 全自动一键歌曲生成-AceStep-1.5-xl_2042852241664643073
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/全自动一键歌曲生成-AceStep-1.5-xl_2042852241664643073.json
hash: dd52c40ce7aa6091
coverage: 0.866667
learned_at: 2026-10-18 02:28:47
nodes: [VAELoader, ConditioningZeroOut, llama_cpp_parameters, TextEncodeAceStepAudio1.5, CR Text, llama_cpp_parameters, LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, CR Text, easy promptConcat, llama_cpp_instruct_adv, PrimitiveNode, CR Text Concatenate, easy promptConcat, easy promptConcat, CR Text, PrimitiveBoolean, CR Text, easy promptConcat, easy ifElse, easy showAnything, VAEDecodeAudio, ModelSamplingAuraFlow, KSampler, llama_cpp_model_loader, llama_cpp_model_loader, UNETLoader, DualCLIPLoader, easy showAnything, easy showAnything, CR Text, SaveAudioMP3, EmptyAceStep1.5LatentAudio, Float, CR Text, PrimitiveBoolean, easy ifElse, easy promptConcat, easy promptConcat, CR Text, Text, easy saveText, llama_cpp_instruct_adv, Text String Truncate, CR Text]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 80, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 音频生成/音频生成/全自动一键歌曲生成-AceStep-1.5-xl_2042852241664643073.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/全自动一键歌曲生成-AceStep-1.5-xl_2042852241664643073.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（45 个）：
- `VAELoader`
- `ConditioningZeroOut`
- `llama_cpp_parameters`
- `TextEncodeAceStepAudio1.5`
- `CR Text`
- `llama_cpp_parameters`
- `LayerUtility: PurgeVRAM V2`
- `LayerUtility: PurgeVRAM V2`
- `CR Text`
- `easy promptConcat`
- `llama_cpp_instruct_adv`
- `PrimitiveNode`
- `CR Text Concatenate`
- `easy promptConcat`
- `easy promptConcat`
- `CR Text`
- `PrimitiveBoolean`
- `CR Text`
- `easy promptConcat`
- `easy ifElse`
- `easy showAnything`
- `VAEDecodeAudio` ★核心
- `ModelSamplingAuraFlow`
- `KSampler` ★核心
- `llama_cpp_model_loader`
- `llama_cpp_model_loader`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `easy showAnything`
- `easy showAnything`
- `CR Text`
- `SaveAudioMP3`
- `EmptyAceStep1.5LatentAudio`
- `Float`
- `CR Text`
- `PrimitiveBoolean`
- `easy ifElse`
- `easy promptConcat`
- `easy promptConcat`
- `CR Text`
- `Text`
- `easy saveText`
- `llama_cpp_instruct_adv`
- `Text String Truncate`
- `CR Text`

## 关键参数

- `seed` = `80`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **87%**（39/45）

**有卡**：`VAELoader`、`ConditioningZeroOut`、`llama_cpp_parameters`、`TextEncodeAceStepAudio1.5`、`CR Text`、`LayerUtility: PurgeVRAM V2`、`easy promptConcat`、`llama_cpp_instruct_adv`、`CR Text Concatenate`、`PrimitiveBoolean`、`VAEDecodeAudio`、`ModelSamplingAuraFlow`、`KSampler`、`llama_cpp_model_loader`、`UNETLoader`、`DualCLIPLoader`、`SaveAudioMP3`、`EmptyAceStep1.5LatentAudio`、`Float`、`Text`、`easy saveText`、`Text String Truncate`

**用到的条目**：KSampler、VAELoader、ConditioningZeroOut、UNETLoader、VAEDecodeAudio、EmptyAceStep1.5LatentAudio、TextEncodeAceStepAudio1.5、easy promptConcat

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
