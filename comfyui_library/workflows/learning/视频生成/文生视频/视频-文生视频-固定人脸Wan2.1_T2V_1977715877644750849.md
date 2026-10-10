---
key: 视频生成/文生视频/视频-文生视频-固定人脸Wan2.1_T2V_1977715877644750849.json
name: 视频-文生视频-固定人脸Wan2.1_T2V_1977715877644750849
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/视频-文生视频-固定人脸Wan2.1_T2V_1977715877644750849.json
hash: a5d49fa4e3527c11
coverage: 0.638298
learned_at: 2026-10-10 23:13:50
nodes: [WanVideoBlockSwap, WanVideoModelLoader, WanVideoLoraSelectMulti, WanVideoTorchCompileSettings, WanVideoExtraModelSelect, WanVideoTextEncodeCached, GetNode, WanVideoTextEncodeCached, Note, Note, LoadLynxResampler, JWInteger, Wan22PromptSelector, JWInteger, JWInteger, JWInteger, WanVideoVAELoader, WanVideoSetLoRAs, SetNode, WanVideoSetBlockSwap, SetNode, WanVideoAddLynxEmbeds, PreviewImage, PreviewImage, WanVideoEmptyEmbeds, LynxEncodeFaceIP, SetNode, MathExpression|pysssss, Note, ImpactSwitch, Text Concatenate, easy showAnything, Note, MarkdownNote, RH_LLMAPI_NODE, LynxInsightFaceCrop, WanVideoExtraModelSelect, WanVideoDecode, ImageFromBatch+, ImageConcatMulti, VHS_VideoCombine, WanVideoSampler, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, LoadImage, CR Text]
patterns: []
missing: [CR Text, ImageFromBatch+, MathExpression|pysssss, Text Concatenate]
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `Text Concatenate` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/视频-文生视频-固定人脸Wan2.1_T2V_1977715877644750849.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/视频-文生视频-固定人脸Wan2.1_T2V_1977715877644750849.json`

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
- `LoadImage`
- `CR Text`

## 知识

覆盖率 **64%**（30/47）

**有卡**：`WanVideoBlockSwap`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`WanVideoTorchCompileSettings`、`WanVideoExtraModelSelect`、`WanVideoTextEncodeCached`、`LoadLynxResampler`、`JWInteger`、`Wan22PromptSelector`、`WanVideoVAELoader`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`WanVideoAddLynxEmbeds`、`WanVideoEmptyEmbeds`、`LynxEncodeFaceIP`、`RH_LLMAPI_NODE`、`LynxInsightFaceCrop`、`WanVideoDecode`、`ImageConcatMulti`、`VHS_VideoCombine`、`WanVideoSampler`、`LoadImage`

**缺卡**（4）：`CR Text`、`ImageFromBatch+`、`MathExpression|pysssss`、`Text Concatenate`

**用到的条目**：LoadImage、WanVideoSampler、LoadLynxResampler、WanVideoDecode、WanVideoVAELoader、WanVideoTextEncodeCached、LynxEncodeFaceIP、WanVideoSetLoRAs

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Concatenate` 知识库中没有该节点类型的任何知识
