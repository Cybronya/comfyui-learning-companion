---
name: text_to_image_sampler_clip_unet_124
type: Text To Image
frequency: 6
level: moderate
coverage: 0.869167
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Krea2-风格扩展_无限创意_2090018651477987330.json, 图片生成/文生图/Krea2文生图_2095904097835765761.json, 图片生成/文生图/MOSS Image base文生图_2113316857922023426.json, 图片生成/文生图/MOSS Image sft 文生图_2113321575687737346.json, 图片生成/文生图/Z-Image 反推描述生图_1993864386123071490.json, 图片生成/文生图/krea2-场景图_2094627383453241346.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_124

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/Krea2-风格扩展_无限创意_2090018651477987330.json、图片生成/文生图/Krea2文生图_2095904097835765761.json、图片生成/文生图/MOSS Image base文生图_2113316857922023426.json、图片生成/文生图/MOSS Image sft 文生图_2113321575687737346.json、图片生成/文生图/Z-Image 反推描述生图_1993864386123071490.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ResolutionSelector` —— 5/6 个有
- `ConditioningZeroOut` —— 4/6 个有
- `Label (rgthree)` —— 4/6 个有
- `PrimitiveStringMultiline` —— 4/6 个有
- `LoadImage` —— 2/6 个有
- `Seed (rgthree)` —— 2/6 个有
- `easy showAnything` —— 2/6 个有
- `Fast Groups Muter (rgthree)` —— 1/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/6 个有
- `RH_Captioner` —— 1/6 个有
- `easy stylesSelector` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 744 | 512 - 1024 | 6 | 76% |
| 高度 | 1024 | 512 - 1280 | 6 | 75% |
| 采样步数 | 10 | 8 - 50 | 6 | 15% |
| Prompt 约束强度(CFG) | 1 | 1 - 3 | 6 | 43% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 744，观测区间 512 - 1024，6 个样本
- 高度 中位数 1024，观测区间 512 - 1280，6 个样本
- 采样步数 中位数 10，观测区间 8 - 50，6 个样本，取值分散，一致性仅 15%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3，6 个样本，取值分散，一致性仅 43%
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
