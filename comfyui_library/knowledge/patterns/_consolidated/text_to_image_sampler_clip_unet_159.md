---
name: text_to_image_sampler_clip_unet_159
type: Text To Image
frequency: 4
level: strong
coverage: 0.96675
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-image文生图+反推生图_1993976543361908738.json, 图片生成/文生图/Z-image文生图+图生图_1994184481552744449.json, 图片生成/文生图/Z-image文生图-古风插画-gu_2012675993739202562.json, 图片生成/文生图/Zimage图生图(洗图)_1993865488509976578.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_159

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/Z-image文生图+反推生图_1993976543361908738.json、图片生成/文生图/Z-image文生图+图生图_1994184481552744449.json、图片生成/文生图/Z-image文生图-古风插画-gu_2012675993739202562.json、图片生成/文生图/Zimage图生图(洗图)_1993865488509976578.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：97%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 3/4 个有
- `LoadImage` —— 3/4 个有
- `VAEEncode` —— 3/4 个有
- `AILab_QwenVL` —— 1/4 个有
- `ColorMatch` —— 1/4 个有
- `GetImageSizeAndCount` —— 1/4 个有
- `LoraLoaderModelOnly_Any` —— 1/4 个有
- `PrimitiveInt` —— 1/4 个有
- `RH_Captioner` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 9 - 10 | 4 | 96% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 1080 | 1080 - 1536 | 4 | 83% |
| 高度 | 1500 | 1024 - 1920 | 4 | 71% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 9 - 10，4 个样本，取值集中（一致性 96%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 1080，观测区间 1080 - 1536，4 个样本，取值集中（一致性 83%）
- 高度 中位数 1500，观测区间 1024 - 1920，4 个样本
