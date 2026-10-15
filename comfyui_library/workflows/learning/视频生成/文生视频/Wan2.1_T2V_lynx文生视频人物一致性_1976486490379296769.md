---
key: 视频生成/文生视频/Wan2.1_T2V_lynx文生视频人物一致性_1976486490379296769.json
name: Wan2.1_T2V_lynx文生视频人物一致性_1976486490379296769
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.1_T2V_lynx文生视频人物一致性_1976486490379296769.json
hash: 1defe9bf9cb82e94
coverage: 0.723404
learned_at: 2026-10-15 22:47:08
nodes: [WanVideoBlockSwap, WanVideoModelLoader, WanVideoLoraSelectMulti, WanVideoTorchCompileSettings, WanVideoExtraModelSelect, WanVideoTextEncodeCached, GetNode, WanVideoTextEncodeCached, Note, Note, LoadLynxResampler, JWInteger, Wan22PromptSelector, JWInteger, JWInteger, JWInteger, WanVideoVAELoader, WanVideoSetLoRAs, SetNode, WanVideoSetBlockSwap, SetNode, WanVideoAddLynxEmbeds, PreviewImage, PreviewImage, WanVideoEmptyEmbeds, LynxEncodeFaceIP, SetNode, MathExpression|pysssss, Note, LoadImage, ImpactSwitch, Text Concatenate, easy showAnything, Note, MarkdownNote, RH_LLMAPI_NODE, LynxInsightFaceCrop, WanVideoExtraModelSelect, WanVideoDecode, ImageFromBatch+, ImageConcatMulti, VHS_VideoCombine, WanVideoSampler, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, CR Text]
patterns: []
missing: []
---

# 视频生成/文生视频/Wan2.1_T2V_lynx文生视频人物一致性_1976486490379296769.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.1_T2V_lynx文生视频人物一致性_1976486490379296769.json`

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
- `LoadImage`
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

## 知识

覆盖率 **72%**（34/47）

**有卡**：`WanVideoBlockSwap`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`WanVideoTorchCompileSettings`、`WanVideoExtraModelSelect`、`WanVideoTextEncodeCached`、`LoadLynxResampler`、`JWInteger`、`Wan22PromptSelector`、`WanVideoVAELoader`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`WanVideoAddLynxEmbeds`、`WanVideoEmptyEmbeds`、`LynxEncodeFaceIP`、`MathExpression|pysssss`、`LoadImage`、`Text Concatenate`、`RH_LLMAPI_NODE`、`LynxInsightFaceCrop`、`WanVideoDecode`、`ImageFromBatch+`、`ImageConcatMulti`、`VHS_VideoCombine`、`WanVideoSampler`、`CR Text`

**用到的条目**：LoadImage、WanVideoSampler、LoadLynxResampler、WanVideoDecode、WanVideoVAELoader、WanVideoTextEncodeCached、LynxEncodeFaceIP、WanVideoSetLoRAs
