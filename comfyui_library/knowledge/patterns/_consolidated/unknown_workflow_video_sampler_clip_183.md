---
name: unknown_workflow_video_sampler_clip_183
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.941
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, ImageResizeKJ, KSampler, LoadImage, RIFE VFI, UNETLoader, VAEDecodeTiled, VAELoader, VHS_VideoCombine, WanImageToVideo]
problems: [发现KSampler但没有VAEDecode]
missing: []
members: [视频生成/图生视频/1896469685087109121.json, 视频生成/图生视频/1927363115573481473.json, 视频生成/图生视频/1986674575624859650.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_183

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/1896469685087109121.json、视频生成/图生视频/1927363115573481473.json、视频生成/图生视频/1986674575624859650.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `ImageResizeKJ`
- `KSampler`
- `LoadImage`
- `RIFE VFI`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideo`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `WanVideoTeaCacheKJ` —— 2/3 个有
- `CFGZeroStarAndInit` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 30 - 30 | 3 | 100% |
| Prompt 约束强度(CFG) | 6 | 6 - 6 | 3 | 100% |
| 采样算法 | uni_pc | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| 发现KSampler但没有VAEDecode | 3/3 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 30，观测区间 30 - 30，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 6，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 uni_pc，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：发现KSampler但没有VAEDecode
