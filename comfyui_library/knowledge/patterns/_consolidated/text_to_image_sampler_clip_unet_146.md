---
name: text_to_image_sampler_clip_unet_146
type: Text To Image
frequency: 5
level: strong
coverage: 0.8422
common_nodes: [BatchTextReplace, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, PrimitiveBoolean, SaveImage, Text, UNETLoader, VAEDecode, VAELoader, easy cleanGpuUsed, easy ifElse, easy showAnything, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-image+FlashVSR-自动提示词-文生图-图片放大-高清直出_1994371628656173057.json, 图片生成/文生图/Z-image+FlashVSR-自动提示词-文生图-图片放大-高清直出_2053328390534516737.json, 图片生成/文生图/Z-image+FlashVSR-自动提示词-文生图-图片放大-高清直出_2070328858661965826.json, 图片生成/文生图/boogu_turbo_快速出图，自动提示词_2069632430994190338.json, 图片生成/文生图/画质提升-Z-image+FlashVSR-自动提示词-文生图-高清直出_2053127689090936833.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_146

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/Z-image+FlashVSR-自动提示词-文生图-图片放大-高清直出_1994371628656173057.json、图片生成/文生图/Z-image+FlashVSR-自动提示词-文生图-图片放大-高清直出_2053328390534516737.json、图片生成/文生图/Z-image+FlashVSR-自动提示词-文生图-图片放大-高清直出_2070328858661965826.json、图片生成/文生图/boogu_turbo_快速出图，自动提示词_2069632430994190338.json、图片生成/文生图/画质提升-Z-image+FlashVSR-自动提示词-文生图-高清直出_2053127689090936833.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 5 个 workflow 都包含：
- `BatchTextReplace`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `PrimitiveBoolean`
- `SaveImage`
- `Text`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy ifElse`
- `easy showAnything`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`

**可变部分**（部分 workflow 才有）：
- `AddLabel` —— 4/5 个有
- `FlashVSRNode` —— 4/5 个有
- `Int` —— 4/5 个有
- `ShowText` —— 3/5 个有
- `EmptyImage` —— 2/5 个有
- `FluxResolutionNode` —— 2/5 个有
- `Image Comparer (rgthree)` —— 2/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/5 个有
- `PrimitiveStringMultiline` —— 2/5 个有
- `SeedVR2` —— 2/5 个有
- `ShowText|pysssss` —— 2/5 个有
- `LoraLoaderModelOnly` —— 1/5 个有
- `PreviewImage` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1080 | 1024 - 1080 | 5 | 98% |
| 高度 | 1920 | 1024 - 1920 | 5 | 79% |
| 采样步数 | 10 | 4 - 10 | 5 | 73% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 60% |
| 调度器 | simple | - | 5 | 60% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1080，观测区间 1024 - 1080，5 个样本，取值集中（一致性 98%）
- 高度 中位数 1920，观测区间 1024 - 1920，5 个样本
- 采样步数 中位数 10，观测区间 4 - 10，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 60%
- 调度器 最常用 simple，5 个样本，一致性 60%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
