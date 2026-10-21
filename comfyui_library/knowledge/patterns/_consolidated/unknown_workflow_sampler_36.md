---
name: unknown_workflow_sampler_36
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.6285
common_nodes: [LayerUtility: ImageScaleByAspectRatio V2, LoadImage, PreviewImage, RH_Translator, RunningHub ICCustom Loader, RunningHub ICCustom Sampler, SaveImage, easy imageRemBg]
problems: []
missing: [LayerUtility: ImageScaleByAspectRatio V2, RunningHub ICCustom Loader, easy imageRemBg, RunningHub ICCustom Sampler]
members: [图片生成/文生图/1963484973771870210.json, 图片生成/文生图/IC Custom万物迁移_2073390352022728706.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_36

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/1963484973771870210.json、图片生成/文生图/IC Custom万物迁移_2073390352022728706.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：63%

## 共有节点

全部 2 个 workflow 都包含：
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `PreviewImage`
- `RH_Translator`
- `RunningHub ICCustom Loader`
- `RunningHub ICCustom Sampler`
- `SaveImage`
- `easy imageRemBg`

**可变部分**（部分 workflow 才有）：
- `ImageConcanate` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: ImageScaleByAspectRatio V2、RunningHub ICCustom Loader、easy imageRemBg、RunningHub ICCustom Sampler
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
