---
name: text_to_image_sampler_clip_unet_134
type: Text To Image
frequency: 5
level: moderate
coverage: 0.9438
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Z-image图生图超写实_1993925049646252034.json, 图片生成/文生图/001.Z-image生图巅峰006.回车批量文生图.json_2033729781623164930.json, 图片生成/文生图/LH-DMT版本-2.生图片类-028.Z-image回车批量文生图-NF_2016493232032587777.json, 图片生成/文生图/Z-Image-De-Turbo文生图_1997688531524980738.json, 图片生成/文生图/反推提示词+Z-image文生图_2015983039649681410.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_134

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Z-image图生图超写实_1993925049646252034.json、图片生成/文生图/001.Z-image生图巅峰006.回车批量文生图.json_2033729781623164930.json、图片生成/文生图/LH-DMT版本-2.生图片类-028.Z-image回车批量文生图-NF_2016493232032587777.json、图片生成/文生图/Z-Image-De-Turbo文生图_1997688531524980738.json、图片生成/文生图/反推提示词+Z-image文生图_2015983039649681410.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 5 个 workflow 都包含：
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
- `Qwen3_VQA` —— 3/5 个有
- `ShowText|pysssss` —— 3/5 个有
- `LoadImage` —— 2/5 个有
- `easy promptLine` —— 2/5 个有
- `CR Prompt Text` —— 1/5 个有
- `DisplayText` —— 1/5 个有
- `ImageLoader` —— 1/5 个有
- `LayerUtility: PurgeVRAM V2` —— 1/5 个有
- `LoraLoaderModelOnly` —— 1/5 个有
- `SetNode` —— 1/5 个有
- `SomethingToString` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 9 - 30 | 5 | 40% |
| Prompt 约束强度(CFG) | 1 | 1 - 3 | 5 | 43% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 1080 | 832 - 1280 | 5 | 87% |
| 高度 | 1920 | 480 - 1920 | 5 | 53% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 9 - 30，5 个样本，取值分散，一致性仅 40%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3，5 个样本，取值分散，一致性仅 43%
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 1080，观测区间 832 - 1280，5 个样本，取值集中（一致性 87%）
- 高度 中位数 1920，观测区间 480 - 1920，5 个样本
