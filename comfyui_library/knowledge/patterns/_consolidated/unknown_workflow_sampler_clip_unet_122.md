---
name: unknown_workflow_sampler_clip_unet_122
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.7762
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, FluxGuidance, KSamplerSelect, ModelSamplingFlux, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: [LayerUtility: PurgeVRAM V2, String Literal, SDXLEmptyLatentSizePicker+, CR SDXL Aspect Ratio, easy seed]
members: [图片生成/文生图/1910919824812507138.json, 图片生成/文生图/1914942831851466753.json, 图片生成/文生图/1951256026706333697.json, 图片生成/文生图/1952909781780598785.json, 图片生成/文生图/1952978061257076737.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_122

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/1910919824812507138.json、图片生成/文生图/1914942831851466753.json、图片生成/文生图/1951256026706333697.json、图片生成/文生图/1952909781780598785.json、图片生成/文生图/1952978061257076737.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：78%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSamplerSelect`
- `ModelSamplingFlux`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: PurgeVRAM V2` —— 4/5 个有
- `SDXLEmptyLatentSizePicker+` —— 4/5 个有
- `String Literal` —— 4/5 个有
- `AddLabel` —— 3/5 个有
- `ImageConcanate` —— 3/5 个有
- `KSampler` —— 3/5 个有
- `easy seed` —— 3/5 个有
- `CLIPLoader` —— 2/5 个有
- `QwenImageModelLoader` —— 2/5 个有
- `RH_QwenImageGenerator` —— 2/5 个有
- `CR SDXL Aspect Ratio` —— 1/5 个有
- `ConditioningZeroOut` —— 1/5 个有
- `HiDreamSampler` —— 1/5 个有
- `ImageScaleBy` —— 1/5 个有
- `ModelSamplingAuraFlow` —— 1/5 个有
- `ModelSamplingSD3` —— 1/5 个有
- `PreviewImage` —— 1/5 个有
- `VAEEncode` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1280x768 (1.67) | - | 4 | 75% |
| 高度 | 1 | 1 - 1 | 4 | 100% |
| 采样步数 | 20 | 20 - 20 | 3 | 100% |
| Prompt 约束强度(CFG) | 3.5 | 1 - 4 | 3 | 54% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 0.5 - 1 | 3 | 72% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 最常用 1280x768 (1.67)，4 个样本，一致性 75%
- 高度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样步数 中位数 20，观测区间 20 - 20，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 3.5，观测区间 1 - 4，3 个样本
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.5 - 1，3 个样本
- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: PurgeVRAM V2、String Literal、SDXLEmptyLatentSizePicker+、CR SDXL Aspect Ratio、easy seed
