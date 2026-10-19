---
name: unknown_workflow_video_sampler_clip_112
type: Unknown Workflow
frequency: 5
level: strong
coverage: 1
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, KSampler, LoadImage, ModelSamplingSD3, SaveAnimatedWEBP, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/1948299325481844738.json, 视频生成/图生视频/1947841200348872705.json, 视频生成/图生视频/1930296715969204225.json, 视频生成/图生视频/1930315905924808705.json, 视频生成/图生视频/1930311373908250626.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_112

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/1948299325481844738.json、视频生成/图生视频/1947841200348872705.json、视频生成/图生视频/1930296715969204225.json、视频生成/图生视频/1930315905924808705.json、视频生成/图生视频/1930311373908250626.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：100%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `KSampler`
- `LoadImage`
- `ModelSamplingSD3`
- `SaveAnimatedWEBP`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `WanImageToVideo` —— 4/5 个有
- `UnetLoaderGGUF` —— 3/5 个有
- `LoadImageFromUrl` —— 2/5 个有
- `Note Plus (mtb)` —— 2/5 个有
- `UNETLoader` —— 2/5 个有
- `AnimateDiffCombine` —— 1/5 个有
- `CFGZeroStar` —— 1/5 个有
- `LoraLoaderModelOnly` —— 1/5 个有
- `SaveWEBM` —— 1/5 个有
- `WanFunControlToVideo` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 5 | 100% |
| Prompt 约束强度(CFG) | 6 | 6 - 6 | 5 | 100% |
| 采样算法 | uni_pc | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 6，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 uni_pc，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
