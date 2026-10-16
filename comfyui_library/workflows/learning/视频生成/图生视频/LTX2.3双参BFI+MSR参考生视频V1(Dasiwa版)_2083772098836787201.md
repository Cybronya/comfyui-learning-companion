---
key: 视频生成/图生视频/LTX2.3双参BFI+MSR参考生视频V1(Dasiwa版)_2083772098836787201.json
name: LTX2.3双参BFI+MSR参考生视频V1(Dasiwa版)_2083772098836787201
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3双参BFI+MSR参考生视频V1(Dasiwa版)_2083772098836787201.json
hash: ca6e3a7e7425ccc6
coverage: 0.829268
learned_at: 2026-10-16 19:17:11
nodes: [PrimitiveFloat, StringConcatenate, StringConcatenate, SimpleCalculatorKJ, ComfyNumberConvert, SamplerCustomAdvanced, LTXVSeparateAVLatent, DualCLIPLoader, VAELoaderKJ, VAELoaderKJ, LTXVConditioning, RandomNoise, KSamplerSelect, CFGGuider, LTXVConcatAVLatent, BasicScheduler, LTXVCropGuides, VAEDecode, CreateVideo, LTXVEmptyLatentAudio, EmptyLTXVLatentVideo, LTXVAudioVAEDecode, ImageResizeKJv2, PreviewAny, LTXIdentityOverlapConditioning, LoraLoaderModelOnly, LTX2_NAG, CLIPTextEncode, CLIPTextEncode, PrimitiveInt, PrimitiveInt, LTXICLoRALoaderModelOnly, UNETLoader, UNETLoader, PreviewAny, TextGenerate, LoraLoaderModelOnly, PrimitiveStringMultiline, PrimitiveFloat, LoadImage, SaveVideo]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX2.3双参BFI+MSR参考生视频V1(Dasiwa版)_2083772098836787201.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/LTX2.3双参BFI+MSR参考生视频V1(Dasiwa版)_2083772098836787201.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（41 个）：
- `PrimitiveFloat`
- `StringConcatenate`
- `StringConcatenate`
- `SimpleCalculatorKJ`
- `ComfyNumberConvert`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `DualCLIPLoader`
- `VAELoaderKJ`
- `VAELoaderKJ`
- `LTXVConditioning`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `CFGGuider`
- `LTXVConcatAVLatent`
- `BasicScheduler`
- `LTXVCropGuides`
- `VAEDecode` ★核心
- `CreateVideo`
- `LTXVEmptyLatentAudio` ★核心
- `EmptyLTXVLatentVideo`
- `LTXVAudioVAEDecode` ★核心
- `ImageResizeKJv2`
- `PreviewAny`
- `LTXIdentityOverlapConditioning`
- `LoraLoaderModelOnly` ★核心
- `LTX2_NAG`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `PrimitiveInt`
- `PrimitiveInt`
- `LTXICLoRALoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `PreviewAny`
- `TextGenerate`
- `LoraLoaderModelOnly` ★核心
- `PrimitiveStringMultiline`
- `PrimitiveFloat`
- `LoadImage`
- `SaveVideo`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **83%**（34/41）

**有卡**：`StringConcatenate`、`SimpleCalculatorKJ`、`ComfyNumberConvert`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`DualCLIPLoader`、`VAELoaderKJ`、`LTXVConditioning`、`RandomNoise`、`KSamplerSelect`、`CFGGuider`、`LTXVConcatAVLatent`、`BasicScheduler`、`LTXVCropGuides`、`VAEDecode`、`CreateVideo`、`LTXVEmptyLatentAudio`、`EmptyLTXVLatentVideo`、`LTXVAudioVAEDecode`、`ImageResizeKJv2`、`LTXIdentityOverlapConditioning`、`LoraLoaderModelOnly`、`LTX2_NAG`、`CLIPTextEncode`、`LTXICLoRALoaderModelOnly`、`UNETLoader`、`TextGenerate`、`LoadImage`、`SaveVideo`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
