---
name: unknown_workflow_upscale_11
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.877667
common_nodes: [LoadImage, SaveImage, VOSR2ModelLoader, VOSR2Upscale]
problems: []
missing: []
members: [图片生成/图生图/VOSR2高清放大_2108736205721530369.json, 图片生成/图生图/VOSR2高清放大_2110183612711784450.json, 图片生成/图生图/vosr2图片放大（速度超快、效果好）_2099019638217728002.json, 图片生成/图生图/文字高清_2108520593934077954.json, 图片生成/图生图/文字高清_2111735832481722370.json, 图片生成/图生图/生图-图放大-VOSR 2.0_2097354360434020354.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_11

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/VOSR2高清放大_2108736205721530369.json、图片生成/图生图/VOSR2高清放大_2110183612711784450.json、图片生成/图生图/vosr2图片放大（速度超快、效果好）_2099019638217728002.json、图片生成/图生图/文字高清_2108520593934077954.json、图片生成/图生图/文字高清_2111735832481722370.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 6 个 workflow 都包含：
- `LoadImage`
- `SaveImage`
- `VOSR2ModelLoader`
- `VOSR2Upscale`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 4/6 个有
- `Int` —— 3/6 个有
- `图像缩放范围孤海` —— 2/6 个有
- `GetImageSizeAndCount` —— 1/6 个有
- `ImageConcanate` —— 1/6 个有
- `PreviewImage` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
