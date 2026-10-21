---
name: text_to_image_sampler_clip_unet_72
type: Text To Image
frequency: 7
level: moderate
coverage: 0.960429
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen2512反推提示词-出图_2012715450945245186.json, 图片生成/文生图/Qwen2512性感迷人身材美女_2017894712933359617.json, 图片生成/文生图/Qwen2512文生图基础款_2024281731670482946.json, 图片生成/文生图/Qwen2512日系少女甜妹美女_2019045029121101826.json, 图片生成/文生图/Qwen2512梨形完美身材美女_2018952499717218306.json, 图片生成/文生图/Z-Image-Turbo-洗图升级版（每次6张）_1994584620748378114.json, 图片生成/文生图/Z-image-base 反推提示词文生图_2016442671014875137.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_72

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/Qwen2512反推提示词-出图_2012715450945245186.json、图片生成/文生图/Qwen2512性感迷人身材美女_2017894712933359617.json、图片生成/文生图/Qwen2512文生图基础款_2024281731670482946.json、图片生成/文生图/Qwen2512日系少女甜妹美女_2019045029121101826.json、图片生成/文生图/Qwen2512梨形完美身材美女_2018952499717218306.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingAuraFlow` —— 6/7 个有
- `LoraLoaderModelOnly` —— 5/7 个有
- `LoadImage` —— 3/7 个有
- `PreviewAny` —— 3/7 个有
- `AILab_QwenVL` —— 2/7 个有
- `CompressImages` —— 2/7 个有
- `ImageScaleDownToSize` —— 2/7 个有
- `LatentFrequencyEnhancer_lrzjason` —— 1/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/7 个有
- `PreviewImage` —— 1/7 个有
- `RH_Captioner` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 904 | 768 - 1024 | 7 | 88% |
| 高度 | 1024 | 1024 - 1664 | 7 | 79% |
| 采样步数 | 16 | 4 - 35 | 7 | 36% |
| Prompt 约束强度(CFG) | 3 | 1 - 4 | 7 | 49% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 71% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 904，观测区间 768 - 1024，7 个样本，取值集中（一致性 88%）
- 高度 中位数 1024，观测区间 1024 - 1664，7 个样本
- 采样步数 中位数 16，观测区间 4 - 35，7 个样本，取值分散，一致性仅 36%
- Prompt 约束强度(CFG) 中位数 3，观测区间 1 - 4，7 个样本，取值分散，一致性仅 49%
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 71%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
