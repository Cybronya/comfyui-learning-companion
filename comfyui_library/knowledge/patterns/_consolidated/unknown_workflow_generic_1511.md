---
name: unknown_workflow_generic_1511
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.832
common_nodes: [CR SDXL Aspect Ratio, DF_Get_image_size, ImageConcanate, ImageResizeKJv2, ImageScaleDownToSize, LoadImage, PreviewImage, RH_Translator, RunningHub DreamO, SaveImage, ShowText|pysssss]
problems: []
missing: []
members: [图片生成/图生图/字节DreamO-ID人像摄影_1926853143127072770.json, 图片生成/图生图/字节DreamO-风格迁移_1926871922779299842.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1511

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/字节DreamO-ID人像摄影_1926853143127072770.json、图片生成/图生图/字节DreamO-风格迁移_1926871922779299842.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：83%

## 共有节点

全部 2 个 workflow 都包含：
- `CR SDXL Aspect Ratio`
- `DF_Get_image_size`
- `ImageConcanate`
- `ImageResizeKJv2`
- `ImageScaleDownToSize`
- `LoadImage`
- `PreviewImage`
- `RH_Translator`
- `RunningHub DreamO`
- `SaveImage`
- `ShowText|pysssss`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 1/2 个有
- `TextInputBasic` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
