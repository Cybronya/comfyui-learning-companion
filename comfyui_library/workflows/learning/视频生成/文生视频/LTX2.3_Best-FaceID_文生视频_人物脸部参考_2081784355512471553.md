---
key: 视频生成/文生视频/LTX2.3_Best-FaceID_文生视频_人物脸部参考_2081784355512471553.json
name: LTX2.3_Best-FaceID_文生视频_人物脸部参考_2081784355512471553
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.3_Best-FaceID_文生视频_人物脸部参考_2081784355512471553.json
hash: dfbca56c8c02d73d
coverage: 0.375
learned_at: 2026-10-15 22:45:05
nodes: [SetNode, GetNode, SetNode, SetNode, SimpleCalculatorKJ, SetNode, GetNode, SetNode, PrimitiveFloat, GetNode, GetNode, GetNode, ImageConcatMulti, GetNode, GetNode, GetNode, GetNode, ComfyNumberConvert, GetNode, GetNode, EmptyLTXVLatentVideo, LTXVConcatAVLatent, SetNode, LTXVEmptyLatentAudio, GetNode, GetNode, GetNode, RecordAudio, GetNode, SetNode, GetNode, AddLabel, SetNode, KSamplerSelect, ManualSigmas, GetNode, GetNode, GetNode, LTXVConditioning, LTXIdentityOverlapConditioning, GetNode, GetNode, GetNode, LTX2SamplingPreviewOverride, GetNode, GetNode, TextGenerate, GetNode, GetNode, StringConcatenate, StringConcatenate, PreviewAny, SetNode, SetNode, CLIPTextEncode, CLIPTextEncode, GetNode, GetNode, SetNode, SetNode, VAELoader, SetNode, SetNode, SetNode, SetNode, SetNode, LTXVCropGuides, Reroute, Reroute, Reroute, Reroute, BasicScheduler, SetNode, SetNode, SetNode, SetNode, SetNode, VAEDecode, GetNode, LTXVAudioVAEDecode, GetNode, LTXVSeparateAVLatent, SamplerCustomAdvanced, CFGGuider, RandomNoise, CreateVideo, VHS_VideoCombine, SaveVideo, UNETLoader, VAELoaderKJ, VAELoaderKJ, DualCLIPLoader, LatentUpscaleModelLoader, MarkdownNote, LoraLoaderModelOnly, LoadImage, LoadAudio, SetNode, PrimitiveInt, LayerUtility: ImageScaleByAspectRatio V2, SetNode, PreviewImage, PrimitiveStringMultiline, PrimitiveFloat]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/文生视频/LTX2.3_Best-FaceID_文生视频_人物脸部参考_2081784355512471553.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.3_Best-FaceID_文生视频_人物脸部参考_2081784355512471553.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（104 个）：
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SimpleCalculatorKJ`
- `SetNode`
- `GetNode`
- `SetNode`
- `PrimitiveFloat`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageConcatMulti`
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
- `LTXVEmptyLatentAudio` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `RecordAudio`
- `GetNode`
- `SetNode`
- `GetNode`
- `AddLabel`
- `SetNode`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVConditioning`
- `LTXIdentityOverlapConditioning`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTX2SamplingPreviewOverride`
- `GetNode`
- `GetNode`
- `TextGenerate`
- `GetNode`
- `GetNode`
- `StringConcatenate`
- `StringConcatenate`
- `PreviewAny`
- `SetNode`
- `SetNode`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `VAELoader`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `LTXVCropGuides`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `BasicScheduler`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `VAEDecode` ★核心
- `GetNode`
- `LTXVAudioVAEDecode` ★核心
- `GetNode`
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `CFGGuider`
- `RandomNoise`
- `CreateVideo`
- `VHS_VideoCombine`
- `SaveVideo`
- `UNETLoader` ★核心
- `VAELoaderKJ`
- `VAELoaderKJ`
- `DualCLIPLoader`
- `LatentUpscaleModelLoader`
- `MarkdownNote`
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `LoadAudio`
- `SetNode`
- `PrimitiveInt`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `PreviewImage`
- `PrimitiveStringMultiline`
- `PrimitiveFloat`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **38%**（39/104）

**有卡**：`SimpleCalculatorKJ`、`ImageConcatMulti`、`ComfyNumberConvert`、`EmptyLTXVLatentVideo`、`LTXVConcatAVLatent`、`LTXVEmptyLatentAudio`、`RecordAudio`、`AddLabel`、`KSamplerSelect`、`ManualSigmas`、`LTXVConditioning`、`LTXIdentityOverlapConditioning`、`LTX2SamplingPreviewOverride`、`TextGenerate`、`StringConcatenate`、`CLIPTextEncode`、`VAELoader`、`LTXVCropGuides`、`BasicScheduler`、`VAEDecode`、`LTXVAudioVAEDecode`、`LTXVSeparateAVLatent`、`SamplerCustomAdvanced`、`CFGGuider`、`RandomNoise`、`CreateVideo`、`VHS_VideoCombine`、`SaveVideo`、`UNETLoader`、`VAELoaderKJ`、`DualCLIPLoader`、`LatentUpscaleModelLoader`、`LoraLoaderModelOnly`、`LoadImage`、`LoadAudio`、`LayerUtility: ImageScaleByAspectRatio V2`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect
