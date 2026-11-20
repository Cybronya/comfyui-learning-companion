---
name: unknown_workflow_generic_1850
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.635
common_nodes: [LoadImage, PreviewImage, RH_Nano_Banana2_Image2Image, SaveImage, ShowText|pysssss]
problems: []
missing: []
members: [图片生成/文生图/全能图片V1 Pro 文生图（图片反推）_1998180384842088450.json, 平台全量/电商产品_api_2038862280120602626.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1850

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/全能图片V1 Pro 文生图（图片反推）_1998180384842088450.json、平台全量/电商产品_api_2038862280120602626.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：64%

## 共有节点

全部 2 个 workflow 都包含：
- `LoadImage`
- `PreviewImage`
- `RH_Nano_Banana2_Image2Image`
- `SaveImage`
- `ShowText|pysssss`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: JoyCaptionBeta1` —— 1/2 个有
- `LayerUtility: LoadJoyCaptionBeta1Model` —— 1/2 个有
- `RH_LLMAPI_Pro_Node` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
