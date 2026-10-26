---
name: unknown_workflow_lora_sampler_unet_134
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.9476
common_nodes: [CLIPLoader, DF_Integer, EmptyLatentImage, Get Image Size, Image Comparer (rgthree), ImageResize+, ImpactMinMax, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, SeedVR2, SimpleMath+, TTP_Image_Assy, TTP_Image_Tile_Batch, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/2511情趣换装_2045783275750301698.json, 图片生成/图生图/Qwen Image Edit 2511+SeedVR2 8K 3图编辑_2004427606441291778.json, 图片生成/图生图/换装 进来就懂（超低算力去除ai感，超级懒人版 ）_2067309223591112705.json, 图片生成/图生图/模特试穿+去AI感+放大_2067803923590762497.json, 视频生成/图生视频/换装  进来就懂（超低算力去除ai感，超级懒人版 ）_2067629071596613633.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_134

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/2511情趣换装_2045783275750301698.json、图片生成/图生图/Qwen Image Edit 2511+SeedVR2 8K 3图编辑_2004427606441291778.json、图片生成/图生图/换装 进来就懂（超低算力去除ai感，超级懒人版 ）_2067309223591112705.json、图片生成/图生图/模特试穿+去AI感+放大_2067803923590762497.json、视频生成/图生视频/换装  进来就懂（超低算力去除ai感，超级懒人版 ）_2067629071596613633.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：95%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `DF_Integer`
- `EmptyLatentImage`
- `Get Image Size`
- `Image Comparer (rgthree)`
- `ImageResize+`
- `ImpactMinMax`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `SeedVR2`
- `SimpleMath+`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 4/5 个有
- `ConditioningZeroOut` —— 4/5 个有
- `ConstrainImage|pysssss` —— 4/5 个有
- `FluxKontextMultiReferenceLatentMethod` —— 4/5 个有
- `GetImageSize+` —— 4/5 个有
- `ImageColorMatchAdobe+` —— 4/5 个有
- `LayerUtility: PurgeVRAM V2` —— 4/5 个有
- `PainterFluxImageEdit` —— 4/5 个有
- `SeedVR2BlockSwap` —— 4/5 个有
- `PreviewImage` —— 1/5 个有
- `easy cleanGpuUsed` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 80% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 2048 | 1440 - 2048 | 5 | 87% |
| 高度 | 2048 | 2048 - 2064 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 2048，观测区间 1440 - 2048，5 个样本，取值集中（一致性 87%）
- 高度 中位数 2048，观测区间 2048 - 2064，5 个样本，取值集中（一致性 100%）
- 高发问题（9/5 个样本）：Steps较低可能导致细节不足
