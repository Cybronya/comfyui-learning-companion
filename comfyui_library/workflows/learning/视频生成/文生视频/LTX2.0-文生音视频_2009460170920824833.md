---
key: 视频生成/文生视频/LTX2.0-文生音视频_2009460170920824833.json
name: LTX2.0-文生音视频_2009460170920824833
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.0-文生音视频_2009460170920824833.json
hash: 1e6abfbc8f084d28
coverage: 0.681818
learned_at: 2026-10-11 03:07:09
nodes: [LTXVAudioVAELoader, CheckpointLoaderSimple, CLIPTextEncode, easy cleanGpuUsed, VAEDecode, LTXVAudioVAEDecode, LTXAVTextEncoderLoader, CLIPTextEncode, PainterSamplerLTXV, ManualSigmas, PainterLTXVtoVideo, ShowAnything|Mie, VHS_VideoCombine, Note, Note, Note, Note, RH_LLMAPI_Pro_Node, CR Prompt Text, JWInteger, JWInteger, JWInteger]
patterns: []
missing: [ShowAnything|Mie, easy cleanGpuUsed, CR Prompt Text]
parameters: {"checkpoint": "ltx-2-19b-distilled-fp8.safetensors"}
discoveries: [次要节点 `ShowAnything|Mie` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/LTX2.0-文生音视频_2009460170920824833.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.0-文生音视频_2009460170920824833.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（22 个）：
- `LTXVAudioVAELoader`
- `CheckpointLoaderSimple` ★核心
- `CLIPTextEncode` ★核心
- `easy cleanGpuUsed`
- `VAEDecode` ★核心
- `LTXVAudioVAEDecode` ★核心
- `LTXAVTextEncoderLoader`
- `CLIPTextEncode` ★核心
- `PainterSamplerLTXV` ★核心
- `ManualSigmas`
- `PainterLTXVtoVideo`
- `ShowAnything|Mie`
- `VHS_VideoCombine`
- `Note`
- `Note`
- `Note`
- `Note`
- `RH_LLMAPI_Pro_Node`
- `CR Prompt Text`
- `JWInteger`
- `JWInteger`
- `JWInteger`

## 关键参数

- `checkpoint` = `ltx-2-19b-distilled-fp8.safetensors`

## 知识

覆盖率 **68%**（15/22）

**有卡**：`LTXVAudioVAELoader`、`CheckpointLoaderSimple`、`CLIPTextEncode`、`VAEDecode`、`LTXVAudioVAEDecode`、`LTXAVTextEncoderLoader`、`PainterSamplerLTXV`、`ManualSigmas`、`PainterLTXVtoVideo`、`VHS_VideoCombine`、`RH_LLMAPI_Pro_Node`、`JWInteger`

**缺卡**（3）：`ShowAnything|Mie`、`easy cleanGpuUsed`、`CR Prompt Text`

**用到的条目**：VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、PainterSamplerLTXV、LTXVAudioVAEDecode、LTXAVTextEncoderLoader、LTXVAudioVAELoader、ManualSigmas

## 学习发现

- 次要节点 `ShowAnything|Mie` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
