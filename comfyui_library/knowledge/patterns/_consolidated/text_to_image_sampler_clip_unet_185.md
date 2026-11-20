---
name: text_to_image_sampler_clip_unet_185
type: Text To Image
frequency: 3
level: moderate
coverage: 0.976333
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Z-image图生图超写实_1993925049646252034.json, 图片生成/文生图/001.Z-image生图巅峰008.文生图-语义理解升级_2033732546902630402.json, 图片生成/文生图/LH-DMT版本-2.生图片类-038. Z image_v3升级版更强提示词理解-文生图_2016524578054475777.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_185

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Z-image图生图超写实_1993925049646252034.json、图片生成/文生图/001.Z-image生图巅峰008.文生图-语义理解升级_2033732546902630402.json、图片生成/文生图/LH-DMT版本-2.生图片类-038. Z image_v3升级版更强提示词理解-文生图_2016524578054475777.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 3 个 workflow 都包含：
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
- `LayerUtility: PurgeVRAM` —— 2/3 个有
- `DisplayText` —— 1/3 个有
- `ImageLoader` —— 1/3 个有
- `Qwen3_VQA` —— 1/3 个有
- `ShowText|pysssss` —— 1/3 个有
- `SomethingToString` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 12 | 10 - 20 | 3 | 69% |
| Prompt 约束强度(CFG) | 3 | 1 - 3 | 3 | 60% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 1080 | 720 - 1080 | 3 | 82% |
| 高度 | 1920 | 1280 - 1920 | 3 | 82% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 12，观测区间 10 - 20，3 个样本
- Prompt 约束强度(CFG) 中位数 3，观测区间 1 - 3，3 个样本
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 1080，观测区间 720 - 1080，3 个样本，取值集中（一致性 82%）
- 高度 中位数 1920，观测区间 1280 - 1920，3 个样本，取值集中（一致性 82%）
