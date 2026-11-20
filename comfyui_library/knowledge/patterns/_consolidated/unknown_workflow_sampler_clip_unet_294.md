---
name: unknown_workflow_sampler_clip_unet_294
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.7198
common_nodes: [BatchImagesNode, CLIPLoader, CLIPTextEncode, KSampler, LoadImage, PreviewAny, PrimitiveStringMultiline, ReferenceMultiLatent, SaveImage, TextGenerate, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Flux3-klein指定位置修改_2111273557820006402.json, 图片生成/图生图/Flux3-klein普通图像编辑PUP增强_2111479605000499202.json, 图片生成/图生图/Flux3_Klein_生图及编辑_2116700359514218497.json, 图片生成/文生图/Flux3_Klein 生图及编辑_2111988620776263681.json, 视频生成/图生视频/Flux3_Klein_生图及编辑_2116663657978482690.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_294

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Flux3-klein指定位置修改_2111273557820006402.json、图片生成/图生图/Flux3-klein普通图像编辑PUP增强_2111479605000499202.json、图片生成/图生图/Flux3_Klein_生图及编辑_2116700359514218497.json、图片生成/文生图/Flux3_Klein 生图及编辑_2111988620776263681.json、视频生成/图生视频/Flux3_Klein_生图及编辑_2116663657978482690.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：72%

## 共有节点

全部 5 个 workflow 都包含：
- `BatchImagesNode`
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `LoadImage`
- `PreviewAny`
- `PrimitiveStringMultiline`
- `ReferenceMultiLatent`
- `SaveImage`
- `TextGenerate`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ComfySwitchNode` —— 4/5 个有
- `EmptyFlux2LatentImage` —— 4/5 个有
- `Ideogram4PromptBuilderKJ` —— 4/5 个有
- `PreviewImage` —— 4/5 个有
- `ConditioningZeroOut` —— 3/5 个有
- `Image Comparer (rgthree)` —— 3/5 个有
- `ImagePadKJ` —— 3/5 个有
- `Label (rgthree)` —— 3/5 个有
- `LoraLoaderModelOnly` —— 3/5 个有
- `RegexReplace` —— 3/5 个有
- `ResolutionSelector` —— 3/5 个有
- `ShowText|fofo` —— 3/5 个有
- `StringConcatenate` —— 3/5 个有
- `Text` —— 3/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 16 | 16 - 16 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 16，观测区间 16 - 16，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（3/5 个样本）：Steps较低可能导致细节不足
