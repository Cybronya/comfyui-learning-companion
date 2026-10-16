---
key: 视频生成/图生视频/MiniMax H3 Ref2VA 多图参考生视频优化版 V1.1_2091138712674594817.json
name: MiniMax H3 Ref2VA 多图参考生视频优化版 V1.1_2091138712674594817
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/MiniMax H3 Ref2VA 多图参考生视频优化版 V1.1_2091138712674594817.json
hash: d8dce642a936341b
coverage: 0.95
learned_at: 2026-10-16 22:30:36
nodes: [RHMiniMaxH3Ref2VATextEncoderLoader, RHMiniMaxH3Ref2VAModelLoader, RHMiniMaxH3Ref2VAVAELoader, LoadImage, RHMiniMaxH3DualSigmaSampler, LoadImage, RHMiniMaxH3Ref2VAImageReference, RHMiniMaxH3EmptyAVLatent, RHMiniMaxH3DecodeAV, CreateVideo, RHMiniMaxH3Ref2VAImageReference, RHMiniMaxH3Ref2VAImageReference, RHMiniMaxH3Ref2VAImageReference, LoadImage, RHMiniMaxH3Ref2VATarget, RHMiniMaxH3Ref2VAEncode, MarkdownNote, Label (rgthree), SaveVideo, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/MiniMax H3 Ref2VA 多图参考生视频优化版 V1.1_2091138712674594817.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/MiniMax H3 Ref2VA 多图参考生视频优化版 V1.1_2091138712674594817.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（20 个）：
- `RHMiniMaxH3Ref2VATextEncoderLoader`
- `RHMiniMaxH3Ref2VAModelLoader`
- `RHMiniMaxH3Ref2VAVAELoader`
- `LoadImage`
- `RHMiniMaxH3DualSigmaSampler` ★核心
- `LoadImage`
- `RHMiniMaxH3Ref2VAImageReference`
- `RHMiniMaxH3EmptyAVLatent`
- `RHMiniMaxH3DecodeAV`
- `CreateVideo`
- `RHMiniMaxH3Ref2VAImageReference`
- `RHMiniMaxH3Ref2VAImageReference`
- `RHMiniMaxH3Ref2VAImageReference`
- `LoadImage`
- `RHMiniMaxH3Ref2VATarget`
- `RHMiniMaxH3Ref2VAEncode`
- `MarkdownNote`
- `Label (rgthree)`
- `SaveVideo`
- `LoadImage`

## 知识

覆盖率 **95%**（19/20）

**有卡**：`RHMiniMaxH3Ref2VATextEncoderLoader`、`RHMiniMaxH3Ref2VAModelLoader`、`RHMiniMaxH3Ref2VAVAELoader`、`LoadImage`、`RHMiniMaxH3DualSigmaSampler`、`RHMiniMaxH3Ref2VAImageReference`、`RHMiniMaxH3EmptyAVLatent`、`RHMiniMaxH3DecodeAV`、`CreateVideo`、`RHMiniMaxH3Ref2VATarget`、`RHMiniMaxH3Ref2VAEncode`、`Label (rgthree)`、`SaveVideo`

**用到的条目**：LoadImage、RHMiniMaxH3DualSigmaSampler、RHMiniMaxH3DecodeAV、RHMiniMaxH3EmptyAVLatent、RHMiniMaxH3Ref2VAEncode、RHMiniMaxH3Ref2VATextEncoderLoader、RHMiniMaxH3Ref2VAVAELoader、SaveVideo
