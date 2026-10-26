---
name: unknown_workflow_generic_1547
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.95
common_nodes: [ImageConcanate, LoadImage, RH_Nano_Banana2_Image2Image, SaveImage]
problems: []
missing: []
members: [图片生成/图生图/果味GW-图像高清修复_2017936048059322369.json, 图片生成/图生图/王泽荣耀-全能生图PRO_2046409071376470018.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1547

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/果味GW-图像高清修复_2017936048059322369.json、图片生成/图生图/王泽荣耀-全能生图PRO_2046409071376470018.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：95%

## 共有节点

全部 2 个 workflow 都包含：
- `ImageConcanate`
- `LoadImage`
- `RH_Nano_Banana2_Image2Image`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `FluxKontextImageScale` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
