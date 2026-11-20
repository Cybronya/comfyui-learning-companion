---
name: unknown_workflow_generic_736
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.775
common_nodes: [EG_ZZ_TMTX, GrowMaskWithBlur, LayerMask: MaskPreview, LoadImage, PreviewImage, SaveImage]
problems: []
missing: []
members: [平台全量/02-抠图_1926183733198557186.json, 平台全量/抠图（自动抠图+去白边）_1925031123494051842.json, 平台全量/抠图（自动抠图+去白边）_1971036407559004162.json, 平台全量/抠图（自动抠图+去白边）_2042619346572283906.json, 平台全量/最强抠图_1953098150468849665.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_736

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（平台全量/02-抠图_1926183733198557186.json、平台全量/抠图（自动抠图+去白边）_1925031123494051842.json、平台全量/抠图（自动抠图+去白边）_1971036407559004162.json、平台全量/抠图（自动抠图+去白边）_2042619346572283906.json、平台全量/最强抠图_1953098150468849665.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：78%

## 共有节点

全部 5 个 workflow 都包含：
- `EG_ZZ_TMTX`
- `GrowMaskWithBlur`
- `LayerMask: MaskPreview`
- `LoadImage`
- `PreviewImage`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `BiRefNet_Hugo` —— 4/5 个有
- `BRIA_RMBG_ModelLoader_Zho` —— 1/5 个有
- `BRIA_RMBG_Zho` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
