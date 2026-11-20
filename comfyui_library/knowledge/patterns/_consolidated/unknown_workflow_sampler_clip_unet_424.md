---
name: unknown_workflow_sampler_clip_unet_424
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9165
common_nodes: [CLIPTextEncodeFlux, CLIPVisionLoader, DualCLIPLoader, EmptyLatentImage, KSampler, LoadImage, PreviewImage, SaveImage, StyleModelLoader, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Flux Redux - Official Flux Tools by BFL - Beginner_1864884851341217793.json, 图片生成/图生图/REDUX洗图工作流_1967519880650088450.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_424

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Flux Redux - Official Flux Tools by BFL - Beginner_1864884851341217793.json、图片生成/图生图/REDUX洗图工作流_1967519880650088450.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：92%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncodeFlux`
- `CLIPVisionLoader`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `StyleModelLoader`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AIO_Preprocessor` —— 1/2 个有
- `CLIPVisionEncode` —— 1/2 个有
- `ConditioningZeroOut` —— 1/2 个有
- `ControlNetApplyAdvanced` —— 1/2 个有
- `ControlNetLoader` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `ReduxAdvanced` —— 1/2 个有
- `StyleModelApply` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | normal | - | 2 | 50% |
| 重绘幅度 | 1 | - | 2 | 100% |
| 宽度 | 1152 | - | 2 | 89% |
| 高度 | 940 | - | 2 | 91% |
| ControlNet 权重 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 normal，2 个样本，一致性 50%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 1152，样本不足，未给区间，2 个样本，取值集中（一致性 89%）
- 高度 中位数 940，样本不足，未给区间，2 个样本，取值集中（一致性 91%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
