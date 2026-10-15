---
key: 视频生成/文生视频/MiniMax_H3_全能导演台（手动版）_V3.1_2100603957436571649.json
name: MiniMax_H3_全能导演台（手动版）_V3.1_2100603957436571649
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/MiniMax_H3_全能导演台（手动版）_V3.1_2100603957436571649.json
hash: 8c43baf1fcd4c948
coverage: 0.869565
learned_at: 2026-10-15 22:46:30
nodes: [BasicGuider, UNETLoader, VAELoader, VAELoader, easy multiTrackInfoOutput, easy multiTrackTaskOutput, easy minimaxH3ToVideo, ComfyMathExpression, SamplerCustomAdvanced, RandomNoise, MiniMaxH3MultiRateSamplerEXPT8, CLIPLoader, VHS_VideoCombine, MiniMaxH3MemoryEfficientSageAttentionPatch, LoraLoaderBypassModelOnly, LoraLoaderBypassModelOnly, MiniMaxH3AVDecodeT8, easy matchLine, easy promptLine, MarkdownNote, MarkdownNote, easy multiTrackEditor, MarkdownNote]
patterns: []
missing: []
---

# 视频生成/文生视频/MiniMax_H3_全能导演台（手动版）_V3.1_2100603957436571649.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/MiniMax_H3_全能导演台（手动版）_V3.1_2100603957436571649.json`

## 结构

**生成流程**：Model → Sampling → Other

**节点**（23 个）：
- `BasicGuider`
- `UNETLoader` ★核心
- `VAELoader`
- `VAELoader`
- `easy multiTrackInfoOutput`
- `easy multiTrackTaskOutput`
- `easy minimaxH3ToVideo`
- `ComfyMathExpression`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `MiniMaxH3MultiRateSamplerEXPT8` ★核心
- `CLIPLoader`
- `VHS_VideoCombine`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `LoraLoaderBypassModelOnly` ★核心
- `LoraLoaderBypassModelOnly` ★核心
- `MiniMaxH3AVDecodeT8`
- `easy matchLine`
- `easy promptLine`
- `MarkdownNote`
- `MarkdownNote`
- `easy multiTrackEditor`
- `MarkdownNote`

## 知识

覆盖率 **87%**（20/23）

**有卡**：`BasicGuider`、`UNETLoader`、`VAELoader`、`easy multiTrackInfoOutput`、`easy multiTrackTaskOutput`、`easy minimaxH3ToVideo`、`ComfyMathExpression`、`SamplerCustomAdvanced`、`RandomNoise`、`MiniMaxH3MultiRateSamplerEXPT8`、`CLIPLoader`、`VHS_VideoCombine`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`LoraLoaderBypassModelOnly`、`MiniMaxH3AVDecodeT8`、`easy matchLine`、`easy promptLine`、`easy multiTrackEditor`

**用到的条目**：VAELoader、CLIPLoader、UNETLoader、SamplerCustomAdvanced、MiniMaxH3MultiRateSamplerEXPT8、MiniMaxH3AVDecodeT8、LoraLoaderBypassModelOnly、easy promptLine
