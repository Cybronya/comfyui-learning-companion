---
key: 视频生成/文生视频/Wan2.1_T2V_Lynx人物一致性文生视频_1976584449313869825.json
name: Wan2.1_T2V_Lynx人物一致性文生视频_1976584449313869825
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.1_T2V_Lynx人物一致性文生视频_1976584449313869825.json
hash: 567094de4649d118
coverage: 0.5
learned_at: 2026-10-15 22:47:08
nodes: [Note, MarkdownNote, WanVideoLoraSelectMulti, WanVideoVAELoader, LoadLynxResampler, GetNode, GetNode, GetNode, WanVideoTextEncodeCached, Note, Note, SetNode, WanVideoDecode, ImageConcatMulti, GetNode, Note, LynxEncodeFaceIP, GetNode, SetNode, LynxInsightFaceCrop, PreviewImage, PreviewImage, WanVideoBlockSwap, LoadImage, WanVideoEmptyEmbeds, WanVideoAddLynxEmbeds, VHS_VideoCombine, SetNode, SetNode, WanVideoExtraModelSelect, WanVideoExtraModelSelect, WanVideoModelLoader, WanVideoSetLoRAs, WanVideoSetBlockSwap, SetNode, SetNode, SetNode, GetNode, WanVideoSampler, WanVideoTextEncodeCached, GetNode, GetNode, VHS_VideoCombine, CR Text]
patterns: []
missing: []
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

覆盖率 **50%**（22/44）

**有卡**：`WanVideoLoraSelectMulti`、`WanVideoVAELoader`、`LoadLynxResampler`、`WanVideoTextEncodeCached`、`WanVideoDecode`、`ImageConcatMulti`、`LynxEncodeFaceIP`、`LynxInsightFaceCrop`、`WanVideoBlockSwap`、`LoadImage`、`WanVideoEmptyEmbeds`、`WanVideoAddLynxEmbeds`、`VHS_VideoCombine`、`WanVideoExtraModelSelect`、`WanVideoModelLoader`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`WanVideoSampler`、`CR Text`

**用到的条目**：LoadImage、WanVideoSampler、LoadLynxResampler、WanVideoDecode、WanVideoVAELoader、WanVideoTextEncodeCached、LynxEncodeFaceIP、WanVideoSetLoRAs
