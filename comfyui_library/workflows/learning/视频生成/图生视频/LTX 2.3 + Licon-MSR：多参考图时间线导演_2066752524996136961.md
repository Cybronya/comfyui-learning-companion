---
key: 视频生成/图生视频/LTX 2.3 + Licon-MSR：多参考图时间线导演_2066752524996136961.json
name: LTX 2.3 + Licon-MSR：多参考图时间线导演_2066752524996136961.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2066752524996136961.json
hash: 54236e0a32e4d3c4
coverage: 0.888889
learned_at: 2026-10-15 22:39:52
nodes: [SimpleMath+, UNETLoader, DualCLIPLoader, PreviewImage, VAELoader, LoraLoaderModelOnly, VAELoader, LTX2SamplingPreviewOverride, VAELoaderKJ, easy timelineInfoOutput, PrimitiveBoolean, VHS_VideoCombine, LTXVAudioVAEEncode, SetLatentNoiseMask, SolidMask, easy ifElse, PromptRelaySmartEncode, CLIPTextEncode, KSamplerSelect, ManualSigmas, LTXVConcatAVLatent, LTXVSeparateAVLatent, LTXVAudioVAEDecode, VAEDecodeTiled, LTXVConditioning, SaveVideo, PrimitiveNode, LTXVEmptyLatentAudio, PrimitiveNode, EmptyLTXVLatentVideo, easy timelineSegmentOutput, LTXVAddGuidesFromBatchIndexes, CFGGuider, RandomNoise, easy saveVideo, SaveVideo, easy timelineEditor, easy saveVideo, PathchSageAttentionKJ, LTXVMakeRefVideo, LTXVCropGuides, SamplerCustomAdvanced, easy ifElse, LTXVAddGuidesFromBatchIndexes, PrimitiveBoolean]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 24, "width": 97}
---

# 视频生成/图生视频/LTX 2.3 + Licon-MSR：多参考图时间线导演_2066752524996136961.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2066752524996136961.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Output → Other

**节点**（45 个）：
- `SimpleMath+`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `PreviewImage`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `LTX2SamplingPreviewOverride`
- `VAELoaderKJ`
- `easy timelineInfoOutput`
- `PrimitiveBoolean`
- `VHS_VideoCombine`
- `LTXVAudioVAEEncode` ★核心
- `SetLatentNoiseMask`
- `SolidMask`
- `easy ifElse`
- `PromptRelaySmartEncode`
- `CLIPTextEncode` ★核心
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `VAEDecodeTiled` ★核心
- `LTXVConditioning`
- `SaveVideo`
- `PrimitiveNode`
- `LTXVEmptyLatentAudio` ★核心
- `PrimitiveNode`
- `EmptyLTXVLatentVideo`
- `easy timelineSegmentOutput`
- `LTXVAddGuidesFromBatchIndexes`
- `CFGGuider`
- `RandomNoise`
- `easy saveVideo`
- `SaveVideo`
- `easy timelineEditor`
- `easy saveVideo`
- `PathchSageAttentionKJ`
- `LTXVMakeRefVideo`
- `LTXVCropGuides`
- `SamplerCustomAdvanced` ★核心
- `easy ifElse`
- `LTXVAddGuidesFromBatchIndexes`
- `PrimitiveBoolean`

## 关键参数

- `width` = `97`
- `height` = `24`
- `batch_size` = `1`

## 知识

覆盖率 **89%**（40/45）

**有卡**：`SimpleMath+`、`UNETLoader`、`DualCLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`、`LTX2SamplingPreviewOverride`、`VAELoaderKJ`、`easy timelineInfoOutput`、`PrimitiveBoolean`、`VHS_VideoCombine`、`LTXVAudioVAEEncode`、`SetLatentNoiseMask`、`SolidMask`、`PromptRelaySmartEncode`、`CLIPTextEncode`、`KSamplerSelect`、`ManualSigmas`、`LTXVConcatAVLatent`、`LTXVSeparateAVLatent`、`LTXVAudioVAEDecode`、`VAEDecodeTiled`、`LTXVConditioning`、`SaveVideo`、`LTXVEmptyLatentAudio`、`EmptyLTXVLatentVideo`、`easy timelineSegmentOutput`、`LTXVAddGuidesFromBatchIndexes`、`CFGGuider`、`RandomNoise`、`easy saveVideo`、`easy timelineEditor`、`PathchSageAttentionKJ`、`LTXVMakeRefVideo`、`LTXVCropGuides`、`SamplerCustomAdvanced`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPTextEncode、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVConcatAVLatent
