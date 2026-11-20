---
name: unknown_workflow_upscale_12
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.779
common_nodes: [PDIMAGE_LongerSize, VOSR2ModelLoader, VOSR2Upscale]
problems: []
missing: []
members: [图片生成/图生图/Vosr+2图像高清化(10秒4K)_2097353474043367425.json, 图片生成/图生图/Vosr_2图像高清化(10秒4K)_2098947796668862465.json, 图片生成/图生图/Vosr_2图像高清化(10秒4K)_2099059910947463170.json, 视频生成/图生视频/全能图像+视频修复放大【VOSR2】_2098954861361590274.json, 视频生成/图生视频/全能图像+视频修复放大【VOSR2】_2099066562438324226.json, 视频生成/文生视频/VOSR2视频高清化·级联2K放大_2101627140033835009.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_12

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Vosr+2图像高清化(10秒4K)_2097353474043367425.json、图片生成/图生图/Vosr_2图像高清化(10秒4K)_2098947796668862465.json、图片生成/图生图/Vosr_2图像高清化(10秒4K)_2099059910947463170.json、视频生成/图生视频/全能图像+视频修复放大【VOSR2】_2098954861361590274.json、视频生成/图生视频/全能图像+视频修复放大【VOSR2】_2099066562438324226.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：78%

## 共有节点

全部 6 个 workflow 都包含：
- `PDIMAGE_LongerSize`
- `VOSR2ModelLoader`
- `VOSR2Upscale`

**可变部分**（部分 workflow 才有）：
- `EmptyImage` —— 5/6 个有
- `Image Comparer (rgthree)` —— 5/6 个有
- `LoadImage` —— 5/6 个有
- `PreviewImage` —— 5/6 个有
- `SaveImage` —— 5/6 个有
- `VHS_LoadVideo` —— 3/6 个有
- `VHS_VideoCombine` —— 3/6 个有
- `VHS_VideoInfo` —— 3/6 个有
- `Fast Groups Bypasser (rgthree)` —— 2/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
