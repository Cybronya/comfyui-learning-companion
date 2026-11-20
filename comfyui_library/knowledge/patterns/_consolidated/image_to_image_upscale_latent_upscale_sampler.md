---
name: image_to_image_upscale_latent_upscale_sampler
type: Image To Image
frequency: 5
level: weak
coverage: 0.7678
common_nodes: [CLIPTextEncodeFlux, ConditioningZeroOut, DualCLIPLoader, Image Comparer (rgthree), ImageScaleBy, ImageUpscaleWithModel, KSampler, LatentUpscaleBy, LoadImage, SUPIR_Upscale, SaveImage, UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/三种图片高清放大技术集合（Supir放大+图像通过模型放大+Latent放大）_1985268826906501122.json, 图片生成/图生图/三种图片高清放大技术集合（Supir放大+图像通过模型放大+Latent放大）_2006644077445521409.json, 图片生成/图生图/三种图片高清放大技术集合（Supir放大+图像通过模型放大+Latent放大）_2006644910866309121.json, 图片生成/图生图/三种图片高清放大集合（Supir+模型放大+Latent）_2063878919144693762.json, 平台全量/放大工作流_1981246958293647362.json]
source: knowledge_consolidation
---

# image_to_image_upscale_latent_upscale_sampler

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/三种图片高清放大技术集合（Supir放大+图像通过模型放大+Latent放大）_1985268826906501122.json、图片生成/图生图/三种图片高清放大技术集合（Supir放大+图像通过模型放大+Latent放大）_2006644077445521409.json、图片生成/图生图/三种图片高清放大技术集合（Supir放大+图像通过模型放大+Latent放大）_2006644910866309121.json、图片生成/图生图/三种图片高清放大集合（Supir+模型放大+Latent）_2063878919144693762.json、平台全量/放大工作流_1981246958293647362.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：77%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPTextEncodeFlux`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `Image Comparer (rgthree)`
- `ImageScaleBy`
- `ImageUpscaleWithModel`
- `KSampler`
- `LatentUpscaleBy`
- `LoadImage`
- `SUPIR_Upscale`
- `SaveImage`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `JWImageResizeByLongerSide` —— 4/5 个有
- `easy imageScaleDown` —— 1/5 个有
- `easy imageSize` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 25 - 30 | 5 | 92% |
| Prompt 约束强度(CFG) | 1 | 1 - 8 | 5 | 0% |
| 采样算法 | dpmpp_2m | - | 5 | 80% |
| 调度器 | sgm_uniform | - | 5 | 80% |
| 重绘幅度 | 0.3 | 0.3 - 0.5 | 5 | 76% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 25 - 30，5 个样本，取值集中（一致性 92%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 8，5 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 dpmpp_2m，5 个样本，一致性 80%
- 调度器 最常用 sgm_uniform，5 个样本，一致性 80%
- 重绘幅度 中位数 0.3，观测区间 0.3 - 0.5，5 个样本
