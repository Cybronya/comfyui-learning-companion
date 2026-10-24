---
name: unknown_workflow_video_clip_unet_8
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.993111
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/文生视频/Wan2.1-720P-SLG-文生视频_1902680529605668865.json, 视频生成/文生视频/Wan2.2文生视频_1985711544086474753.json, 视频生成/文生视频/Wan2.2文生视频_1997925759635324929.json, 视频生成/文生视频/Wan2.2文生视频_2007645581098881026.json, 视频生成/文生视频/Wan2.2文生视频工作流_1963477743868547073.json, 视频生成/文生视频/Wan2.2文生视频（优化版）_2067195635350196225.json, 视频生成/文生视频/wan2.2文生视频_2087718119883235330.json, 视频生成/文生视频/万象-文生图_1937731773860352001.json, 视频生成/文生视频/文生视频_1913407302773239810.json]
source: knowledge_consolidation
---

# unknown_workflow_video_clip_unet_8

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/文生视频/Wan2.1-720P-SLG-文生视频_1902680529605668865.json、视频生成/文生视频/Wan2.2文生视频_1985711544086474753.json、视频生成/文生视频/Wan2.2文生视频_1997925759635324929.json、视频生成/文生视频/Wan2.2文生视频_2007645581098881026.json、视频生成/文生视频/Wan2.2文生视频工作流_1963477743868547073.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：99%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingSD3` —— 8/9 个有
- `PathchSageAttentionKJ` —— 7/9 个有
- `KSamplerAdvanced` —— 6/9 个有
- `KSampler` —— 3/9 个有
- `WanVideoEnhanceAVideoKJ` —— 3/9 个有
- `WanVideoTeaCacheKJ` —— 3/9 个有
- `SaveWEBM` —— 1/9 个有
- `SkipLayerGuidanceWanVideo` —— 1/9 个有
- `TorchCompileModelWanVideo` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 9 | 56% |
| Prompt 约束强度(CFG) | 20 | 6 - 20 | 9 | 57% |
| 采样算法 | 3.5 | 3.5 - 3.5 | 6 | 100% |
| 调度器 | euler | - | 9 | 67% |
| 重绘幅度 | simple | - | 9 | 67% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，9 个样本，一致性 56%
- Prompt 约束强度(CFG) 中位数 20，观测区间 6 - 20，9 个样本
- 采样算法 中位数 3.5，观测区间 3.5 - 3.5，6 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，9 个样本，一致性 67%
- 重绘幅度 最常用 simple，9 个样本，一致性 67%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
