---
key: 视频生成/文生视频/Bernini+Ltx2.3+PR导演短剧分镜台 多参考 对话时序控制 分镜扩展_2076389200764694530.json
name: Bernini+Ltx2.3+PR导演短剧分镜台 多参考 对话时序控制 分镜扩展_2076389200764694530
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Bernini+Ltx2.3+PR导演短剧分镜台 多参考 对话时序控制 分镜扩展_2076389200764694530.json
hash: 24ce32d332671464
coverage: 0.578125
learned_at: 2026-10-15 22:44:04
nodes: [SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, LTX2AttentionTunerPatch, GetNode, SetNode, GetNode, GetNode, VAELoader, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, LTXVConcatAVLatent, GetNode, GetNode, LTXVCropGuides, GetNode, SetNode, SetNode, CFGGuider, ManualSigmas, RandomNoise, GetNode, GetNode, GetNode, PathchSageAttentionKJ, LTXVSetAudioRefTokens, LTXVCropGuides, LTXVLatentUpsampler, LatentUpscaleModelLoader, DualCLIPLoader, VAELoaderKJ, VAELoader, PrimitiveStringMultiline, GetNode, LTXVSeparateAVLatent, GetNode, VAEDecodeTiled, LTXVAudioVAEDecode, GetNode, SetNode, VAEDecode, CLIPTextEncode, VAELoader, Reroute, CreateVideo, LTXVSeparateAVLatent, SetNode, GetNode, GetNode, ComfyMathExpression, SetNode, SetNode, SetNode, SetNode, CLIPTextEncode, LTXVAudioVAEDecode, VAEDecodeTiled, easy batchAnything, RandomNoise, GetNode, GetNode, LTXVPreprocess, SetNode, LazySwitchKJ, GetImageSizeAndCount, SetNode, SetNode, LoraLoaderModelOnly, KSamplerSelect, ResizeImagesByLongerEdge, GetNode, ComfyMathExpression, SetNode, GetNode, SetNode, SetNode, GetImageRangeFromBatch, easy cleanGpuUsed, MathExpression|pysssss, VHS_GetImageCount, SimpleCalculatorKJ, GetVideoComponents, ImageScaleToTotalPixels, easy batchAnything, GetNode, CreateVideo, easy forLoopStart, easy showAnything, easy imagesSplitImage, ComfySwitchNode, SetNode, PrimitiveFloat, SetNode, SetNode, INTConstant, PrimitiveBoolean, EmptyAudio, SetNode, GetNode, BatchImagesNode, BerniniPromptEnhancer, Remove Text, UNETLoader, PathchSageAttentionKJ, PathchSageAttentionKJ, LoraLoaderModelOnly, LoraLoaderModelOnly, StringReplace, StringReplace, EmptyAudio, StringReplace, SaveVideo, UNETLoader, PreviewAny, UNETLoader, KSamplerSelect, LTXVChunkFeedForward, SetNode, AudioConcat, easy forLoopEnd, PreviewAny, TTP_text_mix, RH_LLMAPI_NODE, easy timelineSegmentCount, KSamplerAdvanced, KSamplerAdvanced, Remove Text, BerniniConditioning, GetNode, VAEEncode, GetNode, SetNode, GetNode, ComfyMathExpression, SetNode, GetImageSizeAndCount, ResizeImageMaskNode, GetImageSizeAndCount, ResizeImageMaskNode, Reroute, Reroute, Reroute, Reroute, Reroute, Bool, SamplerCustomAdvanced, LTX2_NAG, GetNode, BasicScheduler, GetNode, LTXVEmptyLatentAudio, EmptyLTXVLatentVideo, SetNode, SetNode, LoraLoaderModelOnly, SetNode, VAELoader, MathExpression|pysssss, MathExpression|pysssss, MaxNode, TextInput_, CLIPLoader, TTP_text_mix, PromptRelayEncode, ConditioningZeroOut, EmptyHunyuanLatentVideo, GetNode, Reroute, GetNode, CLIPTextEncode, Reroute, CLIPTextEncode, Reroute, TextGenerateLTX2Prompt, GetNode, StringConcatenate, GetNode, GetNode, LTXAddVideoICLoRAGuide, CFGGuider, GetNode, ConditioningZeroOut, ComfySwitchNode, Reroute, PreviewAny, LTXVConditioning, GetImageRangeFromBatch, SetNode, easy showAnything, LTXAddVideoICLoRAGuide, Reroute, SetNode, Reroute, SamplerCustomAdvanced, Any To Any, GetImageSize, SimpleCalculatorKJ, VHS_VideoCombine, StringReplace, Remove Text, CR Prompt Text, VHS_SelectFilename, Qwen3_VQA, PreviewAny, easy timelineSegmentOutput, VHS_VideoCombine, VHS_VideoCombine, PromptRelayEncode, VHS_VideoCombine, SaveVideo, Note, LTXAddVideoICLoRAGuide, LoraLoaderModelOnly, GetNode, GetImageSizeAndCount, ResizeImageMaskNode, GetNode, LTXVEmptyLatentAudio, LTXVConcatAVLatent, LTXVAddLatentGuide, GetImageSizeAndCount, ComfyMathExpression, ComfyMathExpression, LTXVAudioVideoMask, SetNode, ResizeImagesByLongerEdge, INTConstant, LTXVSetAudioRefTokens, PromptRelayEncode, ImageResizeKJv2, SetNode, LTX2SamplingPreviewOverride, LoraLoaderModelOnly, LoraLoaderModelOnly, TextInput_, PreviewAudio, PreviewImage, easy timelineEditor, PreviewAny, easy timelineInfoOutput]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 10, "denoise": "simple", "height": 25, "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "randomize", "width": 97}
---

# 视频生成/文生视频/Bernini+Ltx2.3+PR导演短剧分镜台 多参考 对话时序控制 分镜扩展_2076389200764694530.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Bernini+Ltx2.3+PR导演短剧分镜台 多参考 对话时序控制 分镜扩展_2076389200764694530.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（256 个）：
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTX2AttentionTunerPatch`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `VAELoader`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVConcatAVLatent`
- `GetNode`
- `GetNode`
- `LTXVCropGuides`
- `GetNode`
- `SetNode`
- `SetNode`
- `CFGGuider`
- `ManualSigmas`
- `RandomNoise`
- `GetNode`
- `GetNode`
- `GetNode`
- `PathchSageAttentionKJ`
- `LTXVSetAudioRefTokens`
- `LTXVCropGuides`
- `LTXVLatentUpsampler` ★核心
- `LatentUpscaleModelLoader`
- `DualCLIPLoader`
- `VAELoaderKJ`
- `VAELoader`
- `PrimitiveStringMultiline`
- `GetNode`
- `LTXVSeparateAVLatent`
- `GetNode`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `GetNode`
- `SetNode`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `VAELoader`
- `Reroute`
- `CreateVideo`
- `LTXVSeparateAVLatent`
- `SetNode`
- `GetNode`
- `GetNode`
- `ComfyMathExpression`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `CLIPTextEncode` ★核心
- `LTXVAudioVAEDecode` ★核心
- `VAEDecodeTiled` ★核心
- `easy batchAnything`
- `RandomNoise`
- `GetNode`
- `GetNode`
- `LTXVPreprocess`
- `SetNode`
- `LazySwitchKJ`
- `GetImageSizeAndCount`
- `SetNode`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `KSamplerSelect` ★核心
- `ResizeImagesByLongerEdge`
- `GetNode`
- `ComfyMathExpression`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetImageRangeFromBatch`
- `easy cleanGpuUsed`
- `MathExpression|pysssss`
- `VHS_GetImageCount`
- `SimpleCalculatorKJ`
- `GetVideoComponents`
- `ImageScaleToTotalPixels`
- `easy batchAnything`
- `GetNode`
- `CreateVideo`
- `easy forLoopStart`
- `easy showAnything`
- `easy imagesSplitImage`
- `ComfySwitchNode`
- `SetNode`
- `PrimitiveFloat`
- `SetNode`
- `SetNode`
- `INTConstant`
- `PrimitiveBoolean`
- `EmptyAudio`
- `SetNode`
- `GetNode`
- `BatchImagesNode`
- `BerniniPromptEnhancer`
- `Remove Text`
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `StringReplace`
- `StringReplace`
- `EmptyAudio`
- `StringReplace`
- `SaveVideo`
- `UNETLoader` ★核心
- `PreviewAny`
- `UNETLoader` ★核心
- `KSamplerSelect` ★核心
- `LTXVChunkFeedForward`
- `SetNode`
- `AudioConcat`
- `easy forLoopEnd`
- `PreviewAny`
- `TTP_text_mix`
- `RH_LLMAPI_NODE`
- `easy timelineSegmentCount`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `Remove Text`
- `BerniniConditioning`
- `GetNode`
- `VAEEncode` ★核心
- `GetNode`
- `SetNode`
- `GetNode`
- `ComfyMathExpression`
- `SetNode`
- `GetImageSizeAndCount`
- `ResizeImageMaskNode`
- `GetImageSizeAndCount`
- `ResizeImageMaskNode`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Bool`
- `SamplerCustomAdvanced` ★核心
- `LTX2_NAG`
- `GetNode`
- `BasicScheduler`
- `GetNode`
- `LTXVEmptyLatentAudio` ★核心
- `EmptyLTXVLatentVideo`
- `SetNode`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `VAELoader`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `MaxNode`
- `TextInput_`
- `CLIPLoader`
- `TTP_text_mix`
- `PromptRelayEncode`
- `ConditioningZeroOut`
- `EmptyHunyuanLatentVideo`
- `GetNode`
- `Reroute`
- `GetNode`
- `CLIPTextEncode` ★核心
- `Reroute`
- `CLIPTextEncode` ★核心
- `Reroute`
- `TextGenerateLTX2Prompt`
- `GetNode`
- `StringConcatenate`
- `GetNode`
- `GetNode`
- `LTXAddVideoICLoRAGuide`
- `CFGGuider`
- `GetNode`
- `ConditioningZeroOut`
- `ComfySwitchNode`
- `Reroute`
- `PreviewAny`
- `LTXVConditioning`
- `GetImageRangeFromBatch`
- `SetNode`
- `easy showAnything`
- `LTXAddVideoICLoRAGuide`
- `Reroute`
- `SetNode`
- `Reroute`
- `SamplerCustomAdvanced` ★核心
- `Any To Any`
- `GetImageSize`
- `SimpleCalculatorKJ`
- `VHS_VideoCombine`
- `StringReplace`
- `Remove Text`
- `CR Prompt Text`
- `VHS_SelectFilename`
- `Qwen3_VQA`
- `PreviewAny`
- `easy timelineSegmentOutput`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `PromptRelayEncode`
- `VHS_VideoCombine`
- `SaveVideo`
- `Note`
- `LTXAddVideoICLoRAGuide`
- `LoraLoaderModelOnly` ★核心
- `GetNode`
- `GetImageSizeAndCount`
- `ResizeImageMaskNode`
- `GetNode`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVConcatAVLatent`
- `LTXVAddLatentGuide`
- `GetImageSizeAndCount`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `LTXVAudioVideoMask`
- `SetNode`
- `ResizeImagesByLongerEdge`
- `INTConstant`
- `LTXVSetAudioRefTokens`
- `PromptRelayEncode`
- `ImageResizeKJv2`
- `SetNode`
- `LTX2SamplingPreviewOverride`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `TextInput_`
- `PreviewAudio`
- `PreviewImage`
- `easy timelineEditor`
- `PreviewAny`
- `easy timelineInfoOutput`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `10`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`
- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **58%**（148/256）

**有卡**：`LTX2AttentionTunerPatch`、`VAELoader`、`LTXVConcatAVLatent`、`LTXVCropGuides`、`CFGGuider`、`ManualSigmas`、`RandomNoise`、`PathchSageAttentionKJ`、`LTXVSetAudioRefTokens`、`LTXVLatentUpsampler`、`LatentUpscaleModelLoader`、`DualCLIPLoader`、`VAELoaderKJ`、`LTXVSeparateAVLatent`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`VAEDecode`、`CLIPTextEncode`、`CreateVideo`、`ComfyMathExpression`、`easy batchAnything`、`LTXVPreprocess`、`LazySwitchKJ`、`GetImageSizeAndCount`、`LoraLoaderModelOnly`、`KSamplerSelect`、`ResizeImagesByLongerEdge`、`GetImageRangeFromBatch`、`easy cleanGpuUsed`、`MathExpression|pysssss`、`VHS_GetImageCount`、`SimpleCalculatorKJ`、`GetVideoComponents`、`ImageScaleToTotalPixels`、`easy forLoopStart`、`easy imagesSplitImage`、`INTConstant`、`PrimitiveBoolean`、`EmptyAudio`、`BatchImagesNode`、`BerniniPromptEnhancer`、`Remove Text`、`UNETLoader`、`StringReplace`、`SaveVideo`、`LTXVChunkFeedForward`、`AudioConcat`、`easy forLoopEnd`、`TTP_text_mix`、`RH_LLMAPI_NODE`、`easy timelineSegmentCount`、`KSamplerAdvanced`、`BerniniConditioning`、`VAEEncode`、`ResizeImageMaskNode`、`Bool`、`SamplerCustomAdvanced`、`LTX2_NAG`、`BasicScheduler`、`LTXVEmptyLatentAudio`、`EmptyLTXVLatentVideo`、`MaxNode`、`TextInput_`、`CLIPLoader`、`PromptRelayEncode`、`ConditioningZeroOut`、`EmptyHunyuanLatentVideo`、`TextGenerateLTX2Prompt`、`StringConcatenate`、`LTXAddVideoICLoRAGuide`、`LTXVConditioning`、`Any To Any`、`GetImageSize`、`VHS_VideoCombine`、`CR Prompt Text`、`VHS_SelectFilename`、`Qwen3_VQA`、`easy timelineSegmentOutput`、`LTXVAddLatentGuide`、`LTXVAudioVideoMask`、`ImageResizeKJv2`、`LTX2SamplingPreviewOverride`、`PreviewAudio`、`easy timelineEditor`、`easy timelineInfoOutput`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、UNETLoader、CFGGuider
