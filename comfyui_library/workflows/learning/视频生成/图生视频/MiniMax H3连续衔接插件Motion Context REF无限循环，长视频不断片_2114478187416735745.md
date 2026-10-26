---
key: 视频生成/图生视频/MiniMax H3连续衔接插件Motion Context REF无限循环，长视频不断片_2114478187416735745.json
name: MiniMax H3连续衔接插件Motion Context REF无限循环，长视频不断片_2114478187416735745
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/MiniMax H3连续衔接插件Motion Context REF无限循环，长视频不断片_2114478187416735745.json
hash: 1046a1e9b2c7feb3
coverage: 0.8
learned_at: 2026-10-26 22:12:53
nodes: [MiniMaxH3MemoryEfficientSageAttentionPatch, SamplerCustomAdvanced, LoadAudio, VHS_LoadVideo, RandomNoise, KSamplerSelect, BasicScheduler, ResolutionSelector, ComfyMathExpression, UNETLoader, CLIPLoader, VAELoader, VAELoader, LoraLoaderModelOnly, VAEDecode, VAEDecodeAudio, PrimitiveStringMultiline, PrimitiveStringMultiline, PrimitiveStringMultiline, PrimitiveStringMultiline, PrimitiveStringMultiline, PrimitiveStringMultiline, easy batchAnything, easy showAnything, easy textIndexSwitch, LoadImage, LoadImage, MiniMaxH3MotionContextTrim, CreateVideo, easy forLoopEnd, ShowText|pysssss, easy ifElse, easy forLoopStart, BasicGuider, CreateVideo, PrimitiveFloat, MiniMaxH3ReferenceToVideo, MiniMaxH3MotionContext, GoohaiAnySwitch, easy ifElse, MiniMaxH3MotionContextLoadLatent, ComfyMathExpression, MiniMaxH3MotionContextSaveLatent, SaveVideo, SaveVideo, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPTextEncode, CLIPLoader, JjkText, VAEDecode, EmptyLatentImage, VAELoader, solarL_SaveImagesToZip, Note, SaveImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/MiniMax H3连续衔接插件Motion Context REF无限循环，长视频不断片_2114478187416735745.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/MiniMax H3连续衔接插件Motion Context REF无限循环，长视频不断片_2114478187416735745.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（75 个）：
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `SamplerCustomAdvanced` ★核心
- `LoadAudio`
- `VHS_LoadVideo`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `ResolutionSelector`
- `ComfyMathExpression`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `easy batchAnything`
- `easy showAnything`
- `easy textIndexSwitch`
- `LoadImage`
- `LoadImage`
- `MiniMaxH3MotionContextTrim`
- `CreateVideo`
- `easy forLoopEnd`
- `ShowText|pysssss`
- `easy ifElse`
- `easy forLoopStart`
- `BasicGuider`
- `CreateVideo`
- `PrimitiveFloat`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxH3MotionContext`
- `GoohaiAnySwitch`
- `easy ifElse`
- `MiniMaxH3MotionContextLoadLatent`
- `ComfyMathExpression`
- `MiniMaxH3MotionContextSaveLatent`
- `SaveVideo`
- `SaveVideo`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `JjkText`
- `VAEDecode` ★核心
- `EmptyLatentImage` ★核心
- `VAELoader`
- `solarL_SaveImagesToZip`
- `Note`
- `SaveImage`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`
- `width` = `80`
- `height` = `80`
- `batch_size` = `1`

## 知识

覆盖率 **80%**（60/75）

**有卡**：`MiniMaxH3MemoryEfficientSageAttentionPatch`、`SamplerCustomAdvanced`、`LoadAudio`、`VHS_LoadVideo`、`RandomNoise`、`KSamplerSelect`、`BasicScheduler`、`ResolutionSelector`、`ComfyMathExpression`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`、`VAEDecode`、`VAEDecodeAudio`、`easy batchAnything`、`easy textIndexSwitch`、`LoadImage`、`MiniMaxH3MotionContextTrim`、`CreateVideo`、`easy forLoopEnd`、`easy forLoopStart`、`BasicGuider`、`MiniMaxH3ReferenceToVideo`、`MiniMaxH3MotionContext`、`GoohaiAnySwitch`、`MiniMaxH3MotionContextLoadLatent`、`MiniMaxH3MotionContextSaveLatent`、`SaveVideo`、`KSampler`、`CLIPTextEncode`、`EmptyLatentImage`、`solarL_SaveImagesToZip`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
