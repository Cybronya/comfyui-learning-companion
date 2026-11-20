---
name: unknown_workflow_sampler_unet_vae_319
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.679
common_nodes: [AIO_Preprocessor, CLIPLoader, ConditioningZeroOut, Float, GetNode, Image Comparer (rgthree), LayerUtility: ImageScaleByAspectRatio V2, LoadImage, PreviewImage, ReferenceLatent, SZ_KleinTiledKSampler, SaveImage, SetNode, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecodeTiled, VAEEncodeTiled, VAELoader, YuanColorMatch, easy int]
problems: []
missing: []
members: [图片生成/图生图/klein图像放大_极致细节_latent参考_深度控制_匹配色彩_2085012562663530498.json, 图片生成/图生图/klein图像放大_极致细节_latent参考_深度控制_匹配色彩_2085185251080495105.json, 平台全量/klein图像放大_极致细节_latent参考_深度控制_匹配色彩_2057005661577371650.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_319

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/klein图像放大_极致细节_latent参考_深度控制_匹配色彩_2085012562663530498.json、图片生成/图生图/klein图像放大_极致细节_latent参考_深度控制_匹配色彩_2085185251080495105.json、平台全量/klein图像放大_极致细节_latent参考_深度控制_匹配色彩_2057005661577371650.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：68%

## 共有节点

全部 3 个 workflow 都包含：
- `AIO_Preprocessor`
- `CLIPLoader`
- `ConditioningZeroOut`
- `Float`
- `GetNode`
- `Image Comparer (rgthree)`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `PreviewImage`
- `ReferenceLatent`
- `SZ_KleinTiledKSampler`
- `SaveImage`
- `SetNode`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAEEncodeTiled`
- `VAELoader`
- `YuanColorMatch`
- `easy int`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | er_sde | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
