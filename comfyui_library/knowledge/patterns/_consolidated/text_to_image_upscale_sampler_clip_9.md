---
name: text_to_image_upscale_sampler_clip_9
type: Text To Image
frequency: 11
level: strong
coverage: 0.847091
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, Image Comparer (rgthree), ImageScaleBy, KSampler, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/【4K 高清】Z-Image 文生图_1995501883357847553.json, 图片生成/图生图/千问图像反推+Z-Image+SeedVR2 高清放大_1997203090476580866.json, 图片生成/图生图/反推提示词＋相似图片生成（图生图） 硕阳_2003404747770109954.json, 图片生成/图生图/图像修复放大 - Zimage_2008563835296288770.json, 图片生成/图生图/图像修复放大+-+Zimage_2021785801733971970.json, 图片生成/文生图/001.Z-Image+lora文生图.json_2092039413546176513.json, 图片生成/文生图/001.Z-image生图巅峰001.lora文生图+放大_2033714274614386690.json, 图片生成/文生图/5.其他类型-6.NSF+-09.Z-image生图001.Z-Image+lora文生图带放大_2021966017785761793.json, 图片生成/文生图/Z-IMAGE：文生图、自动反推洗图_1995339189359140866.json, 图片生成/文生图/Z-image 宇宙超级无敌洗图_1995299863191597058.json, 图片生成/文生图/z-image-文生图_洗图_2008808216209133570.json]
source: knowledge_consolidation
---

# text_to_image_upscale_sampler_clip_9

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/【4K 高清】Z-Image 文生图_1995501883357847553.json、图片生成/图生图/千问图像反推+Z-Image+SeedVR2 高清放大_1997203090476580866.json、图片生成/图生图/反推提示词＋相似图片生成（图生图） 硕阳_2003404747770109954.json、图片生成/图生图/图像修复放大 - Zimage_2008563835296288770.json、图片生成/图生图/图像修复放大+-+Zimage_2021785801733971970.json…）

- **类型**：Text To Image
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `Image Comparer (rgthree)`
- `ImageScaleBy`
- `KSampler`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 7/11 个有
- `LoadImage` —— 5/11 个有
- `Qwen3_VQA` —— 5/11 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/11 个有
- `VAEEncode` —— 4/11 个有
- `ImpactInt` —— 3/11 个有
- `LoraLoader` —— 3/11 个有
- `ShowText|pysssss` —— 3/11 个有
- `PreviewImage` —— 2/11 个有
- `ShowAnything|Mie` —— 2/11 个有
- `Text` —— 2/11 个有
- `easy promptList` —— 2/11 个有
- `Any Switch (rgthree)` —— 1/11 个有
- `Fast Groups Muter (rgthree)` —— 1/11 个有
- `Float` —— 1/11 个有
- `GetImageSize` —— 1/11 个有
- `LayerUtility: ImageReel` —— 1/11 个有
- `LayerUtility: ImageReelComposit` —— 1/11 个有
- `PrimitiveFloat` —— 1/11 个有
- `RH_Translator` —— 1/11 个有
- `easy showAnything` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1080 | 720 - 1920 | 11 | 65% |
| 高度 | 1920 | 1080 - 1920 | 11 | 77% |
| 采样步数 | 9 | 9 - 10 | 11 | 95% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 11 | 100% |
| 采样算法 | euler | - | 11 | 100% |
| 调度器 | simple | - | 11 | 73% |
| 重绘幅度 | 1 | 0.3 - 1 | 11 | 78% |
| LoRA 模型强度 | 1 | 1 - 1 | 3 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1080，观测区间 720 - 1920，11 个样本
- 高度 中位数 1920，观测区间 1080 - 1920，11 个样本
- 采样步数 中位数 9，观测区间 9 - 10，11 个样本，取值集中（一致性 95%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，11 个样本，一致性 100%
- 调度器 最常用 simple，11 个样本，一致性 73%
- 重绘幅度 中位数 1，观测区间 0.3 - 1，11 个样本
- LoRA 模型强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（10/11 个样本）：Steps较低可能导致细节不足
