---
name: unknown_workflow_video_clip_unet_11
type: Unknown Workflow
frequency: 8
level: weak
coverage: 0.898875
common_nodes: [CLIPLoader, CLIPTextEncode, LoadImage, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanImageToVideo]
problems: []
missing: []
members: [视频生成/图生视频/2041766400284434433.json, 视频生成/图生视频/1987801301234987009.json, 视频生成/图生视频/2066459393683705858.json, 视频生成/文生视频/1949440813809467394.json, 视频生成/文生视频/1950385703961149441.json, 视频生成/文生视频/Running-Wan2.2图生视频_文生视频_2041761742291734530.json, 视频生成/文生视频/WAN2.2 文生视频、图生视频工作流_2018552915408982018.json, 视频生成/文生视频/Wan2.2&lightx2v加速_2072999665609777152.json]
source: knowledge_consolidation
---

# unknown_workflow_video_clip_unet_11

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/2041766400284434433.json、视频生成/图生视频/1987801301234987009.json、视频生成/图生视频/2066459393683705858.json、视频生成/文生视频/1949440813809467394.json、视频生成/文生视频/1950385703961149441.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `LoadImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideo`

**可变部分**（部分 workflow 才有）：
- `PathchSageAttentionKJ` —— 7/8 个有
- `EmptyHunyuanLatentVideo` —— 6/8 个有
- `KSamplerAdvanced` —— 6/8 个有
- `LoraLoaderModelOnly` —— 6/8 个有
- `ModelSamplingSD3` —— 6/8 个有
- `ModelPatchTorchSettings` —— 5/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/8 个有
- `CFGZeroStarAndInit` —— 2/8 个有
- `LoadVideo` —— 2/8 个有
- `PlaySound|pysssss` —— 2/8 个有
- `WanMoeKSampler` —— 2/8 个有
- `WanVideoEnhanceAVideoKJ` —— 2/8 个有
- `PreviewImage` —— 1/8 个有
- `easy int` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 8 | 75% |
| Prompt 约束强度(CFG) | 8 | 3 - 10 | 8 | 63% |
| 采样算法 | 1 | 1 - 3.5 | 8 | 33% |
| 调度器 | euler | - | 8 | 50% |
| 重绘幅度 | simple | - | 8 | 50% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，8 个样本，一致性 75%
- Prompt 约束强度(CFG) 中位数 8，观测区间 3 - 10，8 个样本
- 采样算法 中位数 1，观测区间 1 - 3.5，8 个样本，取值分散，一致性仅 33%
- 调度器 最常用 euler，8 个样本，一致性 50%
- 重绘幅度 最常用 simple，8 个样本，一致性 50%
