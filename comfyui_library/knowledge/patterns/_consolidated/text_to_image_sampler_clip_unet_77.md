---
name: text_to_image_sampler_clip_unet_77
type: Text To Image
frequency: 8
level: moderate
coverage: 0.786875
common_nodes: [CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/CFG Zero出图_1907792965371371522.json, 图片生成/文生图/ERNIE-Image文生图工作流_2077952838453514242.json, 图片生成/文生图/Ernie-Image最强生图模型+全节点注释_2046103239707332609.json, 图片生成/文生图/Ernie-Image最强生图模型_2046063222658174978.json, 图片生成/文生图/Flux.1-Krea-Dev文生图-无AI味逼真质感_1951288817326215170.json, 图片生成/文生图/Krea2 Turbo + Realism Engineer  V3.1 文生图_2072595346835992577.json, 图片生成/文生图/Krea2-Cc-MJ-影视柔光_2094377283531395074.json, 图片生成/文生图/Krea2-二次元模型总控-云端版_2095727543704965121.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_77

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/CFG Zero出图_1907792965371371522.json、图片生成/文生图/ERNIE-Image文生图工作流_2077952838453514242.json、图片生成/文生图/Ernie-Image最强生图模型+全节点注释_2046103239707332609.json、图片生成/文生图/Ernie-Image最强生图模型_2046063222658174978.json、图片生成/文生图/Flux.1-Krea-Dev文生图-无AI味逼真质感_1951288817326215170.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：79%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 6/8 个有
- `PreviewImage` —— 5/8 个有
- `PrimitiveStringMultiline` —— 5/8 个有
- `LoadImage` —— 3/8 个有
- `LoraLoaderModelOnly` —— 3/8 个有
- `DualCLIPLoader` —— 2/8 个有
- `Fast Groups Bypasser (rgthree)` —— 2/8 个有
- `ResolutionSelector` —— 2/8 个有
- `CFGZeroStarAndInit` —— 1/8 个有
- `ImageConcanate` —— 1/8 个有
- `ImageConcatMulti` —— 1/8 个有
- `PrimitiveInt` —— 1/8 个有
- `StringConcatenate` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 768 - 1280 | 8 | 80% |
| 高度 | 1280 | 720 - 1984 | 8 | 72% |
| 采样步数 | 8 | 4 - 20 | 8 | 34% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler | - | 8 | 88% |
| 调度器 | simple | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 768 - 1280，8 个样本
- 高度 中位数 1280，观测区间 720 - 1984，8 个样本
- 采样步数 中位数 8，观测区间 4 - 20，8 个样本，取值分散，一致性仅 34%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 88%
- 调度器 最常用 simple，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（11/8 个样本）：Steps较低可能导致细节不足
