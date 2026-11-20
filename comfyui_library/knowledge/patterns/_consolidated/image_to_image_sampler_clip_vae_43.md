---
name: image_to_image_sampler_clip_vae_43
type: Image To Image
frequency: 3
level: strong
coverage: 0.815
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, CR Latent Batch Size, ConditioningZeroOut, Florence2ModelLoader, Florence2Run, FluxGuidance, Image Comparer (rgthree), ImageConcanate, ImageResize+, KSampler, KSamplerSelect, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LoadImage, NunchakuFluxDiTLoader, NunchakuQwenImageDiTLoader, NunchakuTextEncoderLoaderV2, PreviewImage, RandomNoise, SamplerCustomAdvanced, SaveImage, ShowText|pysssss, TextEncodeQwenImageEditPlusAdvance_lrzjason, VAEDecode, VAEEncode, VAELoader, seed _O]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/QWEN+KONTEXT  提取模特衣服素材_1982705859321044994.json, 图片生成/图生图/QWEN+KONTEXT 提取衣服素材，纯白底平铺_1998955567731367938.json, 图片生成/图生图/nunchaku qwen edit 2509 + kontext提取衣服工作流_1972317423179395074.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_vae_43

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/QWEN+KONTEXT  提取模特衣服素材_1982705859321044994.json、图片生成/图生图/QWEN+KONTEXT 提取衣服素材，纯白底平铺_1998955567731367938.json、图片生成/图生图/nunchaku qwen edit 2509 + kontext提取衣服工作流_1972317423179395074.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Latent Batch Size`
- `ConditioningZeroOut`
- `Florence2ModelLoader`
- `Florence2Run`
- `FluxGuidance`
- `Image Comparer (rgthree)`
- `ImageConcanate`
- `ImageResize+`
- `KSampler`
- `KSamplerSelect`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `LoadImage`
- `NunchakuFluxDiTLoader`
- `NunchakuQwenImageDiTLoader`
- `NunchakuTextEncoderLoaderV2`
- `PreviewImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `ShowText|pysssss`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `seed _O`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | er_sde | - | 3 | 100% |
| 调度器 | beta57 | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，3 个样本，一致性 100%
- 调度器 最常用 beta57，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
