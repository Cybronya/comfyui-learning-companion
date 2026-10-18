---
key: 音频生成/音频生成/LTX-2.3视频增加音频及时长_2046161682556264450.json
name: LTX-2.3视频增加音频及时长_2046161682556264450
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/LTX-2.3视频增加音频及时长_2046161682556264450.json
hash: a53d72a2babba30d
coverage: 0.5
learned_at: 2026-10-18 03:04:50
nodes: [LTXVConditioning, LTXVConcatAVLatent, CLIPTextEncode, LTXVAudioVAEDecode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetImageSizeAndCount, MarkdownNote, VHS_VideoInfo, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, MarkdownNote, MarkdownNote, SetNode, ManualSigmas, LTX2SamplingPreviewOverride, LTX2_NAG, GetNode, GetImageRangeFromBatch, GetNode, CLIPTextEncode, GetNode, SetNode, SetNode, SimpleCalculatorKJ, SetNode, SetNode, MarkdownNote, GetNode, GetNode, SimpleCalculatorKJ, GetNode, GetNode, SetNode, GetNode, GetNode, SimpleMath+, UNETLoader, DualCLIPLoader, VAELoader, VAELoaderKJ, VAELoader, LTXVEmptyLatentAudio, SetNode, SimpleCalculatorKJ, LTXVSeparateAVLatent, GetNode, SetNode, SamplerCustomAdvanced, LTXVPreprocess, SimpleCalculatorKJ, ImageResizeKJv2, GetNode, VAEEncode, LTXVAudioVideoMask, CFGGuider, GetNode, LoraLoaderModelOnly, SetNode, SetNode, KSamplerSelect, RandomNoise, VAEDecodeTiled, SetNode, VHS_LoadVideo, CLIPTextEncode, VHS_VideoCombine, INTConstant, INTConstant, INTConstant, INTConstant]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 音频生成/音频生成/LTX-2.3视频增加音频及时长_2046161682556264450.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/LTX-2.3视频增加音频及时长_2046161682556264450.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Other

**节点**（80 个）：
- `LTXVConditioning`
- `LTXVConcatAVLatent`
- `CLIPTextEncode` ★核心
- `LTXVAudioVAEDecode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetImageSizeAndCount`
- `MarkdownNote`
- `VHS_VideoInfo`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `MarkdownNote`
- `MarkdownNote`
- `SetNode`
- `ManualSigmas`
- `LTX2SamplingPreviewOverride`
- `LTX2_NAG`
- `GetNode`
- `GetImageRangeFromBatch`
- `GetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `SetNode`
- `SetNode`
- `SimpleCalculatorKJ`
- `SetNode`
- `SetNode`
- `MarkdownNote`
- `GetNode`
- `GetNode`
- `SimpleCalculatorKJ`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SimpleMath+`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `VAELoader`
- `VAELoaderKJ`
- `VAELoader`
- `LTXVEmptyLatentAudio` ★核心
- `SetNode`
- `SimpleCalculatorKJ`
- `LTXVSeparateAVLatent`
- `GetNode`
- `SetNode`
- `SamplerCustomAdvanced` ★核心
- `LTXVPreprocess`
- `SimpleCalculatorKJ`
- `ImageResizeKJv2`
- `GetNode`
- `VAEEncode` ★核心
- `LTXVAudioVideoMask`
- `CFGGuider`
- `GetNode`
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `SetNode`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `VAEDecodeTiled` ★核心
- `SetNode`
- `VHS_LoadVideo`
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `INTConstant`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **50%**（40/80）

**有卡**：`LTXVConditioning`、`LTXVConcatAVLatent`、`CLIPTextEncode`、`LTXVAudioVAEDecode`、`GetImageSizeAndCount`、`VHS_VideoInfo`、`ManualSigmas`、`LTX2SamplingPreviewOverride`、`LTX2_NAG`、`GetImageRangeFromBatch`、`SimpleCalculatorKJ`、`SimpleMath+`、`UNETLoader`、`DualCLIPLoader`、`VAELoader`、`VAELoaderKJ`、`LTXVEmptyLatentAudio`、`LTXVSeparateAVLatent`、`SamplerCustomAdvanced`、`LTXVPreprocess`、`ImageResizeKJv2`、`VAEEncode`、`LTXVAudioVideoMask`、`CFGGuider`、`LoraLoaderModelOnly`、`KSamplerSelect`、`RandomNoise`、`VAEDecodeTiled`、`VHS_LoadVideo`、`VHS_VideoCombine`、`INTConstant`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPTextEncode、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVConcatAVLatent
