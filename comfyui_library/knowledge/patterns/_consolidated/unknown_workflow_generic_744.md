---
name: unknown_workflow_generic_744
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.6365
common_nodes: [AILab_MiniCPM_4_V, CreateVideo, GetImageSizeAndCount, LayerUtility: ImageScaleByAspectRatio V2, ShowText|pysssss, VHS_LoadVideo, VHS_VideoInfoLoaded, easy positive, easy promptReplace, easy saveText]
problems: []
missing: [LayerUtility: ImageScaleByAspectRatio V2, easy positive, easy promptReplace, easy saveText]
members: [视频生成/文生视频/1972214732772077570.json, 视频生成/文生视频/2066055892665430016.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_744

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/文生视频/1972214732772077570.json、视频生成/文生视频/2066055892665430016.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：64%

## 共有节点

全部 2 个 workflow 都包含：
- `AILab_MiniCPM_4_V`
- `CreateVideo`
- `GetImageSizeAndCount`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ShowText|pysssss`
- `VHS_LoadVideo`
- `VHS_VideoInfoLoaded`
- `easy positive`
- `easy promptReplace`
- `easy saveText`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: ImageScaleByAspectRatio V2、easy positive、easy promptReplace、easy saveText
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
