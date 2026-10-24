---
name: unknown_workflow_upscale_latent_upscale_sampler_26
type: Unknown Workflow
frequency: 2
level: weak
coverage: 1
common_nodes: [CLIPLoader, CLIPTextEncode, CompressImages, JoinStrings, KSampler, KSamplerAdvanced, LatentUpscaleBy, LayerUtility: TextBox, SDXL Empty Latent Image (rgthree), UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/anima3二次元文生图_2046060254537977858.json, 图片生成/文生图/anima3二次元文生图（加密）_2048231461412671490.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_sampler_26

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/anima3二次元文生图_2046060254537977858.json、图片生成/文生图/anima3二次元文生图（加密）_2048231461412671490.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：100%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CompressImages`
- `JoinStrings`
- `KSampler`
- `KSamplerAdvanced`
- `LatentUpscaleBy`
- `LayerUtility: TextBox`
- `SDXL Empty Latent Image (rgthree)`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | - | 1 | 100% |
| Prompt 约束强度(CFG) | 17.5 | - | 2 | 29% |
| 采样算法 | 5 | - | 1 | 100% |
| 调度器 | normal | - | 2 | 50% |
| 重绘幅度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- Prompt 约束强度(CFG) 中位数 17.5，样本不足，未给区间，2 个样本，取值分散，一致性仅 29%
- 调度器 最常用 normal，2 个样本，一致性 50%
- 风险：Prompt 约束强度(CFG) 观测到 30，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
