---
key: 视频生成/图生视频/LTX2.3 多段R2V多图参考循环版，平替即梦Seedance2.0_2064600495154618369.json
name: LTX2.3 多段R2V多图参考循环版，平替即梦Seedance2.0_2064600495154618369.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3 多段R2V多图参考循环版，平替即梦Seedance2.0_2064600495154618369.json
hash: 0baeff9a62a0373c
coverage: 0.8375
learned_at: 2026-10-15 22:39:27
nodes: [UNETLoader, VAELoaderKJ, VAELoader, SimpleMath+, DualCLIPLoader, LTX2SamplingPreviewOverride, easy ifElse, LTXVEmptyLatentAudio, SolidMask, SetLatentNoiseMask, easy int, SimpleMath+, LTXVAudioVAEEncode, easy lengthAnything, easy forLoopStart, easy indexAnything, easy string, easy compare, easy ifElse, easy forLoopEnd, easy forLoopStart, PathchSageAttentionKJ, LoraLoaderModelOnly, easy batchAnything, MarkdownNote, LoraLoaderModelOnly, easy timelineSegmentCount, 1hew_MultiStringJoin, easy mergeVideosFromPaths, easy ifElse, easy promptLine, easy indexAnything, SaveVideo, StringReplace, PreviewAny, PrimitiveStringMultiline, PrimitiveNode, PrimitiveNode, CreateVideo, Any Switch (rgthree), SaveVideo, easy forLoopEnd, VAELoader, SimpleMath+, GetImageRangeFromBatch, SimpleMath+, easy forLoopEnd, easy lengthAnything, easy int, easy lengthAnything, CFGGuider, easy forLoopStart, LTXAddVideoICLoRAGuide, LTXVConditioning, ManualSigmas, SamplerCustomAdvanced, LTXVAudioVAEDecode, KSamplerSelect, easy ifElse, LTXAddVideoICLoRAGuide, easy ifElse, CLIPTextEncode, PromptRelaySmartEncode, SimpleMath+, easy ifElse, LTXVMakeRefVideo, VAEDecodeTiled, LTXVCropGuides, LTXVSeparateAVLatent, easy timelineSegmentOutput, EmptyLTXVLatentVideo, PrimitiveInt, LTXVConcatAVLatent, RandomNoise, PrimitiveBoolean, PrimitiveBoolean, easy timelineInfoOutput, easy saveVideo, easy saveVideo, easy timelineEditor]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 24, "width": 97}
---

# 视频生成/图生视频/LTX2.3 多段R2V多图参考循环版，平替即梦Seedance2.0_2064600495154618369.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2064600495154618369.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（80 个）：
- `UNETLoader` ★核心
- `VAELoaderKJ`
- `VAELoader`
- `SimpleMath+`
- `DualCLIPLoader`
- `LTX2SamplingPreviewOverride`
- `easy ifElse`
- `LTXVEmptyLatentAudio` ★核心
- `SolidMask`
- `SetLatentNoiseMask`
- `easy int`
- `SimpleMath+`
- `LTXVAudioVAEEncode` ★核心
- `easy lengthAnything`
- `easy forLoopStart`
- `easy indexAnything`
- `easy string`
- `easy compare`
- `easy ifElse`
- `easy forLoopEnd`
- `easy forLoopStart`
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `easy batchAnything`
- `MarkdownNote`
- `LoraLoaderModelOnly` ★核心
- `easy timelineSegmentCount`
- `1hew_MultiStringJoin`
- `easy mergeVideosFromPaths`
- `easy ifElse`
- `easy promptLine`
- `easy indexAnything`
- `SaveVideo`
- `StringReplace`
- `PreviewAny`
- `PrimitiveStringMultiline`
- `PrimitiveNode`
- `PrimitiveNode`
- `CreateVideo`
- `Any Switch (rgthree)`
- `SaveVideo`
- `easy forLoopEnd`
- `VAELoader`
- `SimpleMath+`
- `GetImageRangeFromBatch`
- `SimpleMath+`
- `easy forLoopEnd`
- `easy lengthAnything`
- `easy int`
- `easy lengthAnything`
- `CFGGuider`
- `easy forLoopStart`
- `LTXAddVideoICLoRAGuide`
- `LTXVConditioning`
- `ManualSigmas`
- `SamplerCustomAdvanced` ★核心
- `LTXVAudioVAEDecode` ★核心
- `KSamplerSelect` ★核心
- `easy ifElse`
- `LTXAddVideoICLoRAGuide`
- `easy ifElse`
- `CLIPTextEncode` ★核心
- `PromptRelaySmartEncode`
- `SimpleMath+`
- `easy ifElse`
- `LTXVMakeRefVideo`
- `VAEDecodeTiled` ★核心
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `easy timelineSegmentOutput`
- `EmptyLTXVLatentVideo`
- `PrimitiveInt`
- `LTXVConcatAVLatent`
- `RandomNoise`
- `PrimitiveBoolean`
- `PrimitiveBoolean`
- `easy timelineInfoOutput`
- `easy saveVideo`
- `easy saveVideo`
- `easy timelineEditor`

## 关键参数

- `width` = `97`
- `height` = `24`
- `batch_size` = `1`

## 知识

覆盖率 **84%**（67/80）

**有卡**：`UNETLoader`、`VAELoaderKJ`、`VAELoader`、`SimpleMath+`、`DualCLIPLoader`、`LTX2SamplingPreviewOverride`、`LTXVEmptyLatentAudio`、`SolidMask`、`SetLatentNoiseMask`、`easy int`、`LTXVAudioVAEEncode`、`easy lengthAnything`、`easy forLoopStart`、`easy indexAnything`、`easy string`、`easy compare`、`easy forLoopEnd`、`PathchSageAttentionKJ`、`LoraLoaderModelOnly`、`easy batchAnything`、`easy timelineSegmentCount`、`1hew_MultiStringJoin`、`easy mergeVideosFromPaths`、`easy promptLine`、`SaveVideo`、`StringReplace`、`CreateVideo`、`GetImageRangeFromBatch`、`CFGGuider`、`LTXAddVideoICLoRAGuide`、`LTXVConditioning`、`ManualSigmas`、`SamplerCustomAdvanced`、`LTXVAudioVAEDecode`、`KSamplerSelect`、`CLIPTextEncode`、`PromptRelaySmartEncode`、`LTXVMakeRefVideo`、`VAEDecodeTiled`、`LTXVCropGuides`、`LTXVSeparateAVLatent`、`easy timelineSegmentOutput`、`EmptyLTXVLatentVideo`、`LTXVConcatAVLatent`、`RandomNoise`、`PrimitiveBoolean`、`easy timelineInfoOutput`、`easy saveVideo`、`easy timelineEditor`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPTextEncode、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVConcatAVLatent
