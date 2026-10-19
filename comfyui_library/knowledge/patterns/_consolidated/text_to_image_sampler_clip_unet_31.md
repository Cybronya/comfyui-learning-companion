---
name: text_to_image_sampler_clip_unet_31
type: Text To Image
frequency: 2
level: weak
coverage: 1
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, EmptyLatentImage, FluxGuidance, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/FLUX.1_ipadapter_1880962162222067713.json, 图片生成/文生图/中文输入自动扩写flux文生图基础工作流-_1892792029888614402.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_31

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/FLUX.1_ipadapter_1880962162222067713.json、图片生成/文生图/中文输入自动扩写flux文生图基础工作流-_1892792029888614402.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：100%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FluxGuidance`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ApplyIPAdapterFlux` —— 1/2 个有
- `DifferentialDiffusion` —— 1/2 个有
- `IPAdapterFluxLoader` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `PreviewTextNode` —— 1/2 个有
- `RH_OneShot_Prompter` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 23 | - | 2 | 87% |
| Prompt 约束强度(CFG) | 1.38 | - | 2 | 72% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | normal | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| 宽度 | 896 | - | 2 | 86% |
| 高度 | 1024 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 23，样本不足，未给区间，2 个样本，取值集中（一致性 87%）
- Prompt 约束强度(CFG) 中位数 1.38，样本不足，未给区间，2 个样本
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 normal，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 896，样本不足，未给区间，2 个样本，取值集中（一致性 86%）
- 高度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
