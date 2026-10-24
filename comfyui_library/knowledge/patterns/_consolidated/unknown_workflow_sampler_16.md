---
name: unknown_workflow_sampler_16
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.7795
common_nodes: [LayeredControlV2Sampler, LoadImage, LoadLayeredControlV2Pipe, SaveImage]
problems: []
missing: []
members: [图片生成/图生图/Qwen layer文本控制_2031980500822265858.json, 图片生成/图生图/Qwen-Image-Layered-Control-V2(图像分层控制-手动遮罩模式)_2030199845872476162.json, 图片生成/图生图/Qwen-Image-Layered-Control-V2(图像分层控制-手画遮罩模式-红色保留）_2030193673991888898.json, 图片生成/图生图/Qwen-Image-Layered-Control-V2(图像分层控制-手画遮罩模式-红黄消除）_2030195256293068802.json, 图片生成/图生图/Qwen-Image-Layered-Control-V2(图像分层控制-提示词控制)_2030210973105135617.json, 图片生成/图生图/龚老师的PPT页面分层_2051236518982897666.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_16

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Qwen layer文本控制_2031980500822265858.json、图片生成/图生图/Qwen-Image-Layered-Control-V2(图像分层控制-手动遮罩模式)_2030199845872476162.json、图片生成/图生图/Qwen-Image-Layered-Control-V2(图像分层控制-手画遮罩模式-红色保留）_2030193673991888898.json、图片生成/图生图/Qwen-Image-Layered-Control-V2(图像分层控制-手画遮罩模式-红黄消除）_2030195256293068802.json、图片生成/图生图/Qwen-Image-Layered-Control-V2(图像分层控制-提示词控制)_2030210973105135617.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：78%

## 共有节点

全部 6 个 workflow 都包含：
- `LayeredControlV2Sampler`
- `LoadImage`
- `LoadLayeredControlV2Pipe`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/6 个有
- `PreviewImage` —— 5/6 个有
- `Mask To Image (mtb)` —— 3/6 个有
- `CR Prompt Text` —— 2/6 个有
- `JWInteger` —— 2/6 个有
- `LayerUtility: ImageScaleByAspectRatio` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
