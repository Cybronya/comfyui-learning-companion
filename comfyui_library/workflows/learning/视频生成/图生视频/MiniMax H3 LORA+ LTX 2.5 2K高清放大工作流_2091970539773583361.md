---
key: 视频生成/图生视频/MiniMax H3 LORA+ LTX 2.5 2K高清放大工作流_2091970539773583361.json
name: MiniMax H3 LORA+ LTX 2.5 2K高清放大工作流_2091970539773583361
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/MiniMax H3 LORA+ LTX 2.5 2K高清放大工作流_2091970539773583361.json
hash: 7eacff59bbce76ac
coverage: 0.858268
learned_at: 2026-10-16 22:30:36
nodes: [LoadAudio, LoadAudio, RandomNoise, RandomNoise, PlaySound|pysssss, llama_cpp_parameters, LayerUtility: PurgeVRAM V2, easy cleanGpuUsed, BasicGuider, SamplerCustomAdvanced, KSamplerSelect, LayerUtility: PurgeVRAM V2, easy cleanGpuUsed, LayerUtility: PurgeVRAM V2, ShowText|pysssss, ComfyMathExpression, PixaromaDuration, Switch any [Crystools], easy seed, MiniMaxH3AVDecodeT8, LTXVDualCFGGuider, LTX2MemoryEfficientSageAttentionPatch, LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, VAELoader, LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, ModelAttentionBackend, CLIPTextEncode, KSamplerSelect, CR Text, ImageResizeKJv2, ImageResizeKJv2, ImageResizeKJv2, PT_H3ConcatAVLatent, BasicGuider, PrimitiveNode, VAEEncode, VAEEncodeAudio, easy cleanGpuUsed, TrimAudioDuration, AudioConcat, VAEDecode, ImageResizeKJv2, VHS_VideoCombine, VHS_VideoCombine, Fast Groups Bypasser (rgthree), LoadImage, ResolutionSelector, Fast Groups Bypasser (rgthree), easy cleanGpuUsed, LTXVConcatAVLatent, PixaromaLabel, PixaromaLabel, LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, VAELoader, LayerUtility: PurgeVRAM V2, PathchSageAttentionKJ, MiniMaxLowVRAMAttention, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxChunkFeedForward, VAELoader, PixaromaLabel, RandomNoise, LTXVSeparateAVLatent, ImageBatchMulti, LoadImage, ImageResizeKJv2, ImageResizeKJv2, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), ImageBatchMulti, LoadImage, MarkdownNote, Any Switch (rgthree), PreviewImage, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), MiniMaxH3DualClockSamplerT8, SamplerCustomAdvanced, BasicScheduler, MiniMaxH3AudioConditioningT8, VAEEncode, LTXVAudioVAEEncode, LTXVConditioning, LTXVImgToVideoInplace, LTXVLatentUpsampler, easy cleanGpuUsed, NotifyPixaroma, LTXVAudioVAEDecode, SamplerCustomAdvanced, VHS_VideoCombine, CLIPTextEncode, VAEDecodeTiled, BasicScheduler, ImageCASharpening+, ImageCASharpening+, UNETLoader, CLIPLoader, ModelAttentionBackend, LoraLoaderModelOnly, LoadImage, LoadImage, llama_cpp_model_loader, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, VAELoader, CLIPLoader, LoadVideoUI, LatentUpscaleModelLoader, LoadImage, LoadImage, MarkdownNote, llama_cpp_instruct_adv, LoadImage, CR Text, Primitive boolean [Crystools], PixaromaLabel, RHHiddenNodes]
patterns: []
missing: []
---

# 视频生成/图生视频/MiniMax H3 LORA+ LTX 2.5 2K高清放大工作流_2091970539773583361.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/MiniMax H3 LORA+ LTX 2.5 2K高清放大工作流_2091970539773583361.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（127 个）：
- `LoadAudio`
- `LoadAudio`
- `RandomNoise`
- `RandomNoise`
- `PlaySound|pysssss`
- `llama_cpp_parameters`
- `LayerUtility: PurgeVRAM V2`
- `easy cleanGpuUsed`
- `BasicGuider`
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
- `LayerUtility: PurgeVRAM V2`
- `easy cleanGpuUsed`
- `LayerUtility: PurgeVRAM V2`
- `ShowText|pysssss`
- `ComfyMathExpression`
- `PixaromaDuration`
- `Switch any [Crystools]`
- `easy seed`
- `MiniMaxH3AVDecodeT8`
- `LTXVDualCFGGuider`
- `LTX2MemoryEfficientSageAttentionPatch`
- `LayerUtility: PurgeVRAM V2`
- `LayerUtility: PurgeVRAM V2`
- `VAELoader`
- `LayerUtility: PurgeVRAM V2`
- `LayerUtility: PurgeVRAM V2`
- `ModelAttentionBackend`
- `CLIPTextEncode` ★核心
- `KSamplerSelect` ★核心
- `CR Text`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `PT_H3ConcatAVLatent`
- `BasicGuider`
- `PrimitiveNode`
- `VAEEncode` ★核心
- `VAEEncodeAudio` ★核心
- `easy cleanGpuUsed`
- `TrimAudioDuration`
- `AudioConcat`
- `VAEDecode` ★核心
- `ImageResizeKJv2`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `ResolutionSelector`
- `Fast Groups Bypasser (rgthree)`
- `easy cleanGpuUsed`
- `LTXVConcatAVLatent`
- `PixaromaLabel`
- `PixaromaLabel`
- `LayerUtility: PurgeVRAM V2`
- `LayerUtility: PurgeVRAM V2`
- `VAELoader`
- `LayerUtility: PurgeVRAM V2`
- `PathchSageAttentionKJ`
- `MiniMaxLowVRAMAttention`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxChunkFeedForward`
- `VAELoader`
- `PixaromaLabel`
- `RandomNoise`
- `LTXVSeparateAVLatent`
- `ImageBatchMulti`
- `LoadImage`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `ImageBatchMulti`
- `LoadImage`
- `MarkdownNote`
- `Any Switch (rgthree)`
- `PreviewImage`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `MiniMaxH3DualClockSamplerT8` ★核心
- `SamplerCustomAdvanced` ★核心
- `BasicScheduler`
- `MiniMaxH3AudioConditioningT8`
- `VAEEncode` ★核心
- `LTXVAudioVAEEncode` ★核心
- `LTXVConditioning`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler` ★核心
- `easy cleanGpuUsed`
- `NotifyPixaroma`
- `LTXVAudioVAEDecode` ★核心
- `SamplerCustomAdvanced` ★核心
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `VAEDecodeTiled` ★核心
- `BasicScheduler`
- `ImageCASharpening+`
- `ImageCASharpening+`
- `UNETLoader` ★核心
- `CLIPLoader`
- `ModelAttentionBackend`
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `LoadImage`
- `llama_cpp_model_loader`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `CLIPLoader`
- `LoadVideoUI`
- `LatentUpscaleModelLoader`
- `LoadImage`
- `LoadImage`
- `MarkdownNote`
- `llama_cpp_instruct_adv`
- `LoadImage`
- `CR Text`
- `Primitive boolean [Crystools]`
- `PixaromaLabel`
- `RHHiddenNodes`

## 知识

覆盖率 **86%**（109/127）

**有卡**：`LoadAudio`、`RandomNoise`、`PlaySound|pysssss`、`llama_cpp_parameters`、`LayerUtility: PurgeVRAM V2`、`easy cleanGpuUsed`、`BasicGuider`、`SamplerCustomAdvanced`、`KSamplerSelect`、`ComfyMathExpression`、`PixaromaDuration`、`Switch any [Crystools]`、`easy seed`、`MiniMaxH3AVDecodeT8`、`LTXVDualCFGGuider`、`LTX2MemoryEfficientSageAttentionPatch`、`VAELoader`、`ModelAttentionBackend`、`CLIPTextEncode`、`CR Text`、`ImageResizeKJv2`、`PT_H3ConcatAVLatent`、`VAEEncode`、`VAEEncodeAudio`、`TrimAudioDuration`、`AudioConcat`、`VAEDecode`、`VHS_VideoCombine`、`LoadImage`、`ResolutionSelector`、`LTXVConcatAVLatent`、`PixaromaLabel`、`PathchSageAttentionKJ`、`MiniMaxLowVRAMAttention`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`MiniMaxChunkFeedForward`、`LTXVSeparateAVLatent`、`ImageBatchMulti`、`MiniMaxH3DualClockSamplerT8`、`BasicScheduler`、`MiniMaxH3AudioConditioningT8`、`LTXVAudioVAEEncode`、`LTXVConditioning`、`LTXVImgToVideoInplace`、`LTXVLatentUpsampler`、`NotifyPixaroma`、`LTXVAudioVAEDecode`、`VAEDecodeTiled`、`ImageCASharpening+`、`UNETLoader`、`CLIPLoader`、`LoraLoaderModelOnly`、`llama_cpp_model_loader`、`LoadVideoUI`、`LatentUpscaleModelLoader`、`llama_cpp_instruct_adv`、`Primitive boolean [Crystools]`、`RHHiddenNodes`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader
