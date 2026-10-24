---
name: unknown_workflow_sampler_clip_unet_246
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.8966
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, LoadImage, ModelPatchLoader, ModelSamplingAuraFlow, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Z openpose工作流_1996536118701072385.json, 图片生成/图生图/Z-Image ControlNet 2.1 （六种控制类型）_2020890700463742978.json, 图片生成/图生图/Z-Image+CN+Qwen3反推洗图工作流_1996919521036406786.json, 图片生成/图生图/Z-Image+CN2.0洗图神器_2000462790190133250.json, 图片生成/图生图/Z-Image+CN2.1All In One_2003517827271303169.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_246

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Z openpose工作流_1996536118701072385.json、图片生成/图生图/Z-Image ControlNet 2.1 （六种控制类型）_2020890700463742978.json、图片生成/图生图/Z-Image+CN+Qwen3反推洗图工作流_1996919521036406786.json、图片生成/图生图/Z-Image+CN2.0洗图神器_2000462790190133250.json、图片生成/图生图/Z-Image+CN2.1All In One_2003517827271303169.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `LoadImage`
- `ModelPatchLoader`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AIO_Preprocessor` —— 4/5 个有
- `ConditioningZeroOut` —— 4/5 个有
- `QwenImageDiffsynthControlnet` —— 4/5 个有
- `AILab_QwenVL` —— 3/5 个有
- `PixelPerfectResolution` —— 3/5 个有
- `Canny` —— 2/5 个有
- `GetImageSize` —— 2/5 个有
- `ImageConcatMulti` —— 2/5 个有
- `Label (rgthree)` —— 2/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/5 个有
- `ShowText|pysssss` —— 2/5 个有
- `GetImageSize+` —— 1/5 个有
- `ImageSharpen` —— 1/5 个有
- `ImpactSwitch` —— 1/5 个有
- `OpenposePreprocessor` —— 1/5 个有
- `PreviewAny` —— 1/5 个有
- `ZImageFunControlnet` —— 1/5 个有
- `easy cleanGpuUsed` —— 1/5 个有
- `easy showAnything` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | 9 - 9 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | res_multistep | - | 5 | 40% |
| 调度器 | simple | - | 5 | 60% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，观测区间 9 - 9，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_multistep，5 个样本，一致性 40%
- 调度器 最常用 simple，5 个样本，一致性 60%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（7/5 个样本）：Steps较低可能导致细节不足
