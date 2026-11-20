---
name: unknown_workflow_sampler_clip_unet_146
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.762556
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, KSampler, PrimitiveStringMultiline, ResolutionSelector, SaveImage, TextGenerate, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/MOSS图生图  洗图 一键洗图  2K极速版_2116367495518048258.json, 图片生成/反推提示词/moss全流程工作流+提示词优化+反推_2100824591068385282.json, 图片生成/图生图/KD_MOSS图生图2K极速版!_2115306017172049922.json, 图片生成/图生图/MOSS Image 超级保真4步急速图像生成_2112898230974500865.json, 图片生成/图生图/MOSS Image-to-Image 2K Speed Edition 图生图2K极速版_2113063271686299649.json, 图片生成/图生图/MOSS Image布局控制图像设计Sft+base_2112216902151008257.json, 图片生成/文生图/FLUX 3 Image Klein 文生图_2111461052599857153.json, 图片生成/文生图/MOSS_BBOX 边界框精准布局 文生图工作流_2113954547713527809.json, 图片生成/文生图/Moss Image-布局控制工作流_元素位置精准可控_2113617975470284801.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_146

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/反推提示词/MOSS图生图  洗图 一键洗图  2K极速版_2116367495518048258.json、图片生成/反推提示词/moss全流程工作流+提示词优化+反推_2100824591068385282.json、图片生成/图生图/KD_MOSS图生图2K极速版!_2115306017172049922.json、图片生成/图生图/MOSS Image 超级保真4步急速图像生成_2112898230974500865.json、图片生成/图生图/MOSS Image-to-Image 2K Speed Edition 图生图2K极速版_2113063271686299649.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：76%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `KSampler`
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `SaveImage`
- `TextGenerate`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ComfySwitchNode` —— 6/9 个有
- `LoadImage` —— 6/9 个有
- `LoraLoaderModelOnly` —— 6/9 个有
- `PreviewAny` —— 5/9 个有
- `CreateBoundingBoxes` —— 4/9 个有
- `MOSSImageLayoutPrompt` —— 4/9 个有
- `PrimitiveBoolean` —— 4/9 个有
- `ImageConcatMulti` —— 3/9 个有
- `SkipLayerGuidanceDiTSimple` —— 3/9 个有
- `Label (rgthree)` —— 2/9 个有
- `ImageCompare` —— 1/9 个有
- `PreviewImage` —— 1/9 个有
- `SpectrumMOSSImageAdaptive` —— 1/9 个有
- `easy showAnything` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 16 | 4 - 50 | 9 | 27% |
| Prompt 约束强度(CFG) | 1.5 | 1 - 3 | 9 | 61% |
| 采样算法 | euler | - | 9 | 78% |
| 调度器 | simple | - | 9 | 56% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 16，观测区间 4 - 50，9 个样本，取值分散，一致性仅 27%
- Prompt 约束强度(CFG) 中位数 1.5，观测区间 1 - 3，9 个样本
- 采样算法 最常用 euler，9 个样本，一致性 78%
- 调度器 最常用 simple，9 个样本，一致性 56%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
