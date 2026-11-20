---
key: 平台全量/LTX-2.3_MSR RV2V邪修之视频参考生视频_2079329374129713153.json
name: LTX-2.3_MSR RV2V邪修之视频参考生视频_2079329374129713153
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/LTX-2.3_MSR RV2V邪修之视频参考生视频_2079329374129713153.json
hash: de87ff92c2ba3d74
coverage: 0.918919
learned_at: 2026-11-14 00:37:10
nodes: [LTXAVTextEncoderLoader, LTXICLoRALoaderModelOnly, LTXVAudioVAELoader, CLIPTextEncode, LTXVConditioning, LTX2_NAG, LTXVCropGuides, LTXVSeparateAVLatent, LTXVConcatAVLatent, CFGGuider, KSamplerSelect, SamplerCustomAdvanced, CreateVideo, ManualSigmas, LowVRAMCheckpointLoader, LiconMSR, PromptRelayEncode, LTXAddVideoICLoRAGuide, LTXVAudioVAEEncode, SolidMask, SetLatentNoiseMask, LTXVPreprocess, LTXVImgToVideoConditionOnly, EmptyLTXVLatentVideo, ResizeImagesByLongerEdge, RandomNoise, PrimitiveNode, GetImageSize, GetImageSize, LoadImage, VHS_LoadVideo, PrimitiveStringMultiline, PrimitiveStringMultiline, VAEDecode, LTXVAudioVAEDecode, INTConstant, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"checkpoint": "ltx-2.3-22b-distilled-1.1.safetensors"}
---

# 平台全量/LTX-2.3_MSR RV2V邪修之视频参考生视频_2079329374129713153.json

> 来源文件 `comfyui_library/workflows/平台全量/LTX-2.3_MSR RV2V邪修之视频参考生视频_2079329374129713153.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（37 个）：
- `LTXAVTextEncoderLoader`
- `LTXICLoRALoaderModelOnly` ★核心
- `LTXVAudioVAELoader`
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `LTX2_NAG`
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `LTXVConcatAVLatent`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `CreateVideo`
- `ManualSigmas`
- `LowVRAMCheckpointLoader` ★核心
- `LiconMSR`
- `PromptRelayEncode`
- `LTXAddVideoICLoRAGuide`
- `LTXVAudioVAEEncode` ★核心
- `SolidMask`
- `SetLatentNoiseMask`
- `LTXVPreprocess`
- `LTXVImgToVideoConditionOnly`
- `EmptyLTXVLatentVideo`
- `ResizeImagesByLongerEdge`
- `RandomNoise`
- `PrimitiveNode`
- `GetImageSize`
- `GetImageSize`
- `LoadImage`
- `VHS_LoadVideo`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `VAEDecode` ★核心
- `LTXVAudioVAEDecode` ★核心
- `INTConstant`
- `VHS_VideoCombine`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-distilled-1.1.safetensors`

## 知识

覆盖率 **92%**（34/37）

**有卡**：`LTXAVTextEncoderLoader`、`LTXICLoRALoaderModelOnly`、`LTXVAudioVAELoader`、`CLIPTextEncode`、`LTXVConditioning`、`LTX2_NAG`、`LTXVCropGuides`、`LTXVSeparateAVLatent`、`LTXVConcatAVLatent`、`CFGGuider`、`KSamplerSelect`、`SamplerCustomAdvanced`、`CreateVideo`、`ManualSigmas`、`LowVRAMCheckpointLoader`、`LiconMSR`、`PromptRelayEncode`、`LTXAddVideoICLoRAGuide`、`LTXVAudioVAEEncode`、`SolidMask`、`SetLatentNoiseMask`、`LTXVPreprocess`、`LTXVImgToVideoConditionOnly`、`EmptyLTXVLatentVideo`、`ResizeImagesByLongerEdge`、`RandomNoise`、`GetImageSize`、`LoadImage`、`VHS_LoadVideo`、`VAEDecode`、`LTXVAudioVAEDecode`、`INTConstant`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、EmptyLTXVLatentVideo、LTXAVTextEncoderLoader
