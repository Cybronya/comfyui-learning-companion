---
key: 视频生成/图生视频/贝尔尼尼Bernini Studio+LTX2.3音频（集三位大佬的思路）_2083377522535915521.json
name: 贝尔尼尼Bernini Studio+LTX2.3音频（集三位大佬的思路）_2083377522535915521
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/贝尔尼尼Bernini Studio+LTX2.3音频（集三位大佬的思路）_2083377522535915521.json
hash: 7e535e91ed735813
coverage: 0.683398
learned_at: 2026-10-16 19:17:45
nodes: [PathchSageAttentionKJ, PathchSageAttentionKJ, SetNode, UNETLoader, UNETLoader, VAELoader, CLIPLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, RTXVideoSuperResolution, ImageConcatMulti, DualCLIPLoader, LTXVConditioning, ConditioningZeroOut, VAELoader, SamplerCustomAdvanced, LTXVSeparateAVLatent, KSamplerSelect, CFGGuider, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVAudioVideoMask, ManualSigmas, RandomNoise, VAELoaderKJ, CLIPTextEncode, LTXVEmptyLatentAudio, VAEEncodeTiled, GetNode, easy cleanGpuUsed, ImageConcatMulti, ImageUpscaleWithModel, CR Text, UNETLoader, GetVideoComponents, GetNode, StringReplace, StringReplace, StringReplace, StringReplace, CR Text Concatenate, GetNode, GetNode, GetNode, easy cleanGpuUsed, easy cleanGpuUsed, StringReplace, CR Text Concatenate, GetNode, BerniniPromptEnhancer, GetNode, CR Text, RH_LLMAPI_Pro_Node, RH_LLMAPI_NODE, GetNode, CR Text, LoraLoaderModelOnly, BasicScheduler, StringReplace, StringReplace, StringReplace, CreateVideo, ImageScaleToMaxDimension, UpscaleModelLoader, RH_LLMAPI_NODE, CR Text, RegexExtract, YUAN_TXTReplace, YUAN_TXTParagraphSplitter, RegexExtract, StringReplace, PrimitiveStringMultiline, YUAN_TXTParagraphSplitter, YUAN_TXTReplace, StringLength, YUAN_TXTConvertAny, ComfySwitchNode, ComfySwitchNode, SetNode, ComfyMathExpression, SetNode, RegexExtract, RegexExtract, RegexExtract, YUAN_TXTParagraphSplitter, StringReplace, StringConcatenate, YUAN_TXTListNumber, RegexExtract, YUAN_TXTParagraphSplitter, YUAN_TXTListNumber, YUAN_TXTReplace, SetNode, RegexExtract, YUAN_TXTReplace, RegexExtract, YUAN_TXTAppearanceOrder, RegexExtract, SetNode, SetNode, GetNode, SetNode, YUAN_TXTAppearanceOrder, GetNode, ComfyMathExpression, YUAN_TXTConvertAny, YUAN_TXTParagraphSplitter, RegexExtract, YUAN_TXTParagraphSplitter, YUAN_TXTReplace, Text, ComfySwitchNode, SetNode, Display Any (rgthree), StringConcatenate, ComfySwitchNode, GetNode, GetNode, GetNode, GetNode, easy showAnything, CR Text, GetNode, SetNode, GetNode, easy positive, CR Text, LoadImage, SetNode, LoadImage, SetNode, LoadImage, SetNode, SetNode, KSamplerAdvanced, KSamplerAdvanced, VAEDecode, GetNode, CreateVideo, FrameInterpolate, ModelPatchMemoryCleaner, FrameInterpolationModelLoader, GetNode, LoadImage, SetNode, LoadImage, LoadImage, SetNode, SetNode, easy showAnything, PrimitiveInt, CR Text, SetNode, EmptyLatentImage, EmptyLatentImage, PrimitiveStringMultiline, RegexExtract, RegexExtract, YUAN_TXTConvertAny, SetNode, YUAN_TXTParagraphSplitter, PrimitiveStringMultiline, GetNode, RegexExtract, YUAN_TXTParagraphSplitter, YUAN_TXTParagraphSplitter, YUAN_TXTParagraphSplitter, YUAN_TXTParagraphSplitter, PrimitiveStringMultiline, PrimitiveBoolean, Fast Groups Bypasser (rgthree), PrimitiveInt, RegexExtract, SaveImage, VAEEncode, VAEDecode, GetNode, MarkdownNote, Fast Groups Bypasser (rgthree), PrimitiveStringMultiline, CLIPTextEncode, CFGGuider, KSamplerSelect, BasicScheduler, CLIPTextEncode, GetNode, SetNode, RandomNoise, PrimitiveStringMultiline, easy positive, CLIPLoader, VAELoader, UNETLoader, UNETLoader, ModelPatchLoader, ClipLoaderGGUF, VAELoader, PrimitiveStringMultiline, CLIPTextEncode, ZImageFunControlnet, LoraLoaderModelOnly, SamplerCustomAdvanced, GetNode, VAEDecode, PreviewImage, GetNode, ComfySwitchNode, GetNode, SeedVR2GGUF, GetNode, YUAN_TXTParagraphSplitter, easy showAnything, PreviewImage, SetNode, easy showAnything, SetNode, GetNode, CR Text, SetNode, SaveImage, LoadImage, LoadImage, CLIPTextEncode, GetNode, KSampler, ComfySwitchNode, GetNode, VHS_VideoCombine, UpscaleModelLoader, ImageUpscaleWithModel, VHS_VideoCombine, VHS_VideoCombine, VHS_LoadVideo, LoadImage, CR Text, CR Text, CR Text, CR Text, VHS_VideoCombine, GetVideoComponents, SaveVideo, VHS_VideoCombine, CR Text, Display Any (rgthree), CR Text Concatenate, GetNode, GetNode, easy cleanGpuUsed, Display Any (rgthree), BerniniStudio, ImpactSwitch, Fast Groups Bypasser (rgthree), CR Text Concatenate, CR Text, SetNode, SetNode, SetNode, LoadImage, GetNode]
patterns: [text_to_image, image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1920, "sampler_name": "res_2s_ode", "scheduler": "kl_optimal", "seed": 948601491650581, "steps": 8, "width": 1080}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/贝尔尼尼Bernini Studio+LTX2.3音频（集三位大佬的思路）_2083377522535915521.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/贝尔尼尼Bernini Studio+LTX2.3音频（集三位大佬的思路）_2083377522535915521.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（259 个）：
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `SetNode`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `VAELoader`
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `RTXVideoSuperResolution`
- `ImageConcatMulti`
- `DualCLIPLoader`
- `LTXVConditioning`
- `ConditioningZeroOut`
- `VAELoader`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `KSamplerSelect` ★核心
- `CFGGuider`
- `LTXVAudioVAEDecode` ★核心
- `LTXVConcatAVLatent`
- `LTXVAudioVideoMask`
- `ManualSigmas`
- `RandomNoise`
- `VAELoaderKJ`
- `CLIPTextEncode` ★核心
- `LTXVEmptyLatentAudio` ★核心
- `VAEEncodeTiled` ★核心
- `GetNode`
- `easy cleanGpuUsed`
- `ImageConcatMulti`
- `ImageUpscaleWithModel`
- `CR Text`
- `UNETLoader` ★核心
- `GetVideoComponents`
- `GetNode`
- `StringReplace`
- `StringReplace`
- `StringReplace`
- `StringReplace`
- `CR Text Concatenate`
- `GetNode`
- `GetNode`
- `GetNode`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `StringReplace`
- `CR Text Concatenate`
- `GetNode`
- `BerniniPromptEnhancer`
- `GetNode`
- `CR Text`
- `RH_LLMAPI_Pro_Node`
- `RH_LLMAPI_NODE`
- `GetNode`
- `CR Text`
- `LoraLoaderModelOnly` ★核心
- `BasicScheduler`
- `StringReplace`
- `StringReplace`
- `StringReplace`
- `CreateVideo`
- `ImageScaleToMaxDimension`
- `UpscaleModelLoader`
- `RH_LLMAPI_NODE`
- `CR Text`
- `RegexExtract`
- `YUAN_TXTReplace`
- `YUAN_TXTParagraphSplitter`
- `RegexExtract`
- `StringReplace`
- `PrimitiveStringMultiline`
- `YUAN_TXTParagraphSplitter`
- `YUAN_TXTReplace`
- `StringLength`
- `YUAN_TXTConvertAny`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `SetNode`
- `ComfyMathExpression`
- `SetNode`
- `RegexExtract`
- `RegexExtract`
- `RegexExtract`
- `YUAN_TXTParagraphSplitter`
- `StringReplace`
- `StringConcatenate`
- `YUAN_TXTListNumber`
- `RegexExtract`
- `YUAN_TXTParagraphSplitter`
- `YUAN_TXTListNumber`
- `YUAN_TXTReplace`
- `SetNode`
- `RegexExtract`
- `YUAN_TXTReplace`
- `RegexExtract`
- `YUAN_TXTAppearanceOrder`
- `RegexExtract`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `YUAN_TXTAppearanceOrder`
- `GetNode`
- `ComfyMathExpression`
- `YUAN_TXTConvertAny`
- `YUAN_TXTParagraphSplitter`
- `RegexExtract`
- `YUAN_TXTParagraphSplitter`
- `YUAN_TXTReplace`
- `Text`
- `ComfySwitchNode`
- `SetNode`
- `Display Any (rgthree)`
- `StringConcatenate`
- `ComfySwitchNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `easy showAnything`
- `CR Text`
- `GetNode`
- `SetNode`
- `GetNode`
- `easy positive`
- `CR Text`
- `LoadImage`
- `SetNode`
- `LoadImage`
- `SetNode`
- `LoadImage`
- `SetNode`
- `SetNode`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `GetNode`
- `CreateVideo`
- `FrameInterpolate`
- `ModelPatchMemoryCleaner`
- `FrameInterpolationModelLoader`
- `GetNode`
- `LoadImage`
- `SetNode`
- `LoadImage`
- `LoadImage`
- `SetNode`
- `SetNode`
- `easy showAnything`
- `PrimitiveInt`
- `CR Text`
- `SetNode`
- `EmptyLatentImage` ★核心
- `EmptyLatentImage` ★核心
- `PrimitiveStringMultiline`
- `RegexExtract`
- `RegexExtract`
- `YUAN_TXTConvertAny`
- `SetNode`
- `YUAN_TXTParagraphSplitter`
- `PrimitiveStringMultiline`
- `GetNode`
- `RegexExtract`
- `YUAN_TXTParagraphSplitter`
- `YUAN_TXTParagraphSplitter`
- `YUAN_TXTParagraphSplitter`
- `YUAN_TXTParagraphSplitter`
- `PrimitiveStringMultiline`
- `PrimitiveBoolean`
- `Fast Groups Bypasser (rgthree)`
- `PrimitiveInt`
- `RegexExtract`
- `SaveImage`
- `VAEEncode` ★核心
- `VAEDecode` ★核心
- `GetNode`
- `MarkdownNote`
- `Fast Groups Bypasser (rgthree)`
- `PrimitiveStringMultiline`
- `CLIPTextEncode` ★核心
- `CFGGuider`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `CLIPTextEncode` ★核心
- `GetNode`
- `SetNode`
- `RandomNoise`
- `PrimitiveStringMultiline`
- `easy positive`
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `ModelPatchLoader`
- `ClipLoaderGGUF`
- `VAELoader`
- `PrimitiveStringMultiline`
- `CLIPTextEncode` ★核心
- `ZImageFunControlnet`
- `LoraLoaderModelOnly` ★核心
- `SamplerCustomAdvanced` ★核心
- `GetNode`
- `VAEDecode` ★核心
- `PreviewImage`
- `GetNode`
- `ComfySwitchNode`
- `GetNode`
- `SeedVR2GGUF`
- `GetNode`
- `YUAN_TXTParagraphSplitter`
- `easy showAnything`
- `PreviewImage`
- `SetNode`
- `easy showAnything`
- `SetNode`
- `GetNode`
- `CR Text`
- `SetNode`
- `SaveImage`
- `LoadImage`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `GetNode`
- `KSampler` ★核心
- `ComfySwitchNode`
- `GetNode`
- `VHS_VideoCombine`
- `UpscaleModelLoader`
- `ImageUpscaleWithModel`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `LoadImage`
- `CR Text`
- `CR Text`
- `CR Text`
- `CR Text`
- `VHS_VideoCombine`
- `GetVideoComponents`
- `SaveVideo`
- `VHS_VideoCombine`
- `CR Text`
- `Display Any (rgthree)`
- `CR Text Concatenate`
- `GetNode`
- `GetNode`
- `easy cleanGpuUsed`
- `Display Any (rgthree)`
- `BerniniStudio`
- `ImpactSwitch`
- `Fast Groups Bypasser (rgthree)`
- `CR Text Concatenate`
- `CR Text`
- `SetNode`
- `SetNode`
- `SetNode`
- `LoadImage`
- `GetNode`

**识别到的模式**：text_to_image、image_to_image

## 关键参数

- `width` = `1080`
- `height` = `1920`
- `batch_size` = `1`
- `seed` = `948601491650581`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `res_2s_ode`
- `scheduler` = `kl_optimal`
- `denoise` = `1`

## 知识

覆盖率 **68%**（177/259）

**有卡**：`PathchSageAttentionKJ`、`UNETLoader`、`VAELoader`、`CLIPLoader`、`LoraLoaderModelOnly`、`RTXVideoSuperResolution`、`ImageConcatMulti`、`DualCLIPLoader`、`LTXVConditioning`、`ConditioningZeroOut`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`KSamplerSelect`、`CFGGuider`、`LTXVAudioVAEDecode`、`LTXVConcatAVLatent`、`LTXVAudioVideoMask`、`ManualSigmas`、`RandomNoise`、`VAELoaderKJ`、`CLIPTextEncode`、`LTXVEmptyLatentAudio`、`VAEEncodeTiled`、`easy cleanGpuUsed`、`ImageUpscaleWithModel`、`CR Text`、`GetVideoComponents`、`StringReplace`、`CR Text Concatenate`、`BerniniPromptEnhancer`、`RH_LLMAPI_Pro_Node`、`RH_LLMAPI_NODE`、`BasicScheduler`、`CreateVideo`、`ImageScaleToMaxDimension`、`UpscaleModelLoader`、`RegexExtract`、`YUAN_TXTReplace`、`YUAN_TXTParagraphSplitter`、`StringLength`、`YUAN_TXTConvertAny`、`ComfyMathExpression`、`StringConcatenate`、`YUAN_TXTListNumber`、`YUAN_TXTAppearanceOrder`、`Text`、`Display Any (rgthree)`、`easy positive`、`LoadImage`、`KSamplerAdvanced`、`VAEDecode`、`FrameInterpolate`、`ModelPatchMemoryCleaner`、`FrameInterpolationModelLoader`、`EmptyLatentImage`、`PrimitiveBoolean`、`SaveImage`、`VAEEncode`、`ModelPatchLoader`、`ClipLoaderGGUF`、`ZImageFunControlnet`、`SeedVR2GGUF`、`KSampler`、`VHS_VideoCombine`、`VHS_LoadVideo`、`SaveVideo`、`BerniniStudio`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
