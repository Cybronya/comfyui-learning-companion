---
key: 视频生成/图生视频/LTX2.3全栈式短剧生成V4（残血版）_2035986971947962370.json
name: LTX2.3全栈式短剧生成V4（残血版）_2035986971947962370.json
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3全栈式短剧生成V4（残血版）_2035986971947962370.json
hash: 0a6802cc6a189f56
coverage: 0.729323
learned_at: 2026-10-15 22:35:50
nodes: [easy indexAnything, easy indexAnything, easy indexAnything, easy indexAnything, PrimitiveStringMultiline, EmptyLTXVLatentVideo, easy indexAnything, GetNode, GetNode, GetNode, GetNode, easy indexAnything, easy indexAnything, GetNode, easy promptList, EmptyImage, ImageBatchMulti, PrimitiveBoolean, GetNode, CLIPTextEncode, PrimitiveInt, LTXVEmptyLatentAudio, GetNode, GetNode, ComfyMathExpression, ComfyMathExpression, PrimitiveInt, LTXVConditioning, CFGGuider, GetNode, SamplerCustomAdvanced, LTXVPreprocess, easy promptReplace, GetNode, KSampler, EmptyLatentImage, easy indexAnything, easy promptLine, easy promptLine, easy indexAnything, PrimitiveStringMultiline, RegexExtract, GetImagesFromBatchIndexed, GetNode, easy indexAnything, RegexExtract, easy promptReplace, easy promptLine, SetNode, easy positive, easy indexAnything, GetNode, GetNode, SetNode, easy promptReplace, easy promptLine, easy promptConcat, SetNode, easy promptReplace, INTConstant, easy indexAnything, PreviewImage, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlus, easy indexAnything, RegexExtract, easy convertAnything, GetNode, ResizeImagesByLongerEdge, LTXVConcatAVLatent, LTXVImgToVideoInplace, GetNode, LTXVSeparateAVLatent, VAEDecodeTiled, INTConstant, INTConstant, easy positive, easy positive, easy promptReplace, LTXVAudioVAEDecode, KSamplerSelect, RandomNoise, SetNode, easy positive, easy indexAnything, GetNode, CLIPTextEncode, SetNode, SetNode, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, SetNode, SetNode, ModelSamplingAuraFlow, VAELoader, CLIPLoader, SetNode, LoraLoaderModelOnly, CFGNorm, SetNode, VAELoaderKJ, SetNode, VAELoaderKJ, SetNode, DualCLIPLoader, LoraLoaderModelOnly, SetNode, LTXVChunkFeedForward, UNETLoader, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelPatchTorchSettings, INTConstant, ManualSigmas, PreviewImage, easy promptConcat, easy positive, ShowText|pysssss, ManualSigmas, UNETLoader, ResizeImageMaskNode, easy forLoopEnd, easy forLoopStart, easy batchAnything, VAEDecode, easy cleanGpuUsed, SaveImage, LoadImage, easy cleanGpuUsed, VHS_VideoCombine]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1.2, "denoise": 1, "height": 720, "sampler_name": "euler", "scheduler": "simple", "seed": 43, "steps": 4, "width": 1280}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/LTX2.3全栈式短剧生成V4（残血版）_2035986971947962370.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2035986971947962370.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（133 个）：
- `easy indexAnything`
- `easy indexAnything`
- `easy indexAnything`
- `easy indexAnything`
- `PrimitiveStringMultiline`
- `EmptyLTXVLatentVideo`
- `easy indexAnything`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `easy indexAnything`
- `easy indexAnything`
- `GetNode`
- `easy promptList`
- `EmptyImage`
- `ImageBatchMulti`
- `PrimitiveBoolean`
- `GetNode`
- `CLIPTextEncode` ★核心
- `PrimitiveInt`
- `LTXVEmptyLatentAudio` ★核心
- `GetNode`
- `GetNode`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `PrimitiveInt`
- `LTXVConditioning`
- `CFGGuider`
- `GetNode`
- `SamplerCustomAdvanced` ★核心
- `LTXVPreprocess`
- `easy promptReplace`
- `GetNode`
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `easy indexAnything`
- `easy promptLine`
- `easy promptLine`
- `easy indexAnything`
- `PrimitiveStringMultiline`
- `RegexExtract`
- `GetImagesFromBatchIndexed`
- `GetNode`
- `easy indexAnything`
- `RegexExtract`
- `easy promptReplace`
- `easy promptLine`
- `SetNode`
- `easy positive`
- `easy indexAnything`
- `GetNode`
- `GetNode`
- `SetNode`
- `easy promptReplace`
- `easy promptLine`
- `easy promptConcat`
- `SetNode`
- `easy promptReplace`
- `INTConstant`
- `easy indexAnything`
- `PreviewImage`
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlus`
- `easy indexAnything`
- `RegexExtract`
- `easy convertAnything`
- `GetNode`
- `ResizeImagesByLongerEdge`
- `LTXVConcatAVLatent`
- `LTXVImgToVideoInplace`
- `GetNode`
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `INTConstant`
- `INTConstant`
- `easy positive`
- `easy positive`
- `easy promptReplace`
- `LTXVAudioVAEDecode` ★核心
- `KSamplerSelect` ★核心
- `RandomNoise`
- `SetNode`
- `easy positive`
- `easy indexAnything`
- `GetNode`
- `CLIPTextEncode` ★核心
- `SetNode`
- `SetNode`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `SetNode`
- `SetNode`
- `ModelSamplingAuraFlow`
- `VAELoader`
- `CLIPLoader`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `CFGNorm`
- `SetNode`
- `VAELoaderKJ`
- `SetNode`
- `VAELoaderKJ`
- `SetNode`
- `DualCLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `LTXVChunkFeedForward`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `INTConstant`
- `ManualSigmas`
- `PreviewImage`
- `easy promptConcat`
- `easy positive`
- `ShowText|pysssss`
- `ManualSigmas`
- `UNETLoader` ★核心
- `ResizeImageMaskNode`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy batchAnything`
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `SaveImage`
- `LoadImage`
- `easy cleanGpuUsed`
- `VHS_VideoCombine`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1280`
- `height` = `720`
- `batch_size` = `1`
- `seed` = `43`
- `steps` = `4`
- `cfg` = `1.2`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **73%**（97/133）

**有卡**：`easy indexAnything`、`EmptyLTXVLatentVideo`、`easy promptList`、`EmptyImage`、`ImageBatchMulti`、`PrimitiveBoolean`、`CLIPTextEncode`、`LTXVEmptyLatentAudio`、`ComfyMathExpression`、`LTXVConditioning`、`CFGGuider`、`SamplerCustomAdvanced`、`LTXVPreprocess`、`easy promptReplace`、`KSampler`、`EmptyLatentImage`、`easy promptLine`、`RegexExtract`、`GetImagesFromBatchIndexed`、`easy positive`、`easy promptConcat`、`INTConstant`、`TextEncodeQwenImageEditPlus`、`easy convertAnything`、`ResizeImagesByLongerEdge`、`LTXVConcatAVLatent`、`LTXVImgToVideoInplace`、`LTXVSeparateAVLatent`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`KSamplerSelect`、`RandomNoise`、`LoadImage`、`ModelSamplingAuraFlow`、`VAELoader`、`CLIPLoader`、`LoraLoaderModelOnly`、`CFGNorm`、`VAELoaderKJ`、`DualCLIPLoader`、`LTXVChunkFeedForward`、`UNETLoader`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`ManualSigmas`、`ResizeImageMaskNode`、`easy forLoopEnd`、`easy forLoopStart`、`easy batchAnything`、`VAEDecode`、`easy cleanGpuUsed`、`SaveImage`、`VHS_VideoCombine`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
