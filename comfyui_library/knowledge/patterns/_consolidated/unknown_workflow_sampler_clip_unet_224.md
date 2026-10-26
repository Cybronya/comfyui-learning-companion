---
name: unknown_workflow_sampler_clip_unet_224
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.8935
common_nodes: [AIO_Preprocessor, CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, LoadImage, ModelPatchLoader, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Z-image-controlnet 2.1 图生图_2009424173604544514.json, 图片生成/文生图/Z Image Turbo Fun Controlnet Union_2063526631158935554.json, 图片生成/文生图/Z-Image ControlNet 2.1 （六种控制类型）_2015974649129082881.json, 图片生成/文生图/Z-lmage ControlNet V2.1 控制洗图工作流【官方版】_2082708775894609922.json, 图片生成/文生图/【阡陌】Z-Image+controlnet 2.1 自动反推提示词洗图工作流_2003449912257880066.json, 图片生成/文生图/【阡陌】Z-Image+controlnet自动反推提示词洗图工作流_1999304671166689282.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_224

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Z-image-controlnet 2.1 图生图_2009424173604544514.json、图片生成/文生图/Z Image Turbo Fun Controlnet Union_2063526631158935554.json、图片生成/文生图/Z-Image ControlNet 2.1 （六种控制类型）_2015974649129082881.json、图片生成/文生图/Z-lmage ControlNet V2.1 控制洗图工作流【官方版】_2082708775894609922.json、图片生成/文生图/【阡陌】Z-Image+controlnet 2.1 自动反推提示词洗图工作流_2003449912257880066.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 6 个 workflow 都包含：
- `AIO_Preprocessor`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `LoadImage`
- `ModelPatchLoader`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 5/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/6 个有
- `PreviewImage` —— 5/6 个有
- `GetImageSize` —— 4/6 个有
- `QwenImageDiffsynthControlnet` —— 4/6 个有
- `QwenVisionNode` —— 3/6 个有
- `easy conditioningIndexSwitch` —— 3/6 个有
- `easy showAnything` —— 3/6 个有
- `Image Comparer (rgthree)` —— 2/6 个有
- `ZImageFunControlnet` —— 2/6 个有
- `Text` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | 9 - 15 | 6 | 78% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 67% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，观测区间 9 - 15，6 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 67%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（4/6 个样本）：Steps较低可能导致细节不足
