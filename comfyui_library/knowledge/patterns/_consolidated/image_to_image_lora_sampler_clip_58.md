---
name: image_to_image_lora_sampler_clip_58
type: Image To Image
frequency: 5
level: moderate
coverage: 0.9028
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/WAN2.1洗图_1947171235845562370.json, 图片生成/图生图/Wan2.1图像高清修复终结者_1899402301684236290.json, 图片生成/图生图/Wan2.1降维打击：你的视觉内容终极利器！强力细节提升、画质增强、画面修复、细节增强_1945633552090451969.json, 图片生成/图生图/Wan2.2  图生图_1952005600597233666.json, 图片生成/图生图/Wan降维打击：智能洗稿洗图，内容创作新范式！一键洗图终极利器~_洗图_洗稿_仿图_图生图_1948924219665653761.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_58

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/WAN2.1洗图_1947171235845562370.json、图片生成/图生图/Wan2.1图像高清修复终结者_1899402301684236290.json、图片生成/图生图/Wan2.1降维打击：你的视觉内容终极利器！强力细节提升、画质增强、画面修复、细节增强_1945633552090451969.json、图片生成/图生图/Wan2.2  图生图_1952005600597233666.json、图片生成/图生图/Wan降维打击：智能洗稿洗图，内容创作新范式！一键洗图终极利器~_洗图_洗稿_仿图_图生图_1948924219665653761.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageUpscaleWithModel` —— 4/5 个有
- `LayerUtility: ImageScaleRestore V2` —— 4/5 个有
- `RH_Captioner` —— 4/5 个有
- `UpscaleModelLoader` —— 4/5 个有
- `Image Comparer (rgthree)` —— 3/5 个有
- `PathchSageAttentionKJ` —— 2/5 个有
- `easy showAnything` —— 2/5 个有
- `ConstrainImage|pysssss` —— 1/5 个有
- `FastFilmGrain` —— 1/5 个有
- `ModelSamplingSD3` —— 1/5 个有
- `Seed_` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 10 - 10 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | uni_pc | - | 5 | 80% |
| 调度器 | simple | - | 5 | 60% |
| 重绘幅度 | 0.2 | 0.1 - 0.5 | 5 | 46% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 10，观测区间 10 - 10，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 uni_pc，5 个样本，一致性 80%
- 调度器 最常用 simple，5 个样本，一致性 60%
- 重绘幅度 中位数 0.2，观测区间 0.1 - 0.5，5 个样本，取值分散，一致性仅 46%
