---
name: unknown_workflow_video_sampler_clip_76
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.870286
common_nodes: [CLIPLoader, CLIPTextEncode, KSamplerAdvanced, LoadImage, ModelSamplingSD3, PathchSageAttentionKJ, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/2003814653497122818.json, 视频生成/图生视频/1950190982249799682.json, 视频生成/图生视频/2025568584335892482.json, 视频生成/图生视频/1955196269809602562.json, 视频生成/图生视频/1949992607571206146.json, 视频生成/图生视频/2077340089688088578.json, 视频生成/文生视频/wan 2.2 图生视频 工作流+全节点注释_2077715652751745025.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_76

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/2003814653497122818.json、视频生成/图生视频/1950190982249799682.json、视频生成/图生视频/2025568584335892482.json、视频生成/图生视频/1955196269809602562.json、视频生成/图生视频/1949992607571206146.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSamplerAdvanced`
- `LoadImage`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 6/7 个有
- `UNETLoader` —— 6/7 个有
- `WanImageToVideo` —— 6/7 个有
- `LayerUtility: PurgeVRAM` —— 5/7 个有
- `ImageResize+` —— 4/7 个有
- `Int` —— 4/7 个有
- `PreviewImage` —— 4/7 个有
- `wanBlockSwap` —— 4/7 个有
- `SimpleMath+` —— 2/7 个有
- `CR Text` —— 1/7 个有
- `EmptyHunyuanLatentVideo` —— 1/7 个有
- `ImageScaleToTotalPixels` —— 1/7 个有
- `UnetLoaderGGUF` —— 1/7 个有
- `WanFirstLastFrameToVideo` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | increment | - | 7 | 57% |
| Prompt 约束强度(CFG) | 8 | 6 - 8 | 7 | 88% |
| 采样算法 | 1 | 1 - 3.5 | 7 | 36% |
| 调度器 | uni_pc | - | 7 | 57% |
| 重绘幅度 | simple | - | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 increment，7 个样本，一致性 57%
- Prompt 约束强度(CFG) 中位数 8，观测区间 6 - 8，7 个样本，取值集中（一致性 88%）
- 采样算法 中位数 1，观测区间 1 - 3.5，7 个样本，取值分散，一致性仅 36%
- 调度器 最常用 uni_pc，7 个样本，一致性 57%
- 重绘幅度 最常用 simple，7 个样本，一致性 100%
