---
name: unknown_workflow_video_lora_unet
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.879143
common_nodes: [CLIPLoader, LoraLoaderModelOnly, ModelAttentionBackend, ModelPreviewOverrideKJ, SaveVideo, UNETLoader, VAELoader, easy modelLoaderPack, easy multiTrackEditor, easy multitrackProject, easy multitrackProjectVideoCombine]
problems: []
missing: []
members: [平台全量/RH-MINIMAX+H3+Motion+Context_长视频生成工作流V2_2108369449270206466.json, 视频生成/图生视频/MiniMax H3 长视频导演台-EasyMedia - Motion Context V2_2107329550337265665.json, 视频生成/图生视频/MiniMax-H3开源-极简导演台_2097630312233783298.json, 视频生成/图生视频/MiniMaxH3-极简导演台_2095766324508184577.json, 视频生成/图生视频/Minmax H4多轨编辑器_2097344874348638209.json, 视频生成/图生视频/RH-MINIMAX+H3+Motion+Context_长视频生成工作流V2_2105583664313749506.json, 视频生成/文生视频/RH-MINIMAX+H3+Motion+Context 长视频生成工作流V2_2103474631964446722.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_unet

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（平台全量/RH-MINIMAX+H3+Motion+Context_长视频生成工作流V2_2108369449270206466.json、视频生成/图生视频/MiniMax H3 长视频导演台-EasyMedia - Motion Context V2_2107329550337265665.json、视频生成/图生视频/MiniMax-H3开源-极简导演台_2097630312233783298.json、视频生成/图生视频/MiniMaxH3-极简导演台_2095766324508184577.json、视频生成/图生视频/Minmax H4多轨编辑器_2097344874348638209.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `LoraLoaderModelOnly`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `SaveVideo`
- `UNETLoader`
- `VAELoader`
- `easy modelLoaderPack`
- `easy multiTrackEditor`
- `easy multitrackProject`
- `easy multitrackProjectVideoCombine`

**可变部分**（部分 workflow 才有）：
- `BasicScheduler` —— 5/7 个有
- `KSamplerSelect` —— 5/7 个有
- `ManualSigmas` —— 4/7 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 4/7 个有
- `easy saveVideo` —— 4/7 个有
- `Fast Groups Bypasser (rgthree)` —— 2/7 个有
- `LoadImage` —— 2/7 个有
- `CreateVideo` —— 1/7 个有
- `GetVideoComponents` —— 1/7 个有
- `ImageResizeKJv2` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
