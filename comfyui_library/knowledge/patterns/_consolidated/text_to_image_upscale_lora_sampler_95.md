---
name: text_to_image_upscale_lora_sampler_95
type: Text To Image
frequency: 3
level: moderate
coverage: 0.855667
common_nodes: [CLIPLoader, CLIPTextEncode, ConstrainImage|pysssss, EmptyLatentImage, Fast Groups Bypasser (rgthree), Get Image Size, Image Comparer (rgthree), ImageResize+, ImageScaleBy, KSampler, LoraLoaderModelOnly, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, VAELoader, easy imageSize]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/ERNIE+ZImage+Wan2.2 文生图_2049306945353420802.json, 图片生成/文生图/Z-Image文生图+TTP高清放大_2059978387187388417.json, 图片生成/文生图/ZImage文生图（TTP高清4K）_2096553840748355585.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_95

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/ERNIE+ZImage+Wan2.2 文生图_2049306945353420802.json、图片生成/文生图/Z-Image文生图+TTP高清放大_2059978387187388417.json、图片生成/文生图/ZImage文生图（TTP高清4K）_2096553840748355585.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConstrainImage|pysssss`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `Get Image Size`
- `Image Comparer (rgthree)`
- `ImageResize+`
- `ImageScaleBy`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy imageSize`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 2/3 个有
- `CR Text` —— 1/3 个有
- `INTConstant` —— 1/3 个有
- `InversionDemoLazyIndexSwitch` —— 1/3 个有
- `KSamplerAdvanced` —— 1/3 个有
- `LayerColor: Brightness & Contrast` —— 1/3 个有
- `ModelSamplingSD3` —— 1/3 个有
- `PathchSageAttentionKJ` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `RH_LLMAPI_NODE` —— 1/3 个有
- `RH_LLMAPI_Pro_Node` —— 1/3 个有
- `VAEEncode` —— 1/3 个有
- `easy showAnything` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 8 | 3 | 1% |
| 采样算法 | dpmpp_2m_sde | - | 3 | 67% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 1 | - | 2 | 100% |
| 宽度 | 1024 | 960 - 1024 | 3 | 97% |
| 高度 | 1536 | 1536 - 1536 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 8，3 个样本，取值分散，一致性仅 1%
- 采样算法 最常用 dpmpp_2m_sde，3 个样本，一致性 67%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 960 - 1024，3 个样本，取值集中（一致性 97%）
- 高度 中位数 1536，观测区间 1536 - 1536，3 个样本，取值集中（一致性 100%）
