---
name: unknown_workflow_upscale_81
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.793
common_nodes: [BooleanPrimitive, FILM VFI, ImageScale, ImageScaleBy, ImageUpscaleWithModel, SimpleMath+, UpscaleModelLoader, VHS_LoadVideo, VHS_VideoInfo, easy ifElse, easy imageSize]
problems: []
missing: []
members: [平台全量/视频放大器-wan2.1_1962399750114906114.json, 平台全量/（支持18禁）视频放大+插帧_2010915275142598658.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_81

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/视频放大器-wan2.1_1962399750114906114.json、平台全量/（支持18禁）视频放大+插帧_2010915275142598658.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：79%

## 共有节点

全部 2 个 workflow 都包含：
- `BooleanPrimitive`
- `FILM VFI`
- `ImageScale`
- `ImageScaleBy`
- `ImageUpscaleWithModel`
- `SimpleMath+`
- `UpscaleModelLoader`
- `VHS_LoadVideo`
- `VHS_VideoInfo`
- `easy ifElse`
- `easy imageSize`

**可变部分**（部分 workflow 才有）：
- `DuckHideNode` —— 1/2 个有
- `GetNode` —— 1/2 个有
- `ImageFromBatch+` —— 1/2 个有
- `Int` —— 1/2 个有
- `SaveImage` —— 1/2 个有
- `SetNode` —— 1/2 个有
- `VHS_VideoCombine` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
