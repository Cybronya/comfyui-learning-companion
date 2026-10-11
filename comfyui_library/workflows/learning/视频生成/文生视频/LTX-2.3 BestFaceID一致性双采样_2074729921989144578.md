---
key: 视频生成/文生视频/LTX-2.3 BestFaceID一致性双采样_2074729921989144578.json
name: LTX-2.3 BestFaceID一致性双采样_2074729921989144578
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX-2.3 BestFaceID一致性双采样_2074729921989144578.json
hash: b0b206177f905f31
coverage: 0.407143
learned_at: 2026-10-11 20:38:34
nodes: [SetNode, GetNode, SetNode, SetNode, SimpleCalculatorKJ, SetNode, GetNode, VAELoaderKJ, SetNode, SetNode, SetNode, SetNode, GetNode, VAELoaderKJ, LatentUpscaleModelLoader, SetNode, SetNode, SetNode, PrimitiveFloat, SetNode, VAELoader, SetNode, GetNode, GetNode, CLIPTextEncode, GetNode, GetNode, StringConcatenate, GetNode, PrimitiveInt, GetNode, GetNode, GetNode, LTX2SamplingPreviewOverride, RandomNoise, CFGGuider, ManualSigmas, Reroute, Reroute, Reroute, GetNode, SetNode, SetNode, SamplerCustomAdvanced, SetNode, GetNode, CLIPTextEncode, CLIPTextEncode, SetNode, GetNode, GetNode, GetNode, GetNode, ComfyNumberConvert, GetNode, GetNode, EmptyLTXVLatentVideo, LTXVConcatAVLatent, SetNode, GetNode, GetNode, LTXVEmptyLatentAudio, GetNode, VAEDecode, SetNode, GetNode, GetNode, GetNode, Reroute, LTXVConditioning, RecordAudio, GetNode, SetNode, SetNode, StringConcatenate, TextGenerate, ImageResizeKJv2, PreviewAny, LTXIdentityOverlapConditioning, KSamplerSelect, BasicScheduler, RandomNoise, LTXVConcatAVLatent, GetNode, SetNode, CFGGuider, LTXIdentityOverlapConditioning, LTX2SamplingPreviewOverride, GetNode, GetNode, GetNode, LTXVSeparateAVLatent, SetNode, LTXVLatentUpsampler, GetNode, GetNode, GetNode, LTXVCropGuides, SetNode, LTXVAudioVAEDecode, SetNode, GetNode, GetNode, ManualSigmas, KSamplerSelect, SamplerCustomAdvanced, LTXVSeparateAVLatent, VAEDecodeTiled, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, AddLabel, AddLabel, CreateVideo, GetNode, GetNode, GetNode, DualCLIPLoader, LoadAudio, SetNode, GetNode, SetNode, SaveVideo, LoadImage, CreateVideo, AddLabel, ImageConcatMulti, SaveVideo, PrimitiveStringMultiline, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, PrimitiveFloat, MarkdownNote, VHS_VideoCombine, UNETLoader]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/文生视频/LTX-2.3 BestFaceID一致性双采样_2074729921989144578.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX-2.3 BestFaceID一致性双采样_2074729921989144578.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（140 个）：
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SimpleCalculatorKJ`
- `SetNode`
- `GetNode`
- `VAELoaderKJ`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `VAELoaderKJ`
- `LatentUpscaleModelLoader`
- `SetNode`
- `SetNode`
- `SetNode`
- `PrimitiveFloat`
- `SetNode`
- `VAELoader`
- `SetNode`
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `StringConcatenate`
- `GetNode`
- `PrimitiveInt`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTX2SamplingPreviewOverride`
- `RandomNoise`
- `CFGGuider`
- `ManualSigmas`
- `Reroute`
- `Reroute`
- `Reroute`
- `GetNode`
- `SetNode`
- `SetNode`
- `SamplerCustomAdvanced` ★核心
- `SetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ComfyNumberConvert`
- `GetNode`
- `GetNode`
- `EmptyLTXVLatentVideo`
- `LTXVConcatAVLatent`
- `SetNode`
- `GetNode`
- `GetNode`
- `LTXVEmptyLatentAudio` ★核心
- `GetNode`
- `VAEDecode` ★核心
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Reroute`
- `LTXVConditioning`
- `RecordAudio`
- `GetNode`
- `SetNode`
- `SetNode`
- `StringConcatenate`
- `TextGenerate`
- `ImageResizeKJv2`
- `PreviewAny`
- `LTXIdentityOverlapConditioning`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `RandomNoise`
- `LTXVConcatAVLatent`
- `GetNode`
- `SetNode`
- `CFGGuider`
- `LTXIdentityOverlapConditioning`
- `LTX2SamplingPreviewOverride`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVSeparateAVLatent`
- `SetNode`
- `LTXVLatentUpsampler` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVCropGuides`
- `SetNode`
- `LTXVAudioVAEDecode` ★核心
- `SetNode`
- `GetNode`
- `GetNode`
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `AddLabel`
- `AddLabel`
- `CreateVideo`
- `GetNode`
- `GetNode`
- `GetNode`
- `DualCLIPLoader`
- `LoadAudio`
- `SetNode`
- `GetNode`
- `SetNode`
- `SaveVideo`
- `LoadImage`
- `CreateVideo`
- `AddLabel`
- `ImageConcatMulti`
- `SaveVideo`
- `PrimitiveStringMultiline`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PrimitiveFloat`
- `MarkdownNote`
- `VHS_VideoCombine`
- `UNETLoader` ★核心

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **41%**（57/140）

**有卡**：`SimpleCalculatorKJ`、`VAELoaderKJ`、`LatentUpscaleModelLoader`、`VAELoader`、`CLIPTextEncode`、`StringConcatenate`、`LTX2SamplingPreviewOverride`、`RandomNoise`、`CFGGuider`、`ManualSigmas`、`SamplerCustomAdvanced`、`ComfyNumberConvert`、`EmptyLTXVLatentVideo`、`LTXVConcatAVLatent`、`LTXVEmptyLatentAudio`、`VAEDecode`、`LTXVConditioning`、`RecordAudio`、`TextGenerate`、`ImageResizeKJv2`、`LTXIdentityOverlapConditioning`、`KSamplerSelect`、`BasicScheduler`、`LTXVSeparateAVLatent`、`LTXVLatentUpsampler`、`LTXVCropGuides`、`LTXVAudioVAEDecode`、`VAEDecodeTiled`、`AddLabel`、`CreateVideo`、`DualCLIPLoader`、`LoadAudio`、`SaveVideo`、`LoadImage`、`ImageConcatMulti`、`LoraLoaderModelOnly`、`VHS_VideoCombine`、`UNETLoader`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect
