---
name: unknown_workflow_upscale_vae_6
type: Unknown Workflow
frequency: 18
level: moderate
coverage: 0.806111
common_nodes: [LoadImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler]
problems: []
missing: []
members: [图片生成/图生图/SeedVR2保留细节_一键4K超清高清放大工作流_1999448839465693186.json, 图片生成/图生图/SeedVR2图像放大_2013201075800641538.json, 图片生成/图生图/SeedVR2图像放大_2062127657986379777.json, 图片生成/图生图/SeedVR2图片高清放大_2011376111472611329.json, 图片生成/图生图/seedvr 2 图像高清放大4K_2084865194706161666.json, 图片生成/图生图/seedvr2-效果、分析图A3文本4k放大工作流_2012001541628104706.json, 图片生成/图生图/seedvr2图像高清放大_2089915225989537794.json, 图片生成/图生图/seedvr2图像高清放大_2090697561052114945.json, 图片生成/图生图/seedvr2图像高清放大_2091719957255122946.json, 图片生成/图生图/seedvr2图像高清放大_2091729482674688002.json, 图片生成/图生图/seedvr2图像高清放大_2092217808426979329.json, 图片生成/图生图/seedvr2图像高清放大_2092433813359128578.json, 图片生成/图生图/seedvr2图像高清放大_2092866550570250242.json, 图片生成/图生图/图片像素放大_2028713549190664193.json, 图片生成/图生图/最新SeedVR2高清放大_2068239377725218817.json, 图片生成/图生图/最新SeedVR2高清放大，文字不乱码_2068218120824774658.json, 图片生成/图生图/高清放大_2062421175283834882.json, 图片生成/图生图/（电商流工具流）SeedVR2单图高清4K_2028382443518038017.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_vae_6

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（图片生成/图生图/SeedVR2保留细节_一键4K超清高清放大工作流_1999448839465693186.json、图片生成/图生图/SeedVR2图像放大_2013201075800641538.json、图片生成/图生图/SeedVR2图像放大_2062127657986379777.json、图片生成/图生图/SeedVR2图片高清放大_2011376111472611329.json、图片生成/图生图/seedvr 2 图像高清放大4K_2084865194706161666.json…）

- **类型**：Unknown Workflow
- **样本数**：18
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 18 个 workflow 都包含：
- `LoadImage`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 17/18 个有
- `ImageScaleToTotalPixels` —— 5/18 个有
- `easy cleanGpuUsed` —— 3/18 个有
- `easy int` —— 3/18 个有
- `PrimitiveInt` —— 2/18 个有
- `Label (rgthree)` —— 1/18 个有
- `easy clearCacheAll` —— 1/18 个有
- `easy imageSize` —— 1/18 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
