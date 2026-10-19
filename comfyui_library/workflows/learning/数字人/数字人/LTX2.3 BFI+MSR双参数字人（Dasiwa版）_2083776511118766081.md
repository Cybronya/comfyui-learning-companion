---
key: 数字人/数字人/LTX2.3 BFI+MSR双参数字人（Dasiwa版）_2083776511118766081.json
name: LTX2.3 BFI+MSR双参数字人（Dasiwa版）_2083776511118766081
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/LTX2.3 BFI+MSR双参数字人（Dasiwa版）_2083776511118766081.json
hash: 3b82d6ae58cd9ec3
coverage: 0.826923
learned_at: 2026-10-18 19:07:41
nodes: [StringConcatenate, StringConcatenate, PreviewAny, SimpleCalculatorKJ, ComfyNumberConvert, TextGenerate, SamplerCustomAdvanced, LTXVSeparateAVLatent, DualCLIPLoader, VAELoaderKJ, LTXVConditioning, RandomNoise, KSamplerSelect, CFGGuider, BasicScheduler, LTXVCropGuides, VAEDecode, CreateVideo, EmptyLTXVLatentVideo, LTXVAudioVAEDecode, PreviewAny, LoraLoaderModelOnly, LoraLoaderModelOnly, LTX2_NAG, CLIPTextEncode, CLIPTextEncode, VAELoaderKJ, ImageResizeKJv2, LTXVConcatAVLatent, LTXVEmptyLatentAudio, SimpleCalculatorKJ, SimpleCalculatorKJ, LTXVAudioVAEEncode, MelBandRoFormerModelLoader, MelBandRoFormerSampler, ComfySwitchNode, SetLatentNoiseMask, SolidMask, VAELoaderKJ, TrimAudioDuration, LTXIdentityOverlapConditioning, PrimitiveFloat, PrimitiveInt, PrimitiveInt, PrimitiveFloat, PrimitiveStringMultiline, UNETLoader, LTXICLoRALoaderModelOnly, Note, LoadAudio, LoadImage, SaveVideo]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 数字人/数字人/LTX2.3 BFI+MSR双参数字人（Dasiwa版）_2083776511118766081.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/LTX2.3 BFI+MSR双参数字人（Dasiwa版）_2083776511118766081.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（52 个）：
- `StringConcatenate`
- `StringConcatenate`
- `PreviewAny`
- `SimpleCalculatorKJ`
- `ComfyNumberConvert`
- `TextGenerate`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `DualCLIPLoader`
- `VAELoaderKJ`
- `LTXVConditioning`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `CFGGuider`
- `BasicScheduler`
- `LTXVCropGuides`
- `VAEDecode` ★核心
- `CreateVideo`
- `EmptyLTXVLatentVideo`
- `LTXVAudioVAEDecode` ★核心
- `PreviewAny`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LTX2_NAG`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAELoaderKJ`
- `ImageResizeKJv2`
- `LTXVConcatAVLatent`
- `LTXVEmptyLatentAudio` ★核心
- `SimpleCalculatorKJ`
- `SimpleCalculatorKJ`
- `LTXVAudioVAEEncode` ★核心
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler` ★核心
- `ComfySwitchNode`
- `SetLatentNoiseMask`
- `SolidMask`
- `VAELoaderKJ`
- `TrimAudioDuration`
- `LTXIdentityOverlapConditioning`
- `PrimitiveFloat`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `UNETLoader` ★核心
- `LTXICLoRALoaderModelOnly` ★核心
- `Note`
- `LoadAudio`
- `LoadImage`
- `SaveVideo`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **83%**（43/52）

**有卡**：`StringConcatenate`、`SimpleCalculatorKJ`、`ComfyNumberConvert`、`TextGenerate`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`DualCLIPLoader`、`VAELoaderKJ`、`LTXVConditioning`、`RandomNoise`、`KSamplerSelect`、`CFGGuider`、`BasicScheduler`、`LTXVCropGuides`、`VAEDecode`、`CreateVideo`、`EmptyLTXVLatentVideo`、`LTXVAudioVAEDecode`、`LoraLoaderModelOnly`、`LTX2_NAG`、`CLIPTextEncode`、`ImageResizeKJv2`、`LTXVConcatAVLatent`、`LTXVEmptyLatentAudio`、`LTXVAudioVAEEncode`、`MelBandRoFormerModelLoader`、`MelBandRoFormerSampler`、`SetLatentNoiseMask`、`SolidMask`、`TrimAudioDuration`、`LTXIdentityOverlapConditioning`、`UNETLoader`、`LTXICLoRALoaderModelOnly`、`LoadAudio`、`LoadImage`、`SaveVideo`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
