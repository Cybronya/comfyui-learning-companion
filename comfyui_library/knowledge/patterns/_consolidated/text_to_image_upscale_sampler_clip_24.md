---
name: text_to_image_upscale_sampler_clip_24
type: Text To Image
frequency: 5
level: strong
coverage: 0.9108
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, ImageScaleBy, KSampler, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/解说漫-人物图设计_2051050872968359937.json, 图片生成/文生图/解说漫-场景图设计_2052044595541880834.json, 图片生成/文生图/超级无敌加速版Nunchaku-Z-image文生图_2005265123503734786.json, 图片生成/文生图/阿里开源 Z-IMAGE 图像生成模型 + SeedVR2洗图高清放大工作流_1994282214103990274.json, 视频生成/图生视频/Z-image-Turbo 优化丰满美女身材 身材优化  更好的身材_2028667422059798530.json]
source: knowledge_consolidation
---

# text_to_image_upscale_sampler_clip_24

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/解说漫-人物图设计_2051050872968359937.json、图片生成/文生图/解说漫-场景图设计_2052044595541880834.json、图片生成/文生图/超级无敌加速版Nunchaku-Z-image文生图_2005265123503734786.json、图片生成/文生图/阿里开源 Z-IMAGE 图像生成模型 + SeedVR2洗图高清放大工作流_1994282214103990274.json、视频生成/图生视频/Z-image-Turbo 优化丰满美女身材 身材优化  更好的身材_2028667422059798530.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
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
- `ConditioningZeroOut` —— 4/5 个有
- `Fast Groups Bypasser (rgthree)` —— 3/5 个有
- `Image Comparer (rgthree)` —— 3/5 个有
- `LoraLoaderModelOnly` —— 2/5 个有
- `easy saveText` —— 2/5 个有
- `CR Prompt Text` —— 1/5 个有
- `ImageLoader` —— 1/5 个有
- `ImageScaleToMaxDimension` —— 1/5 个有
- `ImpactInt` —— 1/5 个有
- `ModelSamplingAuraFlow` —— 1/5 个有
- `NunchakuZImageDiTLoader` —— 1/5 个有
- `Qwen3_VQA` —— 1/5 个有
- `Text` —— 1/5 个有
- `easy promptLine` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 8 - 10 | 5 | 91% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 60% |
| 调度器 | simple | - | 5 | 80% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 1080 | 720 - 1920 | 5 | 66% |
| 高度 | 1560 | 1080 - 1920 | 5 | 78% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 8 - 10，5 个样本，取值集中（一致性 91%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 60%
- 调度器 最常用 simple，5 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 1080，观测区间 720 - 1920，5 个样本
- 高度 中位数 1560，观测区间 1080 - 1920，5 个样本
