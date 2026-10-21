---
name: unknown_workflow_video_sampler_clip_102
type: Unknown Workflow
frequency: 5
level: weak
coverage: 0.694
common_nodes: [CLIPLoader, CLIPTextEncode, KSamplerAdvanced, ModelSamplingSD3, PathchSageAttentionKJ, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanImageToVideo]
problems: []
missing: []
members: [视频生成/图生视频/1991093640317501442.json, 视频生成/图生视频/1991088603090759681.json, 视频生成/图生视频/1949440813809467394.json, 视频生成/图生视频/1995392959409479682.json, 视频生成/图生视频/2018573357712674817.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_102

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/1991093640317501442.json、视频生成/图生视频/1991088603090759681.json、视频生成/图生视频/1949440813809467394.json、视频生成/图生视频/1995392959409479682.json、视频生成/图生视频/2018573357712674817.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：69%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSamplerAdvanced`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideo`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 4/5 个有
- `LoraLoaderModelOnly` —— 4/5 个有
- `ModelPatchTorchSettings` —— 3/5 个有
- `INTConstant` —— 2/5 个有
- `JWInteger` —— 2/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/5 个有
- `LayerUtility: PurgeVRAM` —— 2/5 个有
- `EmptyHunyuanLatentVideo` —— 1/5 个有
- `Int` —— 1/5 个有
- `LoadImageFromURL` —— 1/5 个有
- `LoadVideo` —— 1/5 个有
- `MathExpression|pysssss` —— 1/5 个有
- `PreviewAny` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 5 | 60% |
| Prompt 约束强度(CFG) | 6 | 4 - 8 | 5 | 73% |
| 采样算法 | 1 | 1 - 3.5 | 5 | 33% |
| 调度器 | euler | - | 5 | 60% |
| 重绘幅度 | simple | - | 5 | 60% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，5 个样本，一致性 60%
- Prompt 约束强度(CFG) 中位数 6，观测区间 4 - 8，5 个样本
- 采样算法 中位数 1，观测区间 1 - 3.5，5 个样本，取值分散，一致性仅 33%
- 调度器 最常用 euler，5 个样本，一致性 60%
- 重绘幅度 最常用 simple，5 个样本，一致性 60%
