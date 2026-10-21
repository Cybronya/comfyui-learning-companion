---
name: unknown_workflow_sampler_clip_unet_42
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 1
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, KSampler, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/1951460131294883841.json, 视频生成/文生视频/Wan2.1+文生视频高清动态视频_2010596616985649154.json, 视频生成/文生视频/1934444729025327105.json, 视频生成/文生视频/1935893378293035010.json, 视频生成/文生视频/Wan2.2文生视频工作流_2011439259349159938.json, 视频生成/文生视频/Wan2.2文生视频工作流_2012090867787501569.json, 视频生成/文生视频/1909164954489135106.json, 视频生成/文生视频/wan2.2_t2v 文生视频_2058371729084469249.json, 视频生成/文生视频/1901967053463379970.json, 视频生成/文生视频/1937731773860352001.json, 视频生成/文生视频/1913407302773239810.json, 视频生成/文生视频/1923315554449281025.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_42

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/文生视频/1951460131294883841.json、视频生成/文生视频/Wan2.1+文生视频高清动态视频_2010596616985649154.json、视频生成/文生视频/1934444729025327105.json、视频生成/文生视频/1935893378293035010.json、视频生成/文生视频/Wan2.2文生视频工作流_2011439259349159938.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：100%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `KSampler`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `VHS_VideoCombine` —— 11/12 个有
- `ModelSamplingSD3` —— 5/12 个有
- `WanVideoTeaCacheKJ` —— 4/12 个有
- `WanVideoEnhanceAVideoKJ` —— 3/12 个有
- `SaveWEBM` —— 2/12 个有
- `Label (rgthree)` —— 1/12 个有
- `LoraLoader` —— 1/12 个有
- `SaveImage` —— 1/12 个有
- `VideoCombine_Adv` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 4 - 45 | 12 | 47% |
| Prompt 约束强度(CFG) | 6 | 1 - 6 | 12 | 54% |
| 采样算法 | uni_pc | - | 12 | 67% |
| 调度器 | simple | - | 12 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 30，观测区间 4 - 45，12 个样本，取值分散，一致性仅 47%
- Prompt 约束强度(CFG) 中位数 6，观测区间 1 - 6，12 个样本
- 采样算法 最常用 uni_pc，12 个样本，一致性 67%
- 调度器 最常用 simple，12 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
