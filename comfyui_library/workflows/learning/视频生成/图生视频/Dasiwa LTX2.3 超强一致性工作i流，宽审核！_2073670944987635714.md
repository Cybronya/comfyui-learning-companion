---
key: 视频生成/图生视频/Dasiwa LTX2.3 超强一致性工作i流，宽审核！_2073670944987635714.json
name: Dasiwa LTX2.3 超强一致性工作i流，宽审核！_2073670944987635714.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2073670944987635714.json
hash: 7dba1ba6578542ec
coverage: 0.82
learned_at: 2026-10-15 22:41:08
nodes: [Int, PrimitiveFloat, JWInteger, JWInteger, UNETLoader, LoraLoaderModelOnly, LTXICLoRALoaderModelOnly, LTX2AttentionTunerPatch, PathchSageAttentionKJ, ModelPatchTorchSettings, LTXVImgToVideoConditionOnly, LTXVEmptyLatentAudio, LTXVConcatAVLatent, CM_FloatToInt, GetNode, SamplerCustomAdvanced, ResizeImageMaskNode, EmptyLTXVLatentVideo, SimpleMath+, PrimitiveBoolean, CLIPTextEncode, LTXVConditioning, LTX2_NAG, LTXVChunkFeedForward, CFGGuider, KSamplerSelect, RandomNoise, ManualSigmas, GetNode, LTXVSeparateAVLatent, LTXVAudioVAELoader, VAELoader, SetNode, VAEDecodeTiled, LTXVAudioVAEDecode, LTXAVTextEncoderLoader, CreateVideo, CR Prompt Text, CR Text, CR Text, RH_LLMAPI_Pro_Node, ConcatTextOfUtils, Reroute, 孤海注释, CLIPTextEncode, 孤海注释, PreviewAny, LoadImage, SaveVideo, 孤海注释]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/Dasiwa LTX2.3 超强一致性工作i流，宽审核！_2073670944987635714.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2073670944987635714.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（50 个）：
- `Int`
- `PrimitiveFloat`
- `JWInteger`
- `JWInteger`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LTXICLoRALoaderModelOnly` ★核心
- `LTX2AttentionTunerPatch`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `LTXVImgToVideoConditionOnly`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVConcatAVLatent`
- `CM_FloatToInt`
- `GetNode`
- `SamplerCustomAdvanced` ★核心
- `ResizeImageMaskNode`
- `EmptyLTXVLatentVideo`
- `SimpleMath+`
- `PrimitiveBoolean`
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `LTX2_NAG`
- `LTXVChunkFeedForward`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `ManualSigmas`
- `GetNode`
- `LTXVSeparateAVLatent`
- `LTXVAudioVAELoader`
- `VAELoader`
- `SetNode`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `LTXAVTextEncoderLoader`
- `CreateVideo`
- `CR Prompt Text`
- `CR Text`
- `CR Text`
- `RH_LLMAPI_Pro_Node`
- `ConcatTextOfUtils`
- `Reroute`
- `孤海注释`
- `CLIPTextEncode` ★核心
- `孤海注释`
- `PreviewAny`
- `LoadImage`
- `SaveVideo`
- `孤海注释`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **82%**（41/50）

**有卡**：`Int`、`JWInteger`、`UNETLoader`、`LoraLoaderModelOnly`、`LTXICLoRALoaderModelOnly`、`LTX2AttentionTunerPatch`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`LTXVImgToVideoConditionOnly`、`LTXVEmptyLatentAudio`、`LTXVConcatAVLatent`、`CM_FloatToInt`、`SamplerCustomAdvanced`、`ResizeImageMaskNode`、`EmptyLTXVLatentVideo`、`SimpleMath+`、`PrimitiveBoolean`、`CLIPTextEncode`、`LTXVConditioning`、`LTX2_NAG`、`LTXVChunkFeedForward`、`CFGGuider`、`KSamplerSelect`、`RandomNoise`、`ManualSigmas`、`LTXVSeparateAVLatent`、`LTXVAudioVAELoader`、`VAELoader`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`LTXAVTextEncoderLoader`、`CreateVideo`、`CR Prompt Text`、`CR Text`、`RH_LLMAPI_Pro_Node`、`ConcatTextOfUtils`、`LoadImage`、`SaveVideo`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
