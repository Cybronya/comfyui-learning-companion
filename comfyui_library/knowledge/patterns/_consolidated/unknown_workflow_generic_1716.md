---
name: unknown_workflow_generic_1716
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.798
common_nodes: [ImageConcatMulti, LoadImage, PreviewImage, RH_Captioner_Pro, RH_Nano_Banana2_Gemini31Flash, SaveImage, easy saveText, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/场景背景复刻迁移产品换背景同个背景换产品_2069780267874734082.json, 平台全量/复刻场景 产品替换_1888633980286337025.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1716

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/场景背景复刻迁移产品换背景同个背景换产品_2069780267874734082.json、平台全量/复刻场景 产品替换_1888633980286337025.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：80%

## 共有节点

全部 2 个 workflow 都包含：
- `ImageConcatMulti`
- `LoadImage`
- `PreviewImage`
- `RH_Captioner_Pro`
- `RH_Nano_Banana2_Gemini31Flash`
- `SaveImage`
- `easy saveText`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `TT_img_enc` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
