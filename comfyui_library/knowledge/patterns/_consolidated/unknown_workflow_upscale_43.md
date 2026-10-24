---
name: unknown_workflow_upscale_43
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.854
common_nodes: [ImageScaleDownToSize, LoadImage, PreviewImage, SaveImage, Text Multiline]
problems: []
missing: []
members: [图片生成/图生图/即梦4.0 图像编辑模型 多图编辑版_1966306375569674241.json, 图片生成/图生图/让修图师失业的老照片修复_1961379946193207297.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_43

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/即梦4.0 图像编辑模型 多图编辑版_1966306375569674241.json、图片生成/图生图/让修图师失业的老照片修复_1961379946193207297.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：85%

## 共有节点

全部 2 个 workflow 都包含：
- `ImageScaleDownToSize`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `Text Multiline`

**可变部分**（部分 workflow 才有）：
- `CR Upscale Image` —— 1/2 个有
- `RH_Jimeng4_Image2Image` —— 1/2 个有
- `RH_Nano_Banana_Image2Image` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
