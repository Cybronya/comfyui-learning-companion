---
name: image_to_image_sampler_clip_vae_4
type: Image To Image
frequency: 3
level: weak
coverage: 0.913667
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LoadImage, PreviewImage, SaveImage, VAEDecode, VAEEncode, VAELoader, image_scale_pixel_v2]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Anima Aesthetic 1.1｜图生图_2078374866838974465.json, 图片生成/文生图/Anima图生图_2021929700087566337.json, 图片生成/文生图/KSK Krea2｜原图重绘风格变身_2072199218311286785.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_vae_4

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Anima Aesthetic 1.1｜图生图_2078374866838974465.json、图片生成/文生图/Anima图生图_2021929700087566337.json、图片生成/文生图/KSK Krea2｜原图重绘风格变身_2072199218311286785.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `image_scale_pixel_v2`

**可变部分**（部分 workflow 才有）：
- `Qwen3VLProcessor` —— 2/3 个有
- `UNETLoader` —— 2/3 个有
- `ClownsharKSampler_Beta` —— 1/3 个有
- `ConditioningKrea2Rebalance` —— 1/3 个有
- `ConditioningZeroOut` —— 1/3 个有
- `EnhancedLoadDiffusionModel` —— 1/3 个有
- `LoraLoaderModelOnly` —— 1/3 个有
- `XB_UNetNameBroadcaster` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 19.5 | - | 2 | 41% |
| Prompt 约束强度(CFG) | 4 | 1 - 31 | 3 | 0% |
| 采样算法 | -1 | - | 3 | 33% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 0.7 | 0.5 - 4 | 3 | 7% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 19.5，样本不足，未给区间，2 个样本，取值分散，一致性仅 41%
- Prompt 约束强度(CFG) 中位数 4，观测区间 1 - 31，3 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 -1，3 个样本，一致性 33%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 0.7，观测区间 0.5 - 4，3 个样本，取值分散，一致性仅 7%
- 风险：Prompt 约束强度(CFG) 观测到 31，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
- 风险：重绘幅度 观测到 4，超出安全上限 1（denoise 接近 1.0 时接近重新生成，初始潜空间影响被抹平）
