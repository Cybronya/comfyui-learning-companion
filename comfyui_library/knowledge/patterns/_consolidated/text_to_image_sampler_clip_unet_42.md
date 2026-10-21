---
name: text_to_image_sampler_clip_unet_42
type: Text To Image
frequency: 10
level: moderate
coverage: 0.8874
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-Image-Base文生图批量生图_2018255513896624130.json, 图片生成/文生图/Z-Image-Base高质量多细节文生图_2015636535781101570.json, 图片生成/文生图/Z-Image-De-Turbo去蒸馏文生图（CFG3 25步）_1997621234118668290.json, 图片生成/文生图/Z-Image-SuperV3-文生图_2018341790440493058.json, 图片生成/文生图/Z-Image-Turbo 浮云2.3_2018528654661263361.json, 图片生成/文生图/Z-image text-to-image-文生图-超自然人像-20秒快速出图_1993970117180669953.json, 图片生成/文生图/Z-image text-to-image-文生图-超自然人像-20秒快速出图_2074311721812062209.json, 图片生成/文生图/Z-image text-to-image-文生图（完美支持中文字+超自然）​【Agent必备】_2088917231601278978.json, 图片生成/文生图/Z-image-神级文生图-20秒超快速出图TEXT TO IMAGE_1993958594863366145.json, 图片生成/文生图/（Z-image）dpmpp-2m-sde对比euler-文生图_1995128750184574977.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_42

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/文生图/Z-Image-Base文生图批量生图_2018255513896624130.json、图片生成/文生图/Z-Image-Base高质量多细节文生图_2015636535781101570.json、图片生成/文生图/Z-Image-De-Turbo去蒸馏文生图（CFG3 25步）_1997621234118668290.json、图片生成/文生图/Z-Image-SuperV3-文生图_2018341790440493058.json、图片生成/文生图/Z-Image-Turbo 浮云2.3_2018528654661263361.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 8/10 个有
- `ConditioningZeroOut` —— 7/10 个有
- `easy promptLine` —— 7/10 个有
- `GetNode` —— 5/10 个有
- `SetNode` —— 5/10 个有
- `LayerUtility: PurgeVRAM` —— 4/10 个有
- `LoadImage` —— 2/10 个有
- `ModelSamplingAuraFlow` —— 2/10 个有
- `Load Lora` —— 1/10 个有
- `PrimitiveInt` —— 1/10 个有
- `Text Multiline` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 8 - 30 | 10 | 46% |
| Prompt 约束强度(CFG) | 1 | 1 - 3 | 10 | 43% |
| 采样算法 | euler | - | 10 | 70% |
| 调度器 | simple | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |
| 宽度 | 1080 | 1024 - 1920 | 10 | 73% |
| 高度 | 1480 | 1080 - 1920 | 10 | 81% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 8 - 30，10 个样本，取值分散，一致性仅 46%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3，10 个样本，取值分散，一致性仅 43%
- 采样算法 最常用 euler，10 个样本，一致性 70%
- 调度器 最常用 simple，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 宽度 中位数 1080，观测区间 1024 - 1920，10 个样本
- 高度 中位数 1480，观测区间 1080 - 1920，10 个样本，取值集中（一致性 81%）
