---
key: 音频生成/音频生成/Bernini视频配音好助手-绘画小子LTX2.3配音-超强一致性支持自定义音频以及文生音频_视频对口型）_2082730525239889921.json
name: Bernini视频配音好助手-绘画小子LTX2.3配音-超强一致性支持自定义音频以及文生音频_视频对口型）_2082730525239889921
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/Bernini视频配音好助手-绘画小子LTX2.3配音-超强一致性支持自定义音频以及文生音频_视频对口型）_2082730525239889921.json
hash: bd16eff036c3031a
coverage: 0.518072
learned_at: 2026-10-18 03:04:48
nodes: [LTXVCropGuides, SetLatentNoiseMask, SetNode, GetNode, SolidMask, GetNode, GetNode, GetNode, easy imageSize, MathExpression|pysssss, LTXVAudioVAEDecode, GetNode, SetNode, SetNode, easy convertAnything, SetNode, LTXVSeparateAVLatent, GetNode, GetNode, SetNode, SetNode, PainterAudioCut, GetNode, LTXVConcatAVLatent, VAEDecodeTiled, SetNode, SetNode, ComfySwitchNode, GetNode, GetNode, PrimitiveBoolean, SetNode, GetNode, GetNode, GetNode, easy int, LoadImage, MarkdownNote, SetNode, GetNode, CR Text, easy seed, VHS_VideoInfoLoaded, LayerUtility: ImageScaleByAspectRatio V2, KSamplerAdvanced, easy cleanGpuUsed, PainterFrameExtractor, SetNode, LTXAVTextEncoderLoader, PathchSageAttentionKJ, CheckpointLoaderSimple, LTXVAudioVAELoader, ModelPatchTorchSettings, PathchSageAttentionKJ, MarkdownNote, CheckpointLoaderSimple, SetNode, SetNode, LTXAVTextEncoderLoader, LoraLoaderModelOnly, SetNode, LTXVAudioVAELoader, LoraLoaderModelOnly, LoraLoaderModelOnly, MarkdownNote, MarkdownNote, SetNode, LTX2SamplingPreviewOverride, CLIPTextEncode, GetNode, GetNode, CLIPTextEncode, LTX2_NAG, GetNode, LTXVAudioVAEEncode, GetNode, GetNode, PainterLTX2Vomni, GetNode, LoadAudio, VHS_VideoCombine, VHS_LoadVideo, easy int]
patterns: []
missing: []
parameters: {"cfg": 9, "checkpoint": "10Eros_v1.4_fp8mixed_learned.safetensors", "denoise": "linear_quadratic", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 音频生成/音频生成/Bernini视频配音好助手-绘画小子LTX2.3配音-超强一致性支持自定义音频以及文生音频_视频对口型）_2082730525239889921.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/Bernini视频配音好助手-绘画小子LTX2.3配音-超强一致性支持自定义音频以及文生音频_视频对口型）_2082730525239889921.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（83 个）：
- `LTXVCropGuides`
- `SetLatentNoiseMask`
- `SetNode`
- `GetNode`
- `SolidMask`
- `GetNode`
- `GetNode`
- `GetNode`
- `easy imageSize`
- `MathExpression|pysssss`
- `LTXVAudioVAEDecode` ★核心
- `GetNode`
- `SetNode`
- `SetNode`
- `easy convertAnything`
- `SetNode`
- `LTXVSeparateAVLatent`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `PainterAudioCut`
- `GetNode`
- `LTXVConcatAVLatent`
- `VAEDecodeTiled` ★核心
- `SetNode`
- `SetNode`
- `ComfySwitchNode`
- `GetNode`
- `GetNode`
- `PrimitiveBoolean`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `easy int`
- `LoadImage`
- `MarkdownNote`
- `SetNode`
- `GetNode`
- `CR Text`
- `easy seed`
- `VHS_VideoInfoLoaded`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `KSamplerAdvanced` ★核心
- `easy cleanGpuUsed`
- `PainterFrameExtractor`
- `SetNode`
- `LTXAVTextEncoderLoader`
- `PathchSageAttentionKJ`
- `CheckpointLoaderSimple` ★核心
- `LTXVAudioVAELoader`
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
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `LTX2_NAG`
- `GetNode`
- `LTXVAudioVAEEncode` ★核心
- `GetNode`
- `GetNode`
- `PainterLTX2Vomni`
- `GetNode`
- `LoadAudio`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `easy int`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `9`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `linear_quadratic`
- `checkpoint` = `10Eros_v1.4_fp8mixed_learned.safetensors`

## 知识

覆盖率 **52%**（43/83）

**有卡**：`LTXVCropGuides`、`SetLatentNoiseMask`、`SolidMask`、`easy imageSize`、`MathExpression|pysssss`、`LTXVAudioVAEDecode`、`easy convertAnything`、`LTXVSeparateAVLatent`、`PainterAudioCut`、`LTXVConcatAVLatent`、`VAEDecodeTiled`、`PrimitiveBoolean`、`easy int`、`LoadImage`、`CR Text`、`easy seed`、`VHS_VideoInfoLoaded`、`LayerUtility: ImageScaleByAspectRatio V2`、`KSamplerAdvanced`、`easy cleanGpuUsed`、`PainterFrameExtractor`、`LTXAVTextEncoderLoader`、`PathchSageAttentionKJ`、`CheckpointLoaderSimple`、`LTXVAudioVAELoader`、`ModelPatchTorchSettings`、`LoraLoaderModelOnly`、`LTX2SamplingPreviewOverride`、`CLIPTextEncode`、`LTX2_NAG`、`LTXVAudioVAEEncode`、`PainterLTX2Vomni`、`LoadAudio`、`VHS_VideoCombine`、`VHS_LoadVideo`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、KSamplerAdvanced、easy seed、LTXVConcatAVLatent、LTXVSeparateAVLatent
