---
name: unknown_workflow_lora_sampler_clip_118
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.813333
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, GetImageSize, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/1981021439052615681.json, 图片生成/文生图/Qwen2511+Fun+ControlNet+1.0_2080490152702603265.json, 图片生成/文生图/SMB根据线稿出图_2019382085378641922.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_118

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/1981021439052615681.json、图片生成/文生图/Qwen2511+Fun+ControlNet+1.0_2080490152702603265.json、图片生成/文生图/SMB根据线稿出图_2019382085378641922.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `GetImageSize`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AIO_Preprocessor` —— 2/3 个有
- `Image Comparer (rgthree)` —— 2/3 个有
- `ModelPatchLoader` —— 2/3 个有
- `QwenImageDiffsynthControlnet` —— 2/3 个有
- `AILab_QwenVL_Advanced` —— 1/3 个有
- `ConditioningZeroOut` —— 1/3 个有
- `ImageScaleToTotalPixels` —— 1/3 个有
- `LatentUpscaleBy` —— 1/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有
- `LayerUtility: PurgeVRAM` —— 1/3 个有
- `ShowText|pysssss` —— 1/3 个有
- `UltimateSDUpscale` —— 1/3 个有
- `UpscaleModelLoader` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 10 | 3 | 89% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 67% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 1 | 0.2 - 1 | 3 | 49% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 10，3 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 67%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 0.2 - 1，3 个样本，取值分散，一致性仅 49%
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
