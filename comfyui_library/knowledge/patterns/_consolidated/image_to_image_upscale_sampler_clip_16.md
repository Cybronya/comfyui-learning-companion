---
name: image_to_image_upscale_sampler_clip_16
type: Image To Image
frequency: 7
level: moderate
coverage: 0.818857
common_nodes: [CLIPLoader, CLIPTextEncode, ImageScaleBy, KSampler, LoadImage, Qwen3_VQA, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, ShowText|pysssss, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Z-Image-Turbo  图生图（反推提示词）_1994053520406020098.json, 图片生成/图生图/Z-image 宇宙超级无敌洗图_2078064317009850370.json, 图片生成/图生图/zimage双K洗图放大_2010944842016235521.json, 图片生成/图生图/【CQ808】保证原图相似度_去AI感_高保真_2015720412482637826.json, 图片生成/图生图/去AI感_高保真_2101964376919072770.json, 图片生成/文生图/Z-Image最新模型 洗图+去除ai感 「24G」可用_2010631129069522946.json, 图片生成/文生图/zimage二次元转真人，双K洗图放大_2006226308195426306.json]
source: knowledge_consolidation
---

# image_to_image_upscale_sampler_clip_16

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/Z-Image-Turbo  图生图（反推提示词）_1994053520406020098.json、图片生成/图生图/Z-image 宇宙超级无敌洗图_2078064317009850370.json、图片生成/图生图/zimage双K洗图放大_2010944842016235521.json、图片生成/图生图/【CQ808】保证原图相似度_去AI感_高保真_2015720412482637826.json、图片生成/图生图/去AI感_高保真_2101964376919072770.json…）

- **类型**：Image To Image
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ImageScaleBy`
- `KSampler`
- `LoadImage`
- `Qwen3_VQA`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `ShowText|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 6/7 个有
- `JoinStrings` —— 6/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 6/7 个有
- `TextInput_` —— 5/7 个有
- `Fast Groups Bypasser (rgthree)` —— 4/7 个有
- `Image Comparer (rgthree)` —— 4/7 个有
- `ImpactInt` —— 4/7 个有
- `PreviewImage` —— 4/7 个有
- `CR Text` —— 3/7 个有
- `LayerUtility: PurgeVRAM` —— 3/7 个有
- `easy cleanGpuUsed` —— 3/7 个有
- `Float` —— 2/7 个有
- `LayerUtility: PurgeVRAM V2` —— 2/7 个有
- `easy clearCacheAll` —— 2/7 个有
- `AILab_QwenVL` —— 1/7 个有
- `Getter` —— 1/7 个有
- `Latent Noise Injection` —— 1/7 个有
- `PrimitiveFloat` —— 1/7 个有
- `RH_Translator` —— 1/7 个有
- `Setter` —— 1/7 个有
- `Text` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 9 - 10 | 7 | 96% |
| Prompt 约束强度(CFG) | 1 | 1 - 1.6 | 7 | 77% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 0.45 | 0.3 - 1 | 7 | 53% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 9 - 10，7 个样本，取值集中（一致性 96%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1.6，7 个样本
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 0.45，观测区间 0.3 - 1，7 个样本
