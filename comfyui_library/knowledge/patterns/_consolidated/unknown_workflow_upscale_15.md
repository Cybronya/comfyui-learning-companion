---
name: unknown_workflow_upscale_15
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.765286
common_nodes: [Image Comparer (rgthree), LoadImage, SaveImage, VOSR2ModelLoader, VOSR2Upscale]
problems: []
missing: []
members: [图片生成/图生图/Vosr+2图像高清化(10秒4K)_2097353474043367425.json, 图片生成/图生图/Vosr_2图像高清化(10秒4K)_2098947796668862465.json, 图片生成/图生图/Vosr_2图像高清化(10秒4K)_2099059910947463170.json, 平台全量/Vosr 2图像高清化(10秒4K)_2096958059879952385.json, 平台全量/Vosr 2图像高清化_2100081096292651009.json, 数字人/数字人/图像无损高清放大 - Vosr2_2097147455497400321.json, 数字人/数字人/图像高清放大  Vosr 2_2097144545875161090.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_15

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/Vosr+2图像高清化(10秒4K)_2097353474043367425.json、图片生成/图生图/Vosr_2图像高清化(10秒4K)_2098947796668862465.json、图片生成/图生图/Vosr_2图像高清化(10秒4K)_2099059910947463170.json、平台全量/Vosr 2图像高清化(10秒4K)_2096958059879952385.json、平台全量/Vosr 2图像高清化_2100081096292651009.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：77%

## 共有节点

全部 7 个 workflow 都包含：
- `Image Comparer (rgthree)`
- `LoadImage`
- `SaveImage`
- `VOSR2ModelLoader`
- `VOSR2Upscale`

**可变部分**（部分 workflow 才有）：
- `PDIMAGE_LongerSize` —— 5/7 个有
- `PreviewImage` —— 4/7 个有
- `EmptyImage` —— 2/7 个有
- `LoadImagesFromFolderKJ` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
