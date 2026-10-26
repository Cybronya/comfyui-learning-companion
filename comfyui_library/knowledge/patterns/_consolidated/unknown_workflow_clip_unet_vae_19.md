---
name: unknown_workflow_clip_unet_vae_19
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.960667
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, SaveAnimatedWEBP, SaveImage, SaveWEBM, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/text_to_video_wan22_14B官方优化版_1950503480169517058.json, 视频生成/文生视频/【AI由北】Wan2.1 文生视频 全能版_1927645156290215937.json, 视频生成/文生视频/通义万相WAN2.1文生视频基础工作流_1924310147001143297.json]
source: knowledge_consolidation
---

# unknown_workflow_clip_unet_vae_19

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/文生视频/text_to_video_wan22_14B官方优化版_1950503480169517058.json、视频生成/文生视频/【AI由北】Wan2.1 文生视频 全能版_1927645156290215937.json、视频生成/文生视频/通义万相WAN2.1文生视频基础工作流_1924310147001143297.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `SaveAnimatedWEBP`
- `SaveImage`
- `SaveWEBM`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `KSampler` —— 2/3 个有
- `ModelSamplingSD3` —— 2/3 个有
- `KSamplerAdvanced` —— 1/3 个有
- `LoadImage` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 6 | 6 - 20 | 3 | 38% |
| 采样算法 | uni_pc | - | 3 | 67% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 30，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 20，3 个样本，取值分散，一致性仅 38%
- 采样算法 最常用 uni_pc，3 个样本，一致性 67%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
