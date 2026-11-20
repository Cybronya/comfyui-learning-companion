---
name: unknown_workflow_generic_1384
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7625
common_nodes: [ImageConcatMulti, LoadImage, PreviewImage, QwenImageModelLoader, RH_Captioner, RH_QwenImageGenerator, SaveImage, easy cleanGpuUsed, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/Landingpage落地页图生图洗图_1952646160060231681.json, 图片生成/文生图/通义千问反推图生图(可反推汉字)_1952614485590773761.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1384

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Landingpage落地页图生图洗图_1952646160060231681.json、图片生成/文生图/通义千问反推图生图(可反推汉字)_1952614485590773761.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：76%

## 共有节点

全部 2 个 workflow 都包含：
- `ImageConcatMulti`
- `LoadImage`
- `PreviewImage`
- `QwenImageModelLoader`
- `RH_Captioner`
- `RH_QwenImageGenerator`
- `SaveImage`
- `easy cleanGpuUsed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `PrimitiveInt` —— 1/2 个有
- `easy imageSize` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
