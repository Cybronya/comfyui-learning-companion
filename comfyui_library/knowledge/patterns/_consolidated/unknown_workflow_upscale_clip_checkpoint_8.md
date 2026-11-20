---
name: unknown_workflow_upscale_clip_checkpoint_8
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.923
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, ImageUpscaleWithModel, PreviewImage, SaveImage, UpscaleModelLoader, VAEDecode, VAEEncode]
problems: []
missing: []
members: [平台全量/去除背景_1789194789166632961.json, 平台全量/图生图+高清修复_1848234529411698689.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_clip_checkpoint_8

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/去除背景_1789194789166632961.json、平台全量/图生图+高清修复_1848234529411698689.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：92%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ImageUpscaleWithModel`
- `PreviewImage`
- `SaveImage`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`

**可变部分**（部分 workflow 才有）：
- `KSampler` —— 1/2 个有
- `LayerMask: SegmentAnythingUltra` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `RepeatLatentBatch` —— 1/2 个有
- `Tiled KSampler` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10.5 | - | 2 | 10% |
| Prompt 约束强度(CFG) | 18 | - | 2 | 44% |
| 采样算法 | 8 | - | 1 | 100% |
| 调度器 | dpmpp_2m | - | 2 | 50% |
| 重绘幅度 | 0.45 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 10.5，样本不足，未给区间，2 个样本，取值分散，一致性仅 10%
- Prompt 约束强度(CFG) 中位数 18，样本不足，未给区间，2 个样本，取值分散，一致性仅 44%
- 调度器 最常用 dpmpp_2m，2 个样本，一致性 50%
- 风险：Prompt 约束强度(CFG) 观测到 28，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
