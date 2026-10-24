---
name: text_to_image_sampler_clip_vae_34
type: Text To Image
frequency: 3
level: moderate
coverage: 1
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, ModelSamplingAuraFlow, NunchakuQwenImageDiTLoader, SaveImage, VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen-Image（nunchaku）文生图V1_1959799817432150017.json, 图片生成/文生图/nunchaku Qwen image基础工作流_1959617318458437634.json, 图片生成/文生图/qwen文生图+双节棍流_1963549374519414785.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_vae_34

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Qwen-Image（nunchaku）文生图V1_1959799817432150017.json、图片生成/文生图/nunchaku Qwen image基础工作流_1959617318458437634.json、图片生成/文生图/qwen文生图+双节棍流_1963549374519414785.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：100%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `ModelSamplingAuraFlow`
- `NunchakuQwenImageDiTLoader`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `VAELoader` —— 2/3 个有
- `AV_VAELoader` —— 1/3 个有
- `CFGNorm` —— 1/3 个有
- `LayerUtility: PurgeVRAM` —— 1/3 个有
- `LoraLoaderModelOnly` —— 1/3 个有
- `RH_Translator` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 904 - 1328 | 3 | 84% |
| 高度 | 1280 | 1024 - 1328 | 3 | 89% |
| 采样步数 | 10 | 8 - 20 | 3 | 59% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 2.54 | 3 | 64% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 904 - 1328，3 个样本，取值集中（一致性 84%）
- 高度 中位数 1280，观测区间 1024 - 1328，3 个样本，取值集中（一致性 89%）
- 采样步数 中位数 10，观测区间 8 - 20，3 个样本
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 2.54，3 个样本
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
