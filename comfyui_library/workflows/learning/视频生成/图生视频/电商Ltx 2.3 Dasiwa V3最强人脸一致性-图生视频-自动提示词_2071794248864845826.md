---
key: 视频生成/图生视频/电商Ltx 2.3 Dasiwa V3最强人脸一致性-图生视频-自动提示词_2071794248864845826.json
name: 电商Ltx 2.3 Dasiwa V3最强人脸一致性-图生视频-自动提示词_2071794248864845826.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2071794248864845826.json
hash: f6c25bdfc9d0b7fc
coverage: 0.944444
learned_at: 2026-10-15 22:40:48
nodes: [CLIPTextEncode, CFGGuider, FlashVSR_SM_KSampler, LTXICLoRALoaderModelOnly, UNETLoader, LoraLoaderModelOnly, LTX2AttentionTunerPatch, LoraLoaderModelOnly, ModelPatchTorchSettings, PathchSageAttentionKJ, LTXVChunkFeedForward, RandomNoise, CR Text, ConcatTextOfUtils, CR Prompt Text, LTXAVTextEncoderLoader, CLIPTextEncode, LTXVImgToVideoConditionOnly, LTXVEmptyLatentAudio, LTX2_NAG, LTXVConcatAVLatent, KSamplerSelect, SamplerCustomAdvanced, ManualSigmas, LTXVSeparateAVLatent, VAEDecodeTiled, LTXVAudioVAEDecode, LTXVAudioVAELoader, VAELoader, PrimitiveBoolean, LTXVConditioning, EmptyLTXVLatentVideo, ResizeImageMaskNode, LoadImage, CR Text, JWInteger, JWInteger, Int, SimpleMath+, CM_FloatToInt, PrimitiveFloat, RH_LLMAPI_Pro_Node, easy cleanGpuUsed, Float, LayerUtility: ImageScaleByAspectRatio V2, JWInteger, ImageFromBatch+, FlashVSR_SM_Model, JWInteger, CreateVideo, 孤海注释, 孤海注释, VHS_VideoCombine, SaveVideo]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": "randomize", "denoise": 11, "height": 25, "sampler_name": 2, "scheduler": 3.5, "seed": 1280, "steps": 1917427970, "width": 97}
---

# 视频生成/图生视频/电商Ltx 2.3 Dasiwa V3最强人脸一致性-图生视频-自动提示词_2071794248864845826.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2071794248864845826.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（54 个）：
- `CLIPTextEncode` ★核心
- `CFGGuider`
- `FlashVSR_SM_KSampler` ★核心
- `LTXICLoRALoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LTX2AttentionTunerPatch`
- `LoraLoaderModelOnly` ★核心
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `LTXVChunkFeedForward`
- `RandomNoise`
- `CR Text`
- `ConcatTextOfUtils`
- `CR Prompt Text`
- `LTXAVTextEncoderLoader`
- `CLIPTextEncode` ★核心
- `LTXVImgToVideoConditionOnly`
- `LTXVEmptyLatentAudio` ★核心
- `LTX2_NAG`
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `ManualSigmas`
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `LTXVAudioVAELoader`
- `VAELoader`
- `PrimitiveBoolean`
- `LTXVConditioning`
- `EmptyLTXVLatentVideo`
- `ResizeImageMaskNode`
- `LoadImage`
- `CR Text`
- `JWInteger`
- `JWInteger`
- `Int`
- `SimpleMath+`
- `CM_FloatToInt`
- `PrimitiveFloat`
- `RH_LLMAPI_Pro_Node`
- `easy cleanGpuUsed`
- `Float`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `JWInteger`
- `ImageFromBatch+`
- `FlashVSR_SM_Model`
- `JWInteger`
- `CreateVideo`
- `孤海注释`
- `孤海注释`
- `VHS_VideoCombine`
- `SaveVideo`

## 关键参数

- `seed` = `1280`
- `steps` = `1917427970`
- `cfg` = `randomize`
- `sampler_name` = `2`
- `scheduler` = `3.5`
- `denoise` = `11`
- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **94%**（51/54）

**有卡**：`CLIPTextEncode`、`CFGGuider`、`FlashVSR_SM_KSampler`、`LTXICLoRALoaderModelOnly`、`UNETLoader`、`LoraLoaderModelOnly`、`LTX2AttentionTunerPatch`、`ModelPatchTorchSettings`、`PathchSageAttentionKJ`、`LTXVChunkFeedForward`、`RandomNoise`、`CR Text`、`ConcatTextOfUtils`、`CR Prompt Text`、`LTXAVTextEncoderLoader`、`LTXVImgToVideoConditionOnly`、`LTXVEmptyLatentAudio`、`LTX2_NAG`、`LTXVConcatAVLatent`、`KSamplerSelect`、`SamplerCustomAdvanced`、`ManualSigmas`、`LTXVSeparateAVLatent`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`LTXVAudioVAELoader`、`VAELoader`、`PrimitiveBoolean`、`LTXVConditioning`、`EmptyLTXVLatentVideo`、`ResizeImageMaskNode`、`LoadImage`、`JWInteger`、`Int`、`SimpleMath+`、`CM_FloatToInt`、`RH_LLMAPI_Pro_Node`、`easy cleanGpuUsed`、`Float`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageFromBatch+`、`FlashVSR_SM_Model`、`CreateVideo`、`VHS_VideoCombine`、`SaveVideo`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2、CFGGuider、KSamplerSelect
