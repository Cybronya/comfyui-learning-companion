---
name: unknown_workflow_video_sampler_31
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.7048
common_nodes: [DiffuEraserLoader, DiffuEraserSampler, DownloadAndLoadSAM2Model, GrowMaskWithBlur, MaskToImage, PointsEditor, PreviewAnimation, Sam2Segmentation, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo]
problems: []
missing: []
members: [平台全量/视频-万物消除_1989165974425309186.json, 平台全量/视频-万物消除（详细讲解使用）_1915522326769631234.json, 平台全量/视频-万物消除（详细讲解使用）_2056227025672736770.json, 视频生成/图生视频/视频-万物消除详细讲解使用_2115958497782358018.json, 视频生成/图生视频/视频-万物消除详细讲解使用_2115969922005291009.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_31

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（平台全量/视频-万物消除_1989165974425309186.json、平台全量/视频-万物消除（详细讲解使用）_1915522326769631234.json、平台全量/视频-万物消除（详细讲解使用）_2056227025672736770.json、视频生成/图生视频/视频-万物消除详细讲解使用_2115958497782358018.json、视频生成/图生视频/视频-万物消除详细讲解使用_2115969922005291009.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：70%

## 共有节点

全部 5 个 workflow 都包含：
- `DiffuEraserLoader`
- `DiffuEraserSampler`
- `DownloadAndLoadSAM2Model`
- `GrowMaskWithBlur`
- `MaskToImage`
- `PointsEditor`
- `PreviewAnimation`
- `Sam2Segmentation`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 2/5 个有
- `SetNode` —— 2/5 个有
- `VHS_VideoInfoSource` —— 2/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
