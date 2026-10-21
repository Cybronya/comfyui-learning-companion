---
name: unknown_workflow_video_lora_clip_13
type: Unknown Workflow
frequency: 2
level: weak
coverage: 1
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, LoraLoaderModelOnly, PathchSageAttentionKJ, UnetLoaderGGUF, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/文生视频/1958137179354574850.json, 视频生成/文生视频/wan2.2文生视频工作流_1992207253564444674.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_clip_13

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/文生视频/1958137179354574850.json、视频生成/文生视频/wan2.2文生视频工作流_1992207253564444674.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：100%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `LoraLoaderModelOnly`
- `PathchSageAttentionKJ`
- `UnetLoaderGGUF`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `KSamplerAdvanced` —— 1/2 个有
- `ModelSamplingSD3` —— 1/2 个有
- `WanMoeKSampler` —— 1/2 个有
- `wanBlockSwap` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 2 | 50% |
| Prompt 约束强度(CFG) | 4 | - | 2 | 100% |
| 采样算法 | 1 | - | 2 | 100% |
| 调度器 | 1 | - | 1 | 100% |
| 重绘幅度 | euler | - | 2 | 50% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，2 个样本，一致性 50%
- Prompt 约束强度(CFG) 中位数 4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 重绘幅度 最常用 euler，2 个样本，一致性 50%
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
