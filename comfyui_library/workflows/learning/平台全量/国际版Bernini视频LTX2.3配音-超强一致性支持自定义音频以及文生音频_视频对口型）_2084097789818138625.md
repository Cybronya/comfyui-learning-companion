---
key: 平台全量/国际版Bernini视频LTX2.3配音-超强一致性支持自定义音频以及文生音频_视频对口型）_2084097789818138625.json
name: 国际版Bernini视频LTX2.3配音-超强一致性支持自定义音频以及文生音频_视频对口型）_2084097789818138625
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/国际版Bernini视频LTX2.3配音-超强一致性支持自定义音频以及文生音频_视频对口型）_2084097789818138625.json
hash: 9eb259883757ab3d
coverage: 0.512195
learned_at: 2026-11-14 01:53:12
nodes: [LTXVCropGuides, SetNode, GetNode, SolidMask, GetNode, GetNode, GetNode, LTXVAudioVAEDecode, GetNode, SetNode, easy convertAnything, SetNode, LTXVSeparateAVLatent, GetNode, VAEDecodeTiled, SetNode, SetNode, GetNode, GetNode, SetNode, GetNode, easy seed, VHS_VideoInfoLoaded, KSamplerAdvanced, easy cleanGpuUsed, SetNode, LTXAVTextEncoderLoader, PathchSageAttentionKJ, ModelPatchTorchSettings, PathchSageAttentionKJ, MarkdownNote, CheckpointLoaderSimple, SetNode, SetNode, LTXAVTextEncoderLoader, LoraLoaderModelOnly, SetNode, LTXVAudioVAELoader, LoraLoaderModelOnly, LoraLoaderModelOnly, MarkdownNote, MarkdownNote, SetNode, LTX2SamplingPreviewOverride, GetNode, GetNode, CLIPTextEncode, LTX2_NAG, GetNode, LTXVAudioVAEEncode, GetNode, GetNode, GetNode, VHS_VideoCombine, CR Text, MarkdownNote, GetNode, PrimitiveBoolean, GetNode, CLIPTextEncode, PainterLTX2Vomni, LTXVConcatAVLatent, CheckpointLoaderSimple, LTXVAudioVAELoader, LoadAudio, PainterAudioCut, GetNode, ComfySwitchNode, SetLatentNoiseMask, MathExpression|pysssss, SetNode, easy int, SetNode, GetNode, SetNode, SetNode, easy imageSize, PainterFrameExtractor, LayerUtility: ImageScaleByAspectRatio V2, GetNode, easy int, VHS_LoadVideo]
patterns: []
missing: []
parameters: {"cfg": 9, "checkpoint": "ltx-2.3-22b-distilled-1.1-42.9G.safetensors", "denoise": "linear_quadratic", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 平台全量/国际版Bernini视频LTX2.3配音-超强一致性支持自定义音频以及文生音频_视频对口型）_2084097789818138625.json

> 来源文件 `comfyui_library/workflows/平台全量/国际版Bernini视频LTX2.3配音-超强一致性支持自定义音频以及文生音频_视频对口型）_2084097789818138625.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（82 个）：
- `LTXVCropGuides`
- `SetNode`
- `GetNode`
- `SolidMask`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVAudioVAEDecode` ★核心
- `GetNode`
- `SetNode`
- `easy convertAnything`
- `SetNode`
- `LTXVSeparateAVLatent`
- `GetNode`
- `VAEDecodeTiled` ★核心
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `easy seed`
- `VHS_VideoInfoLoaded`
- `KSamplerAdvanced` ★核心
- `easy cleanGpuUsed`
- `SetNode`
- `LTXAVTextEncoderLoader`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `MarkdownNote`
- `CheckpointLoaderSimple` ★核心
- `SetNode`
- `SetNode`
- `LTXAVTextEncoderLoader`
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `LTXVAudioVAELoader`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `MarkdownNote`
- `MarkdownNote`
- `SetNode`
- `LTX2SamplingPreviewOverride`
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `LTX2_NAG`
- `GetNode`
- `LTXVAudioVAEEncode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `CR Text`
- `MarkdownNote`
- `GetNode`
- `PrimitiveBoolean`
- `GetNode`
- `CLIPTextEncode` ★核心
- `PainterLTX2Vomni`
- `LTXVConcatAVLatent`
- `CheckpointLoaderSimple` ★核心
- `LTXVAudioVAELoader`
- `LoadAudio`
- `PainterAudioCut`
- `GetNode`
- `ComfySwitchNode`
- `SetLatentNoiseMask`
- `MathExpression|pysssss`
- `SetNode`
- `easy int`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `easy imageSize`
- `PainterFrameExtractor`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetNode`
- `easy int`
- `VHS_LoadVideo`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `9`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `linear_quadratic`
- `checkpoint` = `ltx-2.3-22b-distilled-1.1-42.9G.safetensors`

## 知识

覆盖率 **51%**（42/82）

**有卡**：`LTXVCropGuides`、`SolidMask`、`LTXVAudioVAEDecode`、`easy convertAnything`、`LTXVSeparateAVLatent`、`VAEDecodeTiled`、`easy seed`、`VHS_VideoInfoLoaded`、`KSamplerAdvanced`、`easy cleanGpuUsed`、`LTXAVTextEncoderLoader`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`CheckpointLoaderSimple`、`LoraLoaderModelOnly`、`LTXVAudioVAELoader`、`LTX2SamplingPreviewOverride`、`CLIPTextEncode`、`LTX2_NAG`、`LTXVAudioVAEEncode`、`VHS_VideoCombine`、`CR Text`、`PrimitiveBoolean`、`PainterLTX2Vomni`、`LTXVConcatAVLatent`、`LoadAudio`、`PainterAudioCut`、`SetLatentNoiseMask`、`MathExpression|pysssss`、`easy int`、`easy imageSize`、`PainterFrameExtractor`、`LayerUtility: ImageScaleByAspectRatio V2`、`VHS_LoadVideo`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、easy seed、KSamplerAdvanced、LTXAVTextEncoderLoader、LTXVAudioVAEDecode、LTXVAudioVAEEncode
