---
name: unknown_workflow_video_sampler_clip_245
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.56
common_nodes: [CLIPLoader, CLIPTextEncode, GetNode, KSamplerAdvanced, LoadImage, ModelSamplingSD3, SetNode, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanImageToVideo]
problems: []
missing: []
members: [视频生成/图生视频/1951120660623990785.json, 视频生成/图生视频/2025730083717124097.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_245

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/1951120660623990785.json、视频生成/图生视频/2025730083717124097.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：56%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `GetNode`
- `KSamplerAdvanced`
- `LoadImage`
- `ModelSamplingSD3`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideo`

**可变部分**（部分 workflow 才有）：
- `INTConstant` —— 1/2 个有
- `ImageResizeKJv2` —— 1/2 个有
- `Label (rgthree)` —— 1/2 个有
- `LayerUtility: PurgeVRAM` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `MathExpression|pysssss` —— 1/2 个有
- `PathchSageAttentionKJ` —— 1/2 个有
- `PreviewImage` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 2 | 100% |
| Prompt 约束强度(CFG) | 15 | - | 2 | 67% |
| 采样算法 | 2.25 | - | 2 | 44% |
| 调度器 | euler | - | 2 | 100% |
| 重绘幅度 | simple | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，2 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 15，样本不足，未给区间，2 个样本
- 采样算法 中位数 2.25，样本不足，未给区间，2 个样本，取值分散，一致性仅 44%
- 调度器 最常用 euler，2 个样本，一致性 100%
- 重绘幅度 最常用 simple，2 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
