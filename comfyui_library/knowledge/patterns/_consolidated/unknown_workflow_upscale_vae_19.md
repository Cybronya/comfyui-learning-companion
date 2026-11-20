---
name: unknown_workflow_upscale_vae_19
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.7661
common_nodes: [Image Comparer (rgthree), LoadImage, SaveImage]
problems: []
missing: []
members: [图片生成/图生图/SeedVR2图像4K放大_2089291110207279106.json, 图片生成/图生图/VOSR图像文字4K超快速放大_2112161469726027778.json, 图片生成/图生图/单图放大_seedVR2_4K_2005946235443970049.json, 图片生成/图生图/图像修复放大 - Zimage_2010989461403865090.json, 图片生成/图生图/图像处理-高清放大_2113897674704506881.json, 图片生成/图生图/最好的高清放大_2011245583637422082.json, 图片生成/图生图/电商高清放大・精修处理-SeedVR2 Video Upscaler_2015100982383878146.json, 图片生成/图生图/高清放大-SeedVR2 Video Upscaler_2009264485617373185.json, 图片生成/图生图/高清放大_2079469358585307137.json, 图片生成/图生图/（Seedvr2分块）万物高清放大修复不改变原细节V8.0_2042398439320854530.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_vae_19

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/SeedVR2图像4K放大_2089291110207279106.json、图片生成/图生图/VOSR图像文字4K超快速放大_2112161469726027778.json、图片生成/图生图/单图放大_seedVR2_4K_2005946235443970049.json、图片生成/图生图/图像修复放大 - Zimage_2010989461403865090.json、图片生成/图生图/图像处理-高清放大_2113897674704506881.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：77%

## 共有节点

全部 10 个 workflow 都包含：
- `Image Comparer (rgthree)`
- `LoadImage`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `SeedVR2LoadDiTModel` —— 9/10 个有
- `SeedVR2LoadVAEModel` —— 9/10 个有
- `SeedVR2VideoUpscaler` —— 9/10 个有
- `ImageScaleBy` —— 8/10 个有
- `PreviewImage` —— 6/10 个有
- `VOSR2ModelLoader` —— 2/10 个有
- `VOSR2Upscale` —— 2/10 个有
- `PIP_图像联结` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
