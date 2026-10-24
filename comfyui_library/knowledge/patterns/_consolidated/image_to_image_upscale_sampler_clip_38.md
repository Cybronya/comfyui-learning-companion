---
name: image_to_image_upscale_sampler_clip_38
type: Image To Image
frequency: 2
level: weak
coverage: 0.7175
common_nodes: [CLIPTextEncode, DualCLIPLoader, Image Comparer (rgthree), ImageScaleBy, ImageUpscaleWithModel, Joy_caption_two, Joy_caption_two_load, KSampler, LoadImage, PreviewImage, SaveImage, UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Flux产品精修工作流_1924048386755129346.json, 图片生成/图生图/flux图生图提示词反推+模型放大工作流_1980444331452641282.json]
source: knowledge_consolidation
---

# image_to_image_upscale_sampler_clip_38

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Flux产品精修工作流_1924048386755129346.json、图片生成/图生图/flux图生图提示词反推+模型放大工作流_1980444331452641282.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：72%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `Image Comparer (rgthree)`
- `ImageScaleBy`
- `ImageUpscaleWithModel`
- `Joy_caption_two`
- `Joy_caption_two_load`
- `KSampler`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncodeFlux` —— 1/2 个有
- `ColorMatch` —— 1/2 个有
- `ConstrainImage|pysssss` —— 1/2 个有
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `JWImageResizeByLongerSide` —— 1/2 个有
- `KSamplerAdvanced` —— 1/2 个有
- `Latent Noise Injection` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `ShowText|pysssss` —— 1/2 个有
- `easy imageSize` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | - | 1 | 100% |
| Prompt 约束强度(CFG) | 5.5 | - | 2 | 18% |
| 采样算法 | 1 | - | 1 | 100% |
| 调度器 | euler | - | 2 | 50% |
| 重绘幅度 | 0.7 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- Prompt 约束强度(CFG) 中位数 5.5，样本不足，未给区间，2 个样本，取值分散，一致性仅 18%
- 调度器 最常用 euler，2 个样本，一致性 50%
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
