---
name: unknown_workflow_sampler_unet_vae_145
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.904
common_nodes: [CLIPLoader, EmptyLatentImage, ImageConcanate, KSampler, LoadImage, ModelSamplingAuraFlow, SaveImage, TextEncodeBooguEdit, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Boogu-Image-Edit图片编辑_2070450081513426945.json, 图片生成/图生图/Boogu-Image-Edit图片编辑工作流_2069671736781660161.json, 图片生成/图生图/Boogu-Image-Edit图片编辑工作流_2078866342920413186.json, 图片生成/图生图/Boogu-Image-Edit图片编辑工作流_2079877696288546817.json, 图片生成/图生图/Boogu-Image-Edit图片编辑工作流_2080470029400895490.json, 图片生成/图生图/boogu edit 单图-编辑_2067886135044562945.json, 图片生成/图生图/boogu edit 多图-编辑_2068139224456581122.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_145

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/Boogu-Image-Edit图片编辑_2070450081513426945.json、图片生成/图生图/Boogu-Image-Edit图片编辑工作流_2069671736781660161.json、图片生成/图生图/Boogu-Image-Edit图片编辑工作流_2078866342920413186.json、图片生成/图生图/Boogu-Image-Edit图片编辑工作流_2079877696288546817.json、图片生成/图生图/Boogu-Image-Edit图片编辑工作流_2080470029400895490.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `ImageConcanate`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeBooguEdit`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `GetImageSize` —— 5/7 个有
- `JjkText` —— 5/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/7 个有
- `Seed (rgthree)` —— 5/7 个有
- `Image Comparer (rgthree)` —— 4/7 个有
- `DF_Get_image_size` —— 2/7 个有
- `ImageScaleToTotalPixels` —— 2/7 个有
- `Label (rgthree)` —— 2/7 个有
- `LoraLoaderBypassModelOnly` —— 2/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 25 - 25 | 7 | 100% |
| Prompt 约束强度(CFG) | 3.5 | 3.5 - 3.5 | 7 | 100% |
| 采样算法 | dpmpp_2m | - | 7 | 71% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| 宽度 | 1984 | 1024 - 1984 | 7 | 75% |
| 高度 | 1536 | 1024 - 1536 | 7 | 83% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 25 - 25，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 3.5，观测区间 3.5 - 3.5，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_2m，7 个样本，一致性 71%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 宽度 中位数 1984，观测区间 1024 - 1984，7 个样本
- 高度 中位数 1536，观测区间 1024 - 1536，7 个样本，取值集中（一致性 83%）
