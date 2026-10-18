---
key: 视频生成/图生视频/for循环--qwen_edit_2509换背景+LTX2.3短剧----微改侃侃的抹布大佬的工作流_2050399637667885057.json
name: for循环--qwen_edit_2509换背景+LTX2.3短剧----微改侃侃的抹布大佬的工作流_2050399637667885057.json
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/for循环--qwen_edit_2509换背景+LTX2.3短剧----微改侃侃的抹布大佬的工作流_2050399637667885057.json
hash: 8bf888c943986f9a
coverage: 0.774194
learned_at: 2026-10-15 22:37:18
nodes: [SetNode, SetNode, KSamplerSelect, BasicScheduler, LTXVConcatAVLatent, easy promptList, easy indexAnything, easy indexAnything, easy indexAnything, easy indexAnything, easy indexAnything, ImageResizeKJv2, ImageResizeKJv2, ImageResizeKJv2, easy imageRemBg, easy imageRemBg, GetNode, LTXVConditioning, LTXVSeparateAVLatent, GetNode, LTXVEmptyLatentAudio, ResizeImagesByLongerEdge, easy imageRemBg, GetImagesFromBatchIndexed, LTXVPreprocess, PreviewImage, ImageInvert, EmptyImage, PathchSageAttentionKJ, ModelPatchTorchSettings, LTXVChunkFeedForward, SetNode, ImageBatchMulti, EmptyLTXVLatentVideo, PrimitiveStringMultiline, SetNode, easy indexAnything, GetNode, GetNode, easy promptLine, easy indexAnything, PrimitiveInt, SetNode, ComfyMathExpression, ComfyMathExpression, GetNode, GetNode, GetNode, ConditioningZeroOut, LTXAddVideoICLoRAGuideAdvanced, LoraLoaderModelOnly, UNETLoader, VAELoaderKJ, VAELoaderKJ, DualCLIPLoader, SetNode, LoadImage, LoadImage, LoadImage, LTXICLoRALoaderModelOnly, SamplerCustom, PathchSageAttentionKJ, LoraLoaderModelOnly, LayerMask: RmBgUltra V2, UNETLoader, KSampler, GetNode, Anything Everywhere3, ModelSamplingAuraFlow, CLIPLoader, ConditioningZeroOut, RegexExtract, easy promptReplace, easy indexAnything, easy indexAnything, easy indexAnything, VAEEncode, PreviewImage, PreviewImage, ImageResize+, AIO_Preprocessor, MuyeTextEditOutput, GetNode, VAELoader, Text Concatenate, TextEncodeQwenImageEditPlus, easy promptReplace, easy promptReplace, easy promptLine, SetNode, SetNode, easy promptReplace, easy convertAnything, SetNode, RegexExtract, easy promptReplace, easy showAnything, VHS_VideoCombine, UpscaleModelLoader, ImageUpscaleWithModel, PrimitiveInt, LongTextToList, easy positive, RegexExtract, easy forLoopEnd, easy batchAnything, GetNode, LTXVAudioVAEDecode, VAEDecodeTiled, VHS_VideoCombine, GetNode, easy positive, LoraLoaderModelOnly, LoraLoaderModelOnly, VHS_SelectImages, SetNode, LongTextToList, easy positive, RegexExtract, easy positive, GetNode, easy promptLine, easy indexAnything, easy indexAnything, easy indexAnything, easy indexAnything, easy indexAnything, PromptRelayEncode, Text Concatenate, easy promptReplace, easy showAnything, Text Concatenate, ShowText|pysssss, easy positive, VHS_VideoCombine, INTConstant, LoadImage, LoadImage, easy forLoopStart, AudioConcat, If ANY execute A else B, easy isNone, EmptyAudio, ShowText|pysssss, MuyeTextEditOutput, PreviewImage, Reroute, ImageAddMulti, VAEDecode, INTConstant, INTConstant, ImageScale, ACE_AnyInputToAny, ACE_AnyInputToAny, ResizeImageMaskNode]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 0.96, "denoise": 1, "height": 24, "sampler_name": "euler", "scheduler": "sgm_uniform", "seed": 374530654004369, "steps": 8, "width": 385}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/for循环--qwen_edit_2509换背景+LTX2.3短剧----微改侃侃的抹布大佬的工作流_2050399637667885057.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2050399637667885057.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（155 个）：
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
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `easy imageRemBg`
- `easy imageRemBg`
- `GetNode`
- `LTXVConditioning`
- `LTXVSeparateAVLatent`
- `GetNode`
- `LTXVEmptyLatentAudio` ★核心
- `ResizeImagesByLongerEdge`
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
- `EmptyLTXVLatentVideo`
- `PrimitiveStringMultiline`
- `SetNode`
- `easy indexAnything`
- `GetNode`
- `GetNode`
- `easy promptLine`
- `easy indexAnything`
- `PrimitiveInt`
- `SetNode`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `GetNode`
- `GetNode`
- `GetNode`
- `ConditioningZeroOut`
- `LTXAddVideoICLoRAGuideAdvanced`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `VAELoaderKJ`
- `VAELoaderKJ`
- `DualCLIPLoader`
- `SetNode`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LTXICLoRALoaderModelOnly` ★核心
- `SamplerCustom` ★核心
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `LayerMask: RmBgUltra V2`
- `UNETLoader` ★核心
- `KSampler` ★核心
- `GetNode`
- `Anything Everywhere3`
- `ModelSamplingAuraFlow`
- `CLIPLoader`
- `ConditioningZeroOut`
- `RegexExtract`
- `easy promptReplace`
- `easy indexAnything`
- `easy indexAnything`
- `easy indexAnything`
- `VAEEncode` ★核心
- `PreviewImage`
- `PreviewImage`
- `ImageResize+`
- `AIO_Preprocessor`
- `MuyeTextEditOutput`
- `GetNode`
- `VAELoader`
- `Text Concatenate`
- `TextEncodeQwenImageEditPlus`
- `easy promptReplace`
- `easy promptReplace`
- `easy promptLine`
- `SetNode`
- `SetNode`
- `easy promptReplace`
- `easy convertAnything`
- `SetNode`
- `RegexExtract`
- `easy promptReplace`
- `easy showAnything`
- `VHS_VideoCombine`
- `UpscaleModelLoader`
- `ImageUpscaleWithModel`
- `PrimitiveInt`
- `LongTextToList`
- `easy positive`
- `RegexExtract`
- `easy forLoopEnd`
- `easy batchAnything`
- `GetNode`
- `LTXVAudioVAEDecode` ★核心
- `VAEDecodeTiled` ★核心
- `VHS_VideoCombine`
- `GetNode`
- `easy positive`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `VHS_SelectImages`
- `SetNode`
- `LongTextToList`
- `easy positive`
- `RegexExtract`
- `easy positive`
- `GetNode`
- `easy promptLine`
- `easy indexAnything`
- `easy indexAnything`
- `easy indexAnything`
- `easy indexAnything`
- `easy indexAnything`
- `PromptRelayEncode`
- `Text Concatenate`
- `easy promptReplace`
- `easy showAnything`
- `Text Concatenate`
- `ShowText|pysssss`
- `easy positive`
- `VHS_VideoCombine`
- `INTConstant`
- `LoadImage`
- `LoadImage`
- `easy forLoopStart`
- `AudioConcat`
- `If ANY execute A else B`
- `easy isNone`
- `EmptyAudio`
- `ShowText|pysssss`
- `MuyeTextEditOutput`
- `PreviewImage`
- `Reroute`
- `ImageAddMulti`
- `VAEDecode` ★核心
- `INTConstant`
- `INTConstant`
- `ImageScale`
- `ACE_AnyInputToAny`
- `ACE_AnyInputToAny`
- `ResizeImageMaskNode`

**识别到的模式**：image_to_image

## 关键参数

- `width` = `385`
- `height` = `24`
- `batch_size` = `1`
- `seed` = `374530654004369`
- `steps` = `8`
- `cfg` = `0.96`
- `sampler_name` = `euler`
- `scheduler` = `sgm_uniform`
- `denoise` = `1`

## 知识

覆盖率 **77%**（120/155）

**有卡**：`KSamplerSelect`、`BasicScheduler`、`LTXVConcatAVLatent`、`easy promptList`、`easy indexAnything`、`ImageResizeKJv2`、`easy imageRemBg`、`LTXVConditioning`、`LTXVSeparateAVLatent`、`LTXVEmptyLatentAudio`、`ResizeImagesByLongerEdge`、`GetImagesFromBatchIndexed`、`LTXVPreprocess`、`ImageInvert`、`EmptyImage`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`LTXVChunkFeedForward`、`ImageBatchMulti`、`EmptyLTXVLatentVideo`、`easy promptLine`、`ComfyMathExpression`、`ConditioningZeroOut`、`LTXAddVideoICLoRAGuideAdvanced`、`LoraLoaderModelOnly`、`UNETLoader`、`VAELoaderKJ`、`DualCLIPLoader`、`LoadImage`、`LTXICLoRALoaderModelOnly`、`SamplerCustom`、`LayerMask: RmBgUltra V2`、`KSampler`、`ModelSamplingAuraFlow`、`CLIPLoader`、`RegexExtract`、`easy promptReplace`、`VAEEncode`、`ImageResize+`、`AIO_Preprocessor`、`MuyeTextEditOutput`、`VAELoader`、`Text Concatenate`、`TextEncodeQwenImageEditPlus`、`easy convertAnything`、`VHS_VideoCombine`、`UpscaleModelLoader`、`ImageUpscaleWithModel`、`LongTextToList`、`easy positive`、`easy forLoopEnd`、`easy batchAnything`、`LTXVAudioVAEDecode`、`VAEDecodeTiled`、`VHS_SelectImages`、`PromptRelayEncode`、`INTConstant`、`easy forLoopStart`、`AudioConcat`、`If ANY execute A else B`、`easy isNone`、`EmptyAudio`、`ImageAddMulti`、`VAEDecode`、`ImageScale`、`ACE_AnyInputToAny`、`ResizeImageMaskNode`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
