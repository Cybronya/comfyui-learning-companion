---
name: text_to_image_sampler_clip_unet_59
type: Text To Image
frequency: 8
level: moderate
coverage: 0.82425
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-Image镜片·光学镜片场景生成_2044682719262674946.json, 图片生成/文生图/Z-image 提示词列表1次生成5张图_2022135215480639489.json, 图片生成/文生图/Z-image文生图工作流_2075475394177880066.json, 图片生成/文生图/Z-image最强真实人物细节多场景生成_2003710733722525697.json, 图片生成/文生图/ZImage3.0-SUPER 文生图_2017812013216436226.json, 图片生成/文生图/Zimage文生图_2013426591489069057.json, 图片生成/文生图/z image 文生图 - 超强随机性_1996217608485617665.json, 图片生成/文生图/超智能提示词反推照片V2_2004362690019684353.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_59

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/Z-Image镜片·光学镜片场景生成_2044682719262674946.json、图片生成/文生图/Z-image 提示词列表1次生成5张图_2022135215480639489.json、图片生成/文生图/Z-image文生图工作流_2075475394177880066.json、图片生成/文生图/Z-image最强真实人物细节多场景生成_2003710733722525697.json、图片生成/文生图/ZImage3.0-SUPER 文生图_2017812013216436226.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 8 个 workflow 都包含：
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
- `easy promptList` —— 5/8 个有
- `PreviewImage` —— 4/8 个有
- `AspectRatio` —— 3/8 个有
- `LoraLoader` —— 3/8 个有
- `ModelSamplingAuraFlow` —— 2/8 个有
- `PrimitiveInt` —— 2/8 个有
- `Fast Groups Muter (rgthree)` —— 1/8 个有
- `HAIGC_SaveImagesToZip` —— 1/8 个有
- `KSamplerAdvanced` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 9 - 30 | 7 | 46% |
| Prompt 约束强度(CFG) | 1 | 1 - 10 | 8 | 0% |
| 采样算法 | euler | - | 8 | 88% |
| 调度器 | simple | - | 8 | 88% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| 宽度 | 1092 | 1024 - 1920 | 8 | 70% |
| 高度 | 1276 | 1024 - 1920 | 8 | 74% |
| LoRA 模型强度 | 0.6 | 0.6 - 0.8 | 3 | 86% |
| LoRA 文本强度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 9 - 30，7 个样本，取值分散，一致性仅 46%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 10，8 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 euler，8 个样本，一致性 88%
- 调度器 最常用 simple，8 个样本，一致性 88%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 宽度 中位数 1092，观测区间 1024 - 1920，8 个样本
- 高度 中位数 1276，观测区间 1024 - 1920，8 个样本
- LoRA 模型强度 中位数 0.6，观测区间 0.6 - 0.8，3 个样本，取值集中（一致性 86%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
