---
name: text_to_image_lora_sampler_clip_564
type: Text To Image
frequency: 3
level: strong
coverage: 0.857333
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, LoraLoaderModelOnly, ResolutionSelector, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/krea2 风格之王 全能模型 文生图工作流（自由版）_2070673954079068162.json, 图片生成/文生图/krea2+Qwen3VL提示词优化文生图_2071171990551097346.json, 图片生成/文生图/超自然文生美女_2075426810342502402.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_564

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/krea2 风格之王 全能模型 文生图工作流（自由版）_2070673954079068162.json、图片生成/文生图/krea2+Qwen3VL提示词优化文生图_2071171990551097346.json、图片生成/文生图/超自然文生美女_2075426810342502402.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `ResolutionSelector`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptyImage` —— 2/3 个有
- `INTConstant` —— 2/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/3 个有
- `PrimitiveStringMultiline` —— 2/3 个有
- `Text Multiline` —— 2/3 个有
- `easy seed` —— 2/3 个有
- `llama_cpp_instruct_adv` —— 2/3 个有
- `llama_cpp_model_loader` —— 2/3 个有
- `llama_cpp_parameters` —— 2/3 个有
- `CR Prompt Text` —— 1/3 个有
- `JoinStrings` —— 1/3 个有
- `Label (rgthree)` —— 1/3 个有
- `PreviewAny` —— 1/3 个有
- `StringConcatenate` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 3 | 100% |
| 高度 | 1536 | 1024 - 1536 | 3 | 82% |
| 采样步数 | 8 | 8 - 10 | 3 | 89% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 67% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，3 个样本，取值集中（一致性 100%）
- 高度 中位数 1536，观测区间 1024 - 1536，3 个样本，取值集中（一致性 82%）
- 采样步数 中位数 8，观测区间 8 - 10，3 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 67%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（2/3 个样本）：Steps较低可能导致细节不足
