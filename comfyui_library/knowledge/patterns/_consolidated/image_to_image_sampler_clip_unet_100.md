---
name: image_to_image_sampler_clip_unet_100
type: Image To Image
frequency: 5
level: strong
coverage: 0.7934
common_nodes: [CLIPLoader, CLIPLoaderGGUF, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, KSampler, LoadImage, ReferenceLatent, SaveImage, UNETLoader, UnetLoaderGGUF, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/flux2-klen三图编辑_2040333512275927041.json, 图片生成/图生图/▶flux-2-klein-单-多图编辑_2035882063211008001.json, 图片生成/图生图/▶flux-2-klein-单-多图编辑_2082029601458573314.json, 图片生成/图生图/▶klein-动漫转真人流_2058927929484206081.json, 图片生成/文生图/B妮B妳_Flux2-klein_N_S_F_W_汇总_2019356802848137218.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_100

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/flux2-klen三图编辑_2040333512275927041.json、图片生成/图生图/▶flux-2-klein-单-多图编辑_2035882063211008001.json、图片生成/图生图/▶flux-2-klein-单-多图编辑_2082029601458573314.json、图片生成/图生图/▶klein-动漫转真人流_2058927929484206081.json、图片生成/文生图/B妮B妳_Flux2-klein_N_S_F_W_汇总_2019356802848137218.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：79%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPLoaderGGUF`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `KSampler`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `UnetLoaderGGUF`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `ImageScaleToTotalPixels` —— 4/5 个有
- `LoraLoaderModelOnly` —— 4/5 个有
- `Fast Groups Bypasser (rgthree)` —— 3/5 个有
- `EasySizeSimpleImage` —— 2/5 个有
- `Image Comparer (rgthree)` —— 2/5 个有
- `ImageResizeKJv2` —— 2/5 个有
- `HAIGC_SaveImagesToZip` —— 1/5 个有
- `If ANY execute A else B` —— 1/5 个有
- `Int` —— 1/5 个有
- `Mute / Bypass Repeater (rgthree)` —— 1/5 个有
- `PreviewBridge` —— 1/5 个有
- `easy boolean` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 6 - 6 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 6 - 6，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（6/5 个样本）：Steps较低可能导致细节不足
