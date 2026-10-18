---
key: 视频生成/图生视频/Bernini+Ltx2.3导演分镜编辑全模态视频_2067515281458688002.json
name: Bernini+Ltx2.3导演分镜编辑全模态视频_2067515281458688002.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Bernini+Ltx2.3导演分镜编辑全模态视频_2067515281458688002.json
hash: c51f658f46ed772f
coverage: 0.567944
learned_at: 2026-10-15 22:40:03
nodes: [SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, KSamplerSelect, SetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, VAELoader, SetNode, Reroute, GetNode, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, LTXVConcatAVLatent, GetNode, GetNode, LTXVCropGuides, GetNode, GetNode, SetNode, SetNode, CFGGuider, ManualSigmas, RandomNoise, LTXAddVideoICLoRAGuide, GetNode, GetNode, GetNode, PathchSageAttentionKJ, LTXVSetAudioRefTokens, LTXVCropGuides, LTXVLatentUpsampler, SamplerCustomAdvanced, LatentUpscaleModelLoader, DualCLIPLoader, VAELoader, VAELoaderKJ, VAELoader, PrimitiveStringMultiline, TextGenerateLTX2Prompt, GetNode, CFGGuider, LTXVConditioning, CLIPTextEncode, StringConcatenate, GetNode, BasicScheduler, GetNode, LTXVSeparateAVLatent, GetNode, VAEDecodeTiled, LTXVAudioVAEDecode, GetNode, CLIPTextEncode, SetNode, GetNode, VAEDecode, CLIPTextEncode, CLIPLoader, VAELoader, Reroute, CreateVideo, LTXVSeparateAVLatent, EmptyLTXVLatentVideo, SetNode, ComfySwitchNode, GetNode, GetNode, GetNode, ComfyMathExpression, SamplerCustomAdvanced, GetImageSizeAndCount, GetImageSizeAndCount, SetNode, SetNode, SetNode, SetNode, ComfyMathExpression, SetNode, SetNode, ResizeImageMaskNode, ResizeImageMaskNode, CLIPTextEncode, GetNode, LTXVAudioVAEDecode, VAEDecodeTiled, easy batchAnything, LTX2_NAG, LTXVEmptyLatentAudio, RandomNoise, LTXVAudioVAEEncode, GetNode, GetNode, GetNode, GetNode, ManualSigmas, GetNode, SetNode, GetNode, LTXVPreprocess, SetNode, GetNode, LTXVConcatAVLatent, ModelSamplingSD3, CFGGuider, BasicScheduler, LazySwitchKJ, GetNode, GetNode, GetImageSizeAndCount, SetNode, GetNode, SetNode, CLIPTextEncode, CLIPTextEncode, RandomNoise, SetNode, SetNode, UNETLoader, LoraLoaderModelOnly, LTXVChunkFeedForward, LTX2SamplingPreviewOverride, GetNode, GetNode, SetNode, Reroute, SamplerCustomAdvanced, LTXVConcatAVLatent, LTXVSetAudioRefTokens, SetNode, PreviewAny, LTX2SamplingPreviewOverride, GetNode, SetNode, LTXVConditioning, LTX2_NAG, GetImageRangeFromBatch, VAEEncode, LTXVAddLatentGuide, SetNode, SetNode, KSamplerSelect, CLIPTextEncode, KSamplerSelect, ResizeImagesByLongerEdge, MarkdownNote, VAEEncode, GetNode, ComfyMathExpression, ComfyMathExpression, GetImageSizeAndCount, LTXVEmptyLatentAudio, GetNode, ComfyMathExpression, SetNode, GetNode, GetImageSizeAndCount, GetNode, GetNode, SetNode, SetNode, ResizeImagesByLongerEdge, GetImageRangeFromBatch, PrimitiveStringMultiline, StringConcatenate, LazySwitchKJ, GetNode, GetNode, TextGenerateLTX2Prompt, SimpleCalculatorKJ, Reroute, GetImageSize, CR Prompt Text, easy cleanGpuUsed, VHS_SelectFilename, Any To Any, MathExpression|pysssss, VHS_GetImageCount, SimpleCalculatorKJ, LTXVSeparateAVLatent, ResizeImageMaskNode, GetImageRangeFromBatch, GetVideoComponents, ImageScaleToTotalPixels, easy batchAnything, AudioConcat, GetNode, CreateVideo, easy forLoopStart, easy forLoopEnd, easy timelineSegmentOutput, easy timelineInfoOutput, MathExpression|pysssss, MathExpression|pysssss, MaxNode, easy showAnything, easy timelineSegmentCount, easy imagesSplitImage, ComfySwitchNode, Bool, SetNode, PrimitiveFloat, SetNode, SetNode, INTConstant, PrimitiveBoolean, EmptyAudio, SetNode, SaveVideo, GetNode, TextInput_, easy showAnything, LTXAddVideoICLoRAGuide, PreviewAny, PrimitiveStringMultiline, BatchImagesNode, BerniniPromptEnhancer, Remove Text, Remove Text, TTP_text_mix, UNETLoader, UNETLoader, PathchSageAttentionKJ, PathchSageAttentionKJ, LoraLoaderModelOnly, LoraLoaderModelOnly, KSamplerAdvanced, BerniniConditioning, TTP_text_mix, StringReplace, StringReplace, PreviewAny, INTConstant, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, GetNode, GetNode, LTXVAudioVAEDecode, GetNode, VAEDecode, PreviewAudio, LTXVAudioVideoMask, EmptyAudio, PreviewAny, KSamplerAdvanced, RH_LLMAPI_NODE, Remove Text, SetNode, VHS_VideoCombine, SetNode, LTX2AttentionTunerPatch, LoraLoaderModelOnly, LoraLoaderModelOnly, SaveVideo, Qwen3_VQA, Any To String (mtb), VHS_VideoCombine, PrimitiveStringMultiline, ImageResizeKJv2, StringReplace, StringReplace, PreviewAny, PreviewAny, easy timelineEditor]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 10, "denoise": "simple", "height": 25, "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "randomize", "width": 97}
---

# 视频生成/图生视频/Bernini+Ltx2.3导演分镜编辑全模态视频_2067515281458688002.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2067515281458688002.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（287 个）：
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
- `KSamplerSelect` ★核心
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `VAELoader`
- `SetNode`
- `Reroute`
- `GetNode`
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
- `LTXVConcatAVLatent`
- `GetNode`
- `GetNode`
- `LTXVCropGuides`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `CFGGuider`
- `ManualSigmas`
- `RandomNoise`
- `LTXAddVideoICLoRAGuide`
- `GetNode`
- `GetNode`
- `GetNode`
- `PathchSageAttentionKJ`
- `LTXVSetAudioRefTokens`
- `LTXVCropGuides`
- `LTXVLatentUpsampler` ★核心
- `SamplerCustomAdvanced` ★核心
- `LatentUpscaleModelLoader`
- `DualCLIPLoader`
- `VAELoader`
- `VAELoaderKJ`
- `VAELoader`
- `PrimitiveStringMultiline`
- `TextGenerateLTX2Prompt`
- `GetNode`
- `CFGGuider`
- `LTXVConditioning`
- `CLIPTextEncode` ★核心
- `StringConcatenate`
- `GetNode`
- `BasicScheduler`
- `GetNode`
- `LTXVSeparateAVLatent`
- `GetNode`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `GetNode`
- `CLIPTextEncode` ★核心
- `SetNode`
- `GetNode`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `VAELoader`
- `Reroute`
- `CreateVideo`
- `LTXVSeparateAVLatent`
- `EmptyLTXVLatentVideo`
- `SetNode`
- `ComfySwitchNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ComfyMathExpression`
- `SamplerCustomAdvanced` ★核心
- `GetImageSizeAndCount`
- `GetImageSizeAndCount`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `ComfyMathExpression`
- `SetNode`
- `SetNode`
- `ResizeImageMaskNode`
- `ResizeImageMaskNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `LTXVAudioVAEDecode` ★核心
- `VAEDecodeTiled` ★核心
- `easy batchAnything`
- `LTX2_NAG`
- `LTXVEmptyLatentAudio` ★核心
- `RandomNoise`
- `LTXVAudioVAEEncode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ManualSigmas`
- `GetNode`
- `SetNode`
- `GetNode`
- `LTXVPreprocess`
- `SetNode`
- `GetNode`
- `LTXVConcatAVLatent`
- `ModelSamplingSD3`
- `CFGGuider`
- `BasicScheduler`
- `LazySwitchKJ`
- `GetNode`
- `GetNode`
- `GetImageSizeAndCount`
- `SetNode`
- `GetNode`
- `SetNode`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `RandomNoise`
- `SetNode`
- `SetNode`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LTXVChunkFeedForward`
- `LTX2SamplingPreviewOverride`
- `GetNode`
- `GetNode`
- `SetNode`
- `Reroute`
- `SamplerCustomAdvanced` ★核心
- `LTXVConcatAVLatent`
- `LTXVSetAudioRefTokens`
- `SetNode`
- `PreviewAny`
- `LTX2SamplingPreviewOverride`
- `GetNode`
- `SetNode`
- `LTXVConditioning`
- `LTX2_NAG`
- `GetImageRangeFromBatch`
- `VAEEncode` ★核心
- `LTXVAddLatentGuide`
- `SetNode`
- `SetNode`
- `KSamplerSelect` ★核心
- `CLIPTextEncode` ★核心
- `KSamplerSelect` ★核心
- `ResizeImagesByLongerEdge`
- `MarkdownNote`
- `VAEEncode` ★核心
- `GetNode`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `GetImageSizeAndCount`
- `LTXVEmptyLatentAudio` ★核心
- `GetNode`
- `ComfyMathExpression`
- `SetNode`
- `GetNode`
- `GetImageSizeAndCount`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `ResizeImagesByLongerEdge`
- `GetImageRangeFromBatch`
- `PrimitiveStringMultiline`
- `StringConcatenate`
- `LazySwitchKJ`
- `GetNode`
- `GetNode`
- `TextGenerateLTX2Prompt`
- `SimpleCalculatorKJ`
- `Reroute`
- `GetImageSize`
- `CR Prompt Text`
- `easy cleanGpuUsed`
- `VHS_SelectFilename`
- `Any To Any`
- `MathExpression|pysssss`
- `VHS_GetImageCount`
- `SimpleCalculatorKJ`
- `LTXVSeparateAVLatent`
- `ResizeImageMaskNode`
- `GetImageRangeFromBatch`
- `GetVideoComponents`
- `ImageScaleToTotalPixels`
- `easy batchAnything`
- `AudioConcat`
- `GetNode`
- `CreateVideo`
- `easy forLoopStart`
- `easy forLoopEnd`
- `easy timelineSegmentOutput`
- `easy timelineInfoOutput`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `MaxNode`
- `easy showAnything`
- `easy timelineSegmentCount`
- `easy imagesSplitImage`
- `ComfySwitchNode`
- `Bool`
- `SetNode`
- `PrimitiveFloat`
- `SetNode`
- `SetNode`
- `INTConstant`
- `PrimitiveBoolean`
- `EmptyAudio`
- `SetNode`
- `SaveVideo`
- `GetNode`
- `TextInput_`
- `easy showAnything`
- `LTXAddVideoICLoRAGuide`
- `PreviewAny`
- `PrimitiveStringMultiline`
- `BatchImagesNode`
- `BerniniPromptEnhancer`
- `Remove Text`
- `Remove Text`
- `TTP_text_mix`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSamplerAdvanced` ★核心
- `BerniniConditioning`
- `TTP_text_mix`
- `StringReplace`
- `StringReplace`
- `PreviewAny`
- `INTConstant`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `LTXVAudioVAEDecode` ★核心
- `GetNode`
- `VAEDecode` ★核心
- `PreviewAudio`
- `LTXVAudioVideoMask`
- `EmptyAudio`
- `PreviewAny`
- `KSamplerAdvanced` ★核心
- `RH_LLMAPI_NODE`
- `Remove Text`
- `SetNode`
- `VHS_VideoCombine`
- `SetNode`
- `LTX2AttentionTunerPatch`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `SaveVideo`
- `Qwen3_VQA`
- `Any To String (mtb)`
- `VHS_VideoCombine`
- `PrimitiveStringMultiline`
- `ImageResizeKJv2`
- `StringReplace`
- `StringReplace`
- `PreviewAny`
- `PreviewAny`
- `easy timelineEditor`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `10`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **57%**（163/287）

**有卡**：`KSamplerSelect`、`VAELoader`、`LTXVConcatAVLatent`、`LTXVCropGuides`、`CFGGuider`、`ManualSigmas`、`RandomNoise`、`LTXAddVideoICLoRAGuide`、`PathchSageAttentionKJ`、`LTXVSetAudioRefTokens`、`LTXVLatentUpsampler`、`SamplerCustomAdvanced`、`LatentUpscaleModelLoader`、`DualCLIPLoader`、`VAELoaderKJ`、`TextGenerateLTX2Prompt`、`LTXVConditioning`、`CLIPTextEncode`、`StringConcatenate`、`BasicScheduler`、`LTXVSeparateAVLatent`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`VAEDecode`、`CLIPLoader`、`CreateVideo`、`EmptyLTXVLatentVideo`、`ComfyMathExpression`、`GetImageSizeAndCount`、`ResizeImageMaskNode`、`easy batchAnything`、`LTX2_NAG`、`LTXVEmptyLatentAudio`、`LTXVAudioVAEEncode`、`LTXVPreprocess`、`ModelSamplingSD3`、`LazySwitchKJ`、`UNETLoader`、`LoraLoaderModelOnly`、`LTXVChunkFeedForward`、`LTX2SamplingPreviewOverride`、`GetImageRangeFromBatch`、`VAEEncode`、`LTXVAddLatentGuide`、`ResizeImagesByLongerEdge`、`SimpleCalculatorKJ`、`GetImageSize`、`CR Prompt Text`、`easy cleanGpuUsed`、`VHS_SelectFilename`、`Any To Any`、`MathExpression|pysssss`、`VHS_GetImageCount`、`GetVideoComponents`、`ImageScaleToTotalPixels`、`AudioConcat`、`easy forLoopStart`、`easy forLoopEnd`、`easy timelineSegmentOutput`、`easy timelineInfoOutput`、`MaxNode`、`easy timelineSegmentCount`、`easy imagesSplitImage`、`Bool`、`INTConstant`、`PrimitiveBoolean`、`EmptyAudio`、`SaveVideo`、`TextInput_`、`BatchImagesNode`、`BerniniPromptEnhancer`、`Remove Text`、`TTP_text_mix`、`KSamplerAdvanced`、`BerniniConditioning`、`StringReplace`、`VHS_VideoCombine`、`PreviewAudio`、`LTXVAudioVideoMask`、`RH_LLMAPI_NODE`、`LTX2AttentionTunerPatch`、`Qwen3_VQA`、`Any To String (mtb)`、`ImageResizeKJv2`、`easy timelineEditor`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、CFGGuider、KSamplerAdvanced
