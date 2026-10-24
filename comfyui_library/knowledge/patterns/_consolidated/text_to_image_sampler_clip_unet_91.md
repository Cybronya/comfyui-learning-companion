---
name: text_to_image_sampler_clip_unet_91
type: Text To Image
frequency: 7
level: moderate
coverage: 0.937857
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Z-image图生图超写实_1993925049646252034.json, 图片生成/图生图/Z-image文生图去AI感_2026166309813227522.json, 图片生成/文生图/001.Z-image生图巅峰005.五列表文生图.json_2033727476014260226.json, 图片生成/文生图/1.阿清的z-image工作流_2037804089450438658.json, 图片生成/文生图/LH-DMT版本-2.生图片类-027.Z-Image五列表文生图-NF_2016493212516487169.json, 图片生成/文生图/Z-Image-De-Turbo文生图_1997688531524980738.json, 图片生成/文生图/反推提示词+Z-image文生图_2015983039649681410.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_91

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/Z-image图生图超写实_1993925049646252034.json、图片生成/图生图/Z-image文生图去AI感_2026166309813227522.json、图片生成/文生图/001.Z-image生图巅峰005.五列表文生图.json_2033727476014260226.json、图片生成/文生图/1.阿清的z-image工作流_2037804089450438658.json、图片生成/文生图/LH-DMT版本-2.生图片类-027.Z-Image五列表文生图-NF_2016493212516487169.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 7 个 workflow 都包含：
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
- `easy promptList` —— 4/7 个有
- `Qwen3_VQA` —— 3/7 个有
- `ShowText|pysssss` —— 3/7 个有
- `LoadImage` —— 2/7 个有
- `CR Prompt Text` —— 1/7 个有
- `DisplayText` —— 1/7 个有
- `ImageLoader` —— 1/7 个有
- `LayerUtility: PurgeVRAM V2` —— 1/7 个有
- `LoraLoaderModelOnly` —— 1/7 个有
- `SetNode` —— 1/7 个有
- `SomethingToString` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 6 - 30 | 7 | 41% |
| Prompt 约束强度(CFG) | 1 | 1 - 3 | 7 | 46% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| 宽度 | 1024 | 480 - 1080 | 7 | 76% |
| 高度 | 1536 | 832 - 1920 | 7 | 74% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 6 - 30，7 个样本，取值分散，一致性仅 41%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3，7 个样本，取值分散，一致性仅 46%
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 480 - 1080，7 个样本
- 高度 中位数 1536，观测区间 832 - 1920，7 个样本
