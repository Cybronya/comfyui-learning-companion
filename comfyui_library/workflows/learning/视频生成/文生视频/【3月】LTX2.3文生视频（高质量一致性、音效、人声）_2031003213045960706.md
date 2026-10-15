---
key: 视频生成/文生视频/【3月】LTX2.3文生视频（高质量一致性、音效、人声）_2031003213045960706.json
name: 【3月】LTX2.3文生视频（高质量一致性、音效、人声）_2031003213045960706
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/【3月】LTX2.3文生视频（高质量一致性、音效、人声）_2031003213045960706.json
hash: b0f4a381adfe53ce
coverage: 0.944444
learned_at: 2026-10-15 22:47:39
nodes: [CheckpointLoaderSimple, LTXVAudioVAELoader, LoraLoaderModelOnly, LTXVChunkFeedForward, ModelPatchTorchSettings, PathchSageAttentionKJ, LatentUpscaleModelLoader, LTXAVTextEncoderLoader, CLIPTextEncode, CLIPTextEncode, LTXVConditioning, EmptyLTXVLatentVideo, CM_FloatToInt, LTXVEmptyLatentAudio, LTXVConcatAVLatent, ManualSigmas, RandomNoise, SamplerCustomAdvanced, CFGGuider, KSamplerSelect, LTXVSeparateAVLatent, VAEDecodeTiled, LTXVAudioVAEDecode, ImpactSwitch, JWInteger, JWInteger, JWInteger, ImpactSwitch, MathExpression|pysssss, CR Text, JWInteger, JWInteger, JWInteger, JWInteger, DF_Int_to_Float, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev-fp8.safetensors", "height": 25, "width": 97}
---

# 视频生成/文生视频/【3月】LTX2.3文生视频（高质量一致性、音效、人声）_2031003213045960706.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/【3月】LTX2.3文生视频（高质量一致性、音效、人声）_2031003213045960706.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Other

**节点**（36 个）：
- `CheckpointLoaderSimple` ★核心
- `LTXVAudioVAELoader`
- `LoraLoaderModelOnly` ★核心
- `LTXVChunkFeedForward`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `LatentUpscaleModelLoader`
- `LTXAVTextEncoderLoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `EmptyLTXVLatentVideo`
- `CM_FloatToInt`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVConcatAVLatent`
- `ManualSigmas`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `CFGGuider`
- `KSamplerSelect` ★核心
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `ImpactSwitch`
- `JWInteger`
- `JWInteger`
- `JWInteger`
- `ImpactSwitch`
- `MathExpression|pysssss`
- `CR Text`
- `JWInteger`
- `JWInteger`
- `JWInteger`
- `JWInteger`
- `DF_Int_to_Float`
- `VHS_VideoCombine`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev-fp8.safetensors`
- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **94%**（34/36）

**有卡**：`CheckpointLoaderSimple`、`LTXVAudioVAELoader`、`LoraLoaderModelOnly`、`LTXVChunkFeedForward`、`ModelPatchTorchSettings`、`PathchSageAttentionKJ`、`LatentUpscaleModelLoader`、`LTXAVTextEncoderLoader`、`CLIPTextEncode`、`LTXVConditioning`、`EmptyLTXVLatentVideo`、`CM_FloatToInt`、`LTXVEmptyLatentAudio`、`LTXVConcatAVLatent`、`ManualSigmas`、`RandomNoise`、`SamplerCustomAdvanced`、`CFGGuider`、`KSamplerSelect`、`LTXVSeparateAVLatent`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`JWInteger`、`MathExpression|pysssss`、`CR Text`、`DF_Int_to_Float`、`VHS_VideoCombine`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVConcatAVLatent、LTXVSeparateAVLatent
