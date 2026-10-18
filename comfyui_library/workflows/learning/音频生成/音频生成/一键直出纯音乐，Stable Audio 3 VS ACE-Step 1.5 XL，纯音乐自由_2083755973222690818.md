---
key: 音频生成/音频生成/一键直出纯音乐，Stable Audio 3 VS ACE-Step 1.5 XL，纯音乐自由_2083755973222690818.json
name: 一键直出纯音乐，Stable Audio 3 VS ACE-Step 1.5 XL，纯音乐自由_2083755973222690818
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/一键直出纯音乐，Stable Audio 3 VS ACE-Step 1.5 XL，纯音乐自由_2083755973222690818.json
hash: 630cd6ac3e2e8d76
coverage: 0.661017
learned_at: 2026-10-18 03:05:01
nodes: [CLIPTextEncode, CLIPLoader, KSampler, EmptyLatentAudio, VAELoader, ConditioningZeroOut, DualCLIPLoader, EmptyAceStep1.5LatentAudio, CheckpointLoaderSimple, CLIPTextEncode, StringConcatenate, PreviewAny, ComfyMathExpression, MarkdownNote, GetNode, MarkdownNote, MarkdownNote, SetNode, RegexExtract, PrimitiveInt, StringConcatenate, PrimitiveStringMultiline, SaveAudioAdvanced, VAEDecodeAudio, PrimitiveFloat, PrimitiveStringMultiline, JsonExtractString, PreviewAny, JsonExtractString, CR String To Number, PreviewAny, JsonExtractString, PreviewAny, JsonExtractString, CR String To Combo, CR String To Combo, PreviewAny, PreviewAny, PreviewAny, UNETLoader, KSampler, JsonExtractString, JsonExtractString, ModelSamplingAuraFlow, StringConcatenate, easy cleanGpuUsed, ShowText|pysssss, llama_cpp_instruct_adv, llama_cpp_model_loader, PreviewAny, PreviewAudio, TextEncodeAceStepAudio1.5, PreviewAudio, PrimitiveStringMultiline, PrimitiveStringMultiline, SaveImage, LoadImage, SaveAudioAdvanced, VAEDecodeAudio]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "checkpoint": "stable_audio_3_medium.safetensors", "denoise": 1, "height": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 0, "steps": 8, "width": 60}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 音频生成/音频生成/一键直出纯音乐，Stable Audio 3 VS ACE-Step 1.5 XL，纯音乐自由_2083755973222690818.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/一键直出纯音乐，Stable Audio 3 VS ACE-Step 1.5 XL，纯音乐自由_2083755973222690818.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（59 个）：
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `KSampler` ★核心
- `EmptyLatentAudio` ★核心
- `VAELoader`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `EmptyAceStep1.5LatentAudio`
- `CheckpointLoaderSimple` ★核心
- `CLIPTextEncode` ★核心
- `StringConcatenate`
- `PreviewAny`
- `ComfyMathExpression`
- `MarkdownNote`
- `GetNode`
- `MarkdownNote`
- `MarkdownNote`
- `SetNode`
- `RegexExtract`
- `PrimitiveInt`
- `StringConcatenate`
- `PrimitiveStringMultiline`
- `SaveAudioAdvanced`
- `VAEDecodeAudio` ★核心
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `JsonExtractString`
- `PreviewAny`
- `JsonExtractString`
- `CR String To Number`
- `PreviewAny`
- `JsonExtractString`
- `PreviewAny`
- `JsonExtractString`
- `CR String To Combo`
- `CR String To Combo`
- `PreviewAny`
- `PreviewAny`
- `PreviewAny`
- `UNETLoader` ★核心
- `KSampler` ★核心
- `JsonExtractString`
- `JsonExtractString`
- `ModelSamplingAuraFlow`
- `StringConcatenate`
- `easy cleanGpuUsed`
- `ShowText|pysssss`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `PreviewAny`
- `PreviewAudio`
- `TextEncodeAceStepAudio1.5`
- `PreviewAudio`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `SaveImage`
- `LoadImage`
- `SaveAudioAdvanced`
- `VAEDecodeAudio` ★核心

## 关键参数

- `seed` = `0`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `60`
- `height` = `1`
- `checkpoint` = `stable_audio_3_medium.safetensors`

## 知识

覆盖率 **66%**（39/59）

**有卡**：`CLIPTextEncode`、`CLIPLoader`、`KSampler`、`EmptyLatentAudio`、`VAELoader`、`ConditioningZeroOut`、`DualCLIPLoader`、`EmptyAceStep1.5LatentAudio`、`CheckpointLoaderSimple`、`StringConcatenate`、`ComfyMathExpression`、`RegexExtract`、`SaveAudioAdvanced`、`VAEDecodeAudio`、`JsonExtractString`、`CR String To Number`、`CR String To Combo`、`UNETLoader`、`ModelSamplingAuraFlow`、`easy cleanGpuUsed`、`llama_cpp_instruct_adv`、`llama_cpp_model_loader`、`PreviewAudio`、`TextEncodeAceStepAudio1.5`、`SaveImage`、`LoadImage`

**用到的条目**：KSampler、VAELoader、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage

## 参数体检

发现 3 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
