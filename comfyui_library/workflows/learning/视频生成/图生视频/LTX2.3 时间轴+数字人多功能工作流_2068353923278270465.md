---
key: 视频生成/图生视频/LTX2.3 时间轴+数字人多功能工作流_2068353923278270465.json
name: LTX2.3 时间轴+数字人多功能工作流_2068353923278270465.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3 时间轴+数字人多功能工作流_2068353923278270465.json
hash: 4cfaab61a1a03c26
coverage: 0.530488
learned_at: 2026-10-15 22:40:19
nodes: [SetNode, GetNode, SetNode, SetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, SetNode, SetNode, RandomNoise, SetNode, SetNode, Anything Everywhere, GetNode, SetNode, SetNode, SetNode, ComfyMathExpression, easy indexAnything, GetNode, easy int, Note, Note, StringReplace, easy compare, GetNode, Note, Note, easy promptLine, easy forLoopStart, easy indexAnything, easy forLoopEnd, easy ifElse, easy lengthAnything, SaveVideo, easy ifElse, GetNode, easy ifElse, SetLatentNoiseMask, GetNode, MelBandRoFormerSampler, Note, PathchSageAttentionKJ, LTXVChunkFeedForward, ModelPatchTorchSettings, GetNode, easy timelineInfoOutput, LoadImage, LoadImage, LoraLoaderModelOnly, SetNode, SetNode, easy makeImageList, PrimitiveInt, easy batchAnything, GetNode, easy string, easy forLoopEnd, easy mergeVideosFromPaths, easy forLoopStart, SetNode, easy timelineSegmentCount, MathExpression|pysssss, easy showAnything, SetNode, easy showAnything, GetNode, GetNode, PreviewAny, PrimitiveStringMultiline, Text Concatenate, LTXVAudioVAEEncode, SetNode, SetNode, SetNode, easy timelineSegmentOutput, SetNode, SetNode, GetNode, CFGGuider, GetNode, GetNode, LoadImage, easy showAnything, EmptyLTXVLatentVideo, LTXVImgToVideoInplace, GetNode, ManualSigmas, VAELoader, GetNode, GetNode, LTXVSeparateAVLatent, KSamplerSelect, CFGGuider, KSamplerSelect, easy indexAnything, GetNode, GetNode, GetNode, GetNode, LTXVConcatAVLatent, RandomNoise, GetNode, LTXVConcatAVLatent, SetNode, LTXVEmptyLatentAudio, GetNode, GetNode, MathExpression|pysssss, GetNode, LTXVAudioVAEDecode, GetNode, PrimitiveBoolean, VAELoader, LoadImage, DualCLIPLoader, LatentUpscaleModelLoader, VAEDecodeTiled, easy ifElse, SetNode, SaveVideo, CreateVideo, LTXVCropGuides, LTXVSeparateAVLatent, LTXVCropGuides, LTXVImgToVideoInplace, LTXVLatentUpsamplerTiled, LTXTiledSampler, GetNode, ManualSigmas, SamplerCustomAdvanced, LoraLoaderModelOnly, PromptRelaySmartEncode, LTXVConditioning, CLIPTextEncode, SetNode, LoraLoaderModelOnly, LoraLoaderModelOnly, easy showAnything, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LTXLikenessGuide, LTXLatentAnchorAware, LTXLikenessAnchor, LTXFaceDetector, easy indexAnything, Note, MelBandRoFormerModelLoader, UNETLoader, LoraLoaderModelOnly, MarkdownNote, LTX2_NAG, SolidMask, easy timelineEditor]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 24, "width": 97}
---

# 视频生成/图生视频/LTX2.3 时间轴+数字人多功能工作流_2068353923278270465.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2068353923278270465.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（164 个）：
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `RandomNoise`
- `SetNode`
- `SetNode`
- `Anything Everywhere`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `ComfyMathExpression`
- `easy indexAnything`
- `GetNode`
- `easy int`
- `Note`
- `Note`
- `StringReplace`
- `easy compare`
- `GetNode`
- `Note`
- `Note`
- `easy promptLine`
- `easy forLoopStart`
- `easy indexAnything`
- `easy forLoopEnd`
- `easy ifElse`
- `easy lengthAnything`
- `SaveVideo`
- `easy ifElse`
- `GetNode`
- `easy ifElse`
- `SetLatentNoiseMask`
- `GetNode`
- `MelBandRoFormerSampler` ★核心
- `Note`
- `PathchSageAttentionKJ`
- `LTXVChunkFeedForward`
- `ModelPatchTorchSettings`
- `GetNode`
- `easy timelineInfoOutput`
- `LoadImage`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `SetNode`
- `easy makeImageList`
- `PrimitiveInt`
- `easy batchAnything`
- `GetNode`
- `easy string`
- `easy forLoopEnd`
- `easy mergeVideosFromPaths`
- `easy forLoopStart`
- `SetNode`
- `easy timelineSegmentCount`
- `MathExpression|pysssss`
- `easy showAnything`
- `SetNode`
- `easy showAnything`
- `GetNode`
- `GetNode`
- `PreviewAny`
- `PrimitiveStringMultiline`
- `Text Concatenate`
- `LTXVAudioVAEEncode` ★核心
- `SetNode`
- `SetNode`
- `SetNode`
- `easy timelineSegmentOutput`
- `SetNode`
- `SetNode`
- `GetNode`
- `CFGGuider`
- `GetNode`
- `GetNode`
- `LoadImage`
- `easy showAnything`
- `EmptyLTXVLatentVideo`
- `LTXVImgToVideoInplace`
- `GetNode`
- `ManualSigmas`
- `VAELoader`
- `GetNode`
- `GetNode`
- `LTXVSeparateAVLatent`
- `KSamplerSelect` ★核心
- `CFGGuider`
- `KSamplerSelect` ★核心
- `easy indexAnything`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVConcatAVLatent`
- `RandomNoise`
- `GetNode`
- `LTXVConcatAVLatent`
- `SetNode`
- `LTXVEmptyLatentAudio` ★核心
- `GetNode`
- `GetNode`
- `MathExpression|pysssss`
- `GetNode`
- `LTXVAudioVAEDecode` ★核心
- `GetNode`
- `PrimitiveBoolean`
- `VAELoader`
- `LoadImage`
- `DualCLIPLoader`
- `LatentUpscaleModelLoader`
- `VAEDecodeTiled` ★核心
- `easy ifElse`
- `SetNode`
- `SaveVideo`
- `CreateVideo`
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `LTXVCropGuides`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsamplerTiled` ★核心
- `LTXTiledSampler` ★核心
- `GetNode`
- `ManualSigmas`
- `SamplerCustomAdvanced` ★核心
- `LoraLoaderModelOnly` ★核心
- `PromptRelaySmartEncode`
- `LTXVConditioning`
- `CLIPTextEncode` ★核心
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `easy showAnything`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LTXLikenessGuide`
- `LTXLatentAnchorAware`
- `LTXLikenessAnchor`
- `LTXFaceDetector`
- `easy indexAnything`
- `Note`
- `MelBandRoFormerModelLoader`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `MarkdownNote`
- `LTX2_NAG`
- `SolidMask`
- `easy timelineEditor`

## 关键参数

- `width` = `97`
- `height` = `24`
- `batch_size` = `1`

## 知识

覆盖率 **53%**（87/164）

**有卡**：`RandomNoise`、`ComfyMathExpression`、`easy indexAnything`、`easy int`、`StringReplace`、`easy compare`、`easy promptLine`、`easy forLoopStart`、`easy forLoopEnd`、`easy lengthAnything`、`SaveVideo`、`SetLatentNoiseMask`、`MelBandRoFormerSampler`、`PathchSageAttentionKJ`、`LTXVChunkFeedForward`、`ModelPatchTorchSettings`、`easy timelineInfoOutput`、`LoadImage`、`LoraLoaderModelOnly`、`easy makeImageList`、`easy batchAnything`、`easy string`、`easy mergeVideosFromPaths`、`easy timelineSegmentCount`、`MathExpression|pysssss`、`Text Concatenate`、`LTXVAudioVAEEncode`、`easy timelineSegmentOutput`、`CFGGuider`、`EmptyLTXVLatentVideo`、`LTXVImgToVideoInplace`、`ManualSigmas`、`VAELoader`、`LTXVSeparateAVLatent`、`KSamplerSelect`、`LTXVConcatAVLatent`、`LTXVEmptyLatentAudio`、`LTXVAudioVAEDecode`、`PrimitiveBoolean`、`DualCLIPLoader`、`LatentUpscaleModelLoader`、`VAEDecodeTiled`、`CreateVideo`、`LTXVCropGuides`、`LTXVLatentUpsamplerTiled`、`LTXTiledSampler`、`SamplerCustomAdvanced`、`PromptRelaySmartEncode`、`LTXVConditioning`、`CLIPTextEncode`、`LTXLikenessGuide`、`LTXLatentAnchorAware`、`LTXLikenessAnchor`、`LTXFaceDetector`、`MelBandRoFormerModelLoader`、`UNETLoader`、`LTX2_NAG`、`SolidMask`、`easy timelineEditor`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
