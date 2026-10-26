---
name: unknown_workflow_controlnet_sampler_clip_2
type: Unknown Workflow
frequency: 9
level: strong
coverage: 0.898889
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptySD3LatentImage, KSampler, LoadImage, ModelPatchLoader, ModelSamplingAuraFlow, PreviewImage, QwenImageDiffsynthControlnet, SaveImage, UNETLoader, VAELoader]
problems: [Steps较低可能导致细节不足, 发现KSampler但没有VAEDecode]
missing: []
members: [图片生成/反推提示词/无损修复+qwen反推+zimage+controlnet_1996941482785456130.json, 图片生成/图生图/Z-Image-Turbo-最新控制生图-2.1_2004016764516245505.json, 图片生成/图生图/Z-image图生图-canny控制_1998928195103641601.json, 图片生成/图生图/Z-image图生图-depth深度控制_1998934414765776897.json, 图片生成/图生图/Z-image图生图-dw姿态控制_1998936679278895105.json, 图片生成/图生图/Z-image图生图-深度控制-真人转美漫_1998939406658588673.json, 图片生成/图生图/Z-image图生图精准控制版_2064281103275483138.json, 图片生成/图生图/Z-lmage-Turbo-Fun-Controlnet(支持多种条件控制)_1996163380232830977.json, 图片生成/文生图/SMB根据线稿出图_2019382085378641922.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_sampler_clip_2

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/反推提示词/无损修复+qwen反推+zimage+controlnet_1996941482785456130.json、图片生成/图生图/Z-Image-Turbo-最新控制生图-2.1_2004016764516245505.json、图片生成/图生图/Z-image图生图-canny控制_1998928195103641601.json、图片生成/图生图/Z-image图生图-depth深度控制_1998934414765776897.json、图片生成/图生图/Z-image图生图-dw姿态控制_1998936679278895105.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptySD3LatentImage`
- `KSampler`
- `LoadImage`
- `ModelPatchLoader`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `QwenImageDiffsynthControlnet`
- `SaveImage`
- `UNETLoader`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `VAEDecode` —— 8/9 个有
- `AIO_Preprocessor` —— 7/9 个有
- `GetImageSize` —— 7/9 个有
- `ImageScaleToMaxDimension` —— 6/9 个有
- `ImageScaleToTotalPixels` —— 3/9 个有
- `Canny` —— 2/9 个有
- `LayerUtility: PurgeVRAM` —— 2/9 个有
- `AILab_QwenVL` —— 1/9 个有
- `CR Image Input Switch (4 way)` —— 1/9 个有
- `DyPE_FLUX` —— 1/9 个有
- `ImageStitch` —— 1/9 个有
- `ImpactSwitch` —— 1/9 个有
- `JWInteger` —— 1/9 个有
- `LoraLoaderModelOnly` —— 1/9 个有
- `VAEDecodeTiled` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | 8 - 10 | 9 | 94% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | res_multistep | - | 9 | 89% |
| 调度器 | simple | - | 9 | 89% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |
| 发现KSampler但没有VAEDecode | 1/9 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 9，观测区间 8 - 10，9 个样本，取值集中（一致性 94%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_multistep，9 个样本，一致性 89%
- 调度器 最常用 simple，9 个样本，一致性 89%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（8/9 个样本）：Steps较低可能导致细节不足
