---
key: 视频生成/图生视频/LTX2.3全栈式短剧生成V3（残血版）_2034616876847861762.json
name: LTX2.3全栈式短剧生成V3（残血版）_2034616876847861762.json
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3全栈式短剧生成V3（残血版）_2034616876847861762.json
hash: 59b450eb014722a0
coverage: 0.766234
learned_at: 2026-10-15 22:35:45
nodes: [LTXVConcatAVLatent, KSamplerSelect, ManualSigmas, CFGGuider, SamplerCustomAdvanced, PrimitiveStringMultiline, EmptyLTXVLatentVideo, SetNode, easy promptReplace, RegexExtract, GetNode, GetNode, GetNode, easy indexAnything, easy indexAnything, easy indexAnything, GetNode, GetNode, easy promptList, EmptyImage, ImageBatchMulti, PrimitiveBoolean, CLIPTextEncode, ResizeImageMaskNode, INTConstant, LTXVEmptyLatentAudio, GetNode, ComfyMathExpression, LTXVConditioning, CFGGuider, RandomNoise, SamplerCustomAdvanced, KSamplerSelect, easy ifElse, ManualSigmas, ManualSigmas, LTXVConcatAVLatent, LTXVImgToVideoInplace, ResizeImagesByLongerEdge, LTXVPreprocess, GetNode, LTXVSeparateAVLatent, LTXVLatentUpsampler, GetNode, LTXVImgToVideoInplace, LTXVCropGuides, LTXVSeparateAVLatent, RTXVideoSuperResolution, GetNode, GetNode, EmptyLatentImage, GetImagesFromBatchIndexed, PreviewImage, easy lengthAnything, easy promptConcat, RandomNoise, KSampler, RTXVideoSuperResolution, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlus, easy promptConcat, CFGNorm, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, LatentUpscaleModelLoader, VAELoaderKJ, DualCLIPLoader, VAELoaderKJ, ModelSamplingAuraFlow, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, VAELoader, CLIPLoader, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, SetNode, VAEDecode, SetNode, INTConstant, easy positive, easy promptReplace, easy positive, RegexExtract, RegexExtract, easy promptReplace, easy promptReplace, easy promptReplace, easy promptLine, SetNode, RegexExtract, easy promptConcat, UNETLoader, PathchSageAttentionKJ, ModelPatchTorchSettings, LTXVChunkFeedForward, easy positive, RegexExtract, easy promptConcat, easy promptLine, easy positive, easy promptLine, easy promptLine, easy promptReplace, easy promptLine, easy mathString, easy ifElse, SetNode, SetNode, INTConstant, easy indexAnything, easy indexAnything, easy indexAnything, easy indexAnything, easy indexAnything, easy convertAnything, ComfyMathExpression, ComfyMathExpression, easy promptLine, easy promptLine, LoadImage, GetNode, GetNode, easy indexAnything, GetNode, easy batchAnything, SaveImage, easy forLoopStart, ComfyMathExpression, PrimitiveInt, easy indexAnything, GetNode, easy forLoopEnd, GetNode, easy indexAnything, GetNode, VAEDecodeTiled, LTXVAudioVAEDecode, easy indexAnything, easy indexAnything, PrimitiveInt, PrimitiveInt, easy positive, CLIPTextEncode, VHS_VideoCombine, INTConstant]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1.2, "denoise": 1, "height": 720, "sampler_name": "lcm", "scheduler": "simple", "seed": 43, "steps": 4, "width": 1280}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/LTX2.3全栈式短剧生成V3（残血版）_2034616876847861762.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2034616876847861762.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（154 个）：
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `PrimitiveStringMultiline`
- `EmptyLTXVLatentVideo`
- `SetNode`
- `easy promptReplace`
- `RegexExtract`
- `GetNode`
- `GetNode`
- `GetNode`
- `easy indexAnything`
- `easy indexAnything`
- `easy indexAnything`
- `GetNode`
- `GetNode`
- `easy promptList`
- `EmptyImage`
- `ImageBatchMulti`
- `PrimitiveBoolean`
- `CLIPTextEncode` ★核心
- `ResizeImageMaskNode`
- `INTConstant`
- `LTXVEmptyLatentAudio` ★核心
- `GetNode`
- `ComfyMathExpression`
- `LTXVConditioning`
- `CFGGuider`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
- `easy ifElse`
- `ManualSigmas`
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `LTXVImgToVideoInplace`
- `ResizeImagesByLongerEdge`
- `LTXVPreprocess`
- `GetNode`
- `LTXVSeparateAVLatent`
- `LTXVLatentUpsampler` ★核心
- `GetNode`
- `LTXVImgToVideoInplace`
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `RTXVideoSuperResolution`
- `GetNode`
- `GetNode`
- `EmptyLatentImage` ★核心
- `GetImagesFromBatchIndexed`
- `PreviewImage`
- `easy lengthAnything`
- `easy promptConcat`
- `RandomNoise`
- `KSampler` ★核心
- `RTXVideoSuperResolution`
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlus`
- `easy promptConcat`
- `CFGNorm`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `LatentUpscaleModelLoader`
- `VAELoaderKJ`
- `DualCLIPLoader`
- `VAELoaderKJ`
- `ModelSamplingAuraFlow`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `VAELoader`
- `CLIPLoader`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `SetNode`
- `VAEDecode` ★核心
- `SetNode`
- `INTConstant`
- `easy positive`
- `easy promptReplace`
- `easy positive`
- `RegexExtract`
- `RegexExtract`
- `easy promptReplace`
- `easy promptReplace`
- `easy promptReplace`
- `easy promptLine`
- `SetNode`
- `RegexExtract`
- `easy promptConcat`
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `LTXVChunkFeedForward`
- `easy positive`
- `RegexExtract`
- `easy promptConcat`
- `easy promptLine`
- `easy positive`
- `easy promptLine`
- `easy promptLine`
- `easy promptReplace`
- `easy promptLine`
- `easy mathString`
- `easy ifElse`
- `SetNode`
- `SetNode`
- `INTConstant`
- `easy indexAnything`
- `easy indexAnything`
- `easy indexAnything`
- `easy indexAnything`
- `easy indexAnything`
- `easy convertAnything`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `easy promptLine`
- `easy promptLine`
- `LoadImage`
- `GetNode`
- `GetNode`
- `easy indexAnything`
- `GetNode`
- `easy batchAnything`
- `SaveImage`
- `easy forLoopStart`
- `ComfyMathExpression`
- `PrimitiveInt`
- `easy indexAnything`
- `GetNode`
- `easy forLoopEnd`
- `GetNode`
- `easy indexAnything`
- `GetNode`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `easy indexAnything`
- `easy indexAnything`
- `PrimitiveInt`
- `PrimitiveInt`
- `easy positive`
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`
- `INTConstant`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1280`
- `height` = `720`
- `batch_size` = `1`
- `seed` = `43`
- `steps` = `4`
- `cfg` = `1.2`
- `sampler_name` = `lcm`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **77%**（118/154）

**有卡**：`LTXVConcatAVLatent`、`KSamplerSelect`、`ManualSigmas`、`CFGGuider`、`SamplerCustomAdvanced`、`EmptyLTXVLatentVideo`、`easy promptReplace`、`RegexExtract`、`easy indexAnything`、`easy promptList`、`EmptyImage`、`ImageBatchMulti`、`PrimitiveBoolean`、`CLIPTextEncode`、`ResizeImageMaskNode`、`INTConstant`、`LTXVEmptyLatentAudio`、`ComfyMathExpression`、`LTXVConditioning`、`RandomNoise`、`LTXVImgToVideoInplace`、`ResizeImagesByLongerEdge`、`LTXVPreprocess`、`LTXVSeparateAVLatent`、`LTXVLatentUpsampler`、`LTXVCropGuides`、`RTXVideoSuperResolution`、`EmptyLatentImage`、`GetImagesFromBatchIndexed`、`easy lengthAnything`、`easy promptConcat`、`KSampler`、`TextEncodeQwenImageEditPlus`、`CFGNorm`、`LatentUpscaleModelLoader`、`VAELoaderKJ`、`DualCLIPLoader`、`ModelSamplingAuraFlow`、`LoraLoaderModelOnly`、`UNETLoader`、`VAELoader`、`CLIPLoader`、`LoadImage`、`VAEDecode`、`easy positive`、`easy promptLine`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`LTXVChunkFeedForward`、`easy mathString`、`easy convertAnything`、`easy batchAnything`、`SaveImage`、`easy forLoopStart`、`easy forLoopEnd`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`VHS_VideoCombine`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
