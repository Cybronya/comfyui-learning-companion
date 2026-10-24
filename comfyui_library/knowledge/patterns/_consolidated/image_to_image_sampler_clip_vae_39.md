---
name: image_to_image_sampler_clip_vae_39
type: Image To Image
frequency: 3
level: moderate
coverage: 0.987333
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, KSampler, LoadImage, NunchakuFluxDiTLoader, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/模糊图像高清放大【4K】_1965272626576936962.json, 图片生成/图生图/生图-图片移除字幕-kontext_nunchaku_1972652889376268289.json, 图片生成/图生图/轻微模糊图像高清放大【4K】_1965275384780607490.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_vae_39

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/模糊图像高清放大【4K】_1965272626576936962.json、图片生成/图生图/生图-图片移除字幕-kontext_nunchaku_1972652889376268289.json、图片生成/图生图/轻微模糊图像高清放大【4K】_1965275384780607490.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：99%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSampler`
- `LoadImage`
- `NunchakuFluxDiTLoader`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConstrainImage|pysssss` —— 2/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/3 个有
- `LoraLoaderModelOnly` —— 2/3 个有
- `RH_Captioner` —— 2/3 个有
- `UltimateSDUpscale` —— 2/3 个有
- `UpscaleModelLoader` —— 2/3 个有
- `HYPIRImageRestoration` —— 1/3 个有
- `ImageScaleBy` —— 1/3 个有
- `ImageUpscaleWithModel` —— 1/3 个有
- `NunchakuFluxLoraLoader` —— 1/3 个有
- `ReferenceLatent` —— 1/3 个有
- `Upscale Model Loader` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 8 - 30 | 3 | 54% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler_ancestral | - | 3 | 67% |
| 调度器 | kl_optimal | - | 3 | 67% |
| 重绘幅度 | 0.45 | 0.25 - 1 | 3 | 44% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 30，观测区间 8 - 30，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，3 个样本，一致性 67%
- 调度器 最常用 kl_optimal，3 个样本，一致性 67%
- 重绘幅度 中位数 0.45，观测区间 0.25 - 1，3 个样本，取值分散，一致性仅 44%
