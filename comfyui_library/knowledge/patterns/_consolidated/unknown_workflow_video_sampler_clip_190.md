---
name: unknown_workflow_video_sampler_clip_190
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.867333
common_nodes: [CLIPLoader, CLIPTextEncode, CR Model Input Switch, EmptyImage, FluxGuidance, Int, KSampler, RIFE VFI, Textbox, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanVideoTeaCacheKJ, easy imageSize]
problems: []
missing: []
members: [平台全量/视频生视频 _ 万相2.1_1897554427598065665.json, 平台全量/视频生视频+_+万相2.1_2041340765019840514.json, 视频生成/文生视频/文生视频 _ 万相2.1_1895740774078349314.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_190

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/视频生视频 _ 万相2.1_1897554427598065665.json、平台全量/视频生视频+_+万相2.1_2041340765019840514.json、视频生成/文生视频/文生视频 _ 万相2.1_1895740774078349314.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Model Input Switch`
- `EmptyImage`
- `FluxGuidance`
- `Int`
- `KSampler`
- `RIFE VFI`
- `Textbox`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanVideoTeaCacheKJ`
- `easy imageSize`

**可变部分**（部分 workflow 才有）：
- `ImageConcatMulti` —— 2/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/3 个有
- `LayerUtility: PurgeVRAM` —— 2/3 个有
- `VAEEncode` —— 2/3 个有
- `VHS_LoadVideo` —— 2/3 个有
- `EmptyHunyuanLatentVideo` —— 1/3 个有
- `Label (rgthree)` —— 1/3 个有
- `MathExpression|pysssss` —— 1/3 个有
- `RH_LLMAPI_NODE` —— 1/3 个有
- `ShowText|pysssss` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 30 - 30 | 3 | 100% |
| Prompt 约束强度(CFG) | 6 | 6 - 6 | 3 | 100% |
| 采样算法 | uni_pc | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 0.65 | 0.65 - 1 | 3 | 78% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 30，观测区间 30 - 30，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 6，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 uni_pc，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 0.65，观测区间 0.65 - 1，3 个样本
