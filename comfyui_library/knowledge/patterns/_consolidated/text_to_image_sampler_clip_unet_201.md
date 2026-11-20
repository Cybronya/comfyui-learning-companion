---
name: text_to_image_sampler_clip_unet_201
type: Text To Image
frequency: 3
level: strong
coverage: 0.632333
common_nodes: [Any Switch (rgthree), CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, Fast Groups Bypasser (rgthree), GetNode, KSampler, LoadImage, MuyeTextEditOutput, PreviewImage, PrimitiveInt, SaveImage, SetNode, UNETLoader, VAEDecode, VAELoader, easy showAnything, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/krea2-多功能工作流_2076921555036233729.json, 图片生成/文生图/krea2多功能生图_2070027725737385985.json, 图片生成/文生图/krea2多功能生图_2070130565822631937.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_201

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/krea2-多功能工作流_2076921555036233729.json、图片生成/文生图/krea2多功能生图_2070027725737385985.json、图片生成/文生图/krea2多功能生图_2070130565822631937.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：63%

## 共有节点

全部 3 个 workflow 都包含：
- `Any Switch (rgthree)`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `KSampler`
- `LoadImage`
- `MuyeTextEditOutput`
- `PreviewImage`
- `PrimitiveInt`
- `SaveImage`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`

**可变部分**（部分 workflow 才有）：
- `DepthAnythingV2Preprocessor` —— 1/3 个有
- `Fast Groups Muter (rgthree)` —— 1/3 个有
- `Krea2ControlApply` —— 1/3 个有
- `Krea2ControlImageEncode` —— 1/3 个有
- `Krea2ControlLoRALoader` —— 1/3 个有
- `LayerUtility: TextJoin` —— 1/3 个有
- `LoraLoaderModelOnly` —— 1/3 个有
- `TextGenerateLTX2Prompt` —— 1/3 个有
- `easy seed` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 3 | 100% |
| 高度 | 1536 | 1536 - 1536 | 3 | 100% |
| 采样步数 | 8 | 8 - 8 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | er_sde | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，3 个样本，取值集中（一致性 100%）
- 高度 中位数 1536，观测区间 1536 - 1536，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 8，观测区间 8 - 8，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
