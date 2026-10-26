---
name: image_to_image_upscale_latent_upscale_sampler
type: Image To Image
frequency: 4
level: strong
coverage: 0.769
common_nodes: [CLIPTextEncodeFlux, ConditioningZeroOut, DualCLIPLoader, Image Comparer (rgthree), ImageScaleBy, ImageUpscaleWithModel, JWImageResizeByLongerSide, KSampler, LatentUpscaleBy, LoadImage, SUPIR_Upscale, SaveImage, UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/三种图片高清放大技术集合（Supir放大+图像通过模型放大+Latent放大）_1985268826906501122.json, 图片生成/图生图/三种图片高清放大技术集合（Supir放大+图像通过模型放大+Latent放大）_2006644077445521409.json, 图片生成/图生图/三种图片高清放大技术集合（Supir放大+图像通过模型放大+Latent放大）_2006644910866309121.json, 图片生成/图生图/三种图片高清放大集合（Supir+模型放大+Latent）_2063878919144693762.json]
source: knowledge_consolidation
---

# image_to_image_upscale_latent_upscale_sampler

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/三种图片高清放大技术集合（Supir放大+图像通过模型放大+Latent放大）_1985268826906501122.json、图片生成/图生图/三种图片高清放大技术集合（Supir放大+图像通过模型放大+Latent放大）_2006644077445521409.json、图片生成/图生图/三种图片高清放大技术集合（Supir放大+图像通过模型放大+Latent放大）_2006644910866309121.json、图片生成/图生图/三种图片高清放大集合（Supir+模型放大+Latent）_2063878919144693762.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：77%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncodeFlux`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `Image Comparer (rgthree)`
- `ImageScaleBy`
- `ImageUpscaleWithModel`
- `JWImageResizeByLongerSide`
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

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 25 - 25 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | dpmpp_2m | - | 4 | 100% |
| 调度器 | sgm_uniform | - | 4 | 100% |
| 重绘幅度 | 0.3 | 0.3 - 0.3 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 25 - 25，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_2m，4 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，4 个样本，一致性 100%
- 重绘幅度 中位数 0.3，观测区间 0.3 - 0.3，4 个样本，取值集中（一致性 100%）
