---
name: unknown_workflow_sampler_clip_unet_85
type: Unknown Workflow
frequency: 13
level: moderate
coverage: 0.738077
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, KSampler, PrimitiveStringMultiline, SaveImage, TextGenerate, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/(贞贞Lora)Ernie Turbo文生图自动提示词优化极速版V1_2045747492465156097.json, 图片生成/文生图/Ernie文生图自动提示词优化满血版V1_2044590595057917954.json, 图片生成/文生图/Ernie文生图自动提示词优化满血版V1_2046103550576562177.json, 图片生成/文生图/Flux3 Image Klein distill t2i加速文生图_2110971162019848193.json, 图片生成/文生图/Flux3-Klein Text-to-Image 文生图工作流_2110954206533341186.json, 图片生成/文生图/HS-image_ernie_image_2044628228756742146.json, 图片生成/文生图/Moss-image Base Fixed文生图_2112185356295688193.json, 图片生成/文生图/Moss-image Base文生图_2112066738195091457.json, 图片生成/文生图/Moss-image Base文生图_2112122177809108994.json, 图片生成/文生图/Moss-image Base文生图_2112140955116728321.json, 图片生成/文生图/Moss-image Sft Fixed文生图_2112185347613487105.json, 图片生成/文生图/Moss-image Sft文生图_2112060921463001089.json, 图片生成/文生图/flux3 t2v 蒸馏版本_2111318527201341441.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_85

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/文生图/(贞贞Lora)Ernie Turbo文生图自动提示词优化极速版V1_2045747492465156097.json、图片生成/文生图/Ernie文生图自动提示词优化满血版V1_2044590595057917954.json、图片生成/文生图/Ernie文生图自动提示词优化满血版V1_2046103550576562177.json、图片生成/文生图/Flux3 Image Klein distill t2i加速文生图_2110971162019848193.json、图片生成/文生图/Flux3-Klein Text-to-Image 文生图工作流_2110954206533341186.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：74%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `KSampler`
- `PrimitiveStringMultiline`
- `SaveImage`
- `TextGenerate`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ComfySwitchNode` —— 12/13 个有
- `PreviewAny` —— 12/13 个有
- `PrimitiveBoolean` —— 9/13 个有
- `ResolutionSelector` —— 8/13 个有
- `StringReplace` —— 4/13 个有
- `Ideogram4PromptBuilderKJ` —— 2/13 个有
- `CR Prompt Text` —— 1/13 个有
- `ConcatTextOfUtils` —— 1/13 个有
- `JjkText` —— 1/13 个有
- `LoraLoaderModelOnly` —— 1/13 个有
- `easy showAnything` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 8 - 50 | 13 | 52% |
| Prompt 约束强度(CFG) | 3 | 1 - 4 | 13 | 56% |
| 采样算法 | er_sde | - | 13 | 62% |
| 调度器 | simple | - | 13 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 25，观测区间 8 - 50，13 个样本
- Prompt 约束强度(CFG) 中位数 3，观测区间 1 - 4，13 个样本
- 采样算法 最常用 er_sde，13 个样本，一致性 62%
- 调度器 最常用 simple，13 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
