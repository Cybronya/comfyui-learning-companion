---
key: 视频生成/图生视频/LTX2.3 多图参考循环版，平替即梦Seedance2.0_2079411679590445058.json
name: LTX2.3 多图参考循环版，平替即梦Seedance2.0_2079411679590445058.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3 多图参考循环版，平替即梦Seedance2.0_2079411679590445058.json
hash: d603e775b1152623
coverage: 0.863636
learned_at: 2026-10-15 22:42:02
nodes: [UNETLoader, VAELoader, VAELoaderKJ, VAELoader, SimpleMath+, LTXVSeparateAVLatent, VAEDecodeTiled, LTXVAudioVAEDecode, DualCLIPLoader, LTX2SamplingPreviewOverride, LTXVConditioning, LTXVCropGuides, SamplerCustomAdvanced, easy ifElse, LTXVEmptyLatentAudio, SolidMask, SetLatentNoiseMask, ManualSigmas, easy int, SimpleMath+, CLIPTextEncode, PromptRelaySmartEncode, LTXVAudioVAEEncode, CFGGuider, EmptyLTXVLatentVideo, easy forLoopEnd, easy lengthAnything, easy forLoopStart, easy indexAnything, easy string, easy compare, easy ifElse, easy forLoopEnd, easy forLoopStart, PathchSageAttentionKJ, LoraLoaderModelOnly, easy timelineSegmentOutput, easy batchAnything, LoraLoaderModelOnly, SimpleMath+, LTXVConcatAVLatent, KSamplerSelect, LTXAddVideoICLoRAGuide, LTXVMakeRefVideo, easy timelineSegmentCount, 1hew_MultiStringJoin, easy mergeVideosFromPaths, easy ifElse, easy promptLine, easy indexAnything, SaveVideo, easy timelineInfoOutput, StringReplace, CreateVideo, PreviewAny, easy saveVideo, PrimitiveStringMultiline, easy saveVideo, PrimitiveNode, PrimitiveNode, RandomNoise, PrimitiveInt, PrimitiveBoolean, MarkdownNote, easy timelineEditor, SaveVideo]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 24, "width": 97}
---

# 视频生成/图生视频/LTX2.3 多图参考循环版，平替即梦Seedance2.0_2079411679590445058.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2079411679590445058.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Output → Other

**节点**（66 个）：
- `UNETLoader` ★核心
- `VAELoader`
- `VAELoaderKJ`
- `VAELoader`
- `SimpleMath+`
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `DualCLIPLoader`
- `LTX2SamplingPreviewOverride`
- `LTXVConditioning`
- `LTXVCropGuides`
- `SamplerCustomAdvanced` ★核心
- `easy ifElse`
- `LTXVEmptyLatentAudio` ★核心
- `SolidMask`
- `SetLatentNoiseMask`
- `ManualSigmas`
- `easy int`
- `SimpleMath+`
- `CLIPTextEncode` ★核心
- `PromptRelaySmartEncode`
- `LTXVAudioVAEEncode` ★核心
- `CFGGuider`
- `EmptyLTXVLatentVideo`
- `easy forLoopEnd`
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
- `easy timelineSegmentOutput`
- `easy batchAnything`
- `LoraLoaderModelOnly` ★核心
- `SimpleMath+`
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `LTXAddVideoICLoRAGuide`
- `LTXVMakeRefVideo`
- `easy timelineSegmentCount`
- `1hew_MultiStringJoin`
- `easy mergeVideosFromPaths`
- `easy ifElse`
- `easy promptLine`
- `easy indexAnything`
- `SaveVideo`
- `easy timelineInfoOutput`
- `StringReplace`
- `CreateVideo`
- `PreviewAny`
- `easy saveVideo`
- `PrimitiveStringMultiline`
- `easy saveVideo`
- `PrimitiveNode`
- `PrimitiveNode`
- `RandomNoise`
- `PrimitiveInt`
- `PrimitiveBoolean`
- `MarkdownNote`
- `easy timelineEditor`
- `SaveVideo`

## 关键参数

- `width` = `97`
- `height` = `24`
- `batch_size` = `1`

## 知识

覆盖率 **86%**（57/66）

**有卡**：`UNETLoader`、`VAELoader`、`VAELoaderKJ`、`SimpleMath+`、`LTXVSeparateAVLatent`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`DualCLIPLoader`、`LTX2SamplingPreviewOverride`、`LTXVConditioning`、`LTXVCropGuides`、`SamplerCustomAdvanced`、`LTXVEmptyLatentAudio`、`SolidMask`、`SetLatentNoiseMask`、`ManualSigmas`、`easy int`、`CLIPTextEncode`、`PromptRelaySmartEncode`、`LTXVAudioVAEEncode`、`CFGGuider`、`EmptyLTXVLatentVideo`、`easy forLoopEnd`、`easy lengthAnything`、`easy forLoopStart`、`easy indexAnything`、`easy string`、`easy compare`、`PathchSageAttentionKJ`、`LoraLoaderModelOnly`、`easy timelineSegmentOutput`、`easy batchAnything`、`LTXVConcatAVLatent`、`KSamplerSelect`、`LTXAddVideoICLoRAGuide`、`LTXVMakeRefVideo`、`easy timelineSegmentCount`、`1hew_MultiStringJoin`、`easy mergeVideosFromPaths`、`easy promptLine`、`SaveVideo`、`easy timelineInfoOutput`、`StringReplace`、`CreateVideo`、`easy saveVideo`、`RandomNoise`、`PrimitiveBoolean`、`easy timelineEditor`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPTextEncode、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVConcatAVLatent
