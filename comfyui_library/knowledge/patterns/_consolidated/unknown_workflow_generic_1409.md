---
name: unknown_workflow_generic_1409
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.3715
common_nodes: [CR Text, CR Text Concatenate, GetNode, InversionDemoLazyIndexSwitch, JjkText, RH_Jimeng4_Image2Image, SaveImage, SetNode, ShowText|pysssss, easy int]
problems: []
missing: []
members: [图片生成/图生图/jimeng4.0-多图编辑版（5张图）Multi image editing version_1967852742049935362.json, 图片生成/文生图/Seedream 4.0 -即梦4.0文生图_1983824221187055617.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1409

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/jimeng4.0-多图编辑版（5张图）Multi image editing version_1967852742049935362.json、图片生成/文生图/Seedream 4.0 -即梦4.0文生图_1983824221187055617.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：37%

## 共有节点

全部 2 个 workflow 都包含：
- `CR Text`
- `CR Text Concatenate`
- `GetNode`
- `InversionDemoLazyIndexSwitch`
- `JjkText`
- `RH_Jimeng4_Image2Image`
- `SaveImage`
- `SetNode`
- `ShowText|pysssss`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `LoadImage` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
