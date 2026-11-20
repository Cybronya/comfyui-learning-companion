---
name: unknown_workflow_generic_1949
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.875
common_nodes: [LoadImage, Preview3D, RunningHubPixal3DImageTo3D, RunningHubPixal3DModelLoader, RunningHubPixal3DSaveGLB, SaveImage]
problems: []
missing: []
members: [平台全量/图片转3D模型Pixal3D，腾讯开源_2056982641458634753.json, 平台全量/电商图片生成3D模型文件 pixal3D_2058795208820744193.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1949

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/图片转3D模型Pixal3D，腾讯开源_2056982641458634753.json、平台全量/电商图片生成3D模型文件 pixal3D_2058795208820744193.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：88%

## 共有节点

全部 2 个 workflow 都包含：
- `LoadImage`
- `Preview3D`
- `RunningHubPixal3DImageTo3D`
- `RunningHubPixal3DModelLoader`
- `RunningHubPixal3DSaveGLB`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
