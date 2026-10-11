---
key: 视频生成/文生视频/MiniMax_H3_全能导演台（手动版）_V3.1_2100603957436571649.json
name: MiniMax_H3_全能导演台（手动版）_V3.1_2100603957436571649
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/MiniMax_H3_全能导演台（手动版）_V3.1_2100603957436571649.json
hash: 8c43baf1fcd4c948
coverage: 0.608696
learned_at: 2026-10-11 22:12:44
nodes: [BasicGuider, UNETLoader, VAELoader, VAELoader, easy multiTrackInfoOutput, easy multiTrackTaskOutput, easy minimaxH3ToVideo, ComfyMathExpression, SamplerCustomAdvanced, RandomNoise, MiniMaxH3MultiRateSamplerEXPT8, CLIPLoader, VHS_VideoCombine, MiniMaxH3MemoryEfficientSageAttentionPatch, LoraLoaderBypassModelOnly, LoraLoaderBypassModelOnly, MiniMaxH3AVDecodeT8, easy matchLine, easy promptLine, MarkdownNote, MarkdownNote, easy multiTrackEditor, MarkdownNote]
patterns: []
missing: [easy matchLine, easy minimaxH3ToVideo, easy multiTrackEditor, easy multiTrackInfoOutput, easy multiTrackTaskOutput, easy promptLine]
discoveries: [次要节点 `easy matchLine` 知识库中没有该节点类型的任何知识, 次要节点 `easy minimaxH3ToVideo` 知识库中没有该节点类型的任何知识, 次要节点 `easy multiTrackEditor` 知识库中没有该节点类型的任何知识, 次要节点 `easy multiTrackInfoOutput` 仅有 SaveImage 的通用知识，没有该节点自己的说明, 次要节点 `easy multiTrackTaskOutput` 仅有 SaveImage 的通用知识，没有该节点自己的说明, 次要节点 `easy promptLine` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
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

覆盖率 **61%**（14/23）

**有卡**：`BasicGuider`、`UNETLoader`、`VAELoader`、`ComfyMathExpression`、`SamplerCustomAdvanced`、`RandomNoise`、`MiniMaxH3MultiRateSamplerEXPT8`、`CLIPLoader`、`VHS_VideoCombine`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`LoraLoaderBypassModelOnly`、`MiniMaxH3AVDecodeT8`

**缺卡**（6）：`easy matchLine`、`easy minimaxH3ToVideo`、`easy multiTrackEditor`、`easy multiTrackInfoOutput`、`easy multiTrackTaskOutput`、`easy promptLine`

**用到的条目**：VAELoader、CLIPLoader、UNETLoader、SamplerCustomAdvanced、MiniMaxH3MultiRateSamplerEXPT8、MiniMaxH3AVDecodeT8、LoraLoaderBypassModelOnly、BasicGuider

## 学习发现

- 次要节点 `easy matchLine` 知识库中没有该节点类型的任何知识
- 次要节点 `easy minimaxH3ToVideo` 知识库中没有该节点类型的任何知识
- 次要节点 `easy multiTrackEditor` 知识库中没有该节点类型的任何知识
- 次要节点 `easy multiTrackInfoOutput` 仅有 SaveImage 的通用知识，没有该节点自己的说明
- 次要节点 `easy multiTrackTaskOutput` 仅有 SaveImage 的通用知识，没有该节点自己的说明
- 次要节点 `easy promptLine` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
