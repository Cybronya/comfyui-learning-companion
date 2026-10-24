---
name: unknown_workflow_controlnet_clip_unet_2
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.902667
common_nodes: [AIO_Preprocessor, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptySD3LatentImage, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, ModelPatchLoader, ModelSamplingAuraFlow, QwenImageDiffsynthControlnet, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/工作流基础系列5-Z-Image-Turbo+CN控制工作流-基础向讲解此工作流_2012487271336906754.json, 图片生成/图生图/工作流基础系列6-Z-Image-Turbo+CN控制工作流+双采样工作流-基础向讲解此工作流_2044661677328703490.json, 图片生成/图生图/组件系列7-Z-image-turbo双采样洗图_2058751468982849537.json, 图片生成/文生图/Z-Image ControlNet 2.1 （六种控制类型）_2015974649129082881.json, 图片生成/文生图/Z-lmage ControlNet V2.1 控制洗图工作流【官方版】_2082708775894609922.json, 图片生成/文生图/ZIT+CN+base双采样_2056090416516222978.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_clip_unet_2

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/工作流基础系列5-Z-Image-Turbo+CN控制工作流-基础向讲解此工作流_2012487271336906754.json、图片生成/图生图/工作流基础系列6-Z-Image-Turbo+CN控制工作流+双采样工作流-基础向讲解此工作流_2044661677328703490.json、图片生成/图生图/组件系列7-Z-image-turbo双采样洗图_2058751468982849537.json、图片生成/文生图/Z-Image ControlNet 2.1 （六种控制类型）_2015974649129082881.json、图片生成/文生图/Z-lmage ControlNet V2.1 控制洗图工作流【官方版】_2082708775894609922.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 6 个 workflow 都包含：
- `AIO_Preprocessor`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptySD3LatentImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `ModelPatchLoader`
- `ModelSamplingAuraFlow`
- `QwenImageDiffsynthControlnet`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 5/6 个有
- `Seed (rgthree)` —— 4/6 个有
- `INTConstant` —— 3/6 个有
- `KSampler` —— 3/6 个有
- `KSamplerAdvanced` —— 3/6 个有
- `Image Comparer (rgthree)` —— 2/6 个有
- `SimpleMath+` —— 2/6 个有
- `Anything Everywhere` —— 1/6 个有
- `ControlNetApplyAdvanced` —— 1/6 个有
- `ControlNetLoader` —— 1/6 个有
- `LatentFrequencyEnhancer_lrzjason` —— 1/6 个有
- `LoraLoaderModelOnly` —— 1/6 个有
- `SeargeIntegerMath` —— 1/6 个有
- `ttN text` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 8 - 15 | 3 | 73% |
| Prompt 约束强度(CFG) | 5.5 | 1 - 10 | 6 | 18% |
| 采样算法 | 1 | 1 - 1 | 3 | 100% |
| 调度器 | simple | - | 6 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| ControlNet 权重 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 8 - 15，3 个样本
- Prompt 约束强度(CFG) 中位数 5.5，观测区间 1 - 10，6 个样本，取值分散，一致性仅 18%
- 采样算法 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 调度器 最常用 simple，6 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
