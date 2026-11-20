---
name: image_to_image_sampler_unet_vae_28
type: Image To Image
frequency: 7
level: weak
coverage: 0.891
common_nodes: [CFGNorm, CLIPLoader, KSampler, LoadImage, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/QIANWEN图像编辑_2088896217135800321.json, 图片生成/图生图/QWEN 2511 图像编辑 百万像素返图 _接入SDPPP 实现图像QWEN图像编辑_2073357158070181889.json, 图片生成/图生图/QWEN image edit 引导版工作流      附详细的多图像范例_1975862522542731265.json, 图片生成/图生图/QWen2509 单图简单编辑_1998227397973540865.json, 图片生成/图生图/Qwen Edit 2509多图编辑_2001660412015853570.json, 图片生成/图生图/Qwen edit 2511无像素偏移_2004837793459306497.json, 图片生成/图生图/Qwen_Edit_2511-无偏移增强版单图编辑工作流_2005187774271680514.json]
source: knowledge_consolidation
---

# image_to_image_sampler_unet_vae_28

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/QIANWEN图像编辑_2088896217135800321.json、图片生成/图生图/QWEN 2511 图像编辑 百万像素返图 _接入SDPPP 实现图像QWEN图像编辑_2073357158070181889.json、图片生成/图生图/QWEN image edit 引导版工作流      附详细的多图像范例_1975862522542731265.json、图片生成/图生图/QWen2509 单图简单编辑_1998227397973540865.json、图片生成/图生图/Qwen Edit 2509多图编辑_2001660412015853570.json…）

- **类型**：Image To Image
- **样本数**：7
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：89%

## 共有节点

全部 7 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 6/7 个有
- `LoraLoaderModelOnly` —— 6/7 个有
- `TextEncodeQwenImageEditPlus` —— 6/7 个有
- `ImageScaleToTotalPixels` —— 4/7 个有
- `FluxKontextImageScale` —— 3/7 个有
- `PreviewImage` —— 3/7 个有
- `TextEncodeQwenImageEdit` —— 3/7 个有
- `GetImageSize` —— 2/7 个有
- `ImageResizeKJv2` —— 2/7 个有
- `ReferenceLatent` —— 2/7 个有
- `CR Prompt Text` —— 1/7 个有
- `FluxKontextMultiReferenceLatentMethod` —— 1/7 个有
- `GetImageSizeAndCount` —— 1/7 个有
- `ImageStitch` —— 1/7 个有
- `JjkText` —— 1/7 个有
- `NunchakuQwenImageDiTLoader` —— 1/7 个有
- `Preview from image [Crystools]` —— 1/7 个有
- `easy float` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 40 | 7 | 0% |
| Prompt 约束强度(CFG) | 1 | 1 - 3 | 7 | 46% |
| 采样算法 | euler | - | 7 | 86% |
| 调度器 | simple | - | 7 | 86% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 40，7 个样本，取值分散，一致性仅 0%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3，7 个样本，取值分散，一致性仅 46%
- 采样算法 最常用 euler，7 个样本，一致性 86%
- 调度器 最常用 simple，7 个样本，一致性 86%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（5/7 个样本）：Steps较低可能导致细节不足
