---
name: text_to_image_sampler_clip_unet_129
type: Text To Image
frequency: 5
level: moderate
coverage: 0.7564
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, Fast Groups Bypasser (rgthree), KSampler, SaveImage, Text Multiline, UNETLoader, VAEDecode, VAELoader, llama_cpp_instruct_adv, llama_cpp_model_loader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Anima三兄弟工作流_2094991229678342145.json, 图片生成/文生图/Anima全家桶工作流_2075594450092511234.json, 图片生成/文生图/Anima怀旧暗黑动漫风格工作流_2058173254162010113.json, 图片生成/文生图/Kera2 Turbo 4步极速工作流_2098378466390536193.json, 数字人/数字人/自用日漫_2097889656049332225.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_129

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/Anima三兄弟工作流_2094991229678342145.json、图片生成/文生图/Anima全家桶工作流_2075594450092511234.json、图片生成/文生图/Anima怀旧暗黑动漫风格工作流_2058173254162010113.json、图片生成/文生图/Kera2 Turbo 4步极速工作流_2098378466390536193.json、数字人/数字人/自用日漫_2097889656049332225.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：76%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `KSampler`
- `SaveImage`
- `Text Multiline`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`

**可变部分**（部分 workflow 才有）：
- `JjkShowText` —— 4/5 个有
- `ModelSamplingAuraFlow` —— 4/5 个有
- `PrimitiveFloat` —— 4/5 个有
- `PrimitiveInt` —— 4/5 个有
- `LoraLoaderModelOnly` —— 3/5 个有
- `ResolutionSelector` —— 3/5 个有
- `Text to String` —— 3/5 个有
- `ComfyMathExpression` —— 2/5 个有
- `Text` —— 2/5 个有
- `CheckpointLoaderSimple` —— 1/5 个有
- `ConditioningZeroOut` —— 1/5 个有
- `LoadImage` —— 1/5 个有
- `easy showAnything` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 4 - 30 | 5 | 58% |
| Prompt 约束强度(CFG) | 4 | 1 - 4 | 5 | 65% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 896 | 512 - 896 | 5 | 81% |
| 高度 | 1152 | 512 - 1152 | 5 | 75% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 30，观测区间 4 - 30，5 个样本
- Prompt 约束强度(CFG) 中位数 4，观测区间 1 - 4，5 个样本
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 896，观测区间 512 - 896，5 个样本，取值集中（一致性 81%）
- 高度 中位数 1152，观测区间 512 - 1152，5 个样本
