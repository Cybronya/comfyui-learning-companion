---
key: 视频生成/图生视频/LTX2.3全栈式短剧生成V14(Prompt Relay版)_2050042685750300673.json
name: LTX2.3全栈式短剧生成V14(Prompt Relay版)_2050042685750300673.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3全栈式短剧生成V14(Prompt Relay版)_2050042685750300673.json
hash: d22e94d27d505df8
coverage: 0.773585
learned_at: 2026-10-15 22:37:16
nodes: [SetNode, SetNode, KSamplerSelect, BasicScheduler, LTXVConcatAVLatent, easy promptList, easy indexAnything, easy indexAnything, easy indexAnything, easy indexAnything, easy indexAnything, easy promptReplace, easy promptReplace, easy promptReplace, SetNode, GetNode, easy indexAnything, easy indexAnything, easy indexAnything, ImageResizeKJv2, ImageResizeKJv2, ImageResizeKJv2, easy imageRemBg, easy imageRemBg, SetNode, GetNode, LTXVConditioning, LTXVSeparateAVLatent, VAEDecodeTiled, GetNode, GetNode, GetNode, LTXVAudioVAEDecode, LTXVEmptyLatentAudio, ResizeImagesByLongerEdge, ImageAddMulti, easy imageRemBg, GetImagesFromBatchIndexed, LTXVPreprocess, PreviewImage, ImageInvert, EmptyImage, PathchSageAttentionKJ, ModelPatchTorchSettings, LTXVChunkFeedForward, SetNode, ImageBatchMulti, ResizeImageMaskNode, EmptyLTXVLatentVideo, PrimitiveStringMultiline, SetNode, easy promptLine, easy indexAnything, easy indexAnything, easy indexAnything, RegexExtract, easy promptLine, Text Concatenate, easy indexAnything, easy indexAnything, GetNode, RegexExtract, GetNode, easy convertAnything, easy promptLine, SetNode, easy indexAnything, PrimitiveInt, SetNode, ComfyMathExpression, ComfyMathExpression, easy indexAnything, RegexExtract, easy positive, easy positive, easy promptReplace, Text Concatenate, INTConstant, INTConstant, VHS_VideoCombine, GetNode, GetNode, PromptRelayEncode, GetNode, ConditioningZeroOut, LTXAddVideoICLoRAGuideAdvanced, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, VAELoaderKJ, VAELoaderKJ, DualCLIPLoader, SetNode, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, easy positive, LongTextToList, easy positive, PrimitiveInt, GetNode, LTXICLoRALoaderModelOnly, SamplerCustom]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 24, "width": 385}
---

# 视频生成/图生视频/LTX2.3全栈式短剧生成V14(Prompt Relay版)_2050042685750300673.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2050042685750300673.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（106 个）：
- `SetNode`
- `SetNode`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `LTXVConcatAVLatent`
- `easy promptList`
- `easy indexAnything`
- `easy indexAnything`
- `easy indexAnything`
- `easy indexAnything`
- `easy indexAnything`
- `easy promptReplace`
- `easy promptReplace`
- `easy promptReplace`
- `SetNode`
- `GetNode`
- `easy indexAnything`
- `easy indexAnything`
- `easy indexAnything`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `easy imageRemBg`
- `easy imageRemBg`
- `SetNode`
- `GetNode`
- `LTXVConditioning`
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVAudioVAEDecode` ★核心
- `LTXVEmptyLatentAudio` ★核心
- `ResizeImagesByLongerEdge`
- `ImageAddMulti`
- `easy imageRemBg`
- `GetImagesFromBatchIndexed`
- `LTXVPreprocess`
- `PreviewImage`
- `ImageInvert`
- `EmptyImage`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `LTXVChunkFeedForward`
- `SetNode`
- `ImageBatchMulti`
- `ResizeImageMaskNode`
- `EmptyLTXVLatentVideo`
- `PrimitiveStringMultiline`
- `SetNode`
- `easy promptLine`
- `easy indexAnything`
- `easy indexAnything`
- `easy indexAnything`
- `RegexExtract`
- `easy promptLine`
- `Text Concatenate`
- `easy indexAnything`
- `easy indexAnything`
- `GetNode`
- `RegexExtract`
- `GetNode`
- `easy convertAnything`
- `easy promptLine`
- `SetNode`
- `easy indexAnything`
- `PrimitiveInt`
- `SetNode`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `easy indexAnything`
- `RegexExtract`
- `easy positive`
- `easy positive`
- `easy promptReplace`
- `Text Concatenate`
- `INTConstant`
- `INTConstant`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `PromptRelayEncode`
- `GetNode`
- `ConditioningZeroOut`
- `LTXAddVideoICLoRAGuideAdvanced`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `VAELoaderKJ`
- `VAELoaderKJ`
- `DualCLIPLoader`
- `SetNode`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `easy positive`
- `LongTextToList`
- `easy positive`
- `PrimitiveInt`
- `GetNode`
- `LTXICLoRALoaderModelOnly` ★核心
- `SamplerCustom` ★核心

## 关键参数

- `width` = `385`
- `height` = `24`
- `batch_size` = `1`

## 知识

覆盖率 **77%**（82/106）

**有卡**：`KSamplerSelect`、`BasicScheduler`、`LTXVConcatAVLatent`、`easy promptList`、`easy indexAnything`、`easy promptReplace`、`ImageResizeKJv2`、`easy imageRemBg`、`LTXVConditioning`、`LTXVSeparateAVLatent`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`LTXVEmptyLatentAudio`、`ResizeImagesByLongerEdge`、`ImageAddMulti`、`GetImagesFromBatchIndexed`、`LTXVPreprocess`、`ImageInvert`、`EmptyImage`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`LTXVChunkFeedForward`、`ImageBatchMulti`、`ResizeImageMaskNode`、`EmptyLTXVLatentVideo`、`easy promptLine`、`RegexExtract`、`Text Concatenate`、`easy convertAnything`、`ComfyMathExpression`、`easy positive`、`INTConstant`、`VHS_VideoCombine`、`PromptRelayEncode`、`ConditioningZeroOut`、`LTXAddVideoICLoRAGuideAdvanced`、`LoraLoaderModelOnly`、`UNETLoader`、`VAELoaderKJ`、`DualCLIPLoader`、`LoadImage`、`LongTextToList`、`LTXICLoRALoaderModelOnly`、`SamplerCustom`

**用到的条目**：LoraLoaderModelOnly、ConditioningZeroOut、LoadImage、UNETLoader、KSamplerSelect、SamplerCustom、LTXVConcatAVLatent、LTXVSeparateAVLatent
