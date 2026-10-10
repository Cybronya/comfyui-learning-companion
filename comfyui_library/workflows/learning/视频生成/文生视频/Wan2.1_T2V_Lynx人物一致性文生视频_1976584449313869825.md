---
key: 视频生成/文生视频/Wan2.1_T2V_Lynx人物一致性文生视频_1976584449313869825.json
name: Wan2.1_T2V_Lynx人物一致性文生视频_1976584449313869825
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.1_T2V_Lynx人物一致性文生视频_1976584449313869825.json
hash: 567094de4649d118
coverage: 0.477273
learned_at: 2026-10-10 23:06:34
nodes: [Note, MarkdownNote, WanVideoLoraSelectMulti, WanVideoVAELoader, LoadLynxResampler, GetNode, GetNode, GetNode, WanVideoTextEncodeCached, Note, Note, SetNode, WanVideoDecode, ImageConcatMulti, GetNode, Note, LynxEncodeFaceIP, GetNode, SetNode, LynxInsightFaceCrop, PreviewImage, PreviewImage, WanVideoBlockSwap, LoadImage, WanVideoEmptyEmbeds, WanVideoAddLynxEmbeds, VHS_VideoCombine, SetNode, SetNode, WanVideoExtraModelSelect, WanVideoExtraModelSelect, WanVideoModelLoader, WanVideoSetLoRAs, WanVideoSetBlockSwap, SetNode, SetNode, SetNode, GetNode, WanVideoSampler, WanVideoTextEncodeCached, GetNode, GetNode, VHS_VideoCombine, CR Text]
patterns: []
missing: [CR Text]
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/Wan2.1_T2V_Lynx人物一致性文生视频_1976584449313869825.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.1_T2V_Lynx人物一致性文生视频_1976584449313869825.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（44 个）：
- `Note`
- `MarkdownNote`
- `WanVideoLoraSelectMulti`
- `WanVideoVAELoader`
- `LoadLynxResampler` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoTextEncodeCached`
- `Note`
- `Note`
- `SetNode`
- `WanVideoDecode`
- `ImageConcatMulti`
- `GetNode`
- `Note`
- `LynxEncodeFaceIP`
- `GetNode`
- `SetNode`
- `LynxInsightFaceCrop`
- `PreviewImage`
- `PreviewImage`
- `WanVideoBlockSwap`
- `LoadImage`
- `WanVideoEmptyEmbeds`
- `WanVideoAddLynxEmbeds`
- `VHS_VideoCombine`
- `SetNode`
- `SetNode`
- `WanVideoExtraModelSelect`
- `WanVideoExtraModelSelect`
- `WanVideoModelLoader`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `WanVideoSampler` ★核心
- `WanVideoTextEncodeCached`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `CR Text`

## 知识

覆盖率 **48%**（21/44）

**有卡**：`WanVideoLoraSelectMulti`、`WanVideoVAELoader`、`LoadLynxResampler`、`WanVideoTextEncodeCached`、`WanVideoDecode`、`ImageConcatMulti`、`LynxEncodeFaceIP`、`LynxInsightFaceCrop`、`WanVideoBlockSwap`、`LoadImage`、`WanVideoEmptyEmbeds`、`WanVideoAddLynxEmbeds`、`VHS_VideoCombine`、`WanVideoExtraModelSelect`、`WanVideoModelLoader`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`WanVideoSampler`

**缺卡**（1）：`CR Text`

**用到的条目**：LoadImage、WanVideoSampler、LoadLynxResampler、WanVideoDecode、WanVideoVAELoader、WanVideoTextEncodeCached、LynxEncodeFaceIP、WanVideoSetLoRAs

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
