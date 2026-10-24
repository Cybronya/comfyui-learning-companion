---
name: unknown_workflow_sampler_clip_checkpoint_33
type: Unknown Workflow
frequency: 2
level: weak
coverage: 1
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, KSamplerAdvanced, LoadImage, SaveImage, VAEDecode, VAEEncode]
problems: []
missing: []
members: [图片生成/图生图/图生图游乐场风格_1933056498794893313.json, 图片生成/图生图/拾光_2079454965298458625.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_checkpoint_33

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/图生图游乐场风格_1933056498794893313.json、图片生成/图生图/拾光_2079454965298458625.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：100%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `KSamplerAdvanced`
- `LoadImage`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `WD14Tagger|pysssss` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 2 | 100% |
| Prompt 约束强度(CFG) | 29 | - | 2 | 97% |
| 采样算法 | 5.25 | - | 2 | 67% |
| 调度器 | dpmpp_2m_sde | - | 2 | 50% |
| 重绘幅度 | exponential | - | 2 | 50% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，2 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 29，样本不足，未给区间，2 个样本，取值集中（一致性 97%）
- 采样算法 中位数 5.25，样本不足，未给区间，2 个样本
- 调度器 最常用 dpmpp_2m_sde，2 个样本，一致性 50%
- 重绘幅度 最常用 exponential，2 个样本，一致性 50%
- 风险：Prompt 约束强度(CFG) 观测到 30，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
