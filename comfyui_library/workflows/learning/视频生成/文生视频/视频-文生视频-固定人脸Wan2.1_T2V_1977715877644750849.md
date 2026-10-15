---
key: 视频生成/文生视频/视频-文生视频-固定人脸Wan2.1_T2V_1977715877644750849.json
name: 视频-文生视频-固定人脸Wan2.1_T2V_1977715877644750849
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/视频-文生视频-固定人脸Wan2.1_T2V_1977715877644750849.json
hash: a5d49fa4e3527c11
coverage: 0.723404
learned_at: 2026-10-15 22:49:00
nodes: [WanVideoBlockSwap, WanVideoModelLoader, WanVideoLoraSelectMulti, WanVideoTorchCompileSettings, WanVideoExtraModelSelect, WanVideoTextEncodeCached, GetNode, WanVideoTextEncodeCached, Note, Note, LoadLynxResampler, JWInteger, Wan22PromptSelector, JWInteger, JWInteger, JWInteger, WanVideoVAELoader, WanVideoSetLoRAs, SetNode, WanVideoSetBlockSwap, SetNode, WanVideoAddLynxEmbeds, PreviewImage, PreviewImage, WanVideoEmptyEmbeds, LynxEncodeFaceIP, SetNode, MathExpression|pysssss, Note, ImpactSwitch, Text Concatenate, easy showAnything, Note, MarkdownNote, RH_LLMAPI_NODE, LynxInsightFaceCrop, WanVideoExtraModelSelect, WanVideoDecode, ImageFromBatch+, ImageConcatMulti, VHS_VideoCombine, WanVideoSampler, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, LoadImage, CR Text]
patterns: []
missing: []
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

覆盖率 **72%**（34/47）

**有卡**：`WanVideoBlockSwap`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`WanVideoTorchCompileSettings`、`WanVideoExtraModelSelect`、`WanVideoTextEncodeCached`、`LoadLynxResampler`、`JWInteger`、`Wan22PromptSelector`、`WanVideoVAELoader`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`WanVideoAddLynxEmbeds`、`WanVideoEmptyEmbeds`、`LynxEncodeFaceIP`、`MathExpression|pysssss`、`Text Concatenate`、`RH_LLMAPI_NODE`、`LynxInsightFaceCrop`、`WanVideoDecode`、`ImageFromBatch+`、`ImageConcatMulti`、`VHS_VideoCombine`、`WanVideoSampler`、`LoadImage`、`CR Text`

**用到的条目**：LoadImage、WanVideoSampler、LoadLynxResampler、WanVideoDecode、WanVideoVAELoader、WanVideoTextEncodeCached、LynxEncodeFaceIP、WanVideoSetLoRAs
