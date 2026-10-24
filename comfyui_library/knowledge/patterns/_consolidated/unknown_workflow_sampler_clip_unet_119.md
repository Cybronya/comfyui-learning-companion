---
name: unknown_workflow_sampler_clip_unet_119
type: Unknown Workflow
frequency: 9
level: weak
coverage: 0.725333
common_nodes: [BatchImagesNode, CLIPLoader, CLIPTextEncode, KSampler, LoadImage, PrimitiveStringMultiline, ReferenceMultiLatent, SaveImage, TextGenerate, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/FLUX 3 Image Klein 图像编辑_2111121518007767042.json, 图片生成/图生图/Flux3 Image Klein distill t2i加速图生图_2110971174585978882.json, 图片生成/图生图/Flux3-klein指定位置修改_2111273557820006402.json, 图片生成/图生图/Flux3-klein普通图像编辑PUP增强_2111479605000499202.json, 图片生成/图生图/Flux3_klein_图像编辑_2111983712979210242.json, 图片生成/图生图/flux3_image_klein多图编辑_2111134357867028482.json, 图片生成/图生图/flux3_klein图片编辑_2112072362408628226.json, 图片生成/图生图/图像编辑 FLUX 3 Image Klein（官方版）_2112793727075971074.json, 图片生成/文生图/Flux3_Klein 生图及编辑_2111988620776263681.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_119

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/FLUX 3 Image Klein 图像编辑_2111121518007767042.json、图片生成/图生图/Flux3 Image Klein distill t2i加速图生图_2110971174585978882.json、图片生成/图生图/Flux3-klein指定位置修改_2111273557820006402.json、图片生成/图生图/Flux3-klein普通图像编辑PUP增强_2111479605000499202.json、图片生成/图生图/Flux3_klein_图像编辑_2111983712979210242.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：73%

## 共有节点

全部 9 个 workflow 都包含：
- `BatchImagesNode`
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `LoadImage`
- `PrimitiveStringMultiline`
- `ReferenceMultiLatent`
- `SaveImage`
- `TextGenerate`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewAny` —— 8/9 个有
- `EmptyFlux2LatentImage` —— 7/9 个有
- `ComfySwitchNode` —— 6/9 个有
- `ConditioningZeroOut` —— 4/9 个有
- `Image Comparer (rgthree)` —— 3/9 个有
- `PreviewImage` —— 3/9 个有
- `Ideogram4PromptBuilderKJ` —— 2/9 个有
- `ResolutionSelector` —— 2/9 个有
- `Text` —— 2/9 个有
- `Fast Groups Bypasser (rgthree)` —— 1/9 个有
- `ImagePadKJ` —— 1/9 个有
- `Label (rgthree)` —— 1/9 个有
- `LoraLoaderModelOnly` —— 1/9 个有
- `PrimitiveBoolean` —— 1/9 个有
- `RegexReplace` —— 1/9 个有
- `ShowText|fofo` —— 1/9 个有
- `StringConcatenate` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 16 | 16 - 50 | 9 | 40% |
| Prompt 约束强度(CFG) | 1 | 1 - 3.5 | 9 | 39% |
| 采样算法 | euler | - | 9 | 100% |
| 调度器 | simple | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 16，观测区间 16 - 50，9 个样本，取值分散，一致性仅 40%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3.5，9 个样本，取值分散，一致性仅 39%
- 采样算法 最常用 euler，9 个样本，一致性 100%
- 调度器 最常用 simple，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
