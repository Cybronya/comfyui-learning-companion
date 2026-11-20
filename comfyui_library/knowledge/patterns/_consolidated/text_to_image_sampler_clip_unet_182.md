---
name: text_to_image_sampler_clip_unet_182
type: Text To Image
frequency: 3
level: weak
coverage: 0.905333
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, Image Comparer (rgthree), KSampler, ResizeImageMaskNode, SaveImage, SeedVR2Conditioning, SeedVR2PostProcessing, SeedVR2Preprocess, UNETLoader, VAEDecode, VAEDecodeTiled, VAEEncodeTiled, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/无损放大细节还原｜图生图画质增强实用利器_2096905289114144770.json, 图片生成/文生图/Krea2快速单采文生图 电影胶片质感图像生成工具_2113423431525027841.json, 图片生成/文生图/krea2文生图，任意风格参考，洗图工作流，三采高清，极致画质_2092791742360809474.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_182

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/无损放大细节还原｜图生图画质增强实用利器_2096905289114144770.json、图片生成/文生图/Krea2快速单采文生图 电影胶片质感图像生成工具_2113423431525027841.json、图片生成/文生图/krea2文生图，任意风格参考，洗图工作流，三采高清，极致画质_2092791742360809474.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `Image Comparer (rgthree)`
- `KSampler`
- `ResizeImageMaskNode`
- `SaveImage`
- `SeedVR2Conditioning`
- `SeedVR2PostProcessing`
- `SeedVR2Preprocess`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncodeTiled`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 2/3 个有
- `ImageScaleToTotalPixels` —— 2/3 个有
- `JjkText` —— 2/3 个有
- `LoraLoaderModelOnly` —— 2/3 个有
- `PreviewAny` —— 2/3 个有
- `WenWuKrea2PromptInstruct` —— 2/3 个有
- `easy cleanGpuUsed` —— 2/3 个有
- `llama_cpp_model_loader` —— 2/3 个有
- `solarL_SaveImagesToZip` —— 2/3 个有
- `孤海注释` —— 2/3 个有
- `INTConstant` —— 1/3 个有
- `JoinImageWithAlpha` —— 1/3 个有
- `KSamplerAdvanced` —— 1/3 个有
- `LayerUtility: PurgeVRAM V2` —— 1/3 个有
- `LoadImage` —— 1/3 个有
- `ModelSamplingAuraFlow` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `ttN int` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 12 | 3 | 49% |
| 采样算法 | er_sde | - | 3 | 67% |
| 调度器 | beta | - | 3 | 67% |
| 重绘幅度 | 1 | - | 2 | 100% |
| 宽度 | 80 | 80 - 1024 | 3 | 0% |
| 高度 | 80 | 80 - 1536 | 3 | 0% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 12，3 个样本，取值分散，一致性仅 49%
- 采样算法 最常用 er_sde，3 个样本，一致性 67%
- 调度器 最常用 beta，3 个样本，一致性 67%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 1024，3 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 1536，3 个样本，取值分散，一致性仅 0%
- 高发问题（5/3 个样本）：Steps较低可能导致细节不足
