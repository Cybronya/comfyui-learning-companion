---
key: 视频生成/图生视频/LTX2.3四宫格短剧V2（单采版）_2047854322393817089.json
name: LTX2.3四宫格短剧V2（单采版）_2047854322393817089.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2047854322393817089.json
hash: a2f4cc40be4eca18
coverage: 0.655914
learned_at: 2026-10-15 22:37:07
nodes: [INTConstant, INTConstant, SetNode, SetNode, ImageFromBatch, ResizeImageMaskNode, ResizeImagesByLongerEdge, LTXVPreprocess, ImageFromBatch, ResizeImageMaskNode, ResizeImagesByLongerEdge, LTXVPreprocess, ImageFromBatch, ResizeImageMaskNode, ResizeImagesByLongerEdge, LTXVPreprocess, ImageFromBatch, ResizeImageMaskNode, ResizeImagesByLongerEdge, LTXVPreprocess, easy imageInsetCrop, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, LTXVConcatAVLatent, CFGGuider, BasicScheduler, SamplerCustomAdvanced, GetNode, GetNode, GetNode, LTXVSeparateAVLatent, LTXVCropGuides, GetNode, GetNode, VAEDecodeTiled, LTXVAudioVAEDecode, GetNode, VHS_VideoCombine, LTXVEnhanceAVideoKJ, PreviewImage, RandomNoise, KSamplerSelect, LTXVConditioning, GetNode, LTXVEmptyLatentAudio, EmptyLTXVLatentVideo, GetNode, GetNode, RegexExtract, RegexExtract, RegexExtract, INTConstant, SetNode, INTConstant, SetNode, INTConstant, SetNode, ComfyMathExpression, easy convertAnything, easy convertAnything, easy convertAnything, SetNode, INTConstant, ComfyMathExpression, easy convertAnything, RegexExtract, CLIPTextEncode, easy promptReplace, GetNode, CLIPTextEncode, SetNode, GetNode, easy ifElse, easy ifElse, easy ifElse, EmptyImage, easy mathString, easy mathString, easy mathString, easy mathString, easy mathString, easy indexAnything, easy positive, easy indexAnything, easy positive, easy indexAnything, easy positive, easy indexAnything, easy positive, easy promptConcat, easy promptConcat, easy promptConcat, easy promptConcat, easy positive, easy promptConcat, easy positive, easy ifElse, easy ifElse, easy ifElse, easy ifElse, easy ifElse, easy promptLine, easy indexAnything, easy indexAnything, easy indexAnything, easy indexAnything, easy indexAnything, easy positive, easy indexAnything, PrimitiveStringMultiline, easy promptList, SaveImage, easy showAnything, Text Concatenate, Text Concatenate, Text Concatenate, easy promptConcat, Text Concatenate, ShowText|pysssss, Note, easy ifElse, easy ifElse, easy showAnything, PrimitiveInt, easy imageSplitGrid, easy ifElse, PrimitiveFloat, Comfly_api_set, SetNode, SetNode, SetNode, PathchSageAttentionKJ, ModelPatchTorchSettings, LTXVChunkFeedForward, SetNode, VAELoaderKJ, DualCLIPLoader, VAELoaderKJ, LatentUpscaleModelLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, SetNode, SetNode, UNETLoader, GetNode, GetNode, easy positive, LongTextToList, easy positive, easy positive, easy positive, easy positive, easy positive, easy positive, SetNode, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, SetNode, Comfly_gpt_image_2_official, GetNode, PrimitiveBoolean, LoadImage, LongTextToList, SetNode, easy positive, PrimitiveInt, ShowText|pysssss, Fast Groups Bypasser (rgthree), GetNode, GetNode, GetNode, GetNode, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, LTXVAddGuideMulti]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 24, "width": 97}
---

# 视频生成/图生视频/LTX2.3四宫格短剧V2（单采版）_2047854322393817089.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2047854322393817089.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（186 个）：
- `INTConstant`
- `INTConstant`
- `SetNode`
- `SetNode`
- `ImageFromBatch`
- `ResizeImageMaskNode`
- `ResizeImagesByLongerEdge`
- `LTXVPreprocess`
- `ImageFromBatch`
- `ResizeImageMaskNode`
- `ResizeImagesByLongerEdge`
- `LTXVPreprocess`
- `ImageFromBatch`
- `ResizeImageMaskNode`
- `ResizeImagesByLongerEdge`
- `LTXVPreprocess`
- `ImageFromBatch`
- `ResizeImageMaskNode`
- `ResizeImagesByLongerEdge`
- `LTXVPreprocess`
- `easy imageInsetCrop`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVConcatAVLatent`
- `CFGGuider`
- `BasicScheduler`
- `SamplerCustomAdvanced` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVSeparateAVLatent`
- `LTXVCropGuides`
- `GetNode`
- `GetNode`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `GetNode`
- `VHS_VideoCombine`
- `LTXVEnhanceAVideoKJ`
- `PreviewImage`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `LTXVConditioning`
- `GetNode`
- `LTXVEmptyLatentAudio` ★核心
- `EmptyLTXVLatentVideo`
- `GetNode`
- `GetNode`
- `RegexExtract`
- `RegexExtract`
- `RegexExtract`
- `INTConstant`
- `SetNode`
- `INTConstant`
- `SetNode`
- `INTConstant`
- `SetNode`
- `ComfyMathExpression`
- `easy convertAnything`
- `easy convertAnything`
- `easy convertAnything`
- `SetNode`
- `INTConstant`
- `ComfyMathExpression`
- `easy convertAnything`
- `RegexExtract`
- `CLIPTextEncode` ★核心
- `easy promptReplace`
- `GetNode`
- `CLIPTextEncode` ★核心
- `SetNode`
- `GetNode`
- `easy ifElse`
- `easy ifElse`
- `easy ifElse`
- `EmptyImage`
- `easy mathString`
- `easy mathString`
- `easy mathString`
- `easy mathString`
- `easy mathString`
- `easy indexAnything`
- `easy positive`
- `easy indexAnything`
- `easy positive`
- `easy indexAnything`
- `easy positive`
- `easy indexAnything`
- `easy positive`
- `easy promptConcat`
- `easy promptConcat`
- `easy promptConcat`
- `easy promptConcat`
- `easy positive`
- `easy promptConcat`
- `easy positive`
- `easy ifElse`
- `easy ifElse`
- `easy ifElse`
- `easy ifElse`
- `easy ifElse`
- `easy promptLine`
- `easy indexAnything`
- `easy indexAnything`
- `easy indexAnything`
- `easy indexAnything`
- `easy indexAnything`
- `easy positive`
- `easy indexAnything`
- `PrimitiveStringMultiline`
- `easy promptList`
- `SaveImage`
- `easy showAnything`
- `Text Concatenate`
- `Text Concatenate`
- `Text Concatenate`
- `easy promptConcat`
- `Text Concatenate`
- `ShowText|pysssss`
- `Note`
- `easy ifElse`
- `easy ifElse`
- `easy showAnything`
- `PrimitiveInt`
- `easy imageSplitGrid`
- `easy ifElse`
- `PrimitiveFloat`
- `Comfly_api_set`
- `SetNode`
- `SetNode`
- `SetNode`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `LTXVChunkFeedForward`
- `SetNode`
- `VAELoaderKJ`
- `DualCLIPLoader`
- `VAELoaderKJ`
- `LatentUpscaleModelLoader`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `SetNode`
- `UNETLoader` ★核心
- `GetNode`
- `GetNode`
- `easy positive`
- `LongTextToList`
- `easy positive`
- `easy positive`
- `easy positive`
- `easy positive`
- `easy positive`
- `easy positive`
- `SetNode`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `SetNode`
- `Comfly_gpt_image_2_official`
- `GetNode`
- `PrimitiveBoolean`
- `LoadImage`
- `LongTextToList`
- `SetNode`
- `easy positive`
- `PrimitiveInt`
- `ShowText|pysssss`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `LTXVAddGuideMulti`

## 关键参数

- `width` = `97`
- `height` = `24`
- `batch_size` = `1`

## 知识

覆盖率 **66%**（122/186）

**有卡**：`INTConstant`、`ImageFromBatch`、`ResizeImageMaskNode`、`ResizeImagesByLongerEdge`、`LTXVPreprocess`、`easy imageInsetCrop`、`LTXVConcatAVLatent`、`CFGGuider`、`BasicScheduler`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`LTXVCropGuides`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`VHS_VideoCombine`、`LTXVEnhanceAVideoKJ`、`RandomNoise`、`KSamplerSelect`、`LTXVConditioning`、`LTXVEmptyLatentAudio`、`EmptyLTXVLatentVideo`、`RegexExtract`、`ComfyMathExpression`、`easy convertAnything`、`CLIPTextEncode`、`easy promptReplace`、`EmptyImage`、`easy mathString`、`easy indexAnything`、`easy positive`、`easy promptConcat`、`easy promptLine`、`easy promptList`、`SaveImage`、`Text Concatenate`、`easy imageSplitGrid`、`Comfly_api_set`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`LTXVChunkFeedForward`、`VAELoaderKJ`、`DualCLIPLoader`、`LatentUpscaleModelLoader`、`LoraLoaderModelOnly`、`UNETLoader`、`LongTextToList`、`LoadImage`、`Comfly_gpt_image_2_official`、`PrimitiveBoolean`、`LTXVAddGuideMulti`

**用到的条目**：LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVConcatAVLatent
