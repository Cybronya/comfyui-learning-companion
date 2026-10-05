---
name: sdxl_portrait_controlnet_lora_sampler
type: SDXL Portrait
frequency: 4
level: strong
coverage: 0.85
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, ControlNetApply, EmptyLatentImage, KSampler, LoraLoader, SaveImage, VAEDecode]
problems: [分辨率未达SDXL常用值（当前N）, CFG值较高（当前N）可能导致Prompt约束过强]
missing: [ControlNetApply]
members: [sdxl_portrait_0.json, sdxl_portrait_1.json, sdxl_portrait_2.json, sdxl_portrait_3.json]
source: knowledge_consolidation
---

# sdxl_portrait_controlnet_lora_sampler

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（sdxl_portrait_0.json、sdxl_portrait_1.json、sdxl_portrait_2.json、sdxl_portrait_3.json）

- **类型**：SDXL Portrait
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ControlNetApply`
- `EmptyLatentImage`
- `KSampler`
- `LoraLoader`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `UpscaleModelLoader` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| Prompt 约束强度(CFG) | 7.5 | 7 - 9 | 4 | 89% |
| 采样步数 | 29 | 25 - 35 | 4 | 88% |
| ControlNet 权重 | 0.675 | 0.6 - 0.75 | 4 | 92% |
| 采样算法 | dpmpp_2m | - | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| 分辨率未达SDXL常用值（当前N） | 3/4 | low | 分辨率未达 SDXL 常用值（当前 512）→ 建议提升到 768 或以上 |
| CFG值较高（当前N）可能导致Prompt约束过强 | 1/4 | medium | CFG值较高（当前 9.0），可能导致Prompt约束过强 → 建议尝试CFG 7-10 |

## 建议与风险

- Prompt 约束强度(CFG) 中位数 7.5，观测区间 7 - 9，4 个样本，取值集中（一致性 89%）
- 采样步数 中位数 29，观测区间 25 - 35，4 个样本，取值集中（一致性 88%）
- ControlNet 权重 中位数 0.675，观测区间 0.6 - 0.75，4 个样本，取值集中（一致性 92%）
- 采样算法 最常用 dpmpp_2m，4 个样本，一致性 100%
- 高发问题（3/4 个样本）：分辨率未达SDXL常用值（当前N）
- 这些节点还没有知识卡，系统对它们的理解有限：ControlNetApply
