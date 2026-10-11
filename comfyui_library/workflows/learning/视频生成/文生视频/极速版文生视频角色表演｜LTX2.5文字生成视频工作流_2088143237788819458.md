---
key: 视频生成/文生视频/极速版文生视频角色表演｜LTX2.5文字生成视频工作流_2088143237788819458.json
name: 极速版文生视频角色表演｜LTX2.5文字生成视频工作流_2088143237788819458
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/极速版文生视频角色表演｜LTX2.5文字生成视频工作流_2088143237788819458.json
hash: b7249e957cc4a7cd
coverage: 0.84507
learned_at: 2026-10-11 20:53:55
nodes: [ComfySwitchNode, LTXVConditioning, RandomNoise, PrimitiveInt, LTXVDualCFGGuider, KSamplerSelect, PrimitiveInt, PrimitiveInt, ComfyMathExpression, LTXVConcatAVLatent, LTXVDualCFGGuider, KSamplerSelect, LTXVConcatAVLatent, ComfyMathExpression, ComfyMathExpression, RandomNoise, ComfyMathExpression, LTXVEmptyLatentAudio, EmptyLTXVLatentVideo, PrimitiveBoolean, PrimitiveInt, VAEDecodeTiled, LTXVSeparateAVLatent, ManualSigmas, ManualSigmas, LTXVAudioVAEDecode, CLIPTextEncode, CLIPTextEncode, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVLatentUpsampler, PreviewAny, ResolutionSelector, UNETLoader, VAELoader, VAELoader, CLIPLoader, CLIPLoader, LatentUpscaleModelLoader, TextGenerateLTX2Prompt, CreateVideo, SamplerCustomAdvanced, SaveVideo, PrimitiveStringMultiline, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, JjkText, solarL_SaveImagesToZip, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/极速版文生视频角色表演｜LTX2.5文字生成视频工作流_2088143237788819458.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/极速版文生视频角色表演｜LTX2.5文字生成视频工作流_2088143237788819458.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（71 个）：
- `ComfySwitchNode`
- `LTXVConditioning`
- `RandomNoise`
- `PrimitiveInt`
- `LTXVDualCFGGuider`
- `KSamplerSelect` ★核心
- `PrimitiveInt`
- `PrimitiveInt`
- `ComfyMathExpression`
- `LTXVConcatAVLatent`
- `LTXVDualCFGGuider`
- `KSamplerSelect` ★核心
- `LTXVConcatAVLatent`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `RandomNoise`
- `ComfyMathExpression`
- `LTXVEmptyLatentAudio` ★核心
- `EmptyLTXVLatentVideo`
- `PrimitiveBoolean`
- `PrimitiveInt`
- `VAEDecodeTiled` ★核心
- `LTXVSeparateAVLatent`
- `ManualSigmas`
- `ManualSigmas`
- `LTXVAudioVAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXVLatentUpsampler` ★核心
- `PreviewAny`
- `ResolutionSelector`
- `UNETLoader` ★核心
- `VAELoader`
- `VAELoader`
- `CLIPLoader`
- `CLIPLoader`
- `LatentUpscaleModelLoader`
- `TextGenerateLTX2Prompt`
- `CreateVideo`
- `SamplerCustomAdvanced` ★核心
- `SaveVideo`
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

**识别到的模式**：text_to_image

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

覆盖率 **85%**（60/71）

**有卡**：`LTXVConditioning`、`RandomNoise`、`LTXVDualCFGGuider`、`KSamplerSelect`、`ComfyMathExpression`、`LTXVConcatAVLatent`、`LTXVEmptyLatentAudio`、`EmptyLTXVLatentVideo`、`PrimitiveBoolean`、`VAEDecodeTiled`、`LTXVSeparateAVLatent`、`ManualSigmas`、`LTXVAudioVAEDecode`、`CLIPTextEncode`、`SamplerCustomAdvanced`、`LTXVLatentUpsampler`、`ResolutionSelector`、`UNETLoader`、`VAELoader`、`CLIPLoader`、`LatentUpscaleModelLoader`、`TextGenerateLTX2Prompt`、`CreateVideo`、`SaveVideo`、`EmptyLatentImage`、`KSampler`、`VAEDecode`、`solarL_SaveImagesToZip`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
