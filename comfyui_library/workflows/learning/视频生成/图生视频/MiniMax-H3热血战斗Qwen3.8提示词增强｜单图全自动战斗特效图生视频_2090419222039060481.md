---
key: 视频生成/图生视频/MiniMax-H3热血战斗Qwen3.8提示词增强｜单图全自动战斗特效图生视频_2090419222039060481.json
name: MiniMax-H3热血战斗Qwen3.8提示词增强｜单图全自动战斗特效图生视频_2090419222039060481
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/MiniMax-H3热血战斗Qwen3.8提示词增强｜单图全自动战斗特效图生视频_2090419222039060481.json
hash: 5d26989a70cf6485
coverage: 0.873016
learned_at: 2026-10-16 22:02:06
nodes: [PT_H3ConcatAVLatent, VAELoader, VAELoader, ComfyMathExpression, BasicGuider, RandomNoise, VAEEncode, BasicGuider, SamplerCustomAdvanced, CLIPLoader, UNETLoader, MiniMaxH3DualClockSamplerT8, KSamplerSelect, BasicScheduler, RandomNoise, VHS_VideoCombine, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3AVDecodeT8, MiniMaxH3AVDecodeT8, MemoryCleaner, MemoryCleaner, VHS_VideoCombine, Fast Groups Bypasser (rgthree), PreviewAny, llama_cpp_parameters, Text, MiniMaxH3AudioConditioningT8, llama_cpp_model_loader, LoraLoaderBypassModelOnly, SamplerCustomAdvanced, LoadImage, llama_cpp_instruct_adv, PrimitiveFloat, ResolutionSelector, easy saveText, PrimitiveStringMultiline, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, JjkText, solarL_SaveImagesToZip, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, Note]
patterns: [text_to_image, image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/MiniMax-H3热血战斗Qwen3.8提示词增强｜单图全自动战斗特效图生视频_2090419222039060481.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/MiniMax-H3热血战斗Qwen3.8提示词增强｜单图全自动战斗特效图生视频_2090419222039060481.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Output → Other

**节点**（63 个）：
- `PT_H3ConcatAVLatent`
- `VAELoader`
- `VAELoader`
- `ComfyMathExpression`
- `BasicGuider`
- `RandomNoise`
- `VAEEncode` ★核心
- `BasicGuider`
- `SamplerCustomAdvanced` ★核心
- `CLIPLoader`
- `UNETLoader` ★核心
- `MiniMaxH3DualClockSamplerT8` ★核心
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `RandomNoise`
- `VHS_VideoCombine`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3AVDecodeT8`
- `MemoryCleaner`
- `MemoryCleaner`
- `VHS_VideoCombine`
- `Fast Groups Bypasser (rgthree)`
- `PreviewAny`
- `llama_cpp_parameters`
- `Text`
- `MiniMaxH3AudioConditioningT8`
- `llama_cpp_model_loader`
- `LoraLoaderBypassModelOnly` ★核心
- `SamplerCustomAdvanced` ★核心
- `LoadImage`
- `llama_cpp_instruct_adv`
- `PrimitiveFloat`
- `ResolutionSelector`
- `easy saveText`
- `PrimitiveStringMultiline`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `JjkText`
- `solarL_SaveImagesToZip`
- `CLIPTextEncode` ★核心
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
- `Note`

**识别到的模式**：text_to_image、image_to_image

## 关键参数

- `width` = `80`
- `height` = `80`
- `batch_size` = `1`
- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **87%**（55/63）

**有卡**：`PT_H3ConcatAVLatent`、`VAELoader`、`ComfyMathExpression`、`BasicGuider`、`RandomNoise`、`VAEEncode`、`SamplerCustomAdvanced`、`CLIPLoader`、`UNETLoader`、`MiniMaxH3DualClockSamplerT8`、`KSamplerSelect`、`BasicScheduler`、`VHS_VideoCombine`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`MiniMaxH3AVDecodeT8`、`MemoryCleaner`、`llama_cpp_parameters`、`Text`、`MiniMaxH3AudioConditioningT8`、`llama_cpp_model_loader`、`LoraLoaderBypassModelOnly`、`LoadImage`、`llama_cpp_instruct_adv`、`ResolutionSelector`、`easy saveText`、`CLIPTextEncode`、`EmptyLatentImage`、`KSampler`、`VAEDecode`、`solarL_SaveImagesToZip`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
