---
name: unknown_workflow_video_clip_unet_7
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.9938
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/文生视频/Wan2.1-720P-SLG-文生视频_1902680529605668865.json, 视频生成/文生视频/Wan2.2文生视频_1985711544086474753.json, 视频生成/文生视频/Wan2.2文生视频_1997925759635324929.json, 视频生成/文生视频/Wan2.2文生视频_2007645581098881026.json, 视频生成/文生视频/Wan2.2文生视频工作流_1963477743868547073.json, 视频生成/文生视频/Wan2.2文生视频（优化版）_2067195635350196225.json, 视频生成/文生视频/wan2.2文生视频_2087718119883235330.json, 视频生成/文生视频/万象-文生图_1937731773860352001.json, 视频生成/文生视频/工作流视频篇1-阿里万相Wan2.2Al视频创作实战_2016870256769245185.json, 视频生成/文生视频/文生视频_1913407302773239810.json]
source: knowledge_consolidation
---

# unknown_workflow_video_clip_unet_7

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/文生视频/Wan2.1-720P-SLG-文生视频_1902680529605668865.json、视频生成/文生视频/Wan2.2文生视频_1985711544086474753.json、视频生成/文生视频/Wan2.2文生视频_1997925759635324929.json、视频生成/文生视频/Wan2.2文生视频_2007645581098881026.json、视频生成/文生视频/Wan2.2文生视频工作流_1963477743868547073.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：99%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingSD3` —— 9/10 个有
- `PathchSageAttentionKJ` —— 8/10 个有
- `KSamplerAdvanced` —— 7/10 个有
- `KSampler` —— 3/10 个有
- `WanVideoEnhanceAVideoKJ` —— 3/10 个有
- `WanVideoTeaCacheKJ` —— 3/10 个有
- `SaveWEBM` —— 1/10 个有
- `SkipLayerGuidanceWanVideo` —— 1/10 个有
- `TorchCompileModelWanVideo` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 10 | 60% |
| Prompt 约束强度(CFG) | 20 | 6 - 20 | 10 | 59% |
| 采样算法 | 3.5 | 3.5 - 3.5 | 7 | 100% |
| 调度器 | euler | - | 10 | 70% |
| 重绘幅度 | simple | - | 10 | 70% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，10 个样本，一致性 60%
- Prompt 约束强度(CFG) 中位数 20，观测区间 6 - 20，10 个样本
- 采样算法 中位数 3.5，观测区间 3.5 - 3.5，7 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，10 个样本，一致性 70%
- 重绘幅度 最常用 simple，10 个样本，一致性 70%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
