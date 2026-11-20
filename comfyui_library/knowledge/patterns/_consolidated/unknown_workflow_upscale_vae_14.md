---
name: unknown_workflow_upscale_vae_14
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.751273
common_nodes: [ImageScaleBy, LoadImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size]
problems: []
missing: []
members: [图片生成/图生图/8K极致高清放大（TTP+Seedvsr2）_2007683849572061185.json, 图片生成/图生图/AIGC人像系列04-人像超高清基于TTP+SeedVR2实现放大_2028739110755639297.json, 图片生成/图生图/B-LANSEDUONAOHE-SEEDVR2+TTP极速一亿像素放大_1992893002534244353.json, 图片生成/图生图/SeedVR2+TTP放大+0损耗压缩_2001611198548307969.json, 图片生成/图生图/九宫格电商详情高端产品分镜+放大(内置免费的全能图片通道)_2071905182362988545.json, 图片生成/图生图/动漫转真实，超低消耗_2071497174474645506.json, 图片生成/图生图/图片放大-rh-SeedVR2+TTP-模板_2013152289002885122.json, 图片生成/图生图/建筑_角色通用放大-seedvr2_2049762190231609346.json, 图片生成/图生图/建筑效果图套A0大板8k放大工作流_2011999694133665794.json, 平台全量/工作流系列03-低清图片4K_8K放大基于TTP分块+SeedVR2实现_2041384398406291457.json, 平台全量/组件系列5-图片超高清放大4K_8K-TTP+SeedVR2_2058737625791553537.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_vae_14

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/8K极致高清放大（TTP+Seedvsr2）_2007683849572061185.json、图片生成/图生图/AIGC人像系列04-人像超高清基于TTP+SeedVR2实现放大_2028739110755639297.json、图片生成/图生图/B-LANSEDUONAOHE-SEEDVR2+TTP极速一亿像素放大_1992893002534244353.json、图片生成/图生图/SeedVR2+TTP放大+0损耗压缩_2001611198548307969.json、图片生成/图生图/九宫格电商详情高端产品分镜+放大(内置免费的全能图片通道)_2071905182362988545.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：75%

## 共有节点

全部 11 个 workflow 都包含：
- `ImageScaleBy`
- `LoadImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 10/11 个有
- `SaveImage` —— 10/11 个有
- `GetImageSize+` —— 9/11 个有
- `ImageResize+` —— 9/11 个有
- `Fast Groups Bypasser (rgthree)` —— 6/11 个有
- `easy showAnything` —— 6/11 个有
- `KOOK_ImageCompression` —— 5/11 个有
- `PreviewImage` —— 5/11 个有
- `easy int` —— 5/11 个有
- `PrimitiveFloat` —— 3/11 个有
- `easy float` —— 3/11 个有
- `easy mathInt` —— 3/11 个有
- `ImageResizeKJv2` —— 2/11 个有
- `MathExpression|pysssss` —— 2/11 个有
- `RHHiddenNodes` —— 2/11 个有
- `easy cleanGpuUsed` —— 2/11 个有
- `easy imageSize` —— 2/11 个有
- `KOOK_SaveJPGImage` —— 1/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
