---
name: unknown_workflow_lora_sampler_vae_16
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.966
common_nodes: [CFGNorm, CLIPLoader, CR Text, ConditioningZeroOut, ImageScaleToTotalPixels, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlusAdvance_lrzjason, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/👾怪獸-千问多图编辑2509PLUS👾_1980984166009409538.json, 图片生成/图生图/👾怪獸-千问桌面手办👾_1982436024448098306.json, 图片生成/文生图/千问图像编辑2511-qwen image edit2511_1980096005066625026.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_vae_16

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/👾怪獸-千问多图编辑2509PLUS👾_1980984166009409538.json、图片生成/图生图/👾怪獸-千问桌面手办👾_1982436024448098306.json、图片生成/文生图/千问图像编辑2511-qwen image edit2511_1980096005066625026.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：97%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `CR Text`
- `ConditioningZeroOut`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `DWPreprocessor` —— 2/3 个有
- `EmptyContext` —— 2/3 个有
- `LazySwitch1way` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `UnetLoaderGGUF` —— 2/3 个有
- `easy blocker` —— 2/3 个有
- `easy boolean` —— 2/3 个有
- `EmptySD3LatentImage` —— 1/3 个有
- `LayerUtility: PurgeVRAM V2` —— 1/3 个有
- `SeedVR2BlockSwap` —— 1/3 个有
- `SeedVR2GGUF` —— 1/3 个有
- `UNETLoader` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | er_sde | - | 3 | 100% |
| 调度器 | beta57 | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，3 个样本，一致性 100%
- 调度器 最常用 beta57，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
