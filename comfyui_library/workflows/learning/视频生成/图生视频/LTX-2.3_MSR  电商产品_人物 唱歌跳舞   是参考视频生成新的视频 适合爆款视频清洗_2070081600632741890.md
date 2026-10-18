---
key: 视频生成/图生视频/LTX-2.3_MSR  电商产品_人物 唱歌跳舞   是参考视频生成新的视频 适合爆款视频清洗_2070081600632741890.json
name: LTX-2.3_MSR  电商产品_人物 唱歌跳舞   是参考视频生成新的视频 适合爆款视频清洗_2070081600632741890.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX-2.3_MSR  电商产品_人物 唱歌跳舞   是参考视频生成新的视频 适合爆款视频清洗_2070081600632741890.json
hash: 6c707ad757420dba
coverage: 0.923077
learned_at: 2026-10-15 22:40:35
nodes: [LTXVConditioning, LTX2_NAG, LTXVAudioVAEDecode, LTXVCropGuides, LTXVSeparateAVLatent, LTXVConcatAVLatent, CFGGuider, KSamplerSelect, SamplerCustomAdvanced, VAEDecode, ManualSigmas, LiconMSR, PromptRelayEncode, LTXAddVideoICLoRAGuide, INTConstant, LTXVAudioVAEEncode, SolidMask, SetLatentNoiseMask, LTXVPreprocess, LTXVImgToVideoConditionOnly, RandomNoise, GetImageSize, GetImageSize, ResizeImagesByLongerEdge, LTXVAudioVAELoader, LTXAVTextEncoderLoader, LowVRAMCheckpointLoader, SaveVideo, LoraLoaderModelOnly, LoraLoaderModelOnly, LTXICLoRALoaderModelOnly, CLIPTextEncode, PrimitiveNode, EmptyLTXVLatentVideo, CreateVideo, VHS_LoadVideo, LoadImage, PrimitiveStringMultiline, PrimitiveStringMultiline]
patterns: []
missing: []
parameters: {"checkpoint": "ltx-2.3-22b-distilled-1.1.safetensors"}
---

# 视频生成/图生视频/LTX-2.3_MSR  电商产品_人物 唱歌跳舞   是参考视频生成新的视频 适合爆款视频清洗_2070081600632741890.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2070081600632741890.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（39 个）：
- `LTXVConditioning`
- `LTX2_NAG`
- `LTXVAudioVAEDecode` ★核心
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `LTXVConcatAVLatent`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `ManualSigmas`
- `LiconMSR`
- `PromptRelayEncode`
- `LTXAddVideoICLoRAGuide`
- `INTConstant`
- `LTXVAudioVAEEncode` ★核心
- `SolidMask`
- `SetLatentNoiseMask`
- `LTXVPreprocess`
- `LTXVImgToVideoConditionOnly`
- `RandomNoise`
- `GetImageSize`
- `GetImageSize`
- `ResizeImagesByLongerEdge`
- `LTXVAudioVAELoader`
- `LTXAVTextEncoderLoader`
- `LowVRAMCheckpointLoader` ★核心
- `SaveVideo`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LTXICLoRALoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `PrimitiveNode`
- `EmptyLTXVLatentVideo`
- `CreateVideo`
- `VHS_LoadVideo`
- `LoadImage`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-distilled-1.1.safetensors`

## 知识

覆盖率 **92%**（36/39）

**有卡**：`LTXVConditioning`、`LTX2_NAG`、`LTXVAudioVAEDecode`、`LTXVCropGuides`、`LTXVSeparateAVLatent`、`LTXVConcatAVLatent`、`CFGGuider`、`KSamplerSelect`、`SamplerCustomAdvanced`、`VAEDecode`、`ManualSigmas`、`LiconMSR`、`PromptRelayEncode`、`LTXAddVideoICLoRAGuide`、`INTConstant`、`LTXVAudioVAEEncode`、`SolidMask`、`SetLatentNoiseMask`、`LTXVPreprocess`、`LTXVImgToVideoConditionOnly`、`RandomNoise`、`GetImageSize`、`ResizeImagesByLongerEdge`、`LTXVAudioVAELoader`、`LTXAVTextEncoderLoader`、`LowVRAMCheckpointLoader`、`SaveVideo`、`LoraLoaderModelOnly`、`LTXICLoRALoaderModelOnly`、`CLIPTextEncode`、`EmptyLTXVLatentVideo`、`CreateVideo`、`VHS_LoadVideo`、`LoadImage`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVConcatAVLatent
