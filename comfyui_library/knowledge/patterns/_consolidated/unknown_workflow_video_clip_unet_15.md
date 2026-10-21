---
name: unknown_workflow_video_clip_unet_15
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.945143
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, ModelSamplingSD3, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/1954771341195960322.json, 视频生成/文生视频/WAN2.2 文生视频、图生视频工作流_2042210649249423362.json, 视频生成/文生视频/1950186717304242177.json, 视频生成/文生视频/1952571860477259777.json, 视频生成/文生视频/1963477743868547073.json, 视频生成/文生视频/Wan2.2文生视频（优化版）_2067195635350196225.json, 视频生成/文生视频/1953331235240202241.json]
source: knowledge_consolidation
---

# unknown_workflow_video_clip_unet_15

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/文生视频/1954771341195960322.json、视频生成/文生视频/WAN2.2 文生视频、图生视频工作流_2042210649249423362.json、视频生成/文生视频/1950186717304242177.json、视频生成/文生视频/1952571860477259777.json、视频生成/文生视频/1963477743868547073.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `ModelSamplingSD3`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 5/7 个有
- `WanImageToVideo` —— 5/7 个有
- `KSamplerAdvanced` —— 4/7 个有
- `PathchSageAttentionKJ` —— 4/7 个有
- `Fast Groups Bypasser (rgthree)` —— 3/7 个有
- `KSampler` —— 3/7 个有
- `LoraLoader` —— 3/7 个有
- `ModelPatchTorchSettings` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 7 | 57% |
| Prompt 约束强度(CFG) | 8 | 1 - 20 | 7 | 7% |
| 采样算法 | 3.5 | 3.5 - 3.5 | 4 | 100% |
| 调度器 | euler | - | 7 | 57% |
| 重绘幅度 | simple | - | 7 | 57% |
| LoRA 模型强度 | 1 | 1 - 1 | 3 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 最常用 randomize，7 个样本，一致性 57%
- Prompt 约束强度(CFG) 中位数 8，观测区间 1 - 20，7 个样本，取值分散，一致性仅 7%
- 采样算法 中位数 3.5，观测区间 3.5 - 3.5，4 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，7 个样本，一致性 57%
- 重绘幅度 最常用 simple，7 个样本，一致性 57%
- LoRA 模型强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
- 高发问题（6/7 个样本）：Steps较低可能导致细节不足
