---
key: 视频生成/图生视频/超强一致性 BF-Ltx2.3角色表文生-图生视频_2075950261675323393.json
name: 超强一致性 BF-Ltx2.3角色表文生-图生视频_2075950261675323393.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/超强一致性 BF-Ltx2.3角色表文生-图生视频_2075950261675323393.json
hash: 62878ff44ae9dada
coverage: 0.394904
learned_at: 2026-10-15 22:41:28
nodes: [SetNode, GetNode, SetNode, SimpleCalculatorKJ, SetNode, SetNode, GetNode, PrimitiveFloat, SetNode, GetNode, PrimitiveFloat, GetNode, GetNode, SetNode, SetNode, SetNode, GetNode, CLIPTextEncode, SetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, Reroute, SetNode, RandomNoise, GetNode, CFGGuider, GetNode, GetNode, SetNode, LTXVCropGuides, SetNode, SetNode, GetNode, GetNode, ManualSigmas, GetNode, GetNode, GetNode, GetNode, CreateVideo, LTXVAudioVAEDecode, LTXVSeparateAVLatent, GetNode, GetNode, SetNode, SetNode, GetNode, GetNode, SolidMask, Reroute, LTXVEmptyLatentAudio, CFGGuider, LTXVConditioning, GetNode, GetNode, GetNode, CLIPTextEncode, SetNode, GetNode, GetNode, StringConcatenate, StringConcatenate, PreviewAny, SetNode, Reroute, Reroute, SetNode, SetNode, RecordAudio, SetNode, CreateVideo, GetNode, GetNode, GetNode, GetNode, LTXVSeparateAVLatent, GetNode, SetNode, VAEDecode, ComfyMathExpression, GetNode, ComfySwitchNode, ComfySwitchNode, GetNode, GetNode, PrimitiveNode, VAEDecodeTiled, SaveVideo, KSamplerSelect, GetNode, LoadAudio, TrimAudioDuration, GetNode, SetNode, SaveVideo, GetNode, LTXVAudioVAEEncode, SetNode, SetNode, SetNode, SetNode, SetNode, PrimitiveInt, PrimitiveInt, GetNode, ImageResizeKJv2, GetNode, GetNode, SetNode, LTXVConcatAVLatent, GetNode, ComfyMathExpression, EmptyLTXVLatentVideo, GetNode, MarkdownNote, LTXVConcatAVLatent, GetNode, RandomNoise, ImageConcatMulti, ManualSigmas, LoadImage, PrimitiveBoolean, PreviewAny, TextGenerate, SetLatentNoiseMask, SamplerCustomAdvanced, LoadImage, CheckpointLoaderSimple, VAELoaderKJ, LatentUpscaleModelLoader, LoraLoaderModelOnly, VHS_VideoCombine, BasicScheduler, KSamplerSelect, VAELoaderKJ, SetNode, LoraLoaderModelOnly, ImageResizeKJv2, ComfyNumberConvert, SamplerCustomAdvanced, DualCLIPLoader, LTXVImgToVideoInplace, LoraLoaderModelOnly, PrimitiveStringMultiline, LTX2SamplingPreviewOverride, GetNode, LTXVLatentUpsampler, GetNode, LTX2SamplingPreviewOverride, GetNode, LTXIdentityTransfer, LTXIdentityTransfer]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev-fp8.safetensors", "height": 25, "width": 97}
---

# 视频生成/图生视频/超强一致性 BF-Ltx2.3角色表文生-图生视频_2075950261675323393.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2075950261675323393.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（157 个）：
- `SetNode`
- `GetNode`
- `SetNode`
- `SimpleCalculatorKJ`
- `SetNode`
- `SetNode`
- `GetNode`
- `PrimitiveFloat`
- `SetNode`
- `GetNode`
- `PrimitiveFloat`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Reroute`
- `SetNode`
- `RandomNoise`
- `GetNode`
- `CFGGuider`
- `GetNode`
- `GetNode`
- `SetNode`
- `LTXVCropGuides`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `ManualSigmas`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CreateVideo`
- `LTXVAudioVAEDecode` ★核心
- `LTXVSeparateAVLatent`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SolidMask`
- `Reroute`
- `LTXVEmptyLatentAudio` ★核心
- `CFGGuider`
- `LTXVConditioning`
- `GetNode`
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `SetNode`
- `GetNode`
- `GetNode`
- `StringConcatenate`
- `StringConcatenate`
- `PreviewAny`
- `SetNode`
- `Reroute`
- `Reroute`
- `SetNode`
- `SetNode`
- `RecordAudio`
- `SetNode`
- `CreateVideo`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVSeparateAVLatent`
- `GetNode`
- `SetNode`
- `VAEDecode` ★核心
- `ComfyMathExpression`
- `GetNode`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `GetNode`
- `GetNode`
- `PrimitiveNode`
- `VAEDecodeTiled` ★核心
- `SaveVideo`
- `KSamplerSelect` ★核心
- `GetNode`
- `LoadAudio`
- `TrimAudioDuration`
- `GetNode`
- `SetNode`
- `SaveVideo`
- `GetNode`
- `LTXVAudioVAEEncode` ★核心
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `PrimitiveInt`
- `PrimitiveInt`
- `GetNode`
- `ImageResizeKJv2`
- `GetNode`
- `GetNode`
- `SetNode`
- `LTXVConcatAVLatent`
- `GetNode`
- `ComfyMathExpression`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `MarkdownNote`
- `LTXVConcatAVLatent`
- `GetNode`
- `RandomNoise`
- `ImageConcatMulti`
- `ManualSigmas`
- `LoadImage`
- `PrimitiveBoolean`
- `PreviewAny`
- `TextGenerate`
- `SetLatentNoiseMask`
- `SamplerCustomAdvanced` ★核心
- `LoadImage`
- `CheckpointLoaderSimple` ★核心
- `VAELoaderKJ`
- `LatentUpscaleModelLoader`
- `LoraLoaderModelOnly` ★核心
- `VHS_VideoCombine`
- `BasicScheduler`
- `KSamplerSelect` ★核心
- `VAELoaderKJ`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `ImageResizeKJv2`
- `ComfyNumberConvert`
- `SamplerCustomAdvanced` ★核心
- `DualCLIPLoader`
- `LTXVImgToVideoInplace`
- `LoraLoaderModelOnly` ★核心
- `PrimitiveStringMultiline`
- `LTX2SamplingPreviewOverride`
- `GetNode`
- `LTXVLatentUpsampler` ★核心
- `GetNode`
- `LTX2SamplingPreviewOverride`
- `GetNode`
- `LTXIdentityTransfer`
- `LTXIdentityTransfer`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-dev-fp8.safetensors`

## 知识

覆盖率 **39%**（62/157）

**有卡**：`SimpleCalculatorKJ`、`CLIPTextEncode`、`RandomNoise`、`CFGGuider`、`LTXVCropGuides`、`ManualSigmas`、`CreateVideo`、`LTXVAudioVAEDecode`、`LTXVSeparateAVLatent`、`SolidMask`、`LTXVEmptyLatentAudio`、`LTXVConditioning`、`StringConcatenate`、`RecordAudio`、`VAEDecode`、`ComfyMathExpression`、`VAEDecodeTiled`、`SaveVideo`、`KSamplerSelect`、`LoadAudio`、`TrimAudioDuration`、`LTXVAudioVAEEncode`、`ImageResizeKJv2`、`LTXVConcatAVLatent`、`EmptyLTXVLatentVideo`、`ImageConcatMulti`、`LoadImage`、`PrimitiveBoolean`、`TextGenerate`、`SetLatentNoiseMask`、`SamplerCustomAdvanced`、`CheckpointLoaderSimple`、`VAELoaderKJ`、`LatentUpscaleModelLoader`、`LoraLoaderModelOnly`、`VHS_VideoCombine`、`BasicScheduler`、`ComfyNumberConvert`、`DualCLIPLoader`、`LTXVImgToVideoInplace`、`LTX2SamplingPreviewOverride`、`LTXVLatentUpsampler`、`LTXIdentityTransfer`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
