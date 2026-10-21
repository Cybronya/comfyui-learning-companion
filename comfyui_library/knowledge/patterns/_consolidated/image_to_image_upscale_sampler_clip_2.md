---
name: image_to_image_upscale_sampler_clip_2
type: Image To Image
frequency: 6
level: moderate
coverage: 0.742167
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [LayerUtility: ImageScaleByAspectRatio V2, CR Text, LayerUtility: ImageReel, LayerUtility: ImageReelComposit]
members: [图片生成/图生图/2007465177616228353.json, 图片生成/图生图/2102306162334068737.json, 图片生成/图生图/2102430336633364482.json, 图片生成/文生图/Z-Image最新模型 洗图+去除ai感 「24G」可用_2010631129069522946.json, 图片生成/文生图/zimage二次元转真人，双K洗图放大_2006226308195426306.json, 视频生成/图生视频/2070330640096120833.json]
source: knowledge_consolidation
---

# image_to_image_upscale_sampler_clip_2

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/2007465177616228353.json、图片生成/图生图/2102306162334068737.json、图片生成/图生图/2102430336633364482.json、图片生成/文生图/Z-Image最新模型 洗图+去除ai感 「24G」可用_2010631129069522946.json、图片生成/文生图/zimage二次元转真人，双K洗图放大_2006226308195426306.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：74%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 5/6 个有
- `ImageScaleBy` —— 5/6 个有
- `ShowText|pysssss` —— 5/6 个有
- `easy showAnything` —— 5/6 个有
- `ImpactInt` —— 4/6 个有
- `JoinStrings` —— 4/6 个有
- `Qwen3_VQA` —— 4/6 个有
- `TextInput_` —— 4/6 个有
- `AILab_QwenVL` —— 3/6 个有
- `CR Text` —— 3/6 个有
- `Image Comparer (rgthree)` —— 3/6 个有
- `Fast Groups Bypasser (rgthree)` —— 2/6 个有
- `LayerUtility: PurgeVRAM` —— 2/6 个有
- `easy cleanGpuUsed` —— 2/6 个有
- `LayerUtility: ImageReel` —— 1/6 个有
- `LayerUtility: ImageReelComposit` —— 1/6 个有
- `LayerUtility: PurgeVRAM V2` —— 1/6 个有
- `LoraLoaderModelOnly` —— 1/6 个有
- `RHUploadZip` —— 1/6 个有
- `RH_RhartVideoSparkvideo20MultimodalVideo` —— 1/6 个有
- `SaveVideo` —— 1/6 个有
- `SetNode` —— 1/6 个有
- `easy clearCacheAll` —— 1/6 个有
- `孤海注释` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 10 - 12 | 6 | 93% |
| Prompt 约束强度(CFG) | 1 | 1 - 2 | 6 | 69% |
| 采样算法 | euler | - | 6 | 83% |
| 调度器 | simple | - | 6 | 83% |
| 重绘幅度 | 0.7 | 0.15 - 1 | 6 | 52% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 10 - 12，6 个样本，取值集中（一致性 93%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2，6 个样本
- 采样算法 最常用 euler，6 个样本，一致性 83%
- 调度器 最常用 simple，6 个样本，一致性 83%
- 重绘幅度 中位数 0.7，观测区间 0.15 - 1，6 个样本
- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: ImageScaleByAspectRatio V2、CR Text、LayerUtility: ImageReel、LayerUtility: ImageReelComposit
