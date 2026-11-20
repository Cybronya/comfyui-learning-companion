---
name: unknown_workflow_sampler_clip_unet_463
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8535
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, KSampler, LatentCutToBatch, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Layered千问分层模型文生图｜可保存psd格式_2003359515636596737.json, 图片生成/文生图/Qwen-Image-Layered文生分层工作流_2002312587633147905.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_463

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/Layered千问分层模型文生图｜可保存psd格式_2003359515636596737.json、图片生成/文生图/Qwen-Image-Layered文生分层工作流_2002312587633147905.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：85%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `KSampler`
- `LatentCutToBatch`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `HAIGC_SavePSD` —— 1/2 个有
- `Int` —— 1/2 个有
- `Label (rgthree)` —— 1/2 个有
- `MathExpression|pysssss` —— 1/2 个有
- `PreviewImage` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | - | 2 | 67% |
| Prompt 约束强度(CFG) | 3.25 | - | 2 | 77% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 30，样本不足，未给区间，2 个样本
- Prompt 约束强度(CFG) 中位数 3.25，样本不足，未给区间，2 个样本
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
