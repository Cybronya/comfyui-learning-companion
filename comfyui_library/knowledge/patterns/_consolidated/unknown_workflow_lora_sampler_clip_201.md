---
name: unknown_workflow_lora_sampler_clip_201
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.80875
common_nodes: [CLIPLoader, CLIPTextEncode, CR SDXL Aspect Ratio, ConditioningZeroOut, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/工作流基础系列34-Krea2文生图工作流_2069974370528874497.json, 平台全量/LORA系列05-fal-Krea-2-Style-LoRAs-用于Krea2-Turbo_2077273546866384898.json, 平台全量/Qwen-Image 小红书爆款中文艺术字海报直出工作流v1.0_1962343195613007874.json, 平台全量/Qwen-Image 手写艺术字海报直出工作流v1.0  by@阮旭东AIGC_1962304978536873985.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_201

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/工作流基础系列34-Krea2文生图工作流_2069974370528874497.json、平台全量/LORA系列05-fal-Krea-2-Style-LoRAs-用于Krea2-Turbo_2077273546866384898.json、平台全量/Qwen-Image 小红书爆款中文艺术字海报直出工作流v1.0_1962343195613007874.json、平台全量/Qwen-Image 手写艺术字海报直出工作流v1.0  by@阮旭东AIGC_1962304978536873985.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR SDXL Aspect Ratio`
- `ConditioningZeroOut`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingAuraFlow` —— 3/4 个有
- `Label (rgthree)` —— 2/4 个有
- `PreviewImage` —— 2/4 个有
- `Seed (rgthree)` —— 2/4 个有
- `AddLabel` —— 1/4 个有
- `ImageConcatMulti` —— 1/4 个有
- `easy promptLine` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 14 | 8 - 20 | 4 | 57% |
| Prompt 约束强度(CFG) | 2.55 | 1 - 4.1 | 4 | 39% |
| 采样算法 | er_sde | - | 4 | 50% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 14，观测区间 8 - 20，4 个样本
- Prompt 约束强度(CFG) 中位数 2.55，观测区间 1 - 4.1，4 个样本，取值分散，一致性仅 39%
- 采样算法 最常用 er_sde，4 个样本，一致性 50%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
