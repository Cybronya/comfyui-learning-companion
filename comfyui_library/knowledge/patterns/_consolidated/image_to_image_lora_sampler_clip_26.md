---
name: image_to_image_lora_sampler_clip_26
type: Image To Image
frequency: 9
level: strong
coverage: 0.607556
common_nodes: [Anything Everywhere3, CLIPLoader, CLIPTextEncode, DF_Integer, Float, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus_lrzjason, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy seed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/水墨插画图生图风格转换-热点视频水墨风图片生成_2053169989598883842.json, 图片生成/图生图/水墨插画图生图风格转换-热点视频水墨风图片生成_2054760424528203777.json, 图片生成/图生图/水墨插画图生图风格转换-热点视频水墨风图片生成_2059974184545116161.json, 图片生成/图生图/水墨插画图生图风格转换_2056925510059520002.json, 图片生成/图生图/水墨插画图生图风格转换_2058799155631443970.json, 图片生成/图生图/风格迁移（水墨插画风）_2054101584358985729.json, 图片生成/图生图/风格迁移（水墨插画风）_2054115985988300802.json, 图片生成/图生图/风格迁移（水墨插画风）_2085933520559628289.json, 图片生成/文生图/彩色图片转水墨+全节点注释_2057404353245442050.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_26

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/水墨插画图生图风格转换-热点视频水墨风图片生成_2053169989598883842.json、图片生成/图生图/水墨插画图生图风格转换-热点视频水墨风图片生成_2054760424528203777.json、图片生成/图生图/水墨插画图生图风格转换-热点视频水墨风图片生成_2059974184545116161.json、图片生成/图生图/水墨插画图生图风格转换_2056925510059520002.json、图片生成/图生图/水墨插画图生图风格转换_2058799155631443970.json…）

- **类型**：Image To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：61%

## 共有节点

全部 9 个 workflow 都包含：
- `Anything Everywhere3`
- `CLIPLoader`
- `CLIPTextEncode`
- `DF_Integer`
- `Float`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditPlus_lrzjason`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy seed`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 8/9 个有
- `SetNode` —— 8/9 个有
- `Text` —— 8/9 个有
- `CR Text` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 9 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler | - | 9 | 100% |
| 调度器 | simple | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，9 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，9 个样本，一致性 100%
- 调度器 最常用 simple，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（9/9 个样本）：Steps较低可能导致细节不足
