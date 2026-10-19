---
name: unknown_workflow_sampler_clip_checkpoint_6
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.996625
common_nodes: [CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CheckpointLoaderSimple, JWInteger, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, ModelSamplingSD3, PathchSageAttentionKJ, SaveImage, WanImageToVideo]
problems: [Steps较低可能导致细节不足, 发现KSampler但没有VAEDecode]
missing: []
members: [视频生成/图生视频/1956025616472702978.json, 视频生成/图生视频/1958145251049353218.json, 视频生成/图生视频/2013897396320739330.json, 视频生成/图生视频/1962792289108115457.json, 视频生成/图生视频/1963949307806273538.json, 视频生成/图生视频/1959492715388022786.json, 视频生成/图生视频/1961655579871789057.json, 视频生成/文生视频/1958350616806494210.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_checkpoint_6

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/1956025616472702978.json、视频生成/图生视频/1958145251049353218.json、视频生成/图生视频/2013897396320739330.json、视频生成/图生视频/1962792289108115457.json、视频生成/图生视频/1963949307806273538.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：100%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple`
- `JWInteger`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `SaveImage`
- `WanImageToVideo`

**可变部分**（部分 workflow 才有）：
- `LoadLatent` —— 7/8 个有
- `VAEDecode` —— 7/8 个有
- `VAELoader` —— 7/8 个有
- `VHS_VideoCombine` —— 7/8 个有
- `CLIPLoader` —— 6/8 个有
- `SaveLatent` —— 6/8 个有
- `CR Prompt Text` —— 5/8 个有
- `LoraLoaderModelOnly` —— 5/8 个有
- `TT_img_enc` —— 3/8 个有
- `JWFloat` —— 2/8 个有
- `CR Text` —— 1/8 个有
- `EmptyHunyuanLatentVideo` —— 1/8 个有
- `Fast Groups Bypasser (rgthree)` —— 1/8 个有
- `TT_img_enc_v2` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 8 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | sa_solver | - | 8 | 75% |
| 调度器 | beta | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |
| 发现KSampler但没有VAEDecode | 1/8 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 sa_solver，8 个样本，一致性 75%
- 调度器 最常用 beta，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（9/8 个样本）：Steps较低可能导致细节不足
