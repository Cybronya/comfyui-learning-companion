---
name: text_to_image_sampler_clip_unet_63
type: Text To Image
frequency: 10
level: weak
coverage: 0.8903
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Z-image高清细节DejpegV2_1998260405262778370.json, 图片生成/文生图/1-Z-image-角色信息+场景出图_2041121891695464449.json, 图片生成/文生图/1-Z-image-角色信息+场景出图_2052377045975486465.json, 图片生成/文生图/2-1-z-image-文生图-角色生成_2061349711671554049.json, 图片生成/文生图/2029928001101635585.json, 图片生成/文生图/A-14 Z-Image Turbo 特定风格 人像大作 文生图_2096961472139194369.json, 图片生成/文生图/Anima base v1 动漫生图_2059172782583410690.json, 图片生成/文生图/Anima base v1 动漫生图_2093989338236407810.json, 图片生成/文生图/Krea2 人物LoRA测试—Taslim_2073325908940902401.json, 图片生成/文生图/Krea2-云上天宫_2095745487965081602.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_63

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/Z-image高清细节DejpegV2_1998260405262778370.json、图片生成/文生图/1-Z-image-角色信息+场景出图_2041121891695464449.json、图片生成/文生图/1-Z-image-角色信息+场景出图_2052377045975486465.json、图片生成/文生图/2-1-z-image-文生图-角色生成_2061349711671554049.json、图片生成/文生图/2029928001101635585.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：弱结论（样本不足）
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
- `ConditioningZeroOut` —— 8/10 个有
- `ModelSamplingAuraFlow` —— 8/10 个有
- `LoraLoaderModelOnly` —— 6/10 个有
- `PrimitiveInt` —— 4/10 个有
- `PrimitiveStringMultiline` —— 3/10 个有
- `AddLabel` —— 2/10 个有
- `ResolutionSelector` —— 2/10 个有
- `Anything Everywhere3` —— 1/10 个有
- `Label (rgthree)` —— 1/10 个有
- `easy promptList` —— 1/10 个有
- `easy seed` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | 8 - 30 | 10 | 37% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 10 | 31% |
| 采样算法 | euler | - | 10 | 60% |
| 调度器 | simple | - | 10 | 90% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |
| 宽度 | 1024 | 512 - 2560 | 10 | 46% |
| 高度 | 1408 | 512 - 2480 | 10 | 63% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，观测区间 8 - 30，10 个样本，取值分散，一致性仅 37%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，10 个样本，取值分散，一致性仅 31%
- 采样算法 最常用 euler，10 个样本，一致性 60%
- 调度器 最常用 simple，10 个样本，一致性 90%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 512 - 2560，10 个样本，取值分散，一致性仅 46%
- 高度 中位数 1408，观测区间 512 - 2480，10 个样本
- 高发问题（7/10 个样本）：Steps较低可能导致细节不足
