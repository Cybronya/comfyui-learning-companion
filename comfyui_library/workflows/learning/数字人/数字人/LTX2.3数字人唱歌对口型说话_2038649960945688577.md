---
key: 数字人/数字人/LTX2.3数字人唱歌对口型说话_2038649960945688577.json
name: LTX2.3数字人唱歌对口型说话_2038649960945688577
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/LTX2.3数字人唱歌对口型说话_2038649960945688577.json
hash: e7b7cde9b6af3d1e
coverage: 0.921053
learned_at: 2026-10-26 01:56:04
nodes: [INTConstant, INTConstant, CM_IntToFloat, LTXAVTextEncoderLoader, LatentUpscaleModelLoader, LTXVAudioVAELoader, CheckpointLoaderSimple, LoraLoaderModelOnly, PrimitiveInt, PrimitiveInt, JWIntegerToString, JWIntegerToString, PreviewAudio, KSamplerSelect, SolidMask, CM_IntToFloat, KSamplerSelect, MathExpression|pysssss, MathExpression|pysssss, CFGGuider, ManualSigmas, ConditioningZeroOut, LTXVConditioning, RandomNoise, RHHiddenNodes, VHS_VideoCombine, ManualSigmas, VRGDG_CreateFinalVideo_SRT, RandomNoise, CLIPTextEncode, SaveVideo, AudioCrop, LoadAudio, INTConstant, INTConstant, LoraLoaderModelOnly, LoraLoaderModelOnly, JjkText]
patterns: []
missing: []
parameters: {"checkpoint": "ltx-2.3-22b-dev-fp8.safetensors"}
---

# 数字人/数字人/LTX2.3数字人唱歌对口型说话_2038649960945688577.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/LTX2.3数字人唱歌对口型说话_2038649960945688577.json`

## 结构

**生成流程**：Model → Condition → Sampling → Output → Other

**节点**（38 个）：
- `INTConstant`
- `INTConstant`
- `CM_IntToFloat`
- `LTXAVTextEncoderLoader`
- `LatentUpscaleModelLoader`
- `LTXVAudioVAELoader`
- `CheckpointLoaderSimple` ★核心
- `LoraLoaderModelOnly` ★核心
- `PrimitiveInt`
- `PrimitiveInt`
- `JWIntegerToString`
- `JWIntegerToString`
- `PreviewAudio`
- `KSamplerSelect` ★核心
- `SolidMask`
- `CM_IntToFloat`
- `KSamplerSelect` ★核心
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `CFGGuider`
- `ManualSigmas`
- `ConditioningZeroOut`
- `LTXVConditioning`
- `RandomNoise`
- `RHHiddenNodes`
- `VHS_VideoCombine`
- `ManualSigmas`
- `VRGDG_CreateFinalVideo_SRT`
- `RandomNoise`
- `CLIPTextEncode` ★核心
- `SaveVideo`
- `AudioCrop`
- `LoadAudio`
- `INTConstant`
- `INTConstant`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `JjkText`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev-fp8.safetensors`

## 知识

覆盖率 **92%**（35/38）

**有卡**：`INTConstant`、`CM_IntToFloat`、`LTXAVTextEncoderLoader`、`LatentUpscaleModelLoader`、`LTXVAudioVAELoader`、`CheckpointLoaderSimple`、`LoraLoaderModelOnly`、`JWIntegerToString`、`PreviewAudio`、`KSamplerSelect`、`SolidMask`、`MathExpression|pysssss`、`CFGGuider`、`ManualSigmas`、`ConditioningZeroOut`、`LTXVConditioning`、`RandomNoise`、`RHHiddenNodes`、`VHS_VideoCombine`、`VRGDG_CreateFinalVideo_SRT`、`CLIPTextEncode`、`SaveVideo`、`AudioCrop`、`LoadAudio`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、ConditioningZeroOut、CFGGuider、KSamplerSelect、LatentUpscaleModelLoader、LTXAVTextEncoderLoader
