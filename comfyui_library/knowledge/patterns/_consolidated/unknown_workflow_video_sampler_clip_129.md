---
name: unknown_workflow_video_sampler_clip_129
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.95375
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, KSampler, LoadImage, VAEDecode, VAELoader, VHS_VideoCombine, WanImageToVideo]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/1989951203440291842.json, 视频生成/图生视频/1935875055609896962.json, 视频生成/图生视频/1898354232771170306.json, 视频生成/图生视频/2015621003442921473.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_129

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/1989951203440291842.json、视频生成/图生视频/1935875055609896962.json、视频生成/图生视频/1898354232771170306.json、视频生成/图生视频/2015621003442921473.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `KSampler`
- `LoadImage`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideo`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingSD3` —— 3/4 个有
- `UnetLoaderGGUF` —— 3/4 个有
- `LoraLoaderModelOnly` —— 2/4 个有
- `PathchSageAttentionKJ` —— 2/4 个有
- `WanVideoTeaCacheKJ` —— 2/4 个有
- `CR Text` —— 1/4 个有
- `EG_FX_BDAPI` —— 1/4 个有
- `INTConstant` —— 1/4 个有
- `ImageResizeKJv2` —— 1/4 个有
- `RIFE VFI` —— 1/4 个有
- `SaveAnimatedWEBP` —— 1/4 个有
- `ShowText|pysssss` —— 1/4 个有
- `UNETLoader` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 16 | 5 - 20 | 4 | 56% |
| Prompt 约束强度(CFG) | 3.5 | 1 - 6 | 4 | 29% |
| 采样算法 | uni_pc | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 16，观测区间 5 - 20，4 个样本
- Prompt 约束强度(CFG) 中位数 3.5，观测区间 1 - 6，4 个样本，取值分散，一致性仅 29%
- 采样算法 最常用 uni_pc，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
