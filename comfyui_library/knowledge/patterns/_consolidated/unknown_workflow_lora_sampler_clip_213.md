---
name: unknown_workflow_lora_sampler_clip_213
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.978
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM V2, LoraLoader, ModelSamplingAuraFlow, SaveImage, SeedVR2BlockSwap, SeedVR2ExtraArgs, SeedVR2GGUF, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen Image 2512双重差异采样高清放大文生图V1_2006342593889701889.json, 图片生成/文生图/Qwen Image 2512双重差异采样高清放大文生图_2007653571558379521.json, 图片生成/文生图/简笔画小狗_2009237785978347521.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_213

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Qwen Image 2512双重差异采样高清放大文生图V1_2006342593889701889.json、图片生成/文生图/Qwen Image 2512双重差异采样高清放大文生图_2007653571558379521.json、图片生成/文生图/简笔画小狗_2009237785978347521.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM V2`
- `LoraLoader`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `SeedVR2BlockSwap`
- `SeedVR2ExtraArgs`
- `SeedVR2GGUF`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 2/3 个有
- `LoraLoaderModelOnly` —— 2/3 个有
- `RH_LLMAPI_NODE` —— 2/3 个有
- `UnetLoaderGGUF` —— 2/3 个有
- `easy showAnything` —— 2/3 个有
- `UNETLoader` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | res_multistep | - | 3 | 67% |
| 调度器 | beta | - | 3 | 67% |
| 重绘幅度 | 0.3 | 0.3 - 1 | 3 | 38% |
| LoRA 模型强度 | 1 | 0.8 - 1 | 3 | 90% |
| LoRA 文本强度 | 1 | 0.8 - 1 | 3 | 90% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_multistep，3 个样本，一致性 67%
- 调度器 最常用 beta，3 个样本，一致性 67%
- 重绘幅度 中位数 0.3，观测区间 0.3 - 1，3 个样本，取值分散，一致性仅 38%
- LoRA 模型强度 中位数 1，观测区间 0.8 - 1，3 个样本，取值集中（一致性 90%）
- LoRA 文本强度 中位数 1，观测区间 0.8 - 1，3 个样本，取值集中（一致性 90%）
- 高发问题（6/3 个样本）：Steps较低可能导致细节不足
