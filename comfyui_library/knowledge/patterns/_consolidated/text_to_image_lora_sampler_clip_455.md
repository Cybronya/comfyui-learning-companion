---
name: text_to_image_lora_sampler_clip_455
type: Text To Image
frequency: 4
level: weak
coverage: 0.889
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, FluxKontextMultiReferenceLatentMethod, KSampler, Krea2OstrisEditModelPatch, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, kkPadImageToCanvas]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Krea2_四视图_角色设计——搬运、仅自用_2115790482134626306.json, 图片生成/图生图/Krea2漫剧角色资产一键生成工作流图生四视图_2100300485814218754.json, 图片生成/图生图/Krea2角色四视图生成2.0 图生图处理工具_2100269060750663682.json, 图片生成/文生图/Krea2_四视图_角色设计_2099385665170530305.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_455

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Krea2_四视图_角色设计——搬运、仅自用_2115790482134626306.json、图片生成/图生图/Krea2漫剧角色资产一键生成工作流图生四视图_2100300485814218754.json、图片生成/图生图/Krea2角色四视图生成2.0 图生图处理工具_2100269060750663682.json、图片生成/文生图/Krea2_四视图_角色设计_2099385665170530305.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：89%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `FluxKontextMultiReferenceLatentMethod`
- `KSampler`
- `Krea2OstrisEditModelPatch`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `kkPadImageToCanvas`

**可变部分**（部分 workflow 才有）：
- `Easy_QwenEdit2509` —— 3/4 个有
- `PreviewImage` —— 3/4 个有
- `JjkText` —— 2/4 个有
- `PrimitiveStringMultiline` —— 2/4 个有
- `StringFunction|pysssss` —— 2/4 个有
- `solarL_SaveImagesToZip` —— 2/4 个有
- `孤海注释` —— 2/4 个有
- `忽略多组孤海` —— 2/4 个有
- `Krea2EditGroundedEncode` —— 1/4 个有
- `VAEEncode` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 4 - 8 | 4 | 67% |
| Prompt 约束强度(CFG) | 2.75 | 1 - 4.5 | 4 | 36% |
| 采样算法 | euler | - | 4 | 50% |
| 调度器 | FlowMatchEulerDiscreteScheduler | - | 4 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 808 | 80 - 1536 | 4 | 10% |
| 高度 | 468 | 80 - 856 | 4 | 17% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 4 - 8，4 个样本
- Prompt 约束强度(CFG) 中位数 2.75，观测区间 1 - 4.5，4 个样本，取值分散，一致性仅 36%
- 采样算法 最常用 euler，4 个样本，一致性 50%
- 调度器 最常用 FlowMatchEulerDiscreteScheduler，4 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 808，观测区间 80 - 1536，4 个样本，取值分散，一致性仅 10%
- 高度 中位数 468，观测区间 80 - 856，4 个样本，取值分散，一致性仅 17%
- 高发问题（8/4 个样本）：Steps较低可能导致细节不足
