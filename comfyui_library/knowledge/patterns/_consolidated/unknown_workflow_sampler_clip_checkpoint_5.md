---
name: unknown_workflow_sampler_clip_checkpoint_5
type: Unknown Workflow
frequency: 12
level: strong
coverage: 1
common_nodes: [CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CheckpointLoaderSimple, KSampler, LoadImage, ModelSamplingSD3, PathchSageAttentionKJ, WanImageToVideo]
problems: [Steps较低可能导致细节不足, 发现KSampler但没有VAEDecode]
missing: []
members: [视频生成/图生视频/1956025616472702978.json, 视频生成/图生视频/1955969682358632450.json, 视频生成/图生视频/1958143493149511681.json, 视频生成/图生视频/1958905954660200450.json, 视频生成/图生视频/1962517255911288834.json, 视频生成/图生视频/1960545575466917890.json, 视频生成/图生视频/1958145251049353218.json, 视频生成/图生视频/2013897396320739330.json, 视频生成/图生视频/1962792289108115457.json, 视频生成/图生视频/1963949307806273538.json, 视频生成/图生视频/1959492715388022786.json, 视频生成/图生视频/1961655579871789057.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_checkpoint_5

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/图生视频/1956025616472702978.json、视频生成/图生视频/1955969682358632450.json、视频生成/图生视频/1958143493149511681.json、视频生成/图生视频/1958905954660200450.json、视频生成/图生视频/1962517255911288834.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：100%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple`
- `KSampler`
- `LoadImage`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `WanImageToVideo`

**可变部分**（部分 workflow 才有）：
- `JWInteger` —— 11/12 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 11/12 个有
- `VAEDecode` —— 11/12 个有
- `VHS_VideoCombine` —— 11/12 个有
- `SaveImage` —— 8/12 个有
- `CLIPLoader` —— 7/12 个有
- `LoadLatent` —— 6/12 个有
- `LoraLoaderModelOnly` —— 6/12 个有
- `VAELoader` —— 6/12 个有
- `CR Prompt Text` —— 5/12 个有
- `SaveLatent` —— 5/12 个有
- `ImageFromBatch+` —— 4/12 个有
- `TT_img_enc` —— 3/12 个有
- `JWFloat` —— 2/12 个有
- `ImageResizeKJv2` —— 1/12 个有
- `RandomInt` —— 1/12 个有
- `TT_img_enc_v2` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 12 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 12 | 100% |
| 采样算法 | sa_solver | - | 12 | 83% |
| 调度器 | beta | - | 12 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 12/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |
| 发现KSampler但没有VAEDecode | 1/12 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，12 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 sa_solver，12 个样本，一致性 83%
- 调度器 最常用 beta，12 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 高发问题（12/12 个样本）：Steps较低可能导致细节不足
