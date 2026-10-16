---
key: 视频生成/图生视频/商业级多图分镜数字人-LTX-2.3 Singularity-MV、口播等_2064156587920551937.json
name: 商业级多图分镜数字人-LTX-2.3 Singularity-MV、口播等_2064156587920551937.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2064156587920551937.json
hash: 81df57f565d09689
coverage: 0.454023
learned_at: 2026-10-15 22:39:20
nodes: [KSamplerSelect, CLIPTextEncode, CLIPTextEncode, KSamplerSelect, ManualSigmas, LTXVConcatAVLatent, RandomNoise, RandomNoise, CFGGuider, CFGGuider, LTXVLatentUpsampler, LatentUpscaleModelLoader, LTXVSeparateAVLatent, GetNode, GetNode, GetNode, SetNode, VAELoaderKJ, SetNode, VAELoaderKJ, GetNode, UNETLoader, UNETLoader, LTXVImgToVideoInplace, SamplerCustomAdvanced, LTXVConditioning, GetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SamplerCustomAdvanced, SetNode, GetNode, MelBandRoFormerModelLoader, SetNode, LoadImage, LoadImage, WujiCleaner, ImageScaleBy, PreviewImage, easy batchAnything, MelBandRoFormerSampler, PreviewAudio, SoundFlow_TrimAudio, LTXVAudioVAEDecode, VAEDecode, PathchSageAttentionKJ, SetNode, SetNode, SetNode, DualCLIPLoader, GetNode, ShowText|pysssss, Dapao_LlamaChat, ShowText|pysssss, SetNode, SetNode, PreviewImage, PreviewAudio, easy showAnything, easy forLoopStart, Display Int (rgthree), SimpleMath+, LTXVPreprocess, GetNode, easy imageSize, EmptyLTXVLatentVideo, PreviewImage, LTXVSeparateAVLatent, LTXVCropGuides, GetNode, ManualSigmas, LTXVConcatAVLatent, SetLatentNoiseMask, LTXVImgToVideoInplace, SolidMask, LTXVAudioVAEEncode, GetNode, GetNode, GetNode, WujiCleaner, AudioConcat, Reroute, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, AudioSelectNode, SetNode, PreviewImage, SoundFlow_GetLength, ResizeImagesByLongerEdge, GetNode, SetNode, Note, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, SizeSelector, AudioSplitNode, SetNode, GetNode, MarkdownNote, PrimitiveStringMultiline, PrimitiveStringMultiline, PrimitiveStringMultiline, PrimitiveStringMultiline, PrimitiveStringMultiline, PrimitiveStringMultiline, PrimitiveStringMultiline, SetNode, SetNode, SelectImageString, GetNode, GetNode, Display Int (rgthree), CR Text, CR Text Replace, easy convertAnything, ShowText|pysssss, PreviewAudio, ImageStringBatch, PrimitiveStringMultiline, easy forLoopEnd, SetNode, SetNode, GetNode, GetNode, easy int, PrimitiveStringMultiline, VHS_VideoCombine, LoraLoaderModelOnly, Fast Groups Bypasser (rgthree), LoadImage, LoadAudio, AudioCrop, PrimitiveStringMultiline, LoadImage, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/商业级多图分镜数字人-LTX-2.3 Singularity-MV、口播等_2064156587920551937.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2064156587920551937.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（174 个）：
- `KSamplerSelect` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `RandomNoise`
- `RandomNoise`
- `CFGGuider`
- `CFGGuider`
- `LTXVLatentUpsampler` ★核心
- `LatentUpscaleModelLoader`
- `LTXVSeparateAVLatent`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `VAELoaderKJ`
- `SetNode`
- `VAELoaderKJ`
- `GetNode`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LTXVImgToVideoInplace`
- `SamplerCustomAdvanced` ★核心
- `LTXVConditioning`
- `GetNode`
- `SetNode`
- `SetNode`
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
- `GetNode`
- `SamplerCustomAdvanced` ★核心
- `SetNode`
- `GetNode`
- `MelBandRoFormerModelLoader`
- `SetNode`
- `LoadImage`
- `LoadImage`
- `WujiCleaner`
- `ImageScaleBy`
- `PreviewImage`
- `easy batchAnything`
- `MelBandRoFormerSampler` ★核心
- `PreviewAudio`
- `SoundFlow_TrimAudio`
- `LTXVAudioVAEDecode` ★核心
- `VAEDecode` ★核心
- `PathchSageAttentionKJ`
- `SetNode`
- `SetNode`
- `SetNode`
- `DualCLIPLoader`
- `GetNode`
- `ShowText|pysssss`
- `Dapao_LlamaChat`
- `ShowText|pysssss`
- `SetNode`
- `SetNode`
- `PreviewImage`
- `PreviewAudio`
- `easy showAnything`
- `easy forLoopStart`
- `Display Int (rgthree)`
- `SimpleMath+`
- `LTXVPreprocess`
- `GetNode`
- `easy imageSize`
- `EmptyLTXVLatentVideo`
- `PreviewImage`
- `LTXVSeparateAVLatent`
- `LTXVCropGuides`
- `GetNode`
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `SetLatentNoiseMask`
- `LTXVImgToVideoInplace`
- `SolidMask`
- `LTXVAudioVAEEncode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `WujiCleaner`
- `AudioConcat`
- `Reroute`
- `SetNode`
- `SetNode`
- `SetNode`
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
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `AudioSelectNode`
- `SetNode`
- `PreviewImage`
- `SoundFlow_GetLength`
- `ResizeImagesByLongerEdge`
- `GetNode`
- `SetNode`
- `Note`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `SizeSelector`
- `AudioSplitNode`
- `SetNode`
- `GetNode`
- `MarkdownNote`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `SetNode`
- `SetNode`
- `SelectImageString`
- `GetNode`
- `GetNode`
- `Display Int (rgthree)`
- `CR Text`
- `CR Text Replace`
- `easy convertAnything`
- `ShowText|pysssss`
- `PreviewAudio`
- `ImageStringBatch`
- `PrimitiveStringMultiline`
- `easy forLoopEnd`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `easy int`
- `PrimitiveStringMultiline`
- `VHS_VideoCombine`
- `LoraLoaderModelOnly` ★核心
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `LoadAudio`
- `AudioCrop`
- `PrimitiveStringMultiline`
- `LoadImage`
- `VHS_VideoCombine`

## 知识

覆盖率 **45%**（79/174）

**有卡**：`KSamplerSelect`、`CLIPTextEncode`、`ManualSigmas`、`LTXVConcatAVLatent`、`RandomNoise`、`CFGGuider`、`LTXVLatentUpsampler`、`LatentUpscaleModelLoader`、`LTXVSeparateAVLatent`、`VAELoaderKJ`、`UNETLoader`、`LTXVImgToVideoInplace`、`SamplerCustomAdvanced`、`LTXVConditioning`、`MelBandRoFormerModelLoader`、`LoadImage`、`WujiCleaner`、`ImageScaleBy`、`easy batchAnything`、`MelBandRoFormerSampler`、`PreviewAudio`、`SoundFlow_TrimAudio`、`LTXVAudioVAEDecode`、`VAEDecode`、`PathchSageAttentionKJ`、`DualCLIPLoader`、`Dapao_LlamaChat`、`easy forLoopStart`、`Display Int (rgthree)`、`SimpleMath+`、`LTXVPreprocess`、`easy imageSize`、`EmptyLTXVLatentVideo`、`LTXVCropGuides`、`SetLatentNoiseMask`、`SolidMask`、`LTXVAudioVAEEncode`、`AudioConcat`、`AudioSelectNode`、`SoundFlow_GetLength`、`ResizeImagesByLongerEdge`、`SizeSelector`、`AudioSplitNode`、`SelectImageString`、`CR Text`、`CR Text Replace`、`easy convertAnything`、`ImageStringBatch`、`easy forLoopEnd`、`easy int`、`VHS_VideoCombine`、`LoraLoaderModelOnly`、`LoadAudio`、`AudioCrop`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
