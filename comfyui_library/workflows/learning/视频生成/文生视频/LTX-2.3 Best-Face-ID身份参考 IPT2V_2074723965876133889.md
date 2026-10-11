---
key: 视频生成/文生视频/LTX-2.3 Best-Face-ID身份参考 IPT2V_2074723965876133889.json
name: LTX-2.3 Best-Face-ID身份参考 IPT2V_2074723965876133889
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX-2.3 Best-Face-ID身份参考 IPT2V_2074723965876133889.json
hash: 918ba2364744cd46
coverage: 0.397351
learned_at: 2026-10-11 20:38:34
nodes: [SetNode, GetNode, SetNode, SetNode, SimpleCalculatorKJ, GetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, PrimitiveFloat, SetNode, GetNode, GetNode, CLIPTextEncode, GetNode, GetNode, GetNode, PrimitiveInt, PrimitiveFloat, GetNode, GetNode, GetNode, LTX2SamplingPreviewOverride, CFGGuider, BasicScheduler, ManualSigmas, Reroute, Reroute, Reroute, GetNode, SetNode, SetNode, SamplerCustomAdvanced, SetNode, GetNode, CLIPTextEncode, SetNode, GetNode, GetNode, GetNode, ComfyNumberConvert, GetNode, GetNode, EmptyLTXVLatentVideo, LTXVConcatAVLatent, SetNode, GetNode, GetNode, LTXVEmptyLatentAudio, GetNode, GetNode, GetNode, GetNode, CreateVideo, Reroute, LTXVConditioning, RecordAudio, GetNode, SetNode, MarkdownNote, GetNode, PreviewAny, SetNode, KSamplerSelect, TextGenerate, LoraLoaderModelOnly, VAELoaderKJ, VAELoaderKJ, DualCLIPLoader, LatentUpscaleModelLoader, VAELoader, LoadAudio, CLIPTextEncode, SetNode, StringConcatenate, StringConcatenate, SetNode, GetNode, LTXIdentityOverlapConditioning, LTXVCropGuides, VAEDecode, GetNode, GetNode, GetNode, LTXVAudioVAEDecode, SetNode, LTXVAudioVAEDecode, SetNode, GetNode, VAEDecode, SetNode, SaveVideo, GetNode, CFGGuider, ManualSigmas, LTXVConcatAVLatent, RandomNoise, SeedGenerator, GetNode, SetNode, GetNode, GetNode, KSamplerSelect, VHS_VideoCombine, LTXVCropGuides, GetNode, ImageConcatMulti, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, LTXVSeparateAVLatent, SamplerCustomAdvanced, Fast Groups Bypasser (rgthree), GetNode, GetNode, GetNode, VHS_VideoCombine, SetNode, AddLabel, GetNode, GetNode, LoadImage, SetNode, RMBG, PrimitiveInt, PrimitiveStringMultiline, VHS_VideoCombine, ImageResizeKJv2, PreviewImage, CropFace, LoraLoaderModelOnly, LoraLoaderModelOnly, SetNode, RandomNoise, SetNode, SetNode, LTXVSeparateAVLatent, GetNode, LTX2SamplingPreviewOverride, GetNode, LTXVLatentUpsampler, LTXIdentityOverlapConditioning, GetNode, UNETLoader]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/文生视频/LTX-2.3 Best-Face-ID身份参考 IPT2V_2074723965876133889.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX-2.3 Best-Face-ID身份参考 IPT2V_2074723965876133889.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（151 个）：
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SimpleCalculatorKJ`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `PrimitiveFloat`
- `SetNode`
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `PrimitiveInt`
- `PrimitiveFloat`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTX2SamplingPreviewOverride`
- `CFGGuider`
- `BasicScheduler`
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
- `SetNode`
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
- `GetNode`
- `GetNode`
- `GetNode`
- `CreateVideo`
- `Reroute`
- `LTXVConditioning`
- `RecordAudio`
- `GetNode`
- `SetNode`
- `MarkdownNote`
- `GetNode`
- `PreviewAny`
- `SetNode`
- `KSamplerSelect` ★核心
- `TextGenerate`
- `LoraLoaderModelOnly` ★核心
- `VAELoaderKJ`
- `VAELoaderKJ`
- `DualCLIPLoader`
- `LatentUpscaleModelLoader`
- `VAELoader`
- `LoadAudio`
- `CLIPTextEncode` ★核心
- `SetNode`
- `StringConcatenate`
- `StringConcatenate`
- `SetNode`
- `GetNode`
- `LTXIdentityOverlapConditioning`
- `LTXVCropGuides`
- `VAEDecode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVAudioVAEDecode` ★核心
- `SetNode`
- `LTXVAudioVAEDecode` ★核心
- `SetNode`
- `GetNode`
- `VAEDecode` ★核心
- `SetNode`
- `SaveVideo`
- `GetNode`
- `CFGGuider`
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `RandomNoise`
- `SeedGenerator`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `KSamplerSelect` ★核心
- `VHS_VideoCombine`
- `LTXVCropGuides`
- `GetNode`
- `ImageConcatMulti`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `SetNode`
- `AddLabel`
- `GetNode`
- `GetNode`
- `LoadImage`
- `SetNode`
- `RMBG`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `VHS_VideoCombine`
- `ImageResizeKJv2`
- `PreviewImage`
- `CropFace`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `RandomNoise`
- `SetNode`
- `SetNode`
- `LTXVSeparateAVLatent`
- `GetNode`
- `LTX2SamplingPreviewOverride`
- `GetNode`
- `LTXVLatentUpsampler` ★核心
- `LTXIdentityOverlapConditioning`
- `GetNode`
- `UNETLoader` ★核心

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **40%**（60/151）

**有卡**：`SimpleCalculatorKJ`、`CLIPTextEncode`、`LTX2SamplingPreviewOverride`、`CFGGuider`、`BasicScheduler`、`ManualSigmas`、`SamplerCustomAdvanced`、`ComfyNumberConvert`、`EmptyLTXVLatentVideo`、`LTXVConcatAVLatent`、`LTXVEmptyLatentAudio`、`CreateVideo`、`LTXVConditioning`、`RecordAudio`、`KSamplerSelect`、`TextGenerate`、`LoraLoaderModelOnly`、`VAELoaderKJ`、`DualCLIPLoader`、`LatentUpscaleModelLoader`、`VAELoader`、`LoadAudio`、`StringConcatenate`、`LTXIdentityOverlapConditioning`、`LTXVCropGuides`、`VAEDecode`、`LTXVAudioVAEDecode`、`SaveVideo`、`RandomNoise`、`SeedGenerator`、`VHS_VideoCombine`、`ImageConcatMulti`、`LTXVSeparateAVLatent`、`AddLabel`、`LoadImage`、`RMBG`、`ImageResizeKJv2`、`CropFace`、`LTXVLatentUpsampler`、`UNETLoader`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect
