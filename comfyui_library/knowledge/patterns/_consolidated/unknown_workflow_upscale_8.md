---
name: unknown_workflow_upscale_8
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.874714
common_nodes: [ImageUpscaleWithModel, LoadImage, SaveImage, UpscaleModelLoader]
problems: []
missing: []
members: [图片生成/图生图/图像放大分辨率提升工作流_1923637812476694530.json, 图片生成/图生图/图像通过模型放大工作流_1989950712320847874.json, 图片生成/图生图/放大模型测试工作流_2044656314676158465.json, 图片生成/图生图/最强图像一键换脸_1985270525016555522.json, 图片生成/图生图/最简单的放大_2094658859259486210.json, 图片生成/图生图/最简单的放大_2094660141705687042.json, 图片生成/图生图/通过模型放大工作流（高性价比放大）_2086073555678224385.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_8

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/图像放大分辨率提升工作流_1923637812476694530.json、图片生成/图生图/图像通过模型放大工作流_1989950712320847874.json、图片生成/图生图/放大模型测试工作流_2044656314676158465.json、图片生成/图生图/最强图像一键换脸_1985270525016555522.json、图片生成/图生图/最简单的放大_2094658859259486210.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 7 个 workflow 都包含：
- `ImageUpscaleWithModel`
- `LoadImage`
- `SaveImage`
- `UpscaleModelLoader`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 5/7 个有
- `ImageScaleBy` —— 3/7 个有
- `ReActorFaceSwap` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
