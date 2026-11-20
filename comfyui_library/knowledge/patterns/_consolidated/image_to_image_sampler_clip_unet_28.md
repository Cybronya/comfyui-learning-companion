---
name: image_to_image_sampler_clip_unet_28
type: Image To Image
frequency: 11
level: moderate
coverage: 0.852182
common_nodes: [AILab_QwenVL, CLIPLoader, CLIPTextEncode, ConditioningKrea2Rebalance, ImageScaleToTotalPixelsX, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, PrimitiveStringMultiline, SaveImage, Seed (rgthree), StringConcatenate, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy imageColorMatch, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/krea2-时尚模特图-九宫格-1600万像素_2074134570479476737.json, 图片生成/图生图/krea2-时尚模特图-九宫格-1600万像素_2075407890147536897.json, 图片生成/图生图/krea2-时尚模特图-九宫格-1600万像素_2082745915298893825.json, 图片生成/图生图/krea2-时尚模特图-九宫格-1600万像素_2112876051205545985.json, 图片生成/图生图/krea2-时尚模特图-九宫格-1600万像素_2112887380985339906.json, 图片生成/文生图/krea2-九宫格-4K画质_2074126083225636865.json, 图片生成/文生图/krea2-时尚模特图-九宫格-1600万像素_2072853530007916546.json, 图片生成/文生图/krea2-时尚模特图-九宫格-1600万像素_2074294745983184898.json, 图片生成/文生图/krea2-时尚模特图-九宫格-1600万像素_2074653110882099201.json, 图片生成/文生图/krea2-时尚模特图-九宫格-1600万像素_2077198174791491586.json, 图片生成/文生图/krea2-洗图-风格参考-内容修改-高清修复-1600万像素_2071855428270649345.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_28

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/krea2-时尚模特图-九宫格-1600万像素_2074134570479476737.json、图片生成/图生图/krea2-时尚模特图-九宫格-1600万像素_2075407890147536897.json、图片生成/图生图/krea2-时尚模特图-九宫格-1600万像素_2082745915298893825.json、图片生成/图生图/krea2-时尚模特图-九宫格-1600万像素_2112876051205545985.json、图片生成/图生图/krea2-时尚模特图-九宫格-1600万像素_2112887380985339906.json…）

- **类型**：Image To Image
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 11 个 workflow 都包含：
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
- `ImageTile+` —— 10/11 个有
- `PreviewImage` —— 10/11 个有
- `ComfyUI-Krea2T-Enhancer` —— 1/11 个有
- `Krea2StyleSemanticConditioning` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 3 | 3 - 8 | 11 | 51% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 11 | 100% |
| 采样算法 | euler_ancestral | - | 11 | 100% |
| 调度器 | simple | - | 11 | 100% |
| 重绘幅度 | 0.3 | 0.3 - 1 | 11 | 37% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 22/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 3，观测区间 3 - 8，11 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，11 个样本，一致性 100%
- 调度器 最常用 simple，11 个样本，一致性 100%
- 重绘幅度 中位数 0.3，观测区间 0.3 - 1，11 个样本，取值分散，一致性仅 37%
- 高发问题（22/11 个样本）：Steps较低可能导致细节不足
