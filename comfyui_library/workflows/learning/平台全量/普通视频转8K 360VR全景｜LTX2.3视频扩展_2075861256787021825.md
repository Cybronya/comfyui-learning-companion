---
key: 平台全量/普通视频转8K 360VR全景｜LTX2.3视频扩展_2075861256787021825.json
name: 普通视频转8K 360VR全景｜LTX2.3视频扩展_2075861256787021825
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/普通视频转8K 360VR全景｜LTX2.3视频扩展_2075861256787021825.json
hash: e9c5f0d3f8e6c312
coverage: 0.978723
learned_at: 2026-11-14 02:13:31
nodes: [Note, LatentUpscaleModelLoader, VAELoaderKJ, UNETLoader, VAELoaderKJ, LTXICLoRALoaderModelOnly, VHS_VideoInfo, RectilinearToEquirect, LTXAVTextEncoderLoader, ResizeImageMaskNode, ResizeImageMaskNode, GetImageSize, CLIPTextEncode, CLIPTextEncode, LTXVConditioning, EquirectCircularVAE, LTXVPreprocess, EmptyLTXVLatentVideo, CM_FloatToInt, LTXVEmptyLatentAudio, LTXVConcatAVLatent, LTXAddVideoICLoRAGuide, LTXVImgToVideoConditionOnly, RandomNoise, EquirectWrappedNoise, LTX2_NAG, KSamplerSelect, ManualSigmas, LTXVChunkFeedForward, EquirectPerStepRoll, CFGGuider, LTXVCropGuides, LTXVSeparateAVLatent, SamplerCustomAdvanced, LTXVLatentUpsampler, VAEDecodeTiled, VAEEncodeTiled, TutuEquirectSourceComposite, LTXVLatentUpsampler, VAEDecodeTiled, ImageCrop, TutuEquirectSourceComposite, TutuEquirectImageLongitudeRoll, UpscaleModelLoader, VHS_LoadVideo, VHS_VideoCombine, TutuStreamUpscaleVideo]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 平台全量/普通视频转8K 360VR全景｜LTX2.3视频扩展_2075861256787021825.json

> 来源文件 `comfyui_library/workflows/平台全量/普通视频转8K 360VR全景｜LTX2.3视频扩展_2075861256787021825.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Other

**节点**（47 个）：
- `Note`
- `LatentUpscaleModelLoader`
- `VAELoaderKJ`
- `UNETLoader` ★核心
- `VAELoaderKJ`
- `LTXICLoRALoaderModelOnly` ★核心
- `VHS_VideoInfo`
- `RectilinearToEquirect`
- `LTXAVTextEncoderLoader`
- `ResizeImageMaskNode`
- `ResizeImageMaskNode`
- `GetImageSize`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `EquirectCircularVAE`
- `LTXVPreprocess`
- `EmptyLTXVLatentVideo`
- `CM_FloatToInt`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVConcatAVLatent`
- `LTXAddVideoICLoRAGuide`
- `LTXVImgToVideoConditionOnly`
- `RandomNoise`
- `EquirectWrappedNoise`
- `LTX2_NAG`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LTXVChunkFeedForward`
- `EquirectPerStepRoll`
- `CFGGuider`
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVLatentUpsampler` ★核心
- `VAEDecodeTiled` ★核心
- `VAEEncodeTiled` ★核心
- `TutuEquirectSourceComposite`
- `LTXVLatentUpsampler` ★核心
- `VAEDecodeTiled` ★核心
- `ImageCrop`
- `TutuEquirectSourceComposite`
- `TutuEquirectImageLongitudeRoll`
- `UpscaleModelLoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `TutuStreamUpscaleVideo`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **98%**（46/47）

**有卡**：`LatentUpscaleModelLoader`、`VAELoaderKJ`、`UNETLoader`、`LTXICLoRALoaderModelOnly`、`VHS_VideoInfo`、`RectilinearToEquirect`、`LTXAVTextEncoderLoader`、`ResizeImageMaskNode`、`GetImageSize`、`CLIPTextEncode`、`LTXVConditioning`、`EquirectCircularVAE`、`LTXVPreprocess`、`EmptyLTXVLatentVideo`、`CM_FloatToInt`、`LTXVEmptyLatentAudio`、`LTXVConcatAVLatent`、`LTXAddVideoICLoRAGuide`、`LTXVImgToVideoConditionOnly`、`RandomNoise`、`EquirectWrappedNoise`、`LTX2_NAG`、`KSamplerSelect`、`ManualSigmas`、`LTXVChunkFeedForward`、`EquirectPerStepRoll`、`CFGGuider`、`LTXVCropGuides`、`LTXVSeparateAVLatent`、`SamplerCustomAdvanced`、`LTXVLatentUpsampler`、`VAEDecodeTiled`、`VAEEncodeTiled`、`TutuEquirectSourceComposite`、`ImageCrop`、`TutuEquirectImageLongitudeRoll`、`UpscaleModelLoader`、`VHS_LoadVideo`、`VHS_VideoCombine`、`TutuStreamUpscaleVideo`

**用到的条目**：CLIPTextEncode、UNETLoader、CFGGuider、KSamplerSelect、LTXVLatentUpsampler、SamplerCustomAdvanced、EmptyLTXVLatentVideo、LatentUpscaleModelLoader
