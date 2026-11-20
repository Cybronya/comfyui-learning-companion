---
name: unknown_workflow_sampler_clip_unet_425
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.77
common_nodes: [AdaptiveLongestEdge_EditUtils, CLIPLoader, CLIPTextEncode, CropWithPadInfo_EditUtils, EditTextEncode_EditUtils, Flux2KleinConfigPreparer_EditUtils, Flux2KleinModelConfig_EditUtils, Flux2KleinOutputExtractor_EditUtils, Image Comparer (rgthree), KSampler, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LoadImage, PreviewImage, PrimitiveInt, ReferenceLatent, SaveImage, UNETLoader, VAELoader]
problems: [Steps较低可能导致细节不足, 发现KSampler但没有VAEDecode]
missing: []
members: [图片生成/图生图/方汤圆flux-2-klein手办工作流 V2_2038847106194083841.json, 平台全量/Flux2 Klein 9B 换装换脸换表情 一致性编辑 万物迁移 局部重绘_2017042275607515138.json, 平台全量/方汤圆flux-2-klein高级应用V1.2_2038933428191629313.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_425

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/方汤圆flux-2-klein手办工作流 V2_2038847106194083841.json、平台全量/Flux2 Klein 9B 换装换脸换表情 一致性编辑 万物迁移 局部重绘_2017042275607515138.json、平台全量/方汤圆flux-2-klein高级应用V1.2_2038933428191629313.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：77%

## 共有节点

全部 3 个 workflow 都包含：
- `AdaptiveLongestEdge_EditUtils`
- `CLIPLoader`
- `CLIPTextEncode`
- `CropWithPadInfo_EditUtils`
- `EditTextEncode_EditUtils`
- `Flux2KleinConfigPreparer_EditUtils`
- `Flux2KleinModelConfig_EditUtils`
- `Flux2KleinOutputExtractor_EditUtils`
- `Image Comparer (rgthree)`
- `KSampler`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `LoadImage`
- `PreviewImage`
- `PrimitiveInt`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Save` —— 2/3 个有
- `ImpactInt` —— 2/3 个有
- `LayerUtility: PurgeVRAM V2` —— 2/3 个有
- `LoraLoaderModelOnly` —— 2/3 个有
- `PrimitiveStringMultiline` —— 2/3 个有
- `VAEDecode` —— 2/3 个有
- `Any Switch (rgthree)` —— 1/3 个有
- `Fast Groups Muter (rgthree)` —— 1/3 个有
- `GetImageSize` —— 1/3 个有
- `JWStringMultiline` —— 1/3 个有
- `LoadImageOutput` —— 1/3 个有
- `ShowText|pysssss` —— 1/3 个有
- `TTP_text_mix` —— 1/3 个有
- `Text Concatenate` —— 1/3 个有
- `VAEDecodeTiled` —— 1/3 个有
- `easy positive` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 20 | 3 | 19% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |
| 发现KSampler但没有VAEDecode | 1/3 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 20，3 个样本，取值分散，一致性仅 19%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
