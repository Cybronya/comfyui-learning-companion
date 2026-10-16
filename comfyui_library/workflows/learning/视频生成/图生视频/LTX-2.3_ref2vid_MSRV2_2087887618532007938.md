---
key: 视频生成/图生视频/LTX-2.3_ref2vid_MSRV2_2087887618532007938.json
name: LTX-2.3_ref2vid_MSRV2_2087887618532007938
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX-2.3_ref2vid_MSRV2_2087887618532007938.json
hash: 002b38047205dc47
coverage: 0.540541
learned_at: 2026-10-16 21:27:31
nodes: [LTXVCropGuides, SetNode, SetNode, GetNode, GetNode, ManualSigmas, LTXVSeparateAVLatent, VAEDecode, SetNode, SetNode, CFGGuider, SetNode, VAELoader, SetNode, SolidMask, GetNode, LoraLoaderModelOnly, SetNode, UNETLoader, PathchSageAttentionKJ, DualCLIPLoader, KSamplerSelect, GetNode, ComfyNumberConvert, LTXVAudioVAEEncode, GetImageSize, GetNode, PreviewAudio, MathExpression|pysssss, SetNode, PrimitiveFloat, RandomNoise, LTXVAudioVAEDecode, CR Float To Integer, SetNode, SetNode, GetImageSize, SetNode, LTXVConcatAVLatent, GetNode, GetNode, GetNode, LTXAddVideoICLoRAGuide, LTX2_NAG, SamplerCustomAdvanced, LiconMSR, VHS_VideoCombine, LTXVConditioning, VAELoader, GetNode, GetNode, GetNode, PrimitiveFloat, easy mathFloat, LoadImage, PromptRelayEncode, GetNode, GetNode, CLIPTextEncode, GetNode, EmptyLTXVLatentVideo, GetNode, SetNode, SetLatentNoiseMask, Any Switch (rgthree), SetNode, GetNode, TrimAudioDuration, LoadAudio, LTXVEmptyLatentAudio, LayerUtility: ImageScaleByAspectRatio V2, AnyBooleanSwitch, PrimitiveFloat, PrimitiveStringMultiline]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 505}
---

# 视频生成/图生视频/LTX-2.3_ref2vid_MSRV2_2087887618532007938.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/LTX-2.3_ref2vid_MSRV2_2087887618532007938.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Other

**节点**（74 个）：
- `LTXVCropGuides`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `ManualSigmas`
- `LTXVSeparateAVLatent`
- `VAEDecode` ★核心
- `SetNode`
- `SetNode`
- `CFGGuider`
- `SetNode`
- `VAELoader`
- `SetNode`
- `SolidMask`
- `GetNode`
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `DualCLIPLoader`
- `KSamplerSelect` ★核心
- `GetNode`
- `ComfyNumberConvert`
- `LTXVAudioVAEEncode` ★核心
- `GetImageSize`
- `GetNode`
- `PreviewAudio`
- `MathExpression|pysssss`
- `SetNode`
- `PrimitiveFloat`
- `RandomNoise`
- `LTXVAudioVAEDecode` ★核心
- `CR Float To Integer`
- `SetNode`
- `SetNode`
- `GetImageSize`
- `SetNode`
- `LTXVConcatAVLatent`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXAddVideoICLoRAGuide`
- `LTX2_NAG`
- `SamplerCustomAdvanced` ★核心
- `LiconMSR`
- `VHS_VideoCombine`
- `LTXVConditioning`
- `VAELoader`
- `GetNode`
- `GetNode`
- `GetNode`
- `PrimitiveFloat`
- `easy mathFloat`
- `LoadImage`
- `PromptRelayEncode`
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `SetNode`
- `SetLatentNoiseMask`
- `Any Switch (rgthree)`
- `SetNode`
- `GetNode`
- `TrimAudioDuration`
- `LoadAudio`
- `LTXVEmptyLatentAudio` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `AnyBooleanSwitch`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`

## 关键参数

- `width` = `505`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **54%**（40/74）

**有卡**：`LTXVCropGuides`、`ManualSigmas`、`LTXVSeparateAVLatent`、`VAEDecode`、`CFGGuider`、`VAELoader`、`SolidMask`、`LoraLoaderModelOnly`、`UNETLoader`、`PathchSageAttentionKJ`、`DualCLIPLoader`、`KSamplerSelect`、`ComfyNumberConvert`、`LTXVAudioVAEEncode`、`GetImageSize`、`PreviewAudio`、`MathExpression|pysssss`、`RandomNoise`、`LTXVAudioVAEDecode`、`CR Float To Integer`、`LTXVConcatAVLatent`、`LTXAddVideoICLoRAGuide`、`LTX2_NAG`、`SamplerCustomAdvanced`、`LiconMSR`、`VHS_VideoCombine`、`LTXVConditioning`、`easy mathFloat`、`LoadImage`、`PromptRelayEncode`、`CLIPTextEncode`、`EmptyLTXVLatentVideo`、`SetLatentNoiseMask`、`TrimAudioDuration`、`LoadAudio`、`LTXVEmptyLatentAudio`、`LayerUtility: ImageScaleByAspectRatio V2`、`AnyBooleanSwitch`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect
