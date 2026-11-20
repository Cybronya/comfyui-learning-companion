---
name: text_to_image_sampler_clip_unet_63
type: Text To Image
frequency: 11
level: moderate
coverage: 0.814818
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/zimage生图_2002992438857875458.json, 图片生成/图生图/文生图 Qwen2512  领军模型 完美中文_2021581695731900418.json, 图片生成/图生图/文生图精简版+全节点注释_2067065224540282881.json, 图片生成/图生图/洗图重绘Qwen反推提示词i-zimage生图_2036694642334375938.json, 图片生成/图生图/电商洗图-主图_头图（一键生成）_1994289823892652033.json, 图片生成/文生图/Anima文生图精简版+全节点注释_2059139633056931841.json, 图片生成/文生图/Z-iamge文生图千问VL反推无需提示词自动文生图_1993913264711155713.json, 图片生成/文生图/krea2反推文生图_2070420567852937217.json, 图片生成/文生图/krea2反推文生图_2070466486245879810.json, 图片生成/文生图/krea2反推文生图无需提示词_2070349490783088642.json, 图片生成/文生图/文生图精简版+全节点注释_2067404118905409537.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_63

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/zimage生图_2002992438857875458.json、图片生成/图生图/文生图 Qwen2512  领军模型 完美中文_2021581695731900418.json、图片生成/图生图/文生图精简版+全节点注释_2067065224540282881.json、图片生成/图生图/洗图重绘Qwen反推提示词i-zimage生图_2036694642334375938.json、图片生成/图生图/电商洗图-主图_头图（一键生成）_1994289823892652033.json…）

- **类型**：Text To Image
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 10/11 个有
- `AILab_QwenVL` —— 6/11 个有
- `ConditioningZeroOut` —— 5/11 个有
- `LoraLoaderModelOnly` —— 5/11 个有
- `TextInput_` —— 5/11 个有
- `easy showAnything` —— 3/11 个有
- `LayerUtility: TextJoin` —— 2/11 个有
- `ModelSamplingAuraFlow` —— 2/11 个有
- `PreviewImage` —— 2/11 个有
- `AILab_QwenVL_Advanced` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 8 - 28 | 11 | 41% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 11 | 35% |
| 采样算法 | euler | - | 11 | 45% |
| 调度器 | simple | - | 11 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |
| 宽度 | 1024 | 752 - 1184 | 11 | 88% |
| 高度 | 1536 | 1000 - 1920 | 11 | 85% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 8 - 28，11 个样本，取值分散，一致性仅 41%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，11 个样本，取值分散，一致性仅 35%
- 采样算法 最常用 euler，11 个样本，一致性 45%
- 调度器 最常用 simple，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 752 - 1184，11 个样本，取值集中（一致性 88%）
- 高度 中位数 1536，观测区间 1000 - 1920，11 个样本，取值集中（一致性 85%）
