---
key: 视频生成/文生视频/LTX-2.5文生视频音画同步生成处理工具_2101378961912721410.json
name: LTX-2.5文生视频音画同步生成处理工具_2101378961912721410
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX-2.5文生视频音画同步生成处理工具_2101378961912721410.json
hash: 6ccb7ec58ca78252
coverage: 0.857143
learned_at: 2026-10-11 22:12:34
nodes: [SaveVideo, ResolutionSelector, CreateVideo, LTXVConcatAVLatent, ManualSigmas, LTXVLatentUpsampler, LTXVAudioVAEDecode, KSamplerSelect, LTXVDualCFGGuider, SamplerCustomAdvanced, RandomNoise, LTXVSeparateAVLatent, LTXVSeparateAVLatent, VAEDecodeTiled, SamplerCustomAdvanced, ManualSigmas, LTXVDualCFGGuider, KSamplerSelect, RandomNoise, LTXVConditioning, LTXVConcatAVLatent, CLIPTextEncode, CLIPTextEncode, EmptyLTXVLatentVideo, LTXVEmptyLatentAudio, PreviewAny, ComfySwitchNode, LatentUpscaleModelLoader, UNETLoader, VAELoader, VAELoader, CLIPLoader, TextGenerateLTX2Prompt, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, PrimitiveInt, PrimitiveInt, PrimitiveInt, PrimitiveInt, PrimitiveStringMultiline, CLIPLoader, PrimitiveBoolean, ImageFromBatch, SaveImage, SaveAudio, VHS_VideoCombine, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/LTX-2.5文生视频音画同步生成处理工具_2101378961912721410.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX-2.5文生视频音画同步生成处理工具_2101378961912721410.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（77 个）：
- `SaveVideo`
- `ResolutionSelector`
- `CreateVideo`
- `LTXVConcatAVLatent`
- `ManualSigmas`
- `LTXVLatentUpsampler` ★核心
- `LTXVAudioVAEDecode` ★核心
- `KSamplerSelect` ★核心
- `LTXVDualCFGGuider`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `LTXVSeparateAVLatent`
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `SamplerCustomAdvanced` ★核心
- `ManualSigmas`
- `LTXVDualCFGGuider`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `LTXVConditioning`
- `LTXVConcatAVLatent`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `EmptyLTXVLatentVideo`
- `LTXVEmptyLatentAudio` ★核心
- `PreviewAny`
- `ComfySwitchNode`
- `LatentUpscaleModelLoader`
- `UNETLoader` ★核心
- `VAELoader`
- `VAELoader`
- `CLIPLoader`
- `TextGenerateLTX2Prompt`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `CLIPLoader`
- `PrimitiveBoolean`
- `ImageFromBatch`
- `SaveImage`
- `SaveAudio`
- `VHS_VideoCombine`
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
- `EmptyLatentImage` ★核心
- `JjkText`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `solarL_SaveImagesToZip`
- `VAEDecode` ★核心
- `CLIPLoader`
- `VAELoader`
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

覆盖率 **86%**（66/77）

**有卡**：`SaveVideo`、`ResolutionSelector`、`CreateVideo`、`LTXVConcatAVLatent`、`ManualSigmas`、`LTXVLatentUpsampler`、`LTXVAudioVAEDecode`、`KSamplerSelect`、`LTXVDualCFGGuider`、`SamplerCustomAdvanced`、`RandomNoise`、`LTXVSeparateAVLatent`、`VAEDecodeTiled`、`LTXVConditioning`、`CLIPTextEncode`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`LatentUpscaleModelLoader`、`UNETLoader`、`VAELoader`、`CLIPLoader`、`TextGenerateLTX2Prompt`、`ComfyMathExpression`、`PrimitiveBoolean`、`ImageFromBatch`、`SaveImage`、`SaveAudio`、`VHS_VideoCombine`、`LoraLoaderModelOnly`、`KSampler`、`EmptyLatentImage`、`solarL_SaveImagesToZip`、`VAEDecode`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
