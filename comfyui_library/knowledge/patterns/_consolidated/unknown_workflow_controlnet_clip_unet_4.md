---
name: unknown_workflow_controlnet_clip_unet_4
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.851
common_nodes: [AILab_QwenVL, AIO_Preprocessor, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptySD3LatentImage, Image Comparer (rgthree), LoadImage, ModelPatchLoader, ModelSamplingAuraFlow, PreviewImage, QwenImageDiffsynthControlnet, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/AIGC人像系列-Z-image-turbo前5步CN控制采样+后5步采样的双采样_2029083151829569537.json, 图片生成/图生图/Z-IMAGE+Controlnet_2004837379913515010.json, 图片生成/图生图/Z-Image文生图高清工作流(无放大)_1996889371469049858.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_clip_unet_4

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/AIGC人像系列-Z-image-turbo前5步CN控制采样+后5步采样的双采样_2029083151829569537.json、图片生成/图生图/Z-IMAGE+Controlnet_2004837379913515010.json、图片生成/图生图/Z-Image文生图高清工作流(无放大)_1996889371469049858.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 3 个 workflow 都包含：
- `AILab_QwenVL`
- `AIO_Preprocessor`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptySD3LatentImage`
- `Image Comparer (rgthree)`
- `LoadImage`
- `ModelPatchLoader`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `QwenImageDiffsynthControlnet`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `KSamplerAdvanced` —— 2/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/3 个有
- `ShowText|pysssss` —— 2/3 个有
- `CR Text` —— 1/3 个有
- `GetImageSize` —— 1/3 个有
- `GetImageSize+` —— 1/3 个有
- `INTConstant` —— 1/3 个有
- `KSampler` —— 1/3 个有
- `PixelPerfectResolution` —— 1/3 个有
- `ShowAnything|Mie` —— 1/3 个有
- `SimpleMath+` —— 1/3 个有
- `easy showAnything` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 3 | 33% |
| Prompt 约束强度(CFG) | 9 | 1 - 12 | 3 | 37% |
| 采样算法 | 1 | - | 2 | 100% |
| 调度器 | euler | - | 3 | 67% |
| 重绘幅度 | simple | - | 3 | 67% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 最常用 fixed，3 个样本，一致性 33%
- Prompt 约束强度(CFG) 中位数 9，观测区间 1 - 12，3 个样本，取值分散，一致性仅 37%
- 采样算法 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，3 个样本，一致性 67%
- 重绘幅度 最常用 simple，3 个样本，一致性 67%
