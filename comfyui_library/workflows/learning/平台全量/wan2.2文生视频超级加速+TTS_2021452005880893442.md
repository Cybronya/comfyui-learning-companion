---
key: 平台全量/wan2.2文生视频超级加速+TTS_2021452005880893442.json
name: wan2.2文生视频超级加速+TTS_2021452005880893442
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/wan2.2文生视频超级加速+TTS_2021452005880893442.json
hash: 97a59366d6006817
coverage: 0.790698
learned_at: 2026-11-14 01:19:50
nodes: [GetNode, GetNode, WanVideoTextEncode, WanVideoSampler, MathExpression|pysssss, WanVideoSetBlockSwap, SetNode, LoadWanVideoT5TextEncoder, WanVideoVAELoader, SetNode, WanVideoSetLoRAs, SetNode, WanVideoSetBlockSwap, WanVideoSetLoRAs, SetNode, WanVideoTorchCompileSettings, GetNode, GetNode, WanVideoContextOptions, WanVideoSampler, MathExpression|pysssss, WanVideoEmptyEmbeds, Note, WanVideoModelLoader, WanVideoModelLoader, WanVideoLoraSelect, WanVideoLoraSelect, StringToFloatList, WanVideoBlockSwap, Primitive integer [Crystools], Qwen3TTSModelLoader, Qwen3TTSVoiceDesign, JWInteger, JWInteger, CR Text, CR Text, JWInteger, CR Text, SaveAudio, FloatToSigmas, WanVideoDecode, VHS_VideoCombine, VHS_VideoCombine]
patterns: []
missing: []
---

# 平台全量/wan2.2文生视频超级加速+TTS_2021452005880893442.json

> 来源文件 `comfyui_library/workflows/平台全量/wan2.2文生视频超级加速+TTS_2021452005880893442.json`

## 结构

**生成流程**：Model → Sampling → Output → Other

**节点**（43 个）：
- `GetNode`
- `GetNode`
- `WanVideoTextEncode`
- `WanVideoSampler` ★核心
- `MathExpression|pysssss`
- `WanVideoSetBlockSwap`
- `SetNode`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `SetNode`
- `WanVideoSetLoRAs`
- `SetNode`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `SetNode`
- `WanVideoTorchCompileSettings`
- `GetNode`
- `GetNode`
- `WanVideoContextOptions`
- `WanVideoSampler` ★核心
- `MathExpression|pysssss`
- `WanVideoEmptyEmbeds`
- `Note`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `StringToFloatList`
- `WanVideoBlockSwap`
- `Primitive integer [Crystools]`
- `Qwen3TTSModelLoader`
- `Qwen3TTSVoiceDesign`
- `JWInteger`
- `JWInteger`
- `CR Text`
- `CR Text`
- `JWInteger`
- `CR Text`
- `SaveAudio`
- `FloatToSigmas`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`

## 知识

覆盖率 **79%**（34/43）

**有卡**：`WanVideoTextEncode`、`WanVideoSampler`、`MathExpression|pysssss`、`WanVideoSetBlockSwap`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoSetLoRAs`、`WanVideoTorchCompileSettings`、`WanVideoContextOptions`、`WanVideoEmptyEmbeds`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`StringToFloatList`、`WanVideoBlockSwap`、`Primitive integer [Crystools]`、`Qwen3TTSModelLoader`、`Qwen3TTSVoiceDesign`、`JWInteger`、`CR Text`、`SaveAudio`、`FloatToSigmas`、`WanVideoDecode`、`VHS_VideoCombine`

**用到的条目**：WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect、WanVideoSetLoRAs、SaveAudio
