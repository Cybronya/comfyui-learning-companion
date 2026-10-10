---
key: 视频生成/文生视频/AA-LTX2.0-huanhuan-手动提示词-独立放大插帧_2012426083651555329.json
name: AA-LTX2.0-huanhuan-手动提示词-独立放大插帧_2012426083651555329
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/AA-LTX2.0-huanhuan-手动提示词-独立放大插帧_2012426083651555329.json
hash: a0a67dfa20fc65c8
coverage: 0.657895
learned_at: 2026-10-11 03:07:08
nodes: [CLIPTextEncode, JWInteger, JWInteger, PainterLTXVtoVideo, ManualSigmas, easy cleanGpuUsed, PainterSamplerLTXV, LTXVAudioVAEDecode, VAEDecode, CheckpointLoaderSimple, LTXVAudioVAELoader, LTXAVTextEncoderLoader, LoraLoaderModelOnly, CLIPTextEncode, CR Prompt Text, CR Prompt Text, RH_Translator, Note, Note, VHS_VideoCombine, ShowAnything|Mie, LayerUtility: TextJoin, ShowAnything|Mie, Float, JWInteger, RIFE VFI, JWInteger, JWInteger, VHS_VideoInfo, FlashVSRNode, easy showAnything, easy showAnything, easy showAnything, easy showAnything, CM_IntToFloat, CM_FloatBinaryOperation, VHS_LoadVideo, VHS_VideoCombine]
patterns: []
missing: [LayerUtility: TextJoin, RIFE VFI, ShowAnything|Mie, ShowAnything|Mie, easy cleanGpuUsed, CR Prompt Text, CR Prompt Text]
parameters: {"checkpoint": "ltx-2-19b-distilled-fp8.safetensors"}
discoveries: [次要节点 `LayerUtility: TextJoin` 知识库中没有该节点类型的任何知识, 次要节点 `RIFE VFI` 知识库中没有该节点类型的任何知识, 次要节点 `ShowAnything|Mie` 知识库中没有该节点类型的任何知识, 次要节点 `ShowAnything|Mie` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/AA-LTX2.0-huanhuan-手动提示词-独立放大插帧_2012426083651555329.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/AA-LTX2.0-huanhuan-手动提示词-独立放大插帧_2012426083651555329.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（38 个）：
- `CLIPTextEncode` ★核心
- `JWInteger`
- `JWInteger`
- `PainterLTXVtoVideo`
- `ManualSigmas`
- `easy cleanGpuUsed`
- `PainterSamplerLTXV` ★核心
- `LTXVAudioVAEDecode` ★核心
- `VAEDecode` ★核心
- `CheckpointLoaderSimple` ★核心
- `LTXVAudioVAELoader`
- `LTXAVTextEncoderLoader`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `CR Prompt Text`
- `CR Prompt Text`
- `RH_Translator`
- `Note`
- `Note`
- `VHS_VideoCombine`
- `ShowAnything|Mie`
- `LayerUtility: TextJoin`
- `ShowAnything|Mie`
- `Float`
- `JWInteger`
- `RIFE VFI`
- `JWInteger`
- `JWInteger`
- `VHS_VideoInfo`
- `FlashVSRNode`
- `easy showAnything`
- `easy showAnything`
- `easy showAnything`
- `easy showAnything`
- `CM_IntToFloat`
- `CM_FloatBinaryOperation`
- `VHS_LoadVideo`
- `VHS_VideoCombine`

## 关键参数

- `checkpoint` = `ltx-2-19b-distilled-fp8.safetensors`

## 知识

覆盖率 **66%**（25/38）

**有卡**：`CLIPTextEncode`、`JWInteger`、`PainterLTXVtoVideo`、`ManualSigmas`、`PainterSamplerLTXV`、`LTXVAudioVAEDecode`、`VAEDecode`、`CheckpointLoaderSimple`、`LTXVAudioVAELoader`、`LTXAVTextEncoderLoader`、`LoraLoaderModelOnly`、`RH_Translator`、`VHS_VideoCombine`、`Float`、`VHS_VideoInfo`、`FlashVSRNode`、`CM_IntToFloat`、`CM_FloatBinaryOperation`、`VHS_LoadVideo`

**缺卡**（7）：`LayerUtility: TextJoin`、`RIFE VFI`、`ShowAnything|Mie`、`ShowAnything|Mie`、`easy cleanGpuUsed`、`CR Prompt Text`、`CR Prompt Text`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、PainterSamplerLTXV、LTXVAudioVAEDecode、LTXAVTextEncoderLoader、LTXVAudioVAELoader

## 学习发现

- 次要节点 `LayerUtility: TextJoin` 知识库中没有该节点类型的任何知识
- 次要节点 `RIFE VFI` 知识库中没有该节点类型的任何知识
- 次要节点 `ShowAnything|Mie` 知识库中没有该节点类型的任何知识
- 次要节点 `ShowAnything|Mie` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
