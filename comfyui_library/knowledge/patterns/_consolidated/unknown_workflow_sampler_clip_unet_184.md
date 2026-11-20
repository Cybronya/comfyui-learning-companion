---
name: unknown_workflow_sampler_clip_unet_184
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.725143
common_nodes: [CLIPLoader, CLIPTextEncode, ComfySwitchNode, EmptyFlux2LatentImage, KSampler, PrimitiveStringMultiline, SaveImage, TextGenerate, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/MOSS image 提示增强_反推_风格参考 全能流_2113532439992823810.json, 图片生成/反推提示词/moss全流程工作流+提示词优化+反推_2100824591068385282.json, 图片生成/图生图/FLUX 3 Image Klein 图像编辑_2111121518007767042.json, 图片生成/图生图/Flux3 Image Klein distill t2i加速图生图_2110971174585978882.json, 图片生成/图生图/Flux3 Klein 图生图局部编辑标准版_2113475197054570497.json, 图片生成/图生图/MOSS Image 超级保真4步急速图像生成_2112898230974500865.json, 图片生成/图生图/MOSS Image布局控制图像设计Sft+base_2112216902151008257.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_184

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/反推提示词/MOSS image 提示增强_反推_风格参考 全能流_2113532439992823810.json、图片生成/反推提示词/moss全流程工作流+提示词优化+反推_2100824591068385282.json、图片生成/图生图/FLUX 3 Image Klein 图像编辑_2111121518007767042.json、图片生成/图生图/Flux3 Image Klein distill t2i加速图生图_2110971174585978882.json、图片生成/图生图/Flux3 Klein 图生图局部编辑标准版_2113475197054570497.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：73%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfySwitchNode`
- `EmptyFlux2LatentImage`
- `KSampler`
- `PrimitiveStringMultiline`
- `SaveImage`
- `TextGenerate`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewAny` —— 6/7 个有
- `LoadImage` —— 5/7 个有
- `PrimitiveBoolean` —— 4/7 个有
- `ResolutionSelector` —— 4/7 个有
- `BatchImagesNode` —— 3/7 个有
- `CreateBoundingBoxes` —— 3/7 个有
- `ReferenceMultiLatent` —— 3/7 个有
- `LoraLoaderModelOnly` —— 2/7 个有
- `MOSSImageLayoutPrompt` —— 2/7 个有
- `SkipLayerGuidanceDiTSimple` —— 2/7 个有
- `ConditioningZeroOut` —— 1/7 个有
- `Flux3LayoutPrompt` —— 1/7 个有
- `Image Comparer (rgthree)` —— 1/7 个有
- `ImageCompare` —— 1/7 个有
- `easy showAnything` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 4 - 50 | 7 | 39% |
| Prompt 约束强度(CFG) | 1 | 1 - 3 | 7 | 51% |
| 采样算法 | euler | - | 7 | 71% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 25，观测区间 4 - 50，7 个样本，取值分散，一致性仅 39%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3，7 个样本
- 采样算法 最常用 euler，7 个样本，一致性 71%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
