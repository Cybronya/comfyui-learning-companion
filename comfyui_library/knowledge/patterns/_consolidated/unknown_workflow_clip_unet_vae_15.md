---
name: unknown_workflow_clip_unet_vae_15
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8345
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Flux2-Klein-9B-True-bf16_2024822336939106306.json, 图片生成/文生图/【文生图】Flux.2.0_Klein9B_2030309405933182978.json]
source: knowledge_consolidation
---

# unknown_workflow_clip_unet_vae_15

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/Flux2-Klein-9B-True-bf16_2024822336939106306.json、图片生成/文生图/【文生图】Flux.2.0_Klein9B_2030309405933182978.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：83%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere3` —— 1/2 个有
- `KSampler` —— 1/2 个有
- `KSamplerAdvanced` —— 1/2 个有
- `MuyeSizeSelector` —— 1/2 个有
- `PrimitiveInt` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | - | 1 | 100% |
| Prompt 约束强度(CFG) | 13 | - | 2 | 8% |
| 采样算法 | 1 | - | 1 | 100% |
| 调度器 | euler | - | 2 | 50% |
| 重绘幅度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- Prompt 约束强度(CFG) 中位数 13，样本不足，未给区间，2 个样本，取值分散，一致性仅 8%
- 调度器 最常用 euler，2 个样本，一致性 50%
- 风险：Prompt 约束强度(CFG) 观测到 25，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
