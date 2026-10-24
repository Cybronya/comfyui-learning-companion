---
name: unknown_workflow_lora_clip_unet_12
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.970667
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, ImpactInt, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/LH-DMT-017.WAN2.2文生图_2016175288681504770.json, 图片生成/文生图/WAN模板_2014608314528698369.json, 图片生成/文生图/Wan2.2-顶级文生图_1951984559229489154.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_clip_unet_12

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/LH-DMT-017.WAN2.2文生图_2016175288681504770.json、图片生成/文生图/WAN模板_2014608314528698369.json、图片生成/文生图/Wan2.2-顶级文生图_1951984559229489154.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `ImpactInt`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CFGZeroStarAndInit` —— 2/3 个有
- `KSamplerAdvanced` —— 2/3 个有
- `ConditioningZeroOut` —— 1/3 个有
- `FL_SDUltimate_Slices` —— 1/3 个有
- `Image Comparer (rgthree)` —— 1/3 个有
- `KSampler` —— 1/3 个有
- `UltimateSDUpscale` —— 1/3 个有
- `UpscaleModelLoader` —— 1/3 个有
- `easy positive` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 3 | 33% |
| Prompt 约束强度(CFG) | 10 | 1 - 12 | 3 | 38% |
| 采样算法 | 1 | - | 2 | 100% |
| 调度器 | euler | - | 3 | 67% |
| 重绘幅度 | beta | - | 3 | 67% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，3 个样本，一致性 33%
- Prompt 约束强度(CFG) 中位数 10，观测区间 1 - 12，3 个样本，取值分散，一致性仅 38%
- 采样算法 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，3 个样本，一致性 67%
- 重绘幅度 最常用 beta，3 个样本，一致性 67%
