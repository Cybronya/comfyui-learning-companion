---
name: unknown_workflow_generic_511
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.717667
common_nodes: [LoadImage, PreviewImage, RH_LLMAPI_NODE, RH_Nano_Banana_Image2Image, SaveImage, Text Multiline, easy showAnything]
problems: []
missing: [CR Text, Text Multiline]
members: [图片生成/文生图/1961650062206156802.json, 图片生成/文生图/1965949778922221569.json, 图片生成/文生图/1981922967787585537.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_511

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/1961650062206156802.json、图片生成/文生图/1965949778922221569.json、图片生成/文生图/1981922967787585537.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：72%

## 共有节点

全部 3 个 workflow 都包含：
- `LoadImage`
- `PreviewImage`
- `RH_LLMAPI_NODE`
- `RH_Nano_Banana_Image2Image`
- `SaveImage`
- `Text Multiline`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 2/3 个有
- `ImageScale` —— 2/3 个有
- `CR Text` —— 1/3 个有
- `ImageConcanate` —— 1/3 个有
- `ImageScaleDownToSize` —— 1/3 个有
- `RH_Translator` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：CR Text、Text Multiline
