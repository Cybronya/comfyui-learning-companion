---
key: 音频生成/音频生成/全能音乐歌曲生成-AceStepAudio1.5_2055109120163893249.json
name: 全能音乐歌曲生成-AceStepAudio1.5_2055109120163893249
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/全能音乐歌曲生成-AceStepAudio1.5_2055109120163893249.json
hash: 2e5eb748167f135d
coverage: 0.897959
learned_at: 2026-10-18 03:05:02
nodes: [KSampler, ModelSamplingAuraFlow, EmptyAceStep1.5LatentAudio, VAEDecodeAudio, DF_Int_to_Float, CheckpointLoaderSimple, CR Text, PrimitiveNode, LayerUtility: TextJoin, CR Text, TextBox, MathExpression|pysssss, MathExpression|pysssss, TextBox, TextBox, TextBox, MathExpression|pysssss, 1hew_AnySwitchSelect, 1hew_AnySwitchSelect, 1hew_AnySwitchSelect, ImpactStringSelector, ImpactStringSelector, ImpactStringSelector, MathExpression|pysssss, TextBox, 1hew_AnySwitchSelect, ImpactStringSelector, TextBox, TextBox, TextBox, TextBox, RH_LLMAPI_NODE, easy showAnything, MuyeTextEditOutput, 孤海注释, LayerUtility: TextJoin, Text Multiline, PreviewAny, CR Text, RH_LLMAPI_NODE, Text Multiline, JWInteger, 1hew_AnySwitchSelect, 忽略多组孤海, easy showAnything, SaveAudioMP3, PreviewAudio, ConditioningZeroOut, TextEncodeAceStepAudio1.5]
patterns: []
missing: []
problems: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "checkpoint": "ace_step_1.5_turbo_aio.safetensors", "denoise": 1, "sampler_name": "res_2s", "scheduler": "beta57", "seed": 49, "steps": 12}
discoveries: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 音频生成/音频生成/全能音乐歌曲生成-AceStepAudio1.5_2055109120163893249.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/全能音乐歌曲生成-AceStepAudio1.5_2055109120163893249.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（49 个）：
- `KSampler` ★核心
- `ModelSamplingAuraFlow`
- `EmptyAceStep1.5LatentAudio`
- `VAEDecodeAudio` ★核心
- `DF_Int_to_Float`
- `CheckpointLoaderSimple` ★核心
- `CR Text`
- `PrimitiveNode`
- `LayerUtility: TextJoin`
- `CR Text`
- `TextBox`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `TextBox`
- `TextBox`
- `TextBox`
- `MathExpression|pysssss`
- `1hew_AnySwitchSelect`
- `1hew_AnySwitchSelect`
- `1hew_AnySwitchSelect`
- `ImpactStringSelector`
- `ImpactStringSelector`
- `ImpactStringSelector`
- `MathExpression|pysssss`
- `TextBox`
- `1hew_AnySwitchSelect`
- `ImpactStringSelector`
- `TextBox`
- `TextBox`
- `TextBox`
- `TextBox`
- `RH_LLMAPI_NODE`
- `easy showAnything`
- `MuyeTextEditOutput`
- `孤海注释`
- `LayerUtility: TextJoin`
- `Text Multiline`
- `PreviewAny`
- `CR Text`
- `RH_LLMAPI_NODE`
- `Text Multiline`
- `JWInteger`
- `1hew_AnySwitchSelect`
- `忽略多组孤海`
- `easy showAnything`
- `SaveAudioMP3`
- `PreviewAudio`
- `ConditioningZeroOut`
- `TextEncodeAceStepAudio1.5`

## 关键参数

- `seed` = `49`
- `steps` = `12`
- `cfg` = `1`
- `sampler_name` = `res_2s`
- `scheduler` = `beta57`
- `denoise` = `1`
- `checkpoint` = `ace_step_1.5_turbo_aio.safetensors`

## 知识

覆盖率 **90%**（44/49）

**有卡**：`KSampler`、`ModelSamplingAuraFlow`、`EmptyAceStep1.5LatentAudio`、`VAEDecodeAudio`、`DF_Int_to_Float`、`CheckpointLoaderSimple`、`CR Text`、`LayerUtility: TextJoin`、`TextBox`、`MathExpression|pysssss`、`1hew_AnySwitchSelect`、`ImpactStringSelector`、`RH_LLMAPI_NODE`、`MuyeTextEditOutput`、`Text Multiline`、`JWInteger`、`忽略多组孤海`、`SaveAudioMP3`、`PreviewAudio`、`ConditioningZeroOut`、`TextEncodeAceStepAudio1.5`

**用到的条目**：KSampler、CheckpointLoaderSimple、ConditioningZeroOut、VAEDecodeAudio、EmptyAceStep1.5LatentAudio、TextEncodeAceStepAudio1.5、MuyeTextEditOutput、PreviewAudio

## 参数体检

发现 1 个问题：
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
