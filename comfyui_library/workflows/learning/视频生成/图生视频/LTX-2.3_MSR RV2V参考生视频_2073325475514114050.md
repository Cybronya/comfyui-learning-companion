---
key: 视频生成/图生视频/LTX-2.3_MSR RV2V参考生视频_2073325475514114050.json
name: LTX-2.3_MSR RV2V参考生视频_2073325475514114050.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX-2.3_MSR RV2V参考生视频_2073325475514114050.json
hash: 95c93ca3a8534edb
coverage: 0.918919
learned_at: 2026-10-15 22:41:06
nodes: [LTXAVTextEncoderLoader, LTXICLoRALoaderModelOnly, LTXVAudioVAELoader, CLIPTextEncode, LTXVConditioning, LTX2_NAG, LTXVAudioVAEDecode, LTXVCropGuides, LTXVSeparateAVLatent, LTXVConcatAVLatent, CFGGuider, KSamplerSelect, SamplerCustomAdvanced, CreateVideo, VAEDecode, SaveVideo, ManualSigmas, LowVRAMCheckpointLoader, LiconMSR, PromptRelayEncode, LTXAddVideoICLoRAGuide, PrimitiveStringMultiline, INTConstant, LTXVAudioVAEEncode, SolidMask, SetLatentNoiseMask, LTXVPreprocess, LTXVImgToVideoConditionOnly, EmptyLTXVLatentVideo, ResizeImagesByLongerEdge, PrimitiveStringMultiline, RandomNoise, PrimitiveNode, GetImageSize, VHS_LoadVideo, LoadImage, GetImageSize]
patterns: []
missing: []
parameters: {"checkpoint": "ltx-2.3-22b-distilled-1.1.safetensors"}
---

# 视频生成/图生视频/LTX-2.3_MSR RV2V参考生视频_2073325475514114050.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2073325475514114050.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（37 个）：
- `LTXAVTextEncoderLoader`
- `LTXICLoRALoaderModelOnly` ★核心
- `LTXVAudioVAELoader`
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `LTX2_NAG`
- `LTXVAudioVAEDecode` ★核心
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `LTXVConcatAVLatent`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `CreateVideo`
- `VAEDecode` ★核心
- `SaveVideo`
- `ManualSigmas`
- `LowVRAMCheckpointLoader` ★核心
- `LiconMSR`
- `PromptRelayEncode`
- `LTXAddVideoICLoRAGuide`
- `PrimitiveStringMultiline`
- `INTConstant`
- `LTXVAudioVAEEncode` ★核心
- `SolidMask`
- `SetLatentNoiseMask`
- `LTXVPreprocess`
- `LTXVImgToVideoConditionOnly`
- `EmptyLTXVLatentVideo`
- `ResizeImagesByLongerEdge`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `PrimitiveNode`
- `GetImageSize`
- `VHS_LoadVideo`
- `LoadImage`
- `GetImageSize`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-distilled-1.1.safetensors`

## 知识

覆盖率 **92%**（34/37）

**有卡**：`LTXAVTextEncoderLoader`、`LTXICLoRALoaderModelOnly`、`LTXVAudioVAELoader`、`CLIPTextEncode`、`LTXVConditioning`、`LTX2_NAG`、`LTXVAudioVAEDecode`、`LTXVCropGuides`、`LTXVSeparateAVLatent`、`LTXVConcatAVLatent`、`CFGGuider`、`KSamplerSelect`、`SamplerCustomAdvanced`、`CreateVideo`、`VAEDecode`、`SaveVideo`、`ManualSigmas`、`LowVRAMCheckpointLoader`、`LiconMSR`、`PromptRelayEncode`、`LTXAddVideoICLoRAGuide`、`INTConstant`、`LTXVAudioVAEEncode`、`SolidMask`、`SetLatentNoiseMask`、`LTXVPreprocess`、`LTXVImgToVideoConditionOnly`、`EmptyLTXVLatentVideo`、`ResizeImagesByLongerEdge`、`RandomNoise`、`GetImageSize`、`VHS_LoadVideo`、`LoadImage`

**用到的条目**：VAEDecode、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVConcatAVLatent、LTXVSeparateAVLatent
