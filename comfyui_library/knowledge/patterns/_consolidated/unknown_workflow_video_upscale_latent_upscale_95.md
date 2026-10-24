---
name: unknown_workflow_video_upscale_latent_upscale_95
type: Unknown Workflow
frequency: 4
level: weak
coverage: 0.672
common_nodes: [CLIPTextEncode, DualCLIPLoader, HunyuanVideo15LatentUpscaleWithModel, HunyuanVideo15SuperResolution, KSamplerAdvanced, LatentUpscaleModelLoader, LoadImage, ModelSamplingSD3, PathchSageAttentionKJ, UNETLoader, VAEDecodeTiled, VAELoader, VHS_VideoCombine]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/hunyuan_video_1.5_step_distilled_720p_i2v_1997124192296439809.json, 视频生成/图生视频/video_hunyuan_video_1.5_720p_i2v_1992627828135096321.json, 视频生成/图生视频/图生视频I2V  混元1.5_1998575871269175297.json, 视频生成/文生视频/video_hunyuan_video_1.5_720p_t2v_1992624616432619521.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_95

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/hunyuan_video_1.5_step_distilled_720p_i2v_1997124192296439809.json、视频生成/图生视频/video_hunyuan_video_1.5_720p_i2v_1992627828135096321.json、视频生成/图生视频/图生视频I2V  混元1.5_1998575871269175297.json、视频生成/文生视频/video_hunyuan_video_1.5_720p_t2v_1992624616432619521.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：67%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `HunyuanVideo15LatentUpscaleWithModel`
- `HunyuanVideo15SuperResolution`
- `KSamplerAdvanced`
- `LatentUpscaleModelLoader`
- `LoadImage`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `AILab_QwenVL` —— 3/4 个有
- `CLIPVisionEncode` —— 3/4 个有
- `CLIPVisionLoader` —— 3/4 个有
- `GetNode` —— 3/4 个有
- `HunyuanVideo15ImageToVideo` —— 3/4 个有
- `KSampler` —— 3/4 个有
- `PreviewAny` —— 3/4 个有
- `SetNode` —— 3/4 个有
- `VAEDecode` —— 3/4 个有
- `ImageResizeKJv2` —— 2/4 个有
- `EmptyHunyuanVideo15Latent` —— 1/4 个有
- `GetImageSize` —— 1/4 个有
- `Int` —— 1/4 个有
- `MultiplicationNode` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 4 | 75% |
| Prompt 约束强度(CFG) | 8 | 1 - 50 | 4 | 0% |
| 采样算法 | 1 | 1 - 1 | 3 | 100% |
| 调度器 | euler | - | 4 | 75% |
| 重绘幅度 | simple | - | 4 | 75% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 最常用 randomize，4 个样本，一致性 75%
- Prompt 约束强度(CFG) 中位数 8，观测区间 1 - 50，4 个样本，取值分散，一致性仅 0%
- 采样算法 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，4 个样本，一致性 75%
- 重绘幅度 最常用 simple，4 个样本，一致性 75%
- 风险：Prompt 约束强度(CFG) 观测到 50，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
