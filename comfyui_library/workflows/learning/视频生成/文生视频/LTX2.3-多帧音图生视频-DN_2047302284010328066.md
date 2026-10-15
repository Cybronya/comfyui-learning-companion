---
key: 视频生成/文生视频/LTX2.3-多帧音图生视频-DN_2047302284010328066.json
name: LTX2.3-多帧音图生视频-DN_2047302284010328066
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.3-多帧音图生视频-DN_2047302284010328066.json
hash: a74ead97ffc89bf7
coverage: 0.481081
learned_at: 2026-10-15 22:45:03
nodes: [SetNode, GetNode, AudioSeparation, GetNode, SetNode, SetLatentNoiseMask, SetNode, LTXVEmptyLatentAudio, GetNode, GetNode, SetNode, CLIPTextEncode, GetNode, Audio Duration (mtb), SetNode, SetNode, SetNode, GetNode, SetNode, LTXVSeparateAVLatent, SamplerCustomAdvanced, GetNode, LTXVConditioning, LTXVConcatAVLatent, SetNode, SetNode, GetNode, GetNode, GetNode, KSamplerSelect, GetNode, GetNode, PrimitiveStringMultiline, GetNode, SetNode, GetNode, LTXVAudioVAEDecode, SamplerCustomAdvanced, VAELoader, PrimitiveStringMultiline, GetNode, SetNode, GetNode, LTXVPreprocess, KSamplerSelect, LTXVSeparateAVLatent, GetNode, LatentUpscaleModelLoader, PreviewAudio, ComfyMathExpression, SetNode, GetNode, PreviewAudio, easy showAnything, ComfySwitchNode, GetNode, ComfyMathExpression, ComfyMathExpression, LTXVChunkFeedForward, EmptyLTXVLatentVideo, GetNode, GetNode, GetNode, PrimitiveStringMultiline, llama_cpp_instruct_adv, ComfySwitchNode, SetNode, GetNode, GetNode, PathchSageAttentionKJ, GetNode, CLIPTextEncode, LTXVTiledVAEDecode, ImageScaleBy, LTXVAudioVAEDecode, ComfySwitchNode, CFGGuider, GetNode, CFGGuider, GetNode, LoadAudio, GetNode, LTXVReferenceAudio, LTXSequencer, LTXVReferenceAudio, PrimitiveString, Pick From Batch (mtb), GetNode, ComfySwitchNode, LTXVTiledVAEDecode, Pick From Batch (mtb), LTXVEnhanceAVideoKJ, GetNode, LTXVEnhanceAVideoKJ, GetNode, GetNode, GetNode, GetNode, RandomNoise, RandomNoise, GetNode, GetNode, GetNode, ComfyMathExpression, ComfyMathExpression, TrimAudioDuration, GetImageSize, ResizeImageMaskNode, GetImageSize, SetNode, SetNode, SetNode, SetNode, GetNode, SolidMask, SetNode, LTXVAudioVAEEncode, SetNode, LTX2SamplingPreviewOverride, LTX2_NAG, CLIPTextEncode, LTXVLatentUpsampler, ManualSigmas, LTXVConcatAVLatent, ManualSigmas, Reroute, GetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, PrimitiveFloat, llama_cpp_parameters, LTXSequencer, VAELoaderKJ, VAELoaderKJ, UNETLoader, PrimitiveStringMultiline, llama_cpp_model_loader, DualCLIPLoader, LoraLoader, LoraLoaderModelOnly, VHS_LoadVideoFFmpeg, LoadAudio, SetReserveVRAM, LoadImage, GetNode, Lora Loader Stack (rgthree), Lora Loader Stack (rgthree), PrimitiveFloat, PrimitiveBoolean, INTConstant, Reroute, CFGGuider, Reroute, Reroute, CFGGuider, GetNode, LoraLoaderModelOnly, LTXVImgToVideoInplace, LTXVImgToVideoInplace, Switch any [Crystools], Switch any [Crystools], GetNode, Switch any [Crystools], GetNode, SetNode, Switch any [Crystools], GetNode, PrimitiveString, GetNode, PrimitiveBoolean, MultiImageLoader, VHS_VideoCombine, PreviewAny, VHS_VideoCombine, ResizeImagesByLongerEdge, PrimitiveFloat, Note, Fast Groups Bypasser (rgthree), Note]
patterns: [lora]
missing: []
parameters: {"batch_size": 1, "height": 25, "lora_name": "gemma-3-12b-it-abliterated_heretic_lora_rank64_bf16.safetensors", "strength_clip": 1, "strength_model": 1, "width": 121}
---

# 视频生成/文生视频/LTX2.3-多帧音图生视频-DN_2047302284010328066.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.3-多帧音图生视频-DN_2047302284010328066.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Other

**节点**（185 个）：
- `SetNode`
- `GetNode`
- `AudioSeparation`
- `GetNode`
- `SetNode`
- `SetLatentNoiseMask`
- `SetNode`
- `LTXVEmptyLatentAudio` ★核心
- `GetNode`
- `GetNode`
- `SetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `Audio Duration (mtb)`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `GetNode`
- `LTXVConditioning`
- `LTXVConcatAVLatent`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `KSamplerSelect` ★核心
- `GetNode`
- `GetNode`
- `PrimitiveStringMultiline`
- `GetNode`
- `SetNode`
- `GetNode`
- `LTXVAudioVAEDecode` ★核心
- `SamplerCustomAdvanced` ★核心
- `VAELoader`
- `PrimitiveStringMultiline`
- `GetNode`
- `SetNode`
- `GetNode`
- `LTXVPreprocess`
- `KSamplerSelect` ★核心
- `LTXVSeparateAVLatent`
- `GetNode`
- `LatentUpscaleModelLoader`
- `PreviewAudio`
- `ComfyMathExpression`
- `SetNode`
- `GetNode`
- `PreviewAudio`
- `easy showAnything`
- `ComfySwitchNode`
- `GetNode`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `LTXVChunkFeedForward`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `GetNode`
- `GetNode`
- `PrimitiveStringMultiline`
- `llama_cpp_instruct_adv`
- `ComfySwitchNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `PathchSageAttentionKJ`
- `GetNode`
- `CLIPTextEncode` ★核心
- `LTXVTiledVAEDecode` ★核心
- `ImageScaleBy`
- `LTXVAudioVAEDecode` ★核心
- `ComfySwitchNode`
- `CFGGuider`
- `GetNode`
- `CFGGuider`
- `GetNode`
- `LoadAudio`
- `GetNode`
- `LTXVReferenceAudio`
- `LTXSequencer`
- `LTXVReferenceAudio`
- `PrimitiveString`
- `Pick From Batch (mtb)`
- `GetNode`
- `ComfySwitchNode`
- `LTXVTiledVAEDecode` ★核心
- `Pick From Batch (mtb)`
- `LTXVEnhanceAVideoKJ`
- `GetNode`
- `LTXVEnhanceAVideoKJ`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `RandomNoise`
- `RandomNoise`
- `GetNode`
- `GetNode`
- `GetNode`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `TrimAudioDuration`
- `GetImageSize`
- `ResizeImageMaskNode`
- `GetImageSize`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `SolidMask`
- `SetNode`
- `LTXVAudioVAEEncode` ★核心
- `SetNode`
- `LTX2SamplingPreviewOverride`
- `LTX2_NAG`
- `CLIPTextEncode` ★核心
- `LTXVLatentUpsampler` ★核心
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `ManualSigmas`
- `Reroute`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `PrimitiveFloat`
- `llama_cpp_parameters`
- `LTXSequencer`
- `VAELoaderKJ`
- `VAELoaderKJ`
- `UNETLoader` ★核心
- `PrimitiveStringMultiline`
- `llama_cpp_model_loader`
- `DualCLIPLoader`
- `LoraLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `VHS_LoadVideoFFmpeg`
- `LoadAudio`
- `SetReserveVRAM`
- `LoadImage`
- `GetNode`
- `Lora Loader Stack (rgthree)`
- `Lora Loader Stack (rgthree)`
- `PrimitiveFloat`
- `PrimitiveBoolean`
- `INTConstant`
- `Reroute`
- `CFGGuider`
- `Reroute`
- `Reroute`
- `CFGGuider`
- `GetNode`
- `LoraLoaderModelOnly` ★核心
- `LTXVImgToVideoInplace`
- `LTXVImgToVideoInplace`
- `Switch any [Crystools]`
- `Switch any [Crystools]`
- `GetNode`
- `Switch any [Crystools]`
- `GetNode`
- `SetNode`
- `Switch any [Crystools]`
- `GetNode`
- `PrimitiveString`
- `GetNode`
- `PrimitiveBoolean`
- `MultiImageLoader`
- `VHS_VideoCombine`
- `PreviewAny`
- `VHS_VideoCombine`
- `ResizeImagesByLongerEdge`
- `PrimitiveFloat`
- `Note`
- `Fast Groups Bypasser (rgthree)`
- `Note`

**识别到的模式**：lora

## 关键参数

- `width` = `121`
- `height` = `25`
- `batch_size` = `1`
- `lora_name` = `gemma-3-12b-it-abliterated_heretic_lora_rank64_bf16.safetensors`
- `strength_model` = `1`
- `strength_clip` = `1`

## 知识

覆盖率 **48%**（89/185）

**有卡**：`AudioSeparation`、`SetLatentNoiseMask`、`LTXVEmptyLatentAudio`、`CLIPTextEncode`、`Audio Duration (mtb)`、`LTXVSeparateAVLatent`、`SamplerCustomAdvanced`、`LTXVConditioning`、`LTXVConcatAVLatent`、`KSamplerSelect`、`LTXVAudioVAEDecode`、`VAELoader`、`LTXVPreprocess`、`LatentUpscaleModelLoader`、`PreviewAudio`、`ComfyMathExpression`、`LTXVChunkFeedForward`、`EmptyLTXVLatentVideo`、`llama_cpp_instruct_adv`、`PathchSageAttentionKJ`、`LTXVTiledVAEDecode`、`ImageScaleBy`、`CFGGuider`、`LoadAudio`、`LTXVReferenceAudio`、`LTXSequencer`、`Pick From Batch (mtb)`、`LTXVEnhanceAVideoKJ`、`RandomNoise`、`TrimAudioDuration`、`GetImageSize`、`ResizeImageMaskNode`、`SolidMask`、`LTXVAudioVAEEncode`、`LTX2SamplingPreviewOverride`、`LTX2_NAG`、`LTXVLatentUpsampler`、`ManualSigmas`、`llama_cpp_parameters`、`VAELoaderKJ`、`UNETLoader`、`llama_cpp_model_loader`、`DualCLIPLoader`、`LoraLoader`、`LoraLoaderModelOnly`、`VHS_LoadVideoFFmpeg`、`SetReserveVRAM`、`LoadImage`、`Lora Loader Stack (rgthree)`、`PrimitiveBoolean`、`INTConstant`、`LTXVImgToVideoInplace`、`Switch any [Crystools]`、`MultiImageLoader`、`VHS_VideoCombine`、`ResizeImagesByLongerEdge`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
