---
key: 视频生成/文生视频/ltx2.3-BFI_2079731636958224385.json
name: ltx2.3-BFI_2079731636958224385
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/ltx2.3-BFI_2079731636958224385.json
hash: e6f14a204b07666f
coverage: 0.353535
learned_at: 2026-10-11 20:38:44
nodes: [GetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, StringConcatenate, GetNode, GetNode, SetNode, GetNode, CLIPTextEncode, GetNode, SetNode, CLIPTextEncode, SetNode, SimpleCalculatorKJ, SetNode, GetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, LTXVConditioning, Reroute, Reroute, Reroute, Reroute, RandomNoise, SetNode, SetNode, LTXVSeparateAVLatent, SetNode, SetNode, SetNode, GetNode, VAEDecode, GetNode, SetNode, SetNode, SetNode, SetNode, LTX2SamplingPreviewOverride, CFGGuider, KSamplerSelect, BasicScheduler, GetNode, GetNode, GetNode, ComfyNumberConvert, LTXVEmptyLatentAudio, SetNode, SetNode, GetNode, SamplerCustomAdvanced, GetNode, GetNode, GetNode, LTXVCropGuides, LTXVAudioVAEDecode, LTXVConcatAVLatent, EmptyLTXVLatentVideo, SetNode, GetNode, GetNode, GetNode, MarkdownNote, VHS_VideoCombine, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, SetReserveVRAM, VAELoaderKJ, VAELoaderKJ, DualCLIPLoader, ImageResizeKJv2, PreviewImage, TextGenerate, StringConcatenate, PreviewAny, PrimitiveFloat, PrimitiveFloat, PrimitiveInt, PrimitiveInt, MarkdownNote, VAELoader, LoadImage, LoadImage, LoraLoaderModelOnly, LTXIdentityOverlapConditioning, PrimitiveStringMultiline]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/文生视频/ltx2.3-BFI_2079731636958224385.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/ltx2.3-BFI_2079731636958224385.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（99 个）：
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `StringConcatenate`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `SetNode`
- `CLIPTextEncode` ★核心
- `SetNode`
- `SimpleCalculatorKJ`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVConditioning`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `RandomNoise`
- `SetNode`
- `SetNode`
- `LTXVSeparateAVLatent`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `VAEDecode` ★核心
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `LTX2SamplingPreviewOverride`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `GetNode`
- `GetNode`
- `GetNode`
- `ComfyNumberConvert`
- `LTXVEmptyLatentAudio` ★核心
- `SetNode`
- `SetNode`
- `GetNode`
- `SamplerCustomAdvanced` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVCropGuides`
- `LTXVAudioVAEDecode` ★核心
- `LTXVConcatAVLatent`
- `EmptyLTXVLatentVideo`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `MarkdownNote`
- `VHS_VideoCombine`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `SetReserveVRAM`
- `VAELoaderKJ`
- `VAELoaderKJ`
- `DualCLIPLoader`
- `ImageResizeKJv2`
- `PreviewImage`
- `TextGenerate`
- `StringConcatenate`
- `PreviewAny`
- `PrimitiveFloat`
- `PrimitiveFloat`
- `PrimitiveInt`
- `PrimitiveInt`
- `MarkdownNote`
- `VAELoader`
- `LoadImage`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `LTXIdentityOverlapConditioning`
- `PrimitiveStringMultiline`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **35%**（35/99）

**有卡**：`StringConcatenate`、`CLIPTextEncode`、`SimpleCalculatorKJ`、`LTXVConditioning`、`RandomNoise`、`LTXVSeparateAVLatent`、`VAEDecode`、`LTX2SamplingPreviewOverride`、`CFGGuider`、`KSamplerSelect`、`BasicScheduler`、`ComfyNumberConvert`、`LTXVEmptyLatentAudio`、`SamplerCustomAdvanced`、`LTXVCropGuides`、`LTXVAudioVAEDecode`、`LTXVConcatAVLatent`、`EmptyLTXVLatentVideo`、`VHS_VideoCombine`、`UNETLoader`、`LoraLoaderModelOnly`、`SetReserveVRAM`、`VAELoaderKJ`、`DualCLIPLoader`、`ImageResizeKJv2`、`TextGenerate`、`VAELoader`、`LoadImage`、`LTXIdentityOverlapConditioning`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect
