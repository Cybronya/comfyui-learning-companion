---
name: text_to_image_upscale_sampler_clip_35
type: Text To Image
frequency: 3
level: strong
coverage: 0.766667
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/解说漫-人物图设计_2051050872968359937.json, 图片生成/文生图/解说漫-场景图设计_2052044595541880834.json, 数字人/数字人/【尺素】krea2 熟颜世绘_2078697317879865345.json]
source: knowledge_consolidation
---

# text_to_image_upscale_sampler_clip_35

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/解说漫-人物图设计_2051050872968359937.json、图片生成/文生图/解说漫-场景图设计_2052044595541880834.json、数字人/数字人/【尺素】krea2 熟颜世绘_2078697317879865345.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：77%

## 共有节点

全部 3 个 workflow 都包含：
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
- `ConditioningZeroOut` —— 2/3 个有
- `ImageScaleBy` —— 2/3 个有
- `LoraLoaderModelOnly` —— 2/3 个有
- `easy saveText` —— 2/3 个有
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `GetNode` —— 1/3 个有
- `INTConstant` —— 1/3 个有
- `ImageScaleToTotalPixels` —— 1/3 个有
- `ImpactInt` —— 1/3 个有
- `SetNode` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 10 | 3 | 89% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | res_2s | - | 3 | 33% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 1080 | 1080 - 1920 | 3 | 71% |
| 高度 | 1920 | 1080 - 1920 | 3 | 76% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 10，3 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_2s，3 个样本，一致性 33%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 1080，观测区间 1080 - 1920，3 个样本
- 高度 中位数 1920，观测区间 1080 - 1920，3 个样本
- 高发问题（2/3 个样本）：Steps较低可能导致细节不足
