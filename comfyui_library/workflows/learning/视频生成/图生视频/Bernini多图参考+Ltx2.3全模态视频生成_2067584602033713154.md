---
key: 视频生成/图生视频/Bernini多图参考+Ltx2.3全模态视频生成_2067584602033713154.json
name: Bernini多图参考+Ltx2.3全模态视频生成_2067584602033713154.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Bernini多图参考+Ltx2.3全模态视频生成_2067584602033713154.json
hash: df92cac37ca9c95e
coverage: 0.6
learned_at: 2026-10-15 22:40:08
nodes: [SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, KSamplerSelect, SetNode, LoraLoaderModelOnly, GetNode, GetNode, LTXVSeparateAVLatent, LTX2AttentionTunerPatch, GetNode, SetNode, GetNode, GetNode, VAELoader, SetNode, LTX2_NAG, Reroute, PrimitiveBoolean, ComfyMathExpression, GetNode, SetNode, SetNode, KSamplerSelect, SetNode, SetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, LTXVConcatAVLatent, GetNode, GetNode, LTXVCropGuides, GetNode, GetNode, GetNode, SetNode, SetNode, CFGGuider, ManualSigmas, RandomNoise, GetNode, GetNode, LTXVEmptyLatentAudio, LTXAddVideoICLoRAGuide, GetNode, GetNode, GetNode, PathchSageAttentionKJ, LTXVChunkFeedForward, LTXVSetAudioRefTokens, LTXVCropGuides, LTXVLatentUpsampler, SamplerCustomAdvanced, UNETLoader, LatentUpscaleModelLoader, DualCLIPLoader, VAELoader, VAELoaderKJ, PrimitiveStringMultiline, TextGenerateLTX2Prompt, GetNode, CFGGuider, LTXVConditioning, CLIPTextEncode, LTXVSetAudioRefTokens, SetNode, ComfyMathExpression, SetNode, GetImageSizeAndCount, SetNode, ResizeImageMaskNode, LTXAddVideoICLoRAGuide, EmptyLTXVLatentVideo, StringConcatenate, GetNode, GetVideoComponents, BasicScheduler, LTXVAudioVAEDecode, GetNode, LTXVSeparateAVLatent, CreateVideo, GetNode, VAEDecodeTiled, LTXVAudioVAEDecode, GetNode, SamplerCustomAdvanced, CLIPTextEncode, PrimitiveFloat, SetNode, SetNode, SetNode, GetImageSizeAndCount, SetNode, ResizeImageMaskNode, SetNode, GetNode, GetImageRangeFromBatch, LTX2SamplingPreviewOverride, VAEDecodeTiled, GetNode, SimpleCalculatorKJ, VHS_GetImageCount, PathchSageAttentionKJ, CLIPTextEncode, CLIPTextEncode, LTXVAudioVAEEncode, LTXVConcatAVLatent, easy cleanGpuUsed, MathExpression|pysssss, INTConstant, ComfySwitchNode, PreviewAny, Reroute, CLIPLoader, easy showAnything, Reroute, ImageResizeKJv2, LoadImage, ImageResizeKJv2, LoadImage, PrimitiveStringMultiline, CreateVideo, ComfySwitchNode, VRAM_Debug, SetNode, SetNode, SetNode, VAELoader, SaveVideo, PrimitiveInt, PrimitiveInt, PrimitiveInt, Bool, VHS_VideoCombine, ImageResizeKJv2, RMBG, LoadImage, HunyuanVideoFoley, VHS_SelectFilename, SetNode, VRAM_Debug, BasicScheduler, LoraLoaderModelOnly, PathchSageAttentionKJ, UNETLoader, UNETLoader, LoraLoaderModelOnly, VAEDecode, KSamplerSelect, SplitSigmas, VAELoader, BatchImagesNode, RH_LLMAPI_NODE, PreviewAny, TTP_text_mix, VRAM_Debug, GetVideoComponents, KSamplerAdvanced, BerniniConditioning, RMBG, VHS_VideoCombine, ImageResizeKJv2, LoadImage, Remove Text, Remove Text, Remove Text, TTP_text_mix, Remove Text, Remove Text, Remove Text, KSamplerAdvanced, StringReplace, BerniniPromptEnhancer, StringReplace, TextInput_, PreviewAny, LoadImage, LoadImage, LoraLoaderModelOnly, LoraLoaderModelOnly, RandomNoise, Qwen3_VQA, Any To String (mtb), easy showAnything, AdjustAudio, LoadImage, VHS_VideoCombine, CR Prompt Text]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 10, "denoise": "simple", "height": 24, "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "randomize", "width": 97}
---

# 视频生成/图生视频/Bernini多图参考+Ltx2.3全模态视频生成_2067584602033713154.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2067584602033713154.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（205 个）：
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
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `KSamplerSelect` ★核心
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `GetNode`
- `GetNode`
- `LTXVSeparateAVLatent`
- `LTX2AttentionTunerPatch`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `VAELoader`
- `SetNode`
- `LTX2_NAG`
- `Reroute`
- `PrimitiveBoolean`
- `ComfyMathExpression`
- `GetNode`
- `SetNode`
- `SetNode`
- `KSamplerSelect` ★核心
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
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
- `GetNode`
- `SetNode`
- `SetNode`
- `CFGGuider`
- `ManualSigmas`
- `RandomNoise`
- `GetNode`
- `GetNode`
- `LTXVEmptyLatentAudio` ★核心
- `LTXAddVideoICLoRAGuide`
- `GetNode`
- `GetNode`
- `GetNode`
- `PathchSageAttentionKJ`
- `LTXVChunkFeedForward`
- `LTXVSetAudioRefTokens`
- `LTXVCropGuides`
- `LTXVLatentUpsampler` ★核心
- `SamplerCustomAdvanced` ★核心
- `UNETLoader` ★核心
- `LatentUpscaleModelLoader`
- `DualCLIPLoader`
- `VAELoader`
- `VAELoaderKJ`
- `PrimitiveStringMultiline`
- `TextGenerateLTX2Prompt`
- `GetNode`
- `CFGGuider`
- `LTXVConditioning`
- `CLIPTextEncode` ★核心
- `LTXVSetAudioRefTokens`
- `SetNode`
- `ComfyMathExpression`
- `SetNode`
- `GetImageSizeAndCount`
- `SetNode`
- `ResizeImageMaskNode`
- `LTXAddVideoICLoRAGuide`
- `EmptyLTXVLatentVideo`
- `StringConcatenate`
- `GetNode`
- `GetVideoComponents`
- `BasicScheduler`
- `LTXVAudioVAEDecode` ★核心
- `GetNode`
- `LTXVSeparateAVLatent`
- `CreateVideo`
- `GetNode`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `GetNode`
- `SamplerCustomAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `PrimitiveFloat`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetImageSizeAndCount`
- `SetNode`
- `ResizeImageMaskNode`
- `SetNode`
- `GetNode`
- `GetImageRangeFromBatch`
- `LTX2SamplingPreviewOverride`
- `VAEDecodeTiled` ★核心
- `GetNode`
- `SimpleCalculatorKJ`
- `VHS_GetImageCount`
- `PathchSageAttentionKJ`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LTXVAudioVAEEncode` ★核心
- `LTXVConcatAVLatent`
- `easy cleanGpuUsed`
- `MathExpression|pysssss`
- `INTConstant`
- `ComfySwitchNode`
- `PreviewAny`
- `Reroute`
- `CLIPLoader`
- `easy showAnything`
- `Reroute`
- `ImageResizeKJv2`
- `LoadImage`
- `ImageResizeKJv2`
- `LoadImage`
- `PrimitiveStringMultiline`
- `CreateVideo`
- `ComfySwitchNode`
- `VRAM_Debug`
- `SetNode`
- `SetNode`
- `SetNode`
- `VAELoader`
- `SaveVideo`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `Bool`
- `VHS_VideoCombine`
- `ImageResizeKJv2`
- `RMBG`
- `LoadImage`
- `HunyuanVideoFoley`
- `VHS_SelectFilename`
- `SetNode`
- `VRAM_Debug`
- `BasicScheduler`
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAEDecode` ★核心
- `KSamplerSelect` ★核心
- `SplitSigmas`
- `VAELoader`
- `BatchImagesNode`
- `RH_LLMAPI_NODE`
- `PreviewAny`
- `TTP_text_mix`
- `VRAM_Debug`
- `GetVideoComponents`
- `KSamplerAdvanced` ★核心
- `BerniniConditioning`
- `RMBG`
- `VHS_VideoCombine`
- `ImageResizeKJv2`
- `LoadImage`
- `Remove Text`
- `Remove Text`
- `Remove Text`
- `TTP_text_mix`
- `Remove Text`
- `Remove Text`
- `Remove Text`
- `KSamplerAdvanced` ★核心
- `StringReplace`
- `BerniniPromptEnhancer`
- `StringReplace`
- `TextInput_`
- `PreviewAny`
- `LoadImage`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `RandomNoise`
- `Qwen3_VQA`
- `Any To String (mtb)`
- `easy showAnything`
- `AdjustAudio`
- `LoadImage`
- `VHS_VideoCombine`
- `CR Prompt Text`

## 关键参数

- `width` = `97`
- `height` = `24`
- `batch_size` = `1`
- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `10`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **60%**（123/205）

**有卡**：`KSamplerSelect`、`LoraLoaderModelOnly`、`LTXVSeparateAVLatent`、`LTX2AttentionTunerPatch`、`VAELoader`、`LTX2_NAG`、`PrimitiveBoolean`、`ComfyMathExpression`、`LTXVConcatAVLatent`、`LTXVCropGuides`、`CFGGuider`、`ManualSigmas`、`RandomNoise`、`LTXVEmptyLatentAudio`、`LTXAddVideoICLoRAGuide`、`PathchSageAttentionKJ`、`LTXVChunkFeedForward`、`LTXVSetAudioRefTokens`、`LTXVLatentUpsampler`、`SamplerCustomAdvanced`、`UNETLoader`、`LatentUpscaleModelLoader`、`DualCLIPLoader`、`VAELoaderKJ`、`TextGenerateLTX2Prompt`、`LTXVConditioning`、`CLIPTextEncode`、`GetImageSizeAndCount`、`ResizeImageMaskNode`、`EmptyLTXVLatentVideo`、`StringConcatenate`、`GetVideoComponents`、`BasicScheduler`、`LTXVAudioVAEDecode`、`CreateVideo`、`VAEDecodeTiled`、`GetImageRangeFromBatch`、`LTX2SamplingPreviewOverride`、`SimpleCalculatorKJ`、`VHS_GetImageCount`、`LTXVAudioVAEEncode`、`easy cleanGpuUsed`、`MathExpression|pysssss`、`INTConstant`、`CLIPLoader`、`ImageResizeKJv2`、`LoadImage`、`VRAM_Debug`、`SaveVideo`、`Bool`、`VHS_VideoCombine`、`RMBG`、`HunyuanVideoFoley`、`VHS_SelectFilename`、`VAEDecode`、`SplitSigmas`、`BatchImagesNode`、`RH_LLMAPI_NODE`、`TTP_text_mix`、`KSamplerAdvanced`、`BerniniConditioning`、`Remove Text`、`StringReplace`、`BerniniPromptEnhancer`、`TextInput_`、`Qwen3_VQA`、`Any To String (mtb)`、`AdjustAudio`、`CR Prompt Text`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、CFGGuider
