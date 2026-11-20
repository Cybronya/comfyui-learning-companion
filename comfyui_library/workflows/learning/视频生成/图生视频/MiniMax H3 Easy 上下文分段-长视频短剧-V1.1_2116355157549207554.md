---
key: 视频生成/图生视频/MiniMax H3 Easy 上下文分段-长视频短剧-V1.1_2116355157549207554.json
name: MiniMax H3 Easy 上下文分段-长视频短剧-V1.1_2116355157549207554
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/MiniMax H3 Easy 上下文分段-长视频短剧-V1.1_2116355157549207554.json
hash: b5e9fc170bd17846
coverage: 0.904762
learned_at: 2026-11-02 19:17:48
nodes: [UNETLoader, CLIPLoader, VAELoader, VAELoader, MiniMaxH3EasyModelAdapter, MiniMaxH3EasyContextSegments, MiniMaxH3MemoryEfficientSageAttentionPatch, LoraLoaderModelOnly, BasicScheduler, KSamplerSelect, MiniMaxH3EasySegmentRender, MiniMaxH3EasySegmentDecode, SaveVideo, Fast Groups Bypasser (rgthree), LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, MarkdownNote]
patterns: []
missing: []
---

# 视频生成/图生视频/MiniMax H3 Easy 上下文分段-长视频短剧-V1.1_2116355157549207554.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/MiniMax H3 Easy 上下文分段-长视频短剧-V1.1_2116355157549207554.json`

## 结构

**生成流程**：Model → Sampling → Output → Other

**节点**（21 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `VAELoader`
- `MiniMaxH3EasyModelAdapter`
- `MiniMaxH3EasyContextSegments`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `LoraLoaderModelOnly` ★核心
- `BasicScheduler`
- `KSamplerSelect` ★核心
- `MiniMaxH3EasySegmentRender`
- `MiniMaxH3EasySegmentDecode`
- `SaveVideo`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `MarkdownNote`

## 知识

覆盖率 **90%**（19/21）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`MiniMaxH3EasyModelAdapter`、`MiniMaxH3EasyContextSegments`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`LoraLoaderModelOnly`、`BasicScheduler`、`KSamplerSelect`、`MiniMaxH3EasySegmentRender`、`MiniMaxH3EasySegmentDecode`、`SaveVideo`、`LoadImage`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader、KSamplerSelect、MiniMaxH3EasySegmentDecode、SaveVideo
