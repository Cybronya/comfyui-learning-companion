---
name: unknown_workflow_video_clip_unet_10
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.947625
common_nodes: [CLIPLoader, CLIPTextEncode, LoadImage, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/2051154615328092161.json, 视频生成/图生视频/1913510854523060225.json, 视频生成/图生视频/1947317037666291713.json, 视频生成/图生视频/1986706185669832705.json, 视频生成/图生视频/2029757199156776962.json, 视频生成/图生视频/2011093205202247682.json, 视频生成/图生视频/1984504641570357250.json, 视频生成/图生视频/2030191511907864578.json]
source: knowledge_consolidation
---

# unknown_workflow_video_clip_unet_10

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/2051154615328092161.json、视频生成/图生视频/1913510854523060225.json、视频生成/图生视频/1947317037666291713.json、视频生成/图生视频/1986706185669832705.json、视频生成/图生视频/2029757199156776962.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `LoadImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `CLIPVisionEncode` —— 7/8 个有
- `CLIPVisionLoader` —— 7/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 6/8 个有
- `ModelSamplingSD3` —— 6/8 个有
- `KSamplerAdvanced` —— 5/8 个有
- `WanImageToVideo` —— 5/8 个有
- `GetNode` —— 3/8 个有
- `ImageResize+` —— 3/8 个有
- `ModelPatchTorchSettings` —— 3/8 个有
- `PathchSageAttentionKJ` —— 3/8 个有
- `SetNode` —— 3/8 个有
- `Text Multiline` —— 3/8 个有
- `WanFirstLastFrameToVideo` —— 3/8 个有
- `easy cleanGpuUsed` —— 3/8 个有
- `KSampler` —— 2/8 个有
- `MultiplePathsInput` —— 2/8 个有
- `Qwen3_VQA` —— 2/8 个有
- `WanMoeKSampler` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 8 | 50% |
| Prompt 约束强度(CFG) | 6 | 1 - 10 | 8 | 54% |
| 采样算法 | 1 | 1 - 1 | 6 | 100% |
| 调度器 | euler | - | 8 | 38% |
| 重绘幅度 | simple | - | 8 | 62% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，8 个样本，一致性 50%
- Prompt 约束强度(CFG) 中位数 6，观测区间 1 - 10，8 个样本
- 采样算法 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，8 个样本，一致性 38%
- 重绘幅度 最常用 simple，8 个样本，一致性 62%
