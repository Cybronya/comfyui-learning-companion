---
name: text_to_image_upscale_sampler_clip_7
type: Text To Image
frequency: 12
level: strong
coverage: 0.905583
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, ImageScaleBy, KSampler, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Zimage-文生图+高清修复_2011971976901955585.json, 图片生成/文生图/Zimage_瑶光_2095722755646902273.json, 图片生成/文生图/Zimage_瑶光（真人皮肤质感很好）_2117036414394265602.json, 图片生成/文生图/Zimage图像修复放大_2045420770012172290.json, 图片生成/文生图/zimage图像修复放大_2032377992323801090.json, 图片生成/文生图/图像修复放大 - Zimage_2009636078482886658.json, 图片生成/文生图/图像修复放大+Zimage双模_2020336239643205634.json, 图片生成/文生图/小而美图像模型：文生图_1995813775376789506.json, 图片生成/文生图/电影级CG写实大模型-Z-Image-支持4K放大_2054175364548702209.json, 图片生成/文生图/解说漫-人物图设计_2051050872968359937.json, 图片生成/文生图/解说漫-场景图设计_2052044595541880834.json, 图片生成/文生图/阿里开源 Z-IMAGE 图像生成模型 + SeedVR2洗图高清放大工作流_1994282214103990274.json]
source: knowledge_consolidation
---

# text_to_image_upscale_sampler_clip_7

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/文生图/Zimage-文生图+高清修复_2011971976901955585.json、图片生成/文生图/Zimage_瑶光_2095722755646902273.json、图片生成/文生图/Zimage_瑶光（真人皮肤质感很好）_2117036414394265602.json、图片生成/文生图/Zimage图像修复放大_2045420770012172290.json、图片生成/文生图/zimage图像修复放大_2032377992323801090.json…）

- **类型**：Text To Image
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 12 个 workflow 都包含：
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
- `ConditioningZeroOut` —— 9/12 个有
- `Fast Groups Bypasser (rgthree)` —— 7/12 个有
- `Image Comparer (rgthree)` —— 6/12 个有
- `Text` —— 6/12 个有
- `LoraLoaderModelOnly` —— 3/12 个有
- `easy promptList` —— 3/12 个有
- `ImpactInt` —— 2/12 个有
- `easy saveText` —— 2/12 个有
- `Resolution` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | 8 - 10 | 12 | 92% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 12 | 100% |
| 采样算法 | euler | - | 12 | 75% |
| 调度器 | simple | - | 12 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |
| 宽度 | 1080 | 720 - 1920 | 12 | 72% |
| 高度 | 1920 | 1080 - 1920 | 12 | 80% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 12/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，观测区间 8 - 10，12 个样本，取值集中（一致性 92%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，12 个样本，一致性 75%
- 调度器 最常用 simple，12 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 宽度 中位数 1080，观测区间 720 - 1920，12 个样本
- 高度 中位数 1920，观测区间 1080 - 1920，12 个样本，取值集中（一致性 80%）
- 高发问题（12/12 个样本）：Steps较低可能导致细节不足
