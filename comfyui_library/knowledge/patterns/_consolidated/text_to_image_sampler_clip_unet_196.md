---
name: text_to_image_sampler_clip_unet_196
type: Text To Image
frequency: 3
level: moderate
coverage: 0.97
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ColorMatch, ConditioningZeroOut, EmptyFlux2LatentImage, EmptyLatentImage, Flux2Scheduler, GetImageSize, ImageScaleToTotalPixels, ImageSharpen, KSampler, KSamplerSelect, LayerUtility: PurgeVRAM V2, PreviewImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAELoader]
problems: [发现KSampler但没有VAEDecode, Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/【KREA-2】文生图_双风格控制_高噪与低噪切换_自动放大_2082756989981118465.json, 图片生成/文生图/【文生图】KREA-2_强烈推荐_自定义参数_超级光影_细节可控_自动放大_一次多张_2080635166338404353.json, 图片生成/文生图/文生图工作流z-image高清放大_2101544123001040898.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_196

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/【KREA-2】文生图_双风格控制_高噪与低噪切换_自动放大_2082756989981118465.json、图片生成/文生图/【文生图】KREA-2_强烈推荐_自定义参数_超级光影_细节可控_自动放大_一次多张_2080635166338404353.json、图片生成/文生图/文生图工作流z-image高清放大_2101544123001040898.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ColorMatch`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `EmptyLatentImage`
- `Flux2Scheduler`
- `GetImageSize`
- `ImageScaleToTotalPixels`
- `ImageSharpen`
- `KSampler`
- `KSamplerSelect`
- `LayerUtility: PurgeVRAM V2`
- `PreviewImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `INTConstant` —— 2/3 个有
- `LoraLoader` —— 2/3 个有
- `TTResolutionSelector` —— 2/3 个有
- `VAEDecodeTiled` —— 2/3 个有
- `VAEEncodeTiled` —— 2/3 个有
- `easy clearCacheAll` —— 2/3 个有
- `VAEDecode` —— 1/3 个有
- `VAEEncode` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | 512 - 1024 | 3 | 65% |
| 高度 | 512 | 512 - 1536 | 3 | 43% |
| 采样步数 | 12 | 9 - 15 | 3 | 80% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | beta | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| LoRA 模型强度 | 0.5 | - | 2 | 0% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| 发现KSampler但没有VAEDecode | 2/3 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |
| Steps较低可能导致细节不足 | 1/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 512，观测区间 512 - 1024，3 个样本
- 高度 中位数 512，观测区间 512 - 1536，3 个样本，取值分散，一致性仅 43%
- 采样步数 中位数 12，观测区间 9 - 15，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.5，样本不足，未给区间，2 个样本，取值分散，一致性仅 0%
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/3 个样本）：发现KSampler但没有VAEDecode
