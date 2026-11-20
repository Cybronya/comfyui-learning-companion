---
name: unknown_workflow_sampler_clip_unet_182
type: Unknown Workflow
frequency: 8
level: weak
coverage: 0.859125
common_nodes: [AIO_Preprocessor, CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, LoadImage, ModelPatchLoader, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Z-image-controlnet 2.1 图生图_2009424173604544514.json, 图片生成/文生图/Z Image Turbo Fun Controlnet Union_2063526631158935554.json, 图片生成/文生图/Z-Image ControlNet 2.1 （六种控制类型）_2015974649129082881.json, 图片生成/文生图/Z-lmage ControlNet V2.1 控制洗图工作流【官方版】_2082708775894609922.json, 图片生成/文生图/【阡陌】Z-Image+controlnet 2.1 自动反推提示词洗图工作流_2003449912257880066.json, 图片生成/文生图/【阡陌】Z-Image+controlnet自动反推提示词洗图工作流_1999304671166689282.json, 平台全量/节点系列29-AIO Aux Preprocessor  ALL-IN-ONE ControlNet 预处理节点_2045017406803808257.json, 平台全量/节点系列31-KSampler (Advanced)高级采样器节点_2044679581315108866.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_182

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/Z-image-controlnet 2.1 图生图_2009424173604544514.json、图片生成/文生图/Z Image Turbo Fun Controlnet Union_2063526631158935554.json、图片生成/文生图/Z-Image ControlNet 2.1 （六种控制类型）_2015974649129082881.json、图片生成/文生图/Z-lmage ControlNet V2.1 控制洗图工作流【官方版】_2082708775894609922.json、图片生成/文生图/【阡陌】Z-Image+controlnet 2.1 自动反推提示词洗图工作流_2003449912257880066.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：86%

## 共有节点

全部 8 个 workflow 都包含：
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
- `ConditioningZeroOut` —— 7/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 7/8 个有
- `PreviewImage` —— 7/8 个有
- `QwenImageDiffsynthControlnet` —— 6/8 个有
- `GetImageSize` —— 4/8 个有
- `Image Comparer (rgthree)` —— 4/8 个有
- `QwenVisionNode` —— 3/8 个有
- `easy conditioningIndexSwitch` —— 3/8 个有
- `easy showAnything` —— 3/8 个有
- `Seed (rgthree)` —— 2/8 个有
- `ZImageFunControlnet` —— 2/8 个有
- `Fast Groups Bypasser (rgthree)` —— 1/8 个有
- `INTConstant` —— 1/8 个有
- `KSamplerAdvanced` —— 1/8 个有
- `SimpleMath+` —— 1/8 个有
- `Text` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | 8 - 15 | 7 | 78% |
| Prompt 约束强度(CFG) | 1 | 1 - 10 | 8 | 0% |
| 采样算法 | euler | - | 8 | 50% |
| 调度器 | simple | - | 8 | 88% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，观测区间 8 - 15，7 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 10，8 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 euler，8 个样本，一致性 50%
- 调度器 最常用 simple，8 个样本，一致性 88%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（9/8 个样本）：Steps较低可能导致细节不足
