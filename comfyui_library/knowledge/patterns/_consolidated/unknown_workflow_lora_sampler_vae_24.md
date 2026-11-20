---
name: unknown_workflow_lora_sampler_vae_24
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.5
common_nodes: [CFGNorm, CLIPLoader, DWPreprocessor, EmptySD3LatentImage, ExpressionEditor, FluxKontextImageScale, GetNode, JoinStringMulti, KSampler, Label (rgthree), LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, PrimitiveFloat, PrimitiveInt, PrimitiveStringMultiline, SaveImage, SetNode, TextEncodeQwenImageEditPlus, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/最强一张图生成一致性角色Lora素材_2000551700429762561.json, 图片生成/图生图/角色设计_1989984266031427585.json, 平台全量/角色设计_2046840811077246977.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_vae_24

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/最强一张图生成一致性角色Lora素材_2000551700429762561.json、图片生成/图生图/角色设计_1989984266031427585.json、平台全量/角色设计_2046840811077246977.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：50%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `DWPreprocessor`
- `EmptySD3LatentImage`
- `ExpressionEditor`
- `FluxKontextImageScale`
- `GetNode`
- `JoinStringMulti`
- `KSampler`
- `Label (rgthree)`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `PrimitiveFloat`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `SaveImage`
- `SetNode`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `StringConstantMultiline` —— 2/3 个有
- `UnetLoaderGGUF` —— 2/3 个有
- `GGUFLoaderKJ` —— 1/3 个有
- `JjkText` —— 1/3 个有
- `Text` —— 1/3 个有
- `Textbox` —— 1/3 个有
- `ttN text` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 45/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（45/3 个样本）：Steps较低可能导致细节不足
