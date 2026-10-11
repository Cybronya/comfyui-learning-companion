---
key: 视频生成/文生视频/LTX2.3-R2V人物参考图-图生视频_2081338352216924161.json
name: LTX2.3-R2V人物参考图-图生视频_2081338352216924161
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.3-R2V人物参考图-图生视频_2081338352216924161.json
hash: f1f33f10ccb01e14
coverage: 0.820513
learned_at: 2026-10-11 20:38:35
nodes: [VAELoaderKJ, DualCLIPLoader, VAELoaderKJ, PrimitiveFloat, PrimitiveInt, PrimitiveInt, PrimitiveFloat, UNETLoader, KSamplerSelect, LTXVConcatAVLatent, RandomNoise, CFGGuider, BasicScheduler, LTXVSeparateAVLatent, VAEDecode, CreateVideo, LTXVAudioVAEDecode, SamplerCustomAdvanced, ComfyNumberConvert, SimpleCalculatorKJ, CLIPTextEncode, LTXVEmptyLatentAudio, CLIPTextEncode, LTXIdentityOverlapConditioning, LTXVConditioning, EmptyLTXVLatentVideo, LTXVCropGuides, PreviewAny, StringConcatenate, StringConcatenate, PreviewAny, ImageResizeKJv2, SaveVideo, LoadImage, TextGenerate, PrimitiveStringMultiline, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/文生视频/LTX2.3-R2V人物参考图-图生视频_2081338352216924161.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.3-R2V人物参考图-图生视频_2081338352216924161.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（39 个）：
- `VAELoaderKJ`
- `DualCLIPLoader`
- `VAELoaderKJ`
- `PrimitiveFloat`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveFloat`
- `UNETLoader` ★核心
- `KSamplerSelect` ★核心
- `LTXVConcatAVLatent`
- `RandomNoise`
- `CFGGuider`
- `BasicScheduler`
- `LTXVSeparateAVLatent`
- `VAEDecode` ★核心
- `CreateVideo`
- `LTXVAudioVAEDecode` ★核心
- `SamplerCustomAdvanced` ★核心
- `ComfyNumberConvert`
- `SimpleCalculatorKJ`
- `CLIPTextEncode` ★核心
- `LTXVEmptyLatentAudio` ★核心
- `CLIPTextEncode` ★核心
- `LTXIdentityOverlapConditioning`
- `LTXVConditioning`
- `EmptyLTXVLatentVideo`
- `LTXVCropGuides`
- `PreviewAny`
- `StringConcatenate`
- `StringConcatenate`
- `PreviewAny`
- `ImageResizeKJv2`
- `SaveVideo`
- `LoadImage`
- `TextGenerate`
- `PrimitiveStringMultiline`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **82%**（32/39）

**有卡**：`VAELoaderKJ`、`DualCLIPLoader`、`UNETLoader`、`KSamplerSelect`、`LTXVConcatAVLatent`、`RandomNoise`、`CFGGuider`、`BasicScheduler`、`LTXVSeparateAVLatent`、`VAEDecode`、`CreateVideo`、`LTXVAudioVAEDecode`、`SamplerCustomAdvanced`、`ComfyNumberConvert`、`SimpleCalculatorKJ`、`CLIPTextEncode`、`LTXVEmptyLatentAudio`、`LTXIdentityOverlapConditioning`、`LTXVConditioning`、`EmptyLTXVLatentVideo`、`LTXVCropGuides`、`StringConcatenate`、`ImageResizeKJv2`、`SaveVideo`、`LoadImage`、`TextGenerate`、`LoraLoaderModelOnly`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
