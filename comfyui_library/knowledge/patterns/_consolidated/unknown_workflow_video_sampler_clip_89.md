---
name: unknown_workflow_video_sampler_clip_89
type: Unknown Workflow
frequency: 6
level: strong
coverage: 1
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, JWInteger, KSampler, ModelSamplingSD3, PathchSageAttentionKJ, VAEDecode, VHS_VideoCombine]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/2035333116356726786.json, 视频生成/图生视频/2035335136459362305.json, 视频生成/图生视频/1992982649104957441.json, 视频生成/图生视频/1997950428413353986.json, 视频生成/图生视频/1967057981361807361.json, 视频生成/图生视频/1962791442060062722.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_89

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/2035333116356726786.json、视频生成/图生视频/2035335136459362305.json、视频生成/图生视频/1992982649104957441.json、视频生成/图生视频/1997950428413353986.json、视频生成/图生视频/1967057981361807361.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：100%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `JWInteger`
- `KSampler`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `VAEDecode`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `CLIPVisionEncode` —— 5/6 个有
- `CLIPVisionLoader` —— 5/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/6 个有
- `LoadImage` —— 5/6 个有
- `LoraLoaderModelOnly` —— 5/6 个有
- `WanImageToVideo` —— 5/6 个有
- `CR Prompt Text` —— 4/6 个有
- `CLIPLoader` —— 3/6 个有
- `ImageFromBatch+` —— 2/6 个有
- `ModelPatchTorchSettings` —— 2/6 个有
- `SaveImage` —— 2/6 个有
- `wanBlockSwap` —— 2/6 个有
- `DuckHideNode` —— 1/6 个有
- `EmptyHunyuanLatentVideo` —— 1/6 个有
- `SaveLatent` —— 1/6 个有
- `TT_img_enc` —— 1/6 个有
- `TT_img_enc_v2` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 6 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | sa_solver | - | 6 | 83% |
| 调度器 | beta | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 sa_solver，6 个样本，一致性 83%
- 调度器 最常用 beta，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足
