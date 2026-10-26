---
name: unknown_workflow_upscale_vae_19
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.688714
common_nodes: [LoadImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler]
problems: []
missing: []
members: [图片生成/图生图/FlashVSR+SeedVR2双重放大_2031676606560870401.json, 图片生成/图生图/SEEDVR2.5 基础放大工作流_2006571587549536258.json, 图片生成/图生图/SEEDVR2放大 图像放大到2K  接入SD-PPP实现 SEEDVR2.5放大_2073377648025358338.json, 图片生成/图生图/图像处理-高清放大_2113897674704506881.json, 图片生成/图生图/图像放大工作流（SeedVR2.5.1）_2110631951051874305.json, 图片生成/图生图/图片像素放大_2028713549190664193.json, 数字人/数字人/YZ金鱼-数字人多角度定妆造_1993619967620874241.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_vae_19

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/FlashVSR+SeedVR2双重放大_2031676606560870401.json、图片生成/图生图/SEEDVR2.5 基础放大工作流_2006571587549536258.json、图片生成/图生图/SEEDVR2放大 图像放大到2K  接入SD-PPP实现 SEEDVR2.5放大_2073377648025358338.json、图片生成/图生图/图像处理-高清放大_2113897674704506881.json、图片生成/图生图/图像放大工作流（SeedVR2.5.1）_2110631951051874305.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：69%

## 共有节点

全部 7 个 workflow 都包含：
- `LoadImage`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 6/7 个有
- `Image Comparer (rgthree)` —— 4/7 个有
- `ImageScaleToTotalPixels` —— 3/7 个有
- `FlashVSRNode` —— 1/7 个有
- `ImageResizeKJv2` —— 1/7 个有
- `PlaySound|pysssss` —— 1/7 个有
- `RH_Nano_Banana2_Image2Image` —— 1/7 个有
- `VRAM_Debug` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
