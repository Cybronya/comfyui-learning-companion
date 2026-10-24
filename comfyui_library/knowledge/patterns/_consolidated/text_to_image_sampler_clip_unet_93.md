---
name: text_to_image_sampler_clip_unet_93
type: Text To Image
frequency: 7
level: moderate
coverage: 0.744571
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/zimage生图_2002992438857875458.json, 图片生成/图生图/文生图 Qwen2512  领军模型 完美中文_2021581695731900418.json, 图片生成/图生图/文生图精简版+全节点注释_2067065224540282881.json, 图片生成/图生图/洗图重绘Qwen反推提示词i-zimage生图_2036694642334375938.json, 图片生成/图生图/电商洗图-主图_头图（一键生成）_1994289823892652033.json, 图片生成/文生图/Anima文生图精简版+全节点注释_2059139633056931841.json, 图片生成/文生图/文生图精简版+全节点注释_2067404118905409537.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_93

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/zimage生图_2002992438857875458.json、图片生成/图生图/文生图 Qwen2512  领军模型 完美中文_2021581695731900418.json、图片生成/图生图/文生图精简版+全节点注释_2067065224540282881.json、图片生成/图生图/洗图重绘Qwen反推提示词i-zimage生图_2036694642334375938.json、图片生成/图生图/电商洗图-主图_头图（一键生成）_1994289823892652033.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：74%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 6/7 个有
- `LoraLoaderModelOnly` —— 5/7 个有
- `TextInput_` —— 5/7 个有
- `easy showAnything` —— 3/7 个有
- `AILab_QwenVL` —— 2/7 个有
- `LayerUtility: TextJoin` —— 2/7 个有
- `ModelSamplingAuraFlow` —— 2/7 个有
- `PreviewImage` —— 2/7 个有
- `AILab_QwenVL_Advanced` —— 1/7 个有
- `ConditioningZeroOut` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 8 - 28 | 7 | 52% |
| Prompt 约束强度(CFG) | 3.5 | 1 - 4 | 7 | 48% |
| 采样算法 | euler | - | 7 | 57% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| 宽度 | 1024 | 752 - 1080 | 7 | 88% |
| 高度 | 1536 | 1000 - 1920 | 7 | 81% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 25，观测区间 8 - 28，7 个样本
- Prompt 约束强度(CFG) 中位数 3.5，观测区间 1 - 4，7 个样本，取值分散，一致性仅 48%
- 采样算法 最常用 euler，7 个样本，一致性 57%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 752 - 1080，7 个样本，取值集中（一致性 88%）
- 高度 中位数 1536，观测区间 1000 - 1920，7 个样本，取值集中（一致性 81%）
