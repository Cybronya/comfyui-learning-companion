---
name: unknown_workflow_generic_1441
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.697
common_nodes: [CR Text, LoadImage, PreviewImage, PrimitiveInt, QwenImageModelLoader, RH_QwenImageGenerator, SaveImage]
problems: []
missing: []
members: [图片生成/图生图/通义千问图像反推生图（可中文）_1952626130375380994.json, 图片生成/图生图/通义千问图像模型（支持中文生成，对标即梦）_1952539310585253890.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1441

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/通义千问图像反推生图（可中文）_1952626130375380994.json、图片生成/图生图/通义千问图像模型（支持中文生成，对标即梦）_1952539310585253890.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：70%

## 共有节点

全部 2 个 workflow 都包含：
- `CR Text`
- `LoadImage`
- `PreviewImage`
- `PrimitiveInt`
- `QwenImageModelLoader`
- `RH_QwenImageGenerator`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `RH_Captioner` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
