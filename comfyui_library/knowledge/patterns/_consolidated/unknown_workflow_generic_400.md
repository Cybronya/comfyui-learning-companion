---
name: unknown_workflow_generic_400
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.813167
common_nodes: [FlashVSRNode, Image Comparer (rgthree), LoadImage, SaveImage]
problems: []
missing: []
members: [图片生成/图生图/FlashVSR放大工作流模糊照片放大_2059091738949672962.json, 图片生成/图生图/FlashVSR放大工作流，模糊照片放大效果更好_2095685096534798338.json, 图片生成/图生图/FlashVSR放大工作流，模糊照片放大效果更好_2095694099302146050.json, 图片生成/图生图/FlashVSR放大，自用_1998393133144662017.json, 图片生成/图生图/flashVSR图片高清放大2k4k88图片像数放大_2067528242667544578.json, 图片生成/图生图/flashVSR图片高清放大_2067075698631729154.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_400

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/FlashVSR放大工作流模糊照片放大_2059091738949672962.json、图片生成/图生图/FlashVSR放大工作流，模糊照片放大效果更好_2095685096534798338.json、图片生成/图生图/FlashVSR放大工作流，模糊照片放大效果更好_2095694099302146050.json、图片生成/图生图/FlashVSR放大，自用_1998393133144662017.json、图片生成/图生图/flashVSR图片高清放大2k4k88图片像数放大_2067528242667544578.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 6 个 workflow 都包含：
- `FlashVSRNode`
- `Image Comparer (rgthree)`
- `LoadImage`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `INTConstant` —— 4/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/6 个有
- `easy imageScaleDownToSize` —— 3/6 个有
- `Int` —— 2/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
