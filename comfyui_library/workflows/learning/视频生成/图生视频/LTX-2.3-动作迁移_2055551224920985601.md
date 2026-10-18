---
key: 视频生成/图生视频/LTX-2.3-动作迁移_2055551224920985601.json
name: LTX-2.3-动作迁移_2055551224920985601.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX-2.3-动作迁移_2055551224920985601.json
hash: f4baf946a1c527eb
coverage: 0.528736
learned_at: 2026-10-15 22:37:57
nodes: [LTXVConditioning, CLIPTextEncode, EmptyLTXVLatentVideo, LTXVImgToVideoConditionOnly, LTXVPreprocess, LTXVEmptyLatentAudio, LTXVConcatAVLatent, CFGGuider, SamplerCustomAdvanced, RandomNoise, LTXVSeparateAVLatent, LTXVAudioVAEDecode, VAEDecodeTiled, LTXAddVideoICLoRAGuide, LTXVCropGuides, ManualSigmas, ResizeImageMaskNode, CR Float To Integer, VHS_VideoInfoLoaded, SetNode, GetNode, SetNode, SetNode, PreviewImage, GetNode, GetNode, GetNode, Reroute, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, SetNode, GetNode, SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetImageSize, LTXVAudioVAEEncode, SolidMask, SetLatentNoiseMask, ComfySwitchNode, GetNode, GetNode, MathExpression|pysssss, easy showAnything, LTXVSpatioTemporalTiledVAEDecode, KSamplerSelect, SetNode, SetNode, SetNode, SetNode, SetNode, VAELoaderKJ, VAELoader, SigmasPreview, GetImageSize, VHS_VideoCombine, GetNode, VHS_VideoCombine, GetNode, ImageResizeKJv2, PrimitiveBoolean, ImageResizeKJv2, DepthAnythingV2Preprocessor, CannyEdgePreprocessor, UNETLoader, PathchSageAttentionKJ, LTXVChunkFeedForward, LTXICLoRALoaderModelOnly, DualCLIPLoader, VHS_LoadVideo, CLIPTextEncode, DWPreprocessor, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX-2.3-动作迁移_2055551224920985601.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2055551224920985601.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（87 个）：
- `LTXVConditioning`
- `CLIPTextEncode` ★核心
- `EmptyLTXVLatentVideo`
- `LTXVImgToVideoConditionOnly`
- `LTXVPreprocess`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVConcatAVLatent`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `VAEDecodeTiled` ★核心
- `LTXAddVideoICLoRAGuide`
- `LTXVCropGuides`
- `ManualSigmas`
- `ResizeImageMaskNode`
- `CR Float To Integer`
- `VHS_VideoInfoLoaded`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `PreviewImage`
- `GetNode`
- `GetNode`
- `GetNode`
- `Reroute`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
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
- `GetImageSize`
- `LTXVAudioVAEEncode` ★核心
- `SolidMask`
- `SetLatentNoiseMask`
- `ComfySwitchNode`
- `GetNode`
- `GetNode`
- `MathExpression|pysssss`
- `easy showAnything`
- `LTXVSpatioTemporalTiledVAEDecode` ★核心
- `KSamplerSelect` ★核心
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `VAELoaderKJ`
- `VAELoader`
- `SigmasPreview`
- `GetImageSize`
- `VHS_VideoCombine`
- `GetNode`
- `VHS_VideoCombine`
- `GetNode`
- `ImageResizeKJv2`
- `PrimitiveBoolean`
- `ImageResizeKJv2`
- `DepthAnythingV2Preprocessor`
- `CannyEdgePreprocessor`
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `LTXVChunkFeedForward`
- `LTXICLoRALoaderModelOnly` ★核心
- `DualCLIPLoader`
- `VHS_LoadVideo`
- `CLIPTextEncode` ★核心
- `DWPreprocessor`
- `LoadImage`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **53%**（46/87）

**有卡**：`LTXVConditioning`、`CLIPTextEncode`、`EmptyLTXVLatentVideo`、`LTXVImgToVideoConditionOnly`、`LTXVPreprocess`、`LTXVEmptyLatentAudio`、`LTXVConcatAVLatent`、`CFGGuider`、`SamplerCustomAdvanced`、`RandomNoise`、`LTXVSeparateAVLatent`、`LTXVAudioVAEDecode`、`VAEDecodeTiled`、`LTXAddVideoICLoRAGuide`、`LTXVCropGuides`、`ManualSigmas`、`ResizeImageMaskNode`、`CR Float To Integer`、`VHS_VideoInfoLoaded`、`GetImageSize`、`LTXVAudioVAEEncode`、`SolidMask`、`SetLatentNoiseMask`、`MathExpression|pysssss`、`LTXVSpatioTemporalTiledVAEDecode`、`KSamplerSelect`、`VAELoaderKJ`、`VAELoader`、`SigmasPreview`、`VHS_VideoCombine`、`ImageResizeKJv2`、`PrimitiveBoolean`、`DepthAnythingV2Preprocessor`、`CannyEdgePreprocessor`、`UNETLoader`、`PathchSageAttentionKJ`、`LTXVChunkFeedForward`、`LTXICLoRALoaderModelOnly`、`DualCLIPLoader`、`VHS_LoadVideo`、`DWPreprocessor`、`LoadImage`

**用到的条目**：VAELoader、CLIPTextEncode、LoadImage、UNETLoader、DepthAnythingV2Preprocessor、CannyEdgePreprocessor、CFGGuider、KSamplerSelect
