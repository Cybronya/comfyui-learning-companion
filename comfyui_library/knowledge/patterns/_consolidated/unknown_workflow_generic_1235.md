---
name: unknown_workflow_generic_1235
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.4175
common_nodes: [GetNode, Image Comparer (rgthree), Int, JjkText, LoadImage, RH_Captioner, RH_Nano_Banana_Image2Image, SaveImage, SetNode, ShowText|pysssss, StringFunction|pysssss, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/GTYH_V1.5-2_1984502909108895745.json, 图片生成/图生图/GTYH_V1.6_1985246203967381505.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1235

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/GTYH_V1.5-2_1984502909108895745.json、图片生成/图生图/GTYH_V1.6_1985246203967381505.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：42%

## 共有节点

全部 2 个 workflow 都包含：
- `GetNode`
- `Image Comparer (rgthree)`
- `Int`
- `JjkText`
- `LoadImage`
- `RH_Captioner`
- `RH_Nano_Banana_Image2Image`
- `SaveImage`
- `SetNode`
- `ShowText|pysssss`
- `StringFunction|pysssss`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Big Image Switch [Dream]` —— 1/2 个有
- `CR Text` —— 1/2 个有
- `Image Switch (JPS)` —— 1/2 个有
- `ImpactStringSelector` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `SimpleMath+` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
