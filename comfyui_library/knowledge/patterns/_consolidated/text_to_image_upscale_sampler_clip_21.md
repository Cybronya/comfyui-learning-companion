---
name: text_to_image_upscale_sampler_clip_21
type: Text To Image
frequency: 5
level: moderate
coverage: 0.8986
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/krea2-反推-文生图专用_2074031576870113281.json, 图片生成/文生图/AA--超真实Super Zimage文生图+超清放大_2025977545518223361.json, 图片生成/文生图/Krea2基础生图+ SeedVR 4K 超清放大_2082094625946431490.json, 图片生成/文生图/Z-image文生图+直逼真实摄影+最新seedvr2高清放大工作流_1994801677821730818.json, 视频生成/文生视频/极致电影4K美学-Krea2基础生图++SeedVR+4K+超清放大-极氪白白酱_2082122814294937602.json]
source: knowledge_consolidation
---

# text_to_image_upscale_sampler_clip_21

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/krea2-反推-文生图专用_2074031576870113281.json、图片生成/文生图/AA--超真实Super Zimage文生图+超清放大_2025977545518223361.json、图片生成/文生图/Krea2基础生图+ SeedVR 4K 超清放大_2082094625946431490.json、图片生成/文生图/Z-image文生图+直逼真实摄影+最新seedvr2高清放大工作流_1994801677821730818.json、视频生成/文生视频/极致电影4K美学-Krea2基础生图++SeedVR+4K+超清放大-极氪白白酱_2082122814294937602.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 4/5 个有
- `PreviewImage` —— 4/5 个有
- `ConditioningZeroOut` —— 3/5 个有
- `INTConstant` —— 3/5 个有
- `Image Comparer (rgthree)` —— 3/5 个有
- `ImageScaleToTotalPixels` —— 3/5 个有
- `Lora Loader Stack (rgthree)` —— 2/5 个有
- `Int` —— 1/5 个有
- `LoadImage` —— 1/5 个有
- `LoraLoaderModelOnly` —— 1/5 个有
- `PDRatioSelector` —— 1/5 个有
- `PathchSageAttentionKJ` —— 1/5 个有
- `RH_Translator` —— 1/5 个有
- `easy promptLine` —— 1/5 个有
- `忽略多组孤海` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 6 - 15 | 5 | 67% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | er_sde | - | 5 | 60% |
| 调度器 | simple | - | 5 | 80% |
| 重绘幅度 | 1 | 0.97 - 1 | 5 | 99% |
| 宽度 | 1920 | 1080 - 2048 | 5 | 72% |
| 高度 | 1080 | 856 - 1920 | 5 | 67% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 6 - 15，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，5 个样本，一致性 60%
- 调度器 最常用 simple，5 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 0.97 - 1，5 个样本，取值集中（一致性 99%）
- 宽度 中位数 1920，观测区间 1080 - 2048，5 个样本
- 高度 中位数 1080，观测区间 856 - 1920，5 个样本
- 高发问题（3/5 个样本）：Steps较低可能导致细节不足
