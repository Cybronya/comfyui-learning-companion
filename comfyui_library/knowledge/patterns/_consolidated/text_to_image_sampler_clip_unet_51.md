---
name: text_to_image_sampler_clip_unet_51
type: Text To Image
frequency: 11
level: moderate
coverage: 0.889091
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/反推提示词forZimage_2025858147600048130.json, 图片生成/反推提示词/图片反推提示词_1992900235936722945.json, 图片生成/图生图/Z-image  美女模特时尚人物穿搭 日常穿搭 电影级美学 网红洗图 批量生成 SeedVR2.5_2030806592970559490.json, 图片生成/文生图/2030634268841480193.json, 图片生成/文生图/Z-image-中老年内衣女模特_1999303495641690114.json, 图片生成/文生图/Z-image-女内裤模特图_1998988604456194049.json, 图片生成/文生图/Z-image-电商保暖模特_1996104929171423233.json, 图片生成/文生图/Z-image-电商内衣模特图_2002330895598120962.json, 图片生成/文生图/Z-image-电商女内裤模特图_1999755593114152961.json, 图片生成/文生图/Z-image-男内裤模特_1998588053952299010.json, 图片生成/文生图/Z-image电商文胸模特_1995676126175485954.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_51

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/反推提示词/反推提示词forZimage_2025858147600048130.json、图片生成/反推提示词/图片反推提示词_1992900235936722945.json、图片生成/图生图/Z-image  美女模特时尚人物穿搭 日常穿搭 电影级美学 网红洗图 批量生成 SeedVR2.5_2030806592970559490.json、图片生成/文生图/2030634268841480193.json、图片生成/文生图/Z-image-中老年内衣女模特_1999303495641690114.json…）

- **类型**：Text To Image
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 10/11 个有
- `easy cleanGpuUsed` —— 10/11 个有
- `Image Comparer (rgthree)` —— 9/11 个有
- `ImpactInt` —— 9/11 个有
- `SeedVR2LoadDiTModel` —— 9/11 个有
- `SeedVR2LoadVAEModel` —— 9/11 个有
- `SeedVR2VideoUpscaler` —— 9/11 个有
- `String Literal` —— 9/11 个有
- `Fast Groups Bypasser (rgthree)` —— 8/11 个有
- `LoadImage` —— 3/11 个有
- `Qwen3_VQA` —— 3/11 个有
- `SeedVR2TorchCompileSettings` —— 3/11 个有
- `easy showAnything` —— 3/11 个有
- `ShowText|pysssss` —— 2/11 个有
- `CR Prompt List` —— 1/11 个有
- `PreviewImage` —— 1/11 个有
- `WD14Tagger|pysssss` —— 1/11 个有
- `easy textSwitch` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 1 - 10 | 11 | 72% |
| Prompt 约束强度(CFG) | 1.2 | 0 - 1.5 | 11 | 65% |
| 采样算法 | euler | - | 11 | 100% |
| 调度器 | beta57 | - | 11 | 73% |
| 重绘幅度 | 1 | 0 - 1 | 11 | 68% |
| 宽度 | 720 | 512 - 832 | 11 | 90% |
| 高度 | 1280 | 512 - 1280 | 11 | 82% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 1 - 10，11 个样本
- Prompt 约束强度(CFG) 中位数 1.2，观测区间 0 - 1.5，11 个样本
- 采样算法 最常用 euler，11 个样本，一致性 100%
- 调度器 最常用 beta57，11 个样本，一致性 73%
- 重绘幅度 中位数 1，观测区间 0 - 1，11 个样本
- 宽度 中位数 720，观测区间 512 - 832，11 个样本，取值集中（一致性 90%）
- 高度 中位数 1280，观测区间 512 - 1280，11 个样本，取值集中（一致性 82%）
- 风险：Prompt 约束强度(CFG) 观测到 0，低于常用下限 1（CFG 过低可能导致 Prompt 约束不足、结果偏离描述）
- 风险：重绘幅度 观测到 0，低于常用下限 0.1（）
