---
key: 视频生成/文生视频/Wan2.1_T2V_lynx文生视频人物一致性_1976486490379296769.json
name: Wan2.1_T2V_lynx文生视频人物一致性_1976486490379296769
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.1_T2V_lynx文生视频人物一致性_1976486490379296769.json
hash: 1defe9bf9cb82e94
coverage: 0.638298
learned_at: 2026-10-10 23:06:36
nodes: [WanVideoBlockSwap, WanVideoModelLoader, WanVideoLoraSelectMulti, WanVideoTorchCompileSettings, WanVideoExtraModelSelect, WanVideoTextEncodeCached, GetNode, WanVideoTextEncodeCached, Note, Note, LoadLynxResampler, JWInteger, Wan22PromptSelector, JWInteger, JWInteger, JWInteger, WanVideoVAELoader, WanVideoSetLoRAs, SetNode, WanVideoSetBlockSwap, SetNode, WanVideoAddLynxEmbeds, PreviewImage, PreviewImage, WanVideoEmptyEmbeds, LynxEncodeFaceIP, SetNode, MathExpression|pysssss, Note, LoadImage, ImpactSwitch, Text Concatenate, easy showAnything, Note, MarkdownNote, RH_LLMAPI_NODE, LynxInsightFaceCrop, WanVideoExtraModelSelect, WanVideoDecode, ImageFromBatch+, ImageConcatMulti, VHS_VideoCombine, WanVideoSampler, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, CR Text]
patterns: []
missing: [CR Text, ImageFromBatch+, MathExpression|pysssss, Text Concatenate]
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `Text Concatenate` 知识库中没有该节点类型的任何知识]
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

覆盖率 **64%**（30/47）

**有卡**：`WanVideoBlockSwap`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`WanVideoTorchCompileSettings`、`WanVideoExtraModelSelect`、`WanVideoTextEncodeCached`、`LoadLynxResampler`、`JWInteger`、`Wan22PromptSelector`、`WanVideoVAELoader`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`WanVideoAddLynxEmbeds`、`WanVideoEmptyEmbeds`、`LynxEncodeFaceIP`、`LoadImage`、`RH_LLMAPI_NODE`、`LynxInsightFaceCrop`、`WanVideoDecode`、`ImageConcatMulti`、`VHS_VideoCombine`、`WanVideoSampler`

**缺卡**（4）：`CR Text`、`ImageFromBatch+`、`MathExpression|pysssss`、`Text Concatenate`

**用到的条目**：LoadImage、WanVideoSampler、LoadLynxResampler、WanVideoDecode、WanVideoVAELoader、WanVideoTextEncodeCached、LynxEncodeFaceIP、WanVideoSetLoRAs

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Concatenate` 知识库中没有该节点类型的任何知识
