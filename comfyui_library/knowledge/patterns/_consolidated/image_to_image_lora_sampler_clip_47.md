---
name: image_to_image_lora_sampler_clip_47
type: Image To Image
frequency: 6
level: moderate
coverage: 0.902333
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/WAN2.1洗图_1947171235845562370.json, 图片生成/图生图/Wan2.1图像高清修复终结者_1899402301684236290.json, 图片生成/图生图/Wan2.1降维打击：你的视觉内容终极利器！强力细节提升、画质增强、画面修复、细节增强_1945633552090451969.json, 图片生成/图生图/Wan2.2  图生图_1952005600597233666.json, 图片生成/图生图/Wan降维打击：智能洗稿洗图，内容创作新范式！一键洗图终极利器~_洗图_洗稿_仿图_图生图_1948924219665653761.json, 数字人/数字人/高清修复_1991726670811967489.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_47

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/WAN2.1洗图_1947171235845562370.json、图片生成/图生图/Wan2.1图像高清修复终结者_1899402301684236290.json、图片生成/图生图/Wan2.1降维打击：你的视觉内容终极利器！强力细节提升、画质增强、画面修复、细节增强_1945633552090451969.json、图片生成/图生图/Wan2.2  图生图_1952005600597233666.json、图片生成/图生图/Wan降维打击：智能洗稿洗图，内容创作新范式！一键洗图终极利器~_洗图_洗稿_仿图_图生图_1948924219665653761.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 6 个 workflow 都包含：
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
- `ImageUpscaleWithModel` —— 5/6 个有
- `LayerUtility: ImageScaleRestore V2` —— 5/6 个有
- `RH_Captioner` —— 5/6 个有
- `UpscaleModelLoader` —— 5/6 个有
- `Image Comparer (rgthree)` —— 4/6 个有
- `PathchSageAttentionKJ` —— 2/6 个有
- `easy showAnything` —— 2/6 个有
- `CR Text Concatenate` —— 1/6 个有
- `ConstrainImage|pysssss` —— 1/6 个有
- `FastFilmGrain` —— 1/6 个有
- `ModelSamplingSD3` —— 1/6 个有
- `PrimitiveString` —— 1/6 个有
- `Seed_` —— 1/6 个有
- `ShowText` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 10 - 10 | 6 | 100% |
| Prompt 约束强度(CFG) | 1 | 0.4 - 1 | 6 | 75% |
| 采样算法 | uni_pc | - | 6 | 83% |
| 调度器 | simple | - | 6 | 67% |
| 重绘幅度 | 0.19 | 0.08 - 0.5 | 6 | 37% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 10，观测区间 10 - 10，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 0.4 - 1，6 个样本
- 采样算法 最常用 uni_pc，6 个样本，一致性 83%
- 调度器 最常用 simple，6 个样本，一致性 67%
- 重绘幅度 中位数 0.19，观测区间 0.08 - 0.5，6 个样本，取值分散，一致性仅 37%
- 风险：Prompt 约束强度(CFG) 观测到 0.4，低于常用下限 1（CFG 过低可能导致 Prompt 约束不足、结果偏离描述）
- 风险：重绘幅度 观测到 0.08，低于常用下限 0.1（）
