---
name: image_to_image_sampler_clip_unet_2
type: Image To Image
frequency: 6
level: moderate
coverage: 0.853
common_nodes: [AILab_QwenVL, CLIPLoader, CLIPTextEncode, ConditioningKrea2Rebalance, ImageScaleToTotalPixelsX, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, PrimitiveStringMultiline, SaveImage, Seed (rgthree), StringConcatenate, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy imageColorMatch, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/krea2-九宫格-4K画质_2074126083225636865.json, 图片生成/文生图/krea2-时尚模特图-九宫格-1600万像素_2072853530007916546.json, 图片生成/文生图/krea2-时尚模特图-九宫格-1600万像素_2074294745983184898.json, 图片生成/文生图/krea2-时尚模特图-九宫格-1600万像素_2074653110882099201.json, 图片生成/文生图/krea2-时尚模特图-九宫格-1600万像素_2077198174791491586.json, 图片生成/文生图/krea2-洗图-风格参考-内容修改-高清修复-1600万像素_2071855428270649345.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_2

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/krea2-九宫格-4K画质_2074126083225636865.json、图片生成/文生图/krea2-时尚模特图-九宫格-1600万像素_2072853530007916546.json、图片生成/文生图/krea2-时尚模特图-九宫格-1600万像素_2074294745983184898.json、图片生成/文生图/krea2-时尚模特图-九宫格-1600万像素_2074653110882099201.json、图片生成/文生图/krea2-时尚模特图-九宫格-1600万像素_2077198174791491586.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 6 个 workflow 都包含：
- `AILab_QwenVL`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningKrea2Rebalance`
- `ImageScaleToTotalPixelsX`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `PrimitiveStringMultiline`
- `SaveImage`
- `Seed (rgthree)`
- `StringConcatenate`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy imageColorMatch`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `ImageTile+` —— 5/6 个有
- `PreviewImage` —— 5/6 个有
- `ComfyUI-Krea2T-Enhancer` —— 1/6 个有
- `Krea2StyleSemanticConditioning` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 3 | 3 - 8 | 6 | 49% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler_ancestral | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 0.3 | 0.3 - 1 | 6 | 38% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 12/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 3，观测区间 3 - 8，6 个样本，取值分散，一致性仅 49%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 0.3，观测区间 0.3 - 1，6 个样本，取值分散，一致性仅 38%
- 高发问题（12/6 个样本）：Steps较低可能导致细节不足
