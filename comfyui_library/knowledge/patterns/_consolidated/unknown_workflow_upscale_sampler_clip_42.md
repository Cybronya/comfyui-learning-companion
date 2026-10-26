---
name: unknown_workflow_upscale_sampler_clip_42
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.823
common_nodes: [AILab_QwenVL, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, Fast Groups Bypasser (rgthree), KSamplerAdvanced, PreviewImage, QwenImageLatentAspectRatio, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, Text Multiline, UNETLoader, VAEDecode, VAELoader, easy cleanGpuUsed]
problems: []
missing: []
members: [图片生成/图生图/极速文生图，极速洗图 Zimage-差异生图_2000199609148375041.json, 图片生成/文生图/Zimage-差异生图_2000774772462059522.json, 图片生成/文生图/极速，Zimage-差异生图，高清_2000564738843082754.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_clip_42

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/极速文生图，极速洗图 Zimage-差异生图_2000199609148375041.json、图片生成/文生图/Zimage-差异生图_2000774772462059522.json、图片生成/文生图/极速，Zimage-差异生图，高清_2000564738843082754.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 3 个 workflow 都包含：
- `AILab_QwenVL`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `Fast Groups Bypasser (rgthree)`
- `KSamplerAdvanced`
- `PreviewImage`
- `QwenImageLatentAspectRatio`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `Text Multiline`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 1/3 个有
- `MaraScottIsEmptyOrNone_v1` —— 1/3 个有
- `RH_Captioner` —— 1/3 个有
- `easy ifElse` —— 1/3 个有
- `easy showAnything` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 3 | 100% |
| Prompt 约束强度(CFG) | 10 | 10 - 10 | 3 | 100% |
| 采样算法 | 1 | 1 - 1 | 3 | 100% |
| 调度器 | er_sde | - | 3 | 100% |
| 重绘幅度 | sgm_uniform | - | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，3 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 10，观测区间 10 - 10，3 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 调度器 最常用 er_sde，3 个样本，一致性 100%
- 重绘幅度 最常用 sgm_uniform，3 个样本，一致性 100%
