---
name: image_to_image_lora_sampler_unet_199
type: Image To Image
frequency: 2
level: weak
coverage: 0.8785
common_nodes: [CLIPLoader, FluxKontextMultiReferenceLatentMethod, KSampler, Krea2OstrisEditModelPatch, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Krea2动漫转真人｜Anything2Real V3｜目前最佳方案_2108189059570028546.json, 图片生成/图生图/krea2-角色四视图生成2.0_2099850078163918849.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_199

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Krea2动漫转真人｜Anything2Real V3｜目前最佳方案_2108189059570028546.json、图片生成/图生图/krea2-角色四视图生成2.0_2099850078163918849.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：88%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `FluxKontextMultiReferenceLatentMethod`
- `KSampler`
- `Krea2OstrisEditModelPatch`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere` —— 1/2 个有
- `Easy_QwenEdit2509` —— 1/2 个有
- `INTConstant` —— 1/2 个有
- `ImageScaleToTotalPixels` —— 1/2 个有
- `Krea2EditGroundedEncode` —— 1/2 个有
- `Seed (rgthree)` —— 1/2 个有
- `kkPadImageToCanvas` —— 1/2 个有
- `孤海注释` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | - | 2 | 67% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | er_sde | - | 2 | 50% |
| 调度器 | simple | - | 2 | 50% |
| 重绘幅度 | 0.59 | - | 2 | 31% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，样本不足，未给区间，2 个样本
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，2 个样本，一致性 50%
- 调度器 最常用 simple，2 个样本，一致性 50%
- 重绘幅度 中位数 0.59，样本不足，未给区间，2 个样本，取值分散，一致性仅 31%
- 高发问题（3/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
