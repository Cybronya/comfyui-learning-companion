---
name: image_to_image_upscale_lora_sampler_28
type: Image To Image
frequency: 5
level: strong
coverage: 0.8376
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, Image Comparer (rgthree), Image Lucy Sharpen, ImageScaleBy, ImageUpscaleWithModel, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, UltimateSDUpscaleNoUpscale, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/FLUX-2xNomos 高质量材质修复放大_1935249237552582657.json, 图片生成/图生图/FLUX-2xNomos 高质量材质修复放大_1959792403232272385.json, 图片生成/图生图/面料材质放大【不变形】_2097883345781878785.json, 图片生成/图生图/面料材质放大【不变形】_2099412425505329153.json, 图片生成/文生图/面料材质放大【不变形】_1935227966781849602.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_28

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/FLUX-2xNomos 高质量材质修复放大_1935249237552582657.json、图片生成/图生图/FLUX-2xNomos 高质量材质修复放大_1959792403232272385.json、图片生成/图生图/面料材质放大【不变形】_2097883345781878785.json、图片生成/图生图/面料材质放大【不变形】_2099412425505329153.json、图片生成/文生图/面料材质放大【不变形】_1935227966781849602.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `Image Comparer (rgthree)`
- `Image Lucy Sharpen`
- `ImageScaleBy`
- `ImageUpscaleWithModel`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `UltimateSDUpscaleNoUpscale`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere` —— 4/5 个有
- `PreviewImage` —— 4/5 个有
- `Florence2ModelLoader` —— 3/5 个有
- `Florence2Run` —— 3/5 个有
- `easy showAnything` —— 3/5 个有
- `Anything Everywhere3` —— 1/5 个有
- `Florence2` —— 1/5 个有
- `LayerUtility: JoyCaptionBeta1` —— 1/5 个有
- `LayerUtility: LoadJoyCaptionBeta1Model` —— 1/5 个有
- `LoadFlorence2Model` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | kl_optimal | - | 5 | 100% |
| 重绘幅度 | 0.3 | 0.3 - 0.3 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 kl_optimal，5 个样本，一致性 100%
- 重绘幅度 中位数 0.3，观测区间 0.3 - 0.3，5 个样本，取值集中（一致性 100%）
- 高发问题（8/5 个样本）：Steps较低可能导致细节不足
