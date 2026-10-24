---
name: unknown_workflow_video_clip_unet_13
type: Unknown Workflow
frequency: 5
level: weak
coverage: 0.945
common_nodes: [CLIPLoader, CLIPTextEncode, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, PathchSageAttentionKJ, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/Wan2.2 5B图生视频工作流（官方版）V2_1949897152581558273.json, 视频生成/图生视频/Wan2.2-5B+lighx2v 快速图生视频工作流-官方版_1950103025572601857.json, 视频生成/图生视频/wan2.2 WanMoeKsampler 图生视频_1955829466150965249.json, 视频生成/图生视频/wan2.2(图生视频)_2041766400284434433.json, 视频生成/文生视频/Running-Wan2.2图生视频_文生视频_2041761742291734530.json]
source: knowledge_consolidation
---

# unknown_workflow_video_clip_unet_13

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/Wan2.2 5B图生视频工作流（官方版）V2_1949897152581558273.json、视频生成/图生视频/Wan2.2-5B+lighx2v 快速图生视频工作流-官方版_1950103025572601857.json、视频生成/图生视频/wan2.2 WanMoeKsampler 图生视频_1955829466150965249.json、视频生成/图生视频/wan2.2(图生视频)_2041766400284434433.json、视频生成/文生视频/Running-Wan2.2图生视频_文生视频_2041761742291734530.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：94%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `PathchSageAttentionKJ`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 4/5 个有
- `JWInteger` —— 3/5 个有
- `ModelSamplingSD3` —— 3/5 个有
- `WanImageToVideo` —— 3/5 个有
- `WanMoeKSampler` —— 3/5 个有
- `EmptyHunyuanLatentVideo` —— 2/5 个有
- `KSampler` —— 2/5 个有
- `ModelPatchTorchSettings` —— 2/5 个有
- `PlaySound|pysssss` —— 2/5 个有
- `Wan22ImageToVideoLatent` —— 2/5 个有
- `CR Text` —— 1/5 个有
- `PreviewImage` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 5 | 40% |
| Prompt 约束强度(CFG) | 3 | 1 - 10 | 5 | 30% |
| 采样算法 | 1 | 1 - 3.5 | 3 | 36% |
| 调度器 | 1 | 1 - 1 | 3 | 100% |
| 重绘幅度 | 1 | - | 5 | 40% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，5 个样本，一致性 40%
- Prompt 约束强度(CFG) 中位数 3，观测区间 1 - 10，5 个样本，取值分散，一致性仅 30%
- 采样算法 中位数 1，观测区间 1 - 3.5，3 个样本，取值分散，一致性仅 36%
- 调度器 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 重绘幅度 最常用 1，5 个样本，一致性 40%
