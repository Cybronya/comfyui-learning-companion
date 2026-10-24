---
name: unknown_workflow_generic_1297
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.6025
common_nodes: [LoadAndResizeImage, RH_ComfyFluxKontext, RH_Translator, SaveImage, ShowText|pysssss]
problems: []
missing: []
members: [图片生成/图生图/【免费】Flux-Kontext图像编辑（一句话改图）_1928999736483942401.json, 图片生成/图生图/【电商模特产品展示】Flux Kontext图像编辑（免费）_1929214915087863809.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1297

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/【免费】Flux-Kontext图像编辑（一句话改图）_1928999736483942401.json、图片生成/图生图/【电商模特产品展示】Flux Kontext图像编辑（免费）_1929214915087863809.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：60%

## 共有节点

全部 2 个 workflow 都包含：
- `LoadAndResizeImage`
- `RH_ComfyFluxKontext`
- `RH_Translator`
- `SaveImage`
- `ShowText|pysssss`

**可变部分**（部分 workflow 才有）：
- `ImageConcanate` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `easy imageRemBg` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
