---
name: unknown_workflow_video_upscale_lora_5
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.82
common_nodes: [CLIPLoader, LoraLoaderModelOnly, MiniMaxH3Director, MiniMaxH3DirectorRefine, MiniMaxH3MemoryEfficientSageAttentionPatch, UNETLoader, UpscaleModelLoader, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax H3 导演台全能工作流-fl2v-图生视频_2109971094978523137.json, 视频生成/图生视频/MiniMax H3 导演台全能工作流无水印版_2094988974698876930.json, 视频生成/图生视频/MiniMax H3 导演台工作流-ref2va_2091323053144887297.json, 视频生成/文生视频/MiniMax H3 Director 全能参考视频导演台｜无水印版_2097926685592219649.json, 视频生成/文生视频/MiniMax H3 导演台全能工作流-fl2v_2090357634460372993.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_lora_5

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3 导演台全能工作流-fl2v-图生视频_2109971094978523137.json、视频生成/图生视频/MiniMax H3 导演台全能工作流无水印版_2094988974698876930.json、视频生成/图生视频/MiniMax H3 导演台工作流-ref2va_2091323053144887297.json、视频生成/文生视频/MiniMax H3 Director 全能参考视频导演台｜无水印版_2097926685592219649.json、视频生成/文生视频/MiniMax H3 导演台全能工作流-fl2v_2090357634460372993.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `LoraLoaderModelOnly`
- `MiniMaxH3Director`
- `MiniMaxH3DirectorRefine`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 2/5 个有
- `PreviewAny` —— 2/5 个有
- `孤海注释` —— 2/5 个有
- `DapaoImageSplitNode` —— 1/5 个有
- `SaveImage` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
