---
key: 视频生成/文生视频/MiniMax H3多合一Turbo4 Sage T8 Stable-R2V Turbo6 EXP二_2087347142024327170.json
name: MiniMax H3多合一Turbo4 Sage T8 Stable-R2V Turbo6 EXP二_2087347142024327170
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/MiniMax H3多合一Turbo4 Sage T8 Stable-R2V Turbo6 EXP二_2087347142024327170.json
hash: e77315d595c1e109
coverage: 0.886179
learned_at: 2026-10-15 22:45:55
nodes: [SaveVideo, MiniMaxH3ImageToVideo, SaveVideo, SaveVideo, UNETLoader, UNETLoader, KSamplerSelect, BasicScheduler, BasicScheduler, SamplerCustomAdvanced, VAEDecodeAudio, RandomNoise, BasicGuider, VAEDecode, CreateVideo, MiniMaxH3ImageToVideo, RandomNoise, BasicGuider, BasicGuider, RandomNoise, SamplerCustomAdvanced, VAEDecode, VAEDecodeAudio, CreateVideo, SamplerCustomAdvanced, VAELoader, VAELoader, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, ComfySwitchNode, ComfySwitchNode, ComfySwitchNode, ResolutionSelector, SaveVideo, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadVideo, LoadVideo, LoadImage, LoadVideo, LoadImage, CLIPLoader, GetVideoComponents, GetVideoComponents, GetVideoComponents, LoadAudio, LoadAudio, LoadAudio, BasicGuider, RandomNoise, VAEDecode, VAEDecodeAudio, SamplerCustomAdvanced, CreateVideo, VAEDecode, VAEDecodeAudio, CreateVideo, LoadImage, LoraLoaderBypassModelOnly, MiniMaxH3DualClockSamplerT8, MiniMaxH3DualClockSamplerT8, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3DualClockSamplerT8, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ImageToVideo, LoraLoaderModelOnly, ImageResizeKJv2, PT_H3ConcatAVLatent, KSamplerSelect, BasicScheduler, VAEEncodeAudio, VAEEncode, BasicGuider, SamplerCustomAdvanced, VAEDecode, CreateVideo, ResolutionSelector, ComfyMathExpression, ComfySwitchNode, ComfySwitchNode, MiniMaxH3ReferenceToVideo, ComfySwitchNode, PrimitiveInt, ResolutionSelector, PrimitiveInt, LoadImage, PrimitiveFloat, PrimitiveStringMultiline, LoadImage, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, JjkText, solarL_SaveImagesToZip, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, Note]
patterns: [text_to_image, image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/MiniMax H3多合一Turbo4 Sage T8 Stable-R2V Turbo6 EXP二_2087347142024327170.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/MiniMax H3多合一Turbo4 Sage T8 Stable-R2V Turbo6 EXP二_2087347142024327170.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（123 个）：
- `SaveVideo`
- `MiniMaxH3ImageToVideo`
- `SaveVideo`
- `SaveVideo`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `BasicScheduler`
- `SamplerCustomAdvanced` ★核心
- `VAEDecodeAudio` ★核心
- `RandomNoise`
- `BasicGuider`
- `VAEDecode` ★核心
- `CreateVideo`
- `MiniMaxH3ImageToVideo`
- `RandomNoise`
- `BasicGuider`
- `BasicGuider`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `CreateVideo`
- `SamplerCustomAdvanced` ★核心
- `VAELoader`
- `VAELoader`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `ResolutionSelector`
- `SaveVideo`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadVideo`
- `LoadVideo`
- `LoadImage`
- `LoadVideo`
- `LoadImage`
- `CLIPLoader`
- `GetVideoComponents`
- `GetVideoComponents`
- `GetVideoComponents`
- `LoadAudio`
- `LoadAudio`
- `LoadAudio`
- `BasicGuider`
- `RandomNoise`
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `SamplerCustomAdvanced` ★核心
- `CreateVideo`
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `CreateVideo`
- `LoadImage`
- `LoraLoaderBypassModelOnly` ★核心
- `MiniMaxH3DualClockSamplerT8` ★核心
- `MiniMaxH3DualClockSamplerT8` ★核心
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3DualClockSamplerT8` ★核心
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ImageToVideo`
- `LoraLoaderModelOnly` ★核心
- `ImageResizeKJv2`
- `PT_H3ConcatAVLatent`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `VAEEncodeAudio` ★核心
- `VAEEncode` ★核心
- `BasicGuider`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `CreateVideo`
- `ResolutionSelector`
- `ComfyMathExpression`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `MiniMaxH3ReferenceToVideo`
- `ComfySwitchNode`
- `PrimitiveInt`
- `ResolutionSelector`
- `PrimitiveInt`
- `LoadImage`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `LoadImage`
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

覆盖率 **89%**（109/123）

**有卡**：`SaveVideo`、`MiniMaxH3ImageToVideo`、`UNETLoader`、`KSamplerSelect`、`BasicScheduler`、`SamplerCustomAdvanced`、`VAEDecodeAudio`、`RandomNoise`、`BasicGuider`、`VAEDecode`、`CreateVideo`、`VAELoader`、`ComfyMathExpression`、`ResolutionSelector`、`LoadImage`、`LoadVideo`、`CLIPLoader`、`GetVideoComponents`、`LoadAudio`、`LoraLoaderBypassModelOnly`、`MiniMaxH3DualClockSamplerT8`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`LoraLoaderModelOnly`、`ImageResizeKJv2`、`PT_H3ConcatAVLatent`、`VAEEncodeAudio`、`VAEEncode`、`MiniMaxH3ReferenceToVideo`、`CLIPTextEncode`、`EmptyLatentImage`、`KSampler`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
