---
name: unknown_workflow_video_clip_unet_15
type: Unknown Workflow
frequency: 6
level: weak
coverage: 0.91
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, ModelSamplingSD3, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: [easy cleanGpuUsed]
members: [视频生成/文生视频/1973586919907004418.json, 视频生成/文生视频/1973586939590873089.json, 视频生成/文生视频/1974515256741507074.json, 视频生成/文生视频/1952913163996041218.json, 视频生成/文生视频/1952267409933717505.json, 视频生成/文生视频/电商模特IP Lora 视频版 wan2.2_1985602072307552257.json]
source: knowledge_consolidation
---

# unknown_workflow_video_clip_unet_15

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/文生视频/1973586919907004418.json、视频生成/文生视频/1973586939590873089.json、视频生成/文生视频/1974515256741507074.json、视频生成/文生视频/1952913163996041218.json、视频生成/文生视频/1952267409933717505.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `ModelSamplingSD3`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `KSamplerAdvanced` —— 5/6 个有
- `LoraLoaderModelOnly` —— 5/6 个有
- `PathchSageAttentionKJ` —— 5/6 个有
- `LayerUtility: PurgeVRAM` —— 3/6 个有
- `Text` —— 3/6 个有
- `CFGZeroStar` —— 2/6 个有
- `WanVideoNAG` —— 2/6 个有
- `easy cleanGpuUsed` —— 2/6 个有
- `easy seed` —— 2/6 个有
- `PrimitiveStringMultiline` —— 1/6 个有
- `TextBox` —— 1/6 个有
- `WanMoeKSampler` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 6 | 83% |
| Prompt 约束强度(CFG) | 8 | 6 - 20 | 6 | 52% |
| 采样算法 | 1 | 1 - 3.5 | 6 | 34% |
| 调度器 | lcm | - | 6 | 50% |
| 重绘幅度 | simple | - | 6 | 83% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，6 个样本，一致性 83%
- Prompt 约束强度(CFG) 中位数 8，观测区间 6 - 20，6 个样本
- 采样算法 中位数 1，观测区间 1 - 3.5，6 个样本，取值分散，一致性仅 34%
- 调度器 最常用 lcm，6 个样本，一致性 50%
- 重绘幅度 最常用 simple，6 个样本，一致性 83%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
- 这些节点还没有知识卡，系统对它们的理解有限：easy cleanGpuUsed
