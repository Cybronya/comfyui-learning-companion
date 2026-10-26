---
name: unknown_workflow_upscale_latent_upscale_sampler_25
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.941
common_nodes: [CLIPLoader, CLIPSetLastLayer, CLIPTextEncode, ClownsharKSampler_Beta, EmptyLatentImage, FluxResolutionNode, LatentUpscaleBy, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Anima 八步极速动漫出图工作流_2052343882582634497.json, 图片生成/文生图/WAI-ANIMA文生图潜在空间放大+高清修复_2046194207995469826.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_sampler_25

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/Anima 八步极速动漫出图工作流_2052343882582634497.json、图片生成/文生图/WAI-ANIMA文生图潜在空间放大+高清修复_2046194207995469826.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：94%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPSetLastLayer`
- `CLIPTextEncode`
- `ClownsharKSampler_Beta`
- `EmptyLatentImage`
- `FluxResolutionNode`
- `LatentUpscaleBy`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `KepStringLiteral` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `Seed Everywhere` —— 1/2 个有
- `Text` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | - | 2 | 100% |
| 高度 | 512 | - | 2 | 100% |
| 采样步数 | beta57 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 19 | - | 2 | 42% |
| 采样算法 | -1 | - | 2 | 100% |
| 调度器 | 0.55 | - | 2 | 100% |
| 重绘幅度 | 2 | - | 2 | 50% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 最常用 beta57，2 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 19，样本不足，未给区间，2 个样本，取值分散，一致性仅 42%
- 采样算法 中位数 -1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 中位数 0.55，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 重绘幅度 中位数 2，样本不足，未给区间，2 个样本
- 风险：Prompt 约束强度(CFG) 观测到 30，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
- 风险：重绘幅度 观测到 3，超出安全上限 1（denoise 接近 1.0 时接近重新生成，初始潜空间影响被抹平）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
