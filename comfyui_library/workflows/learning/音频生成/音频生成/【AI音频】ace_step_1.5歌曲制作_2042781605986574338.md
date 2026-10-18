---
key: 音频生成/音频生成/【AI音频】ace_step_1.5歌曲制作_2042781605986574338.json
name: 【AI音频】ace_step_1.5歌曲制作_2042781605986574338
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/【AI音频】ace_step_1.5歌曲制作_2042781605986574338.json
hash: ccf6edda9c30742e
coverage: 0.733333
learned_at: 2026-10-18 02:28:46
nodes: [TextEncodeAceStepAudio1.5, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters, PreviewAny, KSampler, ModelSamplingAuraFlow, VAEDecodeAudio, CheckpointLoaderSimple, PrimitiveFloat, PrimitiveNode, EmptyAceStep1.5LatentAudio, ConditioningZeroOut, Note, SaveAudioMP3]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "checkpoint": "ace_step_1.5_turbo_aio.safetensors", "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 838858354244039, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 音频生成/音频生成/【AI音频】ace_step_1.5歌曲制作_2042781605986574338.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/【AI音频】ace_step_1.5歌曲制作_2042781605986574338.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（15 个）：
- `TextEncodeAceStepAudio1.5`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `PreviewAny`
- `KSampler` ★核心
- `ModelSamplingAuraFlow`
- `VAEDecodeAudio` ★核心
- `CheckpointLoaderSimple` ★核心
- `PrimitiveFloat`
- `PrimitiveNode`
- `EmptyAceStep1.5LatentAudio`
- `ConditioningZeroOut`
- `Note`
- `SaveAudioMP3`

## 关键参数

- `seed` = `838858354244039`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `checkpoint` = `ace_step_1.5_turbo_aio.safetensors`

## 知识

覆盖率 **73%**（11/15）

**有卡**：`TextEncodeAceStepAudio1.5`、`llama_cpp_instruct_adv`、`llama_cpp_model_loader`、`llama_cpp_parameters`、`KSampler`、`ModelSamplingAuraFlow`、`VAEDecodeAudio`、`CheckpointLoaderSimple`、`EmptyAceStep1.5LatentAudio`、`ConditioningZeroOut`、`SaveAudioMP3`

**用到的条目**：KSampler、CheckpointLoaderSimple、ConditioningZeroOut、VAEDecodeAudio、EmptyAceStep1.5LatentAudio、TextEncodeAceStepAudio1.5、SaveAudioMP3、llama_cpp_instruct_adv

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
