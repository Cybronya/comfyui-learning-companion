---
name: unknown_workflow_clip_unet_vae_10
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.83875
common_nodes: [AIO_Preprocessor, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptySD3LatentImage, LoadImage, ModelPatchLoader, ModelSamplingAuraFlow, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/z-image-深度图_1996814449833123841.json, 图片生成/文生图/【阡陌】Z-Image+controlnet 2.1 自动反推提示词洗图工作流_2003449912257880066.json, 图片生成/文生图/【阡陌】Z-Image+controlnet自动反推提示词洗图工作流_1999304671166689282.json, 图片生成/文生图/节点系列11-图像拼接Image Stitch节点_2012816521986314241.json]
source: knowledge_consolidation
---

# unknown_workflow_clip_unet_vae_10

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/z-image-深度图_1996814449833123841.json、图片生成/文生图/【阡陌】Z-Image+controlnet 2.1 自动反推提示词洗图工作流_2003449912257880066.json、图片生成/文生图/【阡陌】Z-Image+controlnet自动反推提示词洗图工作流_1999304671166689282.json、图片生成/文生图/节点系列11-图像拼接Image Stitch节点_2012816521986314241.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 4 个 workflow 都包含：
- `AIO_Preprocessor`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptySD3LatentImage`
- `LoadImage`
- `ModelPatchLoader`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `GetImageSize` —— 3/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/4 个有
- `QwenImageDiffsynthControlnet` —— 3/4 个有
- `KSampler` —— 2/4 个有
- `KSamplerAdvanced` —— 2/4 个有
- `QwenVisionNode` —— 2/4 个有
- `easy conditioningIndexSwitch` —— 2/4 个有
- `easy showAnything` —— 2/4 个有
- `DJZImageScaleToTotalPixels` —— 1/4 个有
- `INTConstant` —— 1/4 个有
- `ImageStitch` —— 1/4 个有
- `SimpleMath+` —— 1/4 个有
- `ZImageFunControlnet` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 10 | 4 | 19% |
| 采样算法 | 1 | - | 2 | 100% |
| 调度器 | euler | - | 4 | 50% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 10，4 个样本，取值分散，一致性仅 19%
- 采样算法 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，4 个样本，一致性 50%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/4 个样本）：Steps较低可能导致细节不足
