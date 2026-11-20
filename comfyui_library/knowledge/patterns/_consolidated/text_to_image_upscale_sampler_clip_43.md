---
name: text_to_image_upscale_sampler_clip_43
type: Text To Image
frequency: 3
level: strong
coverage: 0.961667
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/超级无敌加速版Nunchaku-Z-image文生图_2005265123503734786.json, 平台全量/4.5 Zimage_瑶光（真人皮肤质感很好）_2117740729824014338.json, 平台全量/Z-image文胸模特（电商）_1995754731303735298.json]
source: knowledge_consolidation
---

# text_to_image_upscale_sampler_clip_43

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/超级无敌加速版Nunchaku-Z-image文生图_2005265123503734786.json、平台全量/4.5 Zimage_瑶光（真人皮肤质感很好）_2117740729824014338.json、平台全量/Z-image文胸模特（电商）_1995754731303735298.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：96%

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
- `Image Comparer (rgthree)` —— 2/3 个有
- `ImageScaleBy` —— 2/3 个有
- `LoraLoaderModelOnly` —— 2/3 个有
- `CR Prompt Text` —— 1/3 个有
- `NunchakuZImageDiTLoader` —— 1/3 个有
- `SeedVR2TorchCompileSettings` —— 1/3 个有
- `String Literal` —— 1/3 个有
- `easy cleanGpuUsed` —— 1/3 个有
- `easy promptLine` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1080 | 1024 - 1280 | 3 | 90% |
| 高度 | 1560 | 1536 - 1920 | 3 | 89% |
| 采样步数 | 10 | 8 - 10 | 3 | 90% |
| Prompt 约束强度(CFG) | 1 | 1 - 1.5 | 3 | 80% |
| 采样算法 | res_multistep | - | 3 | 33% |
| 调度器 | simple | - | 3 | 33% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1080，观测区间 1024 - 1280，3 个样本，取值集中（一致性 90%）
- 高度 中位数 1560，观测区间 1536 - 1920，3 个样本，取值集中（一致性 89%）
- 采样步数 中位数 10，观测区间 8 - 10，3 个样本，取值集中（一致性 90%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1.5，3 个样本
- 采样算法 最常用 res_multistep，3 个样本，一致性 33%
- 调度器 最常用 simple，3 个样本，一致性 33%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
