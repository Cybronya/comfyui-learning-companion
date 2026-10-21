---
name: unknown_workflow_lora_sampler_clip_98
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.841667
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, Fast Groups Bypasser (rgthree), Image Comparer (rgthree), KSampler, LoraLoaderModelOnly, ResizeImageMaskNode, SDXLEmptyLatentSizePicker+, SaveImage, Seed (rgthree), SeedVR2Conditioning, SeedVR2PostProcessing, SeedVR2Preprocess, UNETLoader, VAEDecode, VAEDecodeTiled, VAEEncodeTiled, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/1-Krea2Turbo-文生图+风格参考+巨物+四视图工作流V2_2092107358351745026.json, 图片生成/文生图/krea2文生图工作流_2095508049963343873.json, 图片生成/文生图/文生图+风格参考+巨物+四视图工作流_2101553952839004162.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_98

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/1-Krea2Turbo-文生图+风格参考+巨物+四视图工作流V2_2092107358351745026.json、图片生成/文生图/krea2文生图工作流_2095508049963343873.json、图片生成/文生图/文生图+风格参考+巨物+四视图工作流_2101553952839004162.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `Fast Groups Bypasser (rgthree)`
- `Image Comparer (rgthree)`
- `KSampler`
- `LoraLoaderModelOnly`
- `ResizeImageMaskNode`
- `SDXLEmptyLatentSizePicker+`
- `SaveImage`
- `Seed (rgthree)`
- `SeedVR2Conditioning`
- `SeedVR2PostProcessing`
- `SeedVR2Preprocess`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncodeTiled`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Any Switch (rgthree)` —— 2/3 个有
- `Fast Bypasser (rgthree)` —— 2/3 个有
- `MuyeTextEditOutput` —— 2/3 个有
- `PreviewAny` —— 2/3 个有
- `PrimitiveStringMultiline` —— 2/3 个有
- `easy stylesSelector` —— 2/3 个有
- `llama_cpp_instruct_adv` —— 2/3 个有
- `llama_cpp_model_loader` —— 2/3 个有
- `llama_cpp_parameters` —— 2/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024x1024 (1.0) | - | 3 | 100% |
| 高度 | 1 | 1 - 1 | 3 | 100% |
| 采样步数 | 8 | 1 - 8 | 3 | 42% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | beta | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 最常用 1024x1024 (1.0)，3 个样本，一致性 100%
- 高度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 8，观测区间 1 - 8，3 个样本，取值分散，一致性仅 42%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（9/3 个样本）：Steps较低可能导致细节不足
