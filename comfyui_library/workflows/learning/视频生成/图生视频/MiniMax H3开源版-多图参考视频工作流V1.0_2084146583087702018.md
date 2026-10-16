---
key: 视频生成/图生视频/MiniMax H3开源版-多图参考视频工作流V1.0_2084146583087702018.json
name: MiniMax H3开源版-多图参考视频工作流V1.0_2084146583087702018
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/MiniMax H3开源版-多图参考视频工作流V1.0_2084146583087702018.json
hash: f5b892ec9c23e059
coverage: 0.947368
learned_at: 2026-10-16 19:52:15
nodes: [RHMiniMaxH3EmptyAVLatent, RHMiniMaxH3DecodeAV, RHMiniMaxH3Ref2VATextEncoderLoader, RHMiniMaxH3Ref2VAModelLoader, RHMiniMaxH3Ref2VAVAELoader, RHMiniMaxH3Ref2VAImageReference, RHMiniMaxH3DualSigmaSampler, RHMiniMaxH3Ref2VAImageReference, SaveVideo, CreateVideo, RHMiniMaxH3Ref2VAImageReference, LoadImage, LoadImage, LoadImage, RHMiniMaxH3Ref2VAEncode, PreviewAny, RHMiniMaxH3Ref2VATarget, RH_LLMAPI_Pro_Node, Text]
patterns: []
missing: []
---

# 视频生成/图生视频/MiniMax H3开源版-多图参考视频工作流V1.0_2084146583087702018.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/MiniMax H3开源版-多图参考视频工作流V1.0_2084146583087702018.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（19 个）：
- `RHMiniMaxH3EmptyAVLatent`
- `RHMiniMaxH3DecodeAV`
- `RHMiniMaxH3Ref2VATextEncoderLoader`
- `RHMiniMaxH3Ref2VAModelLoader`
- `RHMiniMaxH3Ref2VAVAELoader`
- `RHMiniMaxH3Ref2VAImageReference`
- `RHMiniMaxH3DualSigmaSampler` ★核心
- `RHMiniMaxH3Ref2VAImageReference`
- `SaveVideo`
- `CreateVideo`
- `RHMiniMaxH3Ref2VAImageReference`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `RHMiniMaxH3Ref2VAEncode`
- `PreviewAny`
- `RHMiniMaxH3Ref2VATarget`
- `RH_LLMAPI_Pro_Node`
- `Text`

## 知识

覆盖率 **95%**（18/19）

**有卡**：`RHMiniMaxH3EmptyAVLatent`、`RHMiniMaxH3DecodeAV`、`RHMiniMaxH3Ref2VATextEncoderLoader`、`RHMiniMaxH3Ref2VAModelLoader`、`RHMiniMaxH3Ref2VAVAELoader`、`RHMiniMaxH3Ref2VAImageReference`、`RHMiniMaxH3DualSigmaSampler`、`SaveVideo`、`CreateVideo`、`LoadImage`、`RHMiniMaxH3Ref2VAEncode`、`RHMiniMaxH3Ref2VATarget`、`RH_LLMAPI_Pro_Node`、`Text`

**用到的条目**：LoadImage、RHMiniMaxH3DualSigmaSampler、RHMiniMaxH3DecodeAV、RHMiniMaxH3EmptyAVLatent、RHMiniMaxH3Ref2VAEncode、RHMiniMaxH3Ref2VATextEncoderLoader、RHMiniMaxH3Ref2VAVAELoader、SaveVideo
