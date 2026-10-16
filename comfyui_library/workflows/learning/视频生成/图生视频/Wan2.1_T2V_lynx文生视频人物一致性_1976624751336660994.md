---
key: 视频生成/图生视频/Wan2.1_T2V_lynx文生视频人物一致性_1976624751336660994.json
name: Wan2.1_T2V_lynx文生视频人物一致性_1976624751336660994.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1976624751336660994.json
hash: 2b70c91b0883b786
coverage: 0.723404
learned_at: 2026-10-15 22:32:11
nodes: [WanVideoBlockSwap, WanVideoModelLoader, WanVideoLoraSelectMulti, WanVideoTorchCompileSettings, WanVideoExtraModelSelect, WanVideoTextEncodeCached, GetNode, WanVideoTextEncodeCached, Note, Note, LoadLynxResampler, JWInteger, Wan22PromptSelector, JWInteger, JWInteger, JWInteger, WanVideoVAELoader, WanVideoSetLoRAs, SetNode, WanVideoSetBlockSwap, SetNode, WanVideoAddLynxEmbeds, PreviewImage, PreviewImage, WanVideoEmptyEmbeds, LynxEncodeFaceIP, SetNode, MathExpression|pysssss, Note, ImpactSwitch, Text Concatenate, easy showAnything, Note, MarkdownNote, RH_LLMAPI_NODE, LynxInsightFaceCrop, WanVideoExtraModelSelect, WanVideoDecode, ImageFromBatch+, ImageConcatMulti, VHS_VideoCombine, WanVideoSampler, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, CR Text, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.1_T2V_lynx文生视频人物一致性_1976624751336660994.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1976624751336660994.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（47 个）：
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `WanVideoLoraSelectMulti`
- `WanVideoTorchCompileSettings`
- `WanVideoExtraModelSelect`
- `WanVideoTextEncodeCached`
- `GetNode`
- `WanVideoTextEncodeCached`
- `Note`
- `Note`
- `LoadLynxResampler` ★核心
- `JWInteger`
- `Wan22PromptSelector`
- `JWInteger`
- `JWInteger`
- `JWInteger`
- `WanVideoVAELoader`
- `WanVideoSetLoRAs`
- `SetNode`
- `WanVideoSetBlockSwap`
- `SetNode`
- `WanVideoAddLynxEmbeds`
- `PreviewImage`
- `PreviewImage`
- `WanVideoEmptyEmbeds`
- `LynxEncodeFaceIP`
- `SetNode`
- `MathExpression|pysssss`
- `Note`
- `ImpactSwitch`
- `Text Concatenate`
- `easy showAnything`
- `Note`
- `MarkdownNote`
- `RH_LLMAPI_NODE`
- `LynxInsightFaceCrop`
- `WanVideoExtraModelSelect`
- `WanVideoDecode`
- `ImageFromBatch+`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `WanVideoSampler` ★核心
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `CR Text`
- `LoadImage`

## 知识

覆盖率 **72%**（34/47）

**有卡**：`WanVideoBlockSwap`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`WanVideoTorchCompileSettings`、`WanVideoExtraModelSelect`、`WanVideoTextEncodeCached`、`LoadLynxResampler`、`JWInteger`、`Wan22PromptSelector`、`WanVideoVAELoader`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`WanVideoAddLynxEmbeds`、`WanVideoEmptyEmbeds`、`LynxEncodeFaceIP`、`MathExpression|pysssss`、`Text Concatenate`、`RH_LLMAPI_NODE`、`LynxInsightFaceCrop`、`WanVideoDecode`、`ImageFromBatch+`、`ImageConcatMulti`、`VHS_VideoCombine`、`WanVideoSampler`、`CR Text`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、LoadLynxResampler、WanVideoDecode、WanVideoVAELoader、WanVideoTextEncodeCached、LynxEncodeFaceIP、WanVideoSetLoRAs
