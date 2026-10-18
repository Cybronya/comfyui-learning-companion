---
key: 视频生成/图生视频/◙LTX2.3-无限FOR循环（Text+Image+Audio) to Video-V1.0_2039149145700700161.json
name: ◙LTX2.3-无限FOR循环（Text+Image+Audio) to Video-V1.0_2039149145700700161.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/◙LTX2.3-无限FOR循环（Text+Image+Audio) to Video-V1.0_2039149145700700161.json
hash: eef54fb47afecad3
coverage: 0.780731
learned_at: 2026-10-15 22:36:06
nodes: [ManualSigmas, EmptyLTXVLatentVideo, AudioSelectNode, AudioSelectNode, AudioSelectNode, PreviewImage, PreviewImage, ResizeImageMaskNode, CFGGuider, Reroute, Reroute, RandomNoise, AudioSelectNode, llama_cpp_parameters, Reroute, SimpleMath+, SamplerCustomAdvanced, KSamplerSelect, RandomNoise, LTXVAudioVAEEncode, llama_cpp_model_loader, PreviewImage, PreviewImage, easy showAnything, Reroute, Reroute, LTXVPreprocess, LTXVPreprocess, PreviewAudio, ImpactLogger, SolidMask, Reroute, Reroute, Reroute, Reroute, KSamplerSelect, LTXVScheduler, Reroute, Reroute, Reroute, Reroute, GetImageRangeFromBatch, VHS_GetImageCount, easy showAnything, Reroute, CFGGuider, LTXVConcatAVLatent, LTXVLatentUpsampler, Reroute, Reroute, Reroute, ImpactLogger, Reroute, Reroute, AudioSelectNode, PreviewAudio, PreviewAudio, PreviewAudio, PreviewAudio, PreviewAudio, AudioSplitNode, MarkdownNote, Reroute, Reroute, Reroute, ImageResizeKJv2, ImageResizeKJv2, Reroute, Reroute, Reroute, PreviewImage, PreviewImage, ResizeImageMaskNode, ImageResizeKJv2, PreviewImage, PreviewImage, ResizeImageMaskNode, Reroute, LTXVAudioVAEDecode, Reroute, CLIPTextEncode, easy forLoopStart, easy showAnything, MarkdownNote, MarkdownNote, Float, Audio Duration (mtb), ImpactLogger, ImpactLogger, CLIPTextEncode, SimpleMath+, MelBandRoFormerSampler, GetImageSize, Reroute, ImageConcatMulti, llama_cpp_instruct_adv, Reroute, Reroute, VHS_GetImageCount, easy showAnything, Reroute, PreviewImage, Reroute, VAEDecodeTiled, VAEDecodeTiled, LTXVSeparateAVLatent, GetImageRangeFromBatch, PrimitiveFloat, Setter, Setter, Getter, Setter, Getter, Getter, Getter, Getter, Getter, Getter, Getter, Getter, Getter, CR Float To Integer, Reroute, Getter, MelBandRoFormerModelLoader, Setter, Getter, Reroute, Setter, Getter, RHUploadZip, RHUploadZip, SimpleMath+, RHUploadZip, SimpleMath+, PathchSageAttentionKJ, VRAMReserver, easy cleanGpuUsed, LayerUtility: PurgeVRAM V2, Reroute, easy forLoopEnd, Reroute, Getter, Reroute, easy showAnything, Reroute, Getter, DualCLIPLoader, Setter, Getter, Setter, Setter, VAELoader, Setter, VAELoaderKJ, Setter, LatentUpscaleModelLoader, Setter, LTXVChunkFeedForward, LTX2_NAG, Setter, RHExtractImage, RHExtractImage, RHExtractImage, Getter, Getter, Getter, Getter, Getter, Getter, Getter, Getter, Getter, easy promptLine, Setter, Setter, Getter, Getter, Getter, Getter, Setter, Getter, LTXVConditioning, Setter, Getter, LTXVPreprocess, Getter, Getter, Getter, Getter, Getter, Setter, Getter, Getter, easy batchAnything, Getter, Getter, Getter, Getter, Getter, Getter, Setter, Reroute, AudioSelectNode, Setter, Getter, SetLatentNoiseMask, Setter, LTXVEmptyLatentAudio, Setter, Getter, Reroute, Getter, Getter, Setter, Getter, Setter, Setter, Reroute, Setter, Setter, Setter, Setter, Audio Resample (mtb), Setter, Getter, Getter, Getter, Setter, LTXVCropGuides, Getter, Getter, Getter, LTXVSeparateAVLatent, Setter, Getter, Getter, Getter, Setter, SamplerCustomAdvanced, Getter, Getter, Getter, Setter, Reroute, Getter, Getter, Getter, easy promptLine, Setter, Reroute, Getter, LTXVConditioning, Setter, Getter, Getter, LTXVAddGuideMulti, Reroute, LTXVConcatAVLatent, Getter, Setter, AudioConcatenate, VHS_VideoCombine, VHS_VideoCombine, Setter, VHS_VideoCombine, Setter, SimpleMath+, SimpleMath+, Getter, INTConstant, INTConstant, ResizeImagesByLongerEdge, ResizeImagesByLongerEdge, ResizeImagesByLongerEdge, easy showAnything, SimpleMath+, Setter, Int, Setter, EmptyAudio, Getter, Getter, Setter, Setter, Setter, Getter, Setter, Setter, UNETLoader, TrimAudioDuration, AudioEvenSplitNode, Setter, easy promptLine, LoadAudio, Getter, Getter, Setter, Reroute, MarkdownNote, MarkdownNote]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 30, "width": 97}
---

# 视频生成/图生视频/◙LTX2.3-无限FOR循环（Text+Image+Audio) to Video-V1.0_2039149145700700161.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2039149145700700161.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（301 个）：
- `ManualSigmas`
- `EmptyLTXVLatentVideo`
- `AudioSelectNode`
- `AudioSelectNode`
- `AudioSelectNode`
- `PreviewImage`
- `PreviewImage`
- `ResizeImageMaskNode`
- `CFGGuider`
- `Reroute`
- `Reroute`
- `RandomNoise`
- `AudioSelectNode`
- `llama_cpp_parameters`
- `Reroute`
- `SimpleMath+`
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
- `RandomNoise`
- `LTXVAudioVAEEncode` ★核心
- `llama_cpp_model_loader`
- `PreviewImage`
- `PreviewImage`
- `easy showAnything`
- `Reroute`
- `Reroute`
- `LTXVPreprocess`
- `LTXVPreprocess`
- `PreviewAudio`
- `ImpactLogger`
- `SolidMask`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `KSamplerSelect` ★核心
- `LTXVScheduler`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `GetImageRangeFromBatch`
- `VHS_GetImageCount`
- `easy showAnything`
- `Reroute`
- `CFGGuider`
- `LTXVConcatAVLatent`
- `LTXVLatentUpsampler` ★核心
- `Reroute`
- `Reroute`
- `Reroute`
- `ImpactLogger`
- `Reroute`
- `Reroute`
- `AudioSelectNode`
- `PreviewAudio`
- `PreviewAudio`
- `PreviewAudio`
- `PreviewAudio`
- `PreviewAudio`
- `AudioSplitNode`
- `MarkdownNote`
- `Reroute`
- `Reroute`
- `Reroute`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `Reroute`
- `Reroute`
- `Reroute`
- `PreviewImage`
- `PreviewImage`
- `ResizeImageMaskNode`
- `ImageResizeKJv2`
- `PreviewImage`
- `PreviewImage`
- `ResizeImageMaskNode`
- `Reroute`
- `LTXVAudioVAEDecode` ★核心
- `Reroute`
- `CLIPTextEncode` ★核心
- `easy forLoopStart`
- `easy showAnything`
- `MarkdownNote`
- `MarkdownNote`
- `Float`
- `Audio Duration (mtb)`
- `ImpactLogger`
- `ImpactLogger`
- `CLIPTextEncode` ★核心
- `SimpleMath+`
- `MelBandRoFormerSampler` ★核心
- `GetImageSize`
- `Reroute`
- `ImageConcatMulti`
- `llama_cpp_instruct_adv`
- `Reroute`
- `Reroute`
- `VHS_GetImageCount`
- `easy showAnything`
- `Reroute`
- `PreviewImage`
- `Reroute`
- `VAEDecodeTiled` ★核心
- `VAEDecodeTiled` ★核心
- `LTXVSeparateAVLatent`
- `GetImageRangeFromBatch`
- `PrimitiveFloat`
- `Setter`
- `Setter`
- `Getter`
- `Setter`
- `Getter`
- `Getter`
- `Getter`
- `Getter`
- `Getter`
- `Getter`
- `Getter`
- `Getter`
- `Getter`
- `CR Float To Integer`
- `Reroute`
- `Getter`
- `MelBandRoFormerModelLoader`
- `Setter`
- `Getter`
- `Reroute`
- `Setter`
- `Getter`
- `RHUploadZip`
- `RHUploadZip`
- `SimpleMath+`
- `RHUploadZip`
- `SimpleMath+`
- `PathchSageAttentionKJ`
- `VRAMReserver`
- `easy cleanGpuUsed`
- `LayerUtility: PurgeVRAM V2`
- `Reroute`
- `easy forLoopEnd`
- `Reroute`
- `Getter`
- `Reroute`
- `easy showAnything`
- `Reroute`
- `Getter`
- `DualCLIPLoader`
- `Setter`
- `Getter`
- `Setter`
- `Setter`
- `VAELoader`
- `Setter`
- `VAELoaderKJ`
- `Setter`
- `LatentUpscaleModelLoader`
- `Setter`
- `LTXVChunkFeedForward`
- `LTX2_NAG`
- `Setter`
- `RHExtractImage`
- `RHExtractImage`
- `RHExtractImage`
- `Getter`
- `Getter`
- `Getter`
- `Getter`
- `Getter`
- `Getter`
- `Getter`
- `Getter`
- `Getter`
- `easy promptLine`
- `Setter`
- `Setter`
- `Getter`
- `Getter`
- `Getter`
- `Getter`
- `Setter`
- `Getter`
- `LTXVConditioning`
- `Setter`
- `Getter`
- `LTXVPreprocess`
- `Getter`
- `Getter`
- `Getter`
- `Getter`
- `Getter`
- `Setter`
- `Getter`
- `Getter`
- `easy batchAnything`
- `Getter`
- `Getter`
- `Getter`
- `Getter`
- `Getter`
- `Getter`
- `Setter`
- `Reroute`
- `AudioSelectNode`
- `Setter`
- `Getter`
- `SetLatentNoiseMask`
- `Setter`
- `LTXVEmptyLatentAudio` ★核心
- `Setter`
- `Getter`
- `Reroute`
- `Getter`
- `Getter`
- `Setter`
- `Getter`
- `Setter`
- `Setter`
- `Reroute`
- `Setter`
- `Setter`
- `Setter`
- `Setter`
- `Audio Resample (mtb)`
- `Setter`
- `Getter`
- `Getter`
- `Getter`
- `Setter`
- `LTXVCropGuides`
- `Getter`
- `Getter`
- `Getter`
- `LTXVSeparateAVLatent`
- `Setter`
- `Getter`
- `Getter`
- `Getter`
- `Setter`
- `SamplerCustomAdvanced` ★核心
- `Getter`
- `Getter`
- `Getter`
- `Setter`
- `Reroute`
- `Getter`
- `Getter`
- `Getter`
- `easy promptLine`
- `Setter`
- `Reroute`
- `Getter`
- `LTXVConditioning`
- `Setter`
- `Getter`
- `Getter`
- `LTXVAddGuideMulti`
- `Reroute`
- `LTXVConcatAVLatent`
- `Getter`
- `Setter`
- `AudioConcatenate`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `Setter`
- `VHS_VideoCombine`
- `Setter`
- `SimpleMath+`
- `SimpleMath+`
- `Getter`
- `INTConstant`
- `INTConstant`
- `ResizeImagesByLongerEdge`
- `ResizeImagesByLongerEdge`
- `ResizeImagesByLongerEdge`
- `easy showAnything`
- `SimpleMath+`
- `Setter`
- `Int`
- `Setter`
- `EmptyAudio`
- `Getter`
- `Getter`
- `Setter`
- `Setter`
- `Setter`
- `Getter`
- `Setter`
- `Setter`
- `UNETLoader` ★核心
- `TrimAudioDuration`
- `AudioEvenSplitNode`
- `Setter`
- `easy promptLine`
- `LoadAudio`
- `Getter`
- `Getter`
- `Setter`
- `Reroute`
- `MarkdownNote`
- `MarkdownNote`

## 关键参数

- `width` = `97`
- `height` = `30`
- `batch_size` = `1`

## 知识

覆盖率 **78%**（235/301）

**有卡**：`ManualSigmas`、`EmptyLTXVLatentVideo`、`AudioSelectNode`、`ResizeImageMaskNode`、`CFGGuider`、`RandomNoise`、`llama_cpp_parameters`、`SimpleMath+`、`SamplerCustomAdvanced`、`KSamplerSelect`、`LTXVAudioVAEEncode`、`llama_cpp_model_loader`、`LTXVPreprocess`、`PreviewAudio`、`ImpactLogger`、`SolidMask`、`LTXVScheduler`、`GetImageRangeFromBatch`、`VHS_GetImageCount`、`LTXVConcatAVLatent`、`LTXVLatentUpsampler`、`AudioSplitNode`、`ImageResizeKJv2`、`LTXVAudioVAEDecode`、`CLIPTextEncode`、`easy forLoopStart`、`Float`、`Audio Duration (mtb)`、`MelBandRoFormerSampler`、`GetImageSize`、`ImageConcatMulti`、`llama_cpp_instruct_adv`、`VAEDecodeTiled`、`LTXVSeparateAVLatent`、`Setter`、`Getter`、`CR Float To Integer`、`MelBandRoFormerModelLoader`、`RHUploadZip`、`PathchSageAttentionKJ`、`VRAMReserver`、`easy cleanGpuUsed`、`LayerUtility: PurgeVRAM V2`、`easy forLoopEnd`、`DualCLIPLoader`、`VAELoader`、`VAELoaderKJ`、`LatentUpscaleModelLoader`、`LTXVChunkFeedForward`、`LTX2_NAG`、`RHExtractImage`、`easy promptLine`、`LTXVConditioning`、`easy batchAnything`、`SetLatentNoiseMask`、`LTXVEmptyLatentAudio`、`Audio Resample (mtb)`、`LTXVCropGuides`、`LTXVAddGuideMulti`、`AudioConcatenate`、`VHS_VideoCombine`、`INTConstant`、`ResizeImagesByLongerEdge`、`Int`、`EmptyAudio`、`UNETLoader`、`TrimAudioDuration`、`AudioEvenSplitNode`、`LoadAudio`

**用到的条目**：VAELoader、CLIPTextEncode、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、MelBandRoFormerSampler、LTXVLatentUpsampler
