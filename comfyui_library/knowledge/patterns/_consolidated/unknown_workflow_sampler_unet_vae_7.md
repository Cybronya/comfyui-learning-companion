---
name: unknown_workflow_sampler_unet_vae_7
type: Unknown Workflow
frequency: 24
level: strong
coverage: 0.9085
common_nodes: [BasicScheduler, CLIPLoader, EmptyLatentImage, KSamplerSelect, LoadImage, ModelSamplingAuraFlow, SamplerCustom, SaveImage, TextEncodeBooguEdit, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/BOOGUEDIT 图像编辑_2068133466729959426.json, 图片生成/图生图/Boogu 图片编辑_2068223085454643201.json, 图片生成/图生图/Boogu-Edit 0偏移无损重绘图像语义编辑_2068717915423207425.json, 图片生成/图生图/Boogu-Image Edit单图编辑_2068063056286019585.json, 图片生成/图生图/Boogu-Image Edit图片去字幕去水印_2069811905337847809.json, 图片生成/图生图/Boogu-Image_Edit单图编辑_2085013386194145282.json, 图片生成/图生图/Boogu-Image_Edit单图编辑_2085185274715402242.json, 图片生成/图生图/Boogu-Image_Edit图片去字幕去水印_2085907098508021762.json, 图片生成/图生图/Boogu-Image_Edit图片去字幕去水印_2085925136028487681.json, 图片生成/图生图/boogu edit图像编辑优化版V1_2067834819068911618.json, 图片生成/图生图/boogu edit图像编辑优化版V1_2068274229971345409.json, 图片生成/图生图/boogu edit图像编辑优化版图生图工作流_2082445936030216194.json, 图片生成/图生图/boogu edit图像编辑优化版图生图工作流_2093296625610477570.json, 图片生成/图生图/boogu edit图像编辑优化版图生图工作流_2093310369640046593.json, 图片生成/图生图/boogu edit图像编辑优化版图生图工作流_2103443751074095105.json, 图片生成/图生图/boogu edit图像编辑优化版图生图工作流_2103445400953909249.json, 图片生成/图生图/boogu edit图像编辑优化版图生图工作流_2111774698563526657.json, 图片生成/图生图/boogu edit图像编辑优化版图生图工作流_2111807575577681921.json, 图片生成/图生图/boogu edit图像编辑优化版工作流_2067857270989479937.json, 图片生成/图生图/boogu edit图像编辑优化版工作流_2067877061376700417.json, 图片生成/图生图/boogu_edit图像编辑优化版图生图工作流_2093890774390894593.json, 图片生成/图生图/boogu_edit图像编辑优化版图生图工作流_2093984740893351938.json, 图片生成/图生图/boogu图像编辑模型_2069094367243100162.json, 图片生成/图生图/图像编辑  Boogu Edit_2068132808568172546.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_7

> 由 `engine/knowledge_consolidation` 从 24 个 workflow 归纳得出（图片生成/图生图/BOOGUEDIT 图像编辑_2068133466729959426.json、图片生成/图生图/Boogu 图片编辑_2068223085454643201.json、图片生成/图生图/Boogu-Edit 0偏移无损重绘图像语义编辑_2068717915423207425.json、图片生成/图生图/Boogu-Image Edit单图编辑_2068063056286019585.json、图片生成/图生图/Boogu-Image Edit图片去字幕去水印_2069811905337847809.json…）

- **类型**：Unknown Workflow
- **样本数**：24
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 24 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `EmptyLatentImage`
- `KSamplerSelect`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `SamplerCustom`
- `SaveImage`
- `TextEncodeBooguEdit`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `DF_Get_image_size` —— 23/24 个有
- `CR Prompt Text` —— 22/24 个有
- `ImageScaleToTotalPixels` —— 22/24 个有
- `PreviewImage` —— 22/24 个有
- `easy cleanGpuUsed` —— 21/24 个有
- `ImageConcanate` —— 20/24 个有
- `Image Comparer (rgthree)` —— 4/24 个有
- `GetImageSize+` —— 1/24 个有
- `ImageResize+` —— 1/24 个有
- `JjkText` —— 1/24 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1536 | 24 | 90% |
| 高度 | 1024 | 1024 - 1024 | 24 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1536，24 个样本，取值集中（一致性 90%）
- 高度 中位数 1024，观测区间 1024 - 1024，24 个样本，取值集中（一致性 100%）
