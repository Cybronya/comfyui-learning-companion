---
name: text_to_image_sampler_clip_unet_106
type: Text To Image
frequency: 4
level: moderate
coverage: 0.953
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ColorMatch, ConditioningZeroOut, EmptyFlux2LatentImage, EmptyLatentImage, Flux2Scheduler, GetImageSize, ImageScaleToTotalPixels, ImageSharpen, KSampler, KSamplerSelect, LayerUtility: PurgeVRAM V2, PreviewImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAELoader]
problems: [Steps较低可能导致细节不足, 发现KSampler但没有VAEDecode]
missing: []
members: [图片生成/文生图/Krea2双采+Klein一次放大加细节+seedvr二次放大，高清化极致观感_2073725632059625473.json, 图片生成/文生图/【KREA-2】文生图_双风格控制_高噪与低噪切换_自动放大_2082756989981118465.json, 图片生成/文生图/【文生图】KREA-2_强烈推荐_自定义参数_超级光影_细节可控_自动放大_一次多张_2080635166338404353.json, 图片生成/文生图/文生图工作流z-image高清放大_2101544123001040898.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_106

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/Krea2双采+Klein一次放大加细节+seedvr二次放大，高清化极致观感_2073725632059625473.json、图片生成/文生图/【KREA-2】文生图_双风格控制_高噪与低噪切换_自动放大_2082756989981118465.json、图片生成/文生图/【文生图】KREA-2_强烈推荐_自定义参数_超级光影_细节可控_自动放大_一次多张_2080635166338404353.json、图片生成/文生图/文生图工作流z-image高清放大_2101544123001040898.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 4 个 workflow 都包含：
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
- `INTConstant` —— 2/4 个有
- `LoraLoader` —— 2/4 个有
- `TTResolutionSelector` —— 2/4 个有
- `VAEDecode` —— 2/4 个有
- `VAEDecodeTiled` —— 2/4 个有
- `VAEEncode` —— 2/4 个有
- `VAEEncodeTiled` —— 2/4 个有
- `easy clearCacheAll` —— 2/4 个有
- `Image Comparer (rgthree)` —— 1/4 个有
- `ResolutionSelector` —— 1/4 个有
- `SeedVR2LoadDiTModel` —— 1/4 个有
- `SeedVR2LoadVAEModel` —— 1/4 个有
- `SeedVR2VideoUpscaler` —— 1/4 个有
- `孤海注释` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 768 | 512 - 1024 | 4 | 67% |
| 高度 | 768 | 512 - 1536 | 4 | 53% |
| 采样步数 | 10.5 | 5 - 15 | 4 | 64% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 75% |
| 调度器 | beta | - | 4 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| LoRA 模型强度 | 0.5 | - | 2 | 0% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |
| 发现KSampler但没有VAEDecode | 2/4 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 宽度 中位数 768，观测区间 512 - 1024，4 个样本
- 高度 中位数 768，观测区间 512 - 1536，4 个样本
- 采样步数 中位数 10.5，观测区间 5 - 15，4 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 75%
- 调度器 最常用 beta，4 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.5，样本不足，未给区间，2 个样本，取值分散，一致性仅 0%
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（3/4 个样本）：Steps较低可能导致细节不足
- 高发问题（2/4 个样本）：发现KSampler但没有VAEDecode
