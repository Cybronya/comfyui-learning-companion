---
name: unknown_workflow_generic_1833
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.807
common_nodes: [CR Prompt Text, JWStringConcat, LoadImage, Qwen3_VQA, RH_Nano_Banana2_Image2Image, SaveImage, easy cleanGpuUsed, easy showAnything]
problems: []
missing: []
members: [图片生成/文生图/nano 全能图片V1 2 pro_1992928243825262593.json, 平台全量/分镜脚本_1999034464342790146.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1833

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/nano 全能图片V1 2 pro_1992928243825262593.json、平台全量/分镜脚本_1999034464342790146.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：81%

## 共有节点

全部 2 个 workflow 都包含：
- `CR Prompt Text`
- `JWStringConcat`
- `LoadImage`
- `Qwen3_VQA`
- `RH_Nano_Banana2_Image2Image`
- `SaveImage`
- `easy cleanGpuUsed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `Image Comparer (rgthree)` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
