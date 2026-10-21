---
name: unknown_workflow_video_clip_unet_13
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.877429
common_nodes: [CLIPLoader, CLIPTextEncode, LoadImage, ModelSamplingSD3, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Comfyui教学第二期-文_图生视频_2008727256675389442.json, 视频生成/图生视频/2055499386683183105.json, 视频生成/图生视频/2018238424574070785.json, 视频生成/图生视频/1950190982249799682.json, 视频生成/图生视频/1953283354574712834.json, 视频生成/图生视频/2042575969071931394.json, 视频生成/图生视频/2043827022673219585.json]
source: knowledge_consolidation
---

# unknown_workflow_video_clip_unet_13

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/Comfyui教学第二期-文_图生视频_2008727256675389442.json、视频生成/图生视频/2055499386683183105.json、视频生成/图生视频/2018238424574070785.json、视频生成/图生视频/1950190982249799682.json、视频生成/图生视频/1953283354574712834.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `LoadImage`
- `ModelSamplingSD3`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `KSamplerAdvanced` —— 6/7 个有
- `WanImageToVideo` —— 6/7 个有
- `Fast Groups Bypasser (rgthree)` —— 4/7 个有
- `EmptyHunyuanLatentVideo` —— 3/7 个有
- `ImageResizeKJv2` —— 3/7 个有
- `LoraLoader` —— 3/7 个有
- `PathchSageAttentionKJ` —— 3/7 个有
- `CM_IntToFloat` —— 2/7 个有
- `INTConstant` —— 2/7 个有
- `LayerUtility: PurgeVRAM V2` —— 2/7 个有
- `PreviewImage` —— 2/7 个有
- `SimpleMath+` —— 2/7 个有
- `KSampler` —— 1/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/7 个有
- `RunningHub Deepcleaner` —— 1/7 个有
- `WanFirstLastFrameToVideo` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 7 | 43% |
| Prompt 约束强度(CFG) | 6 | 1 - 20 | 7 | 24% |
| 采样算法 | 1 | 1 - 3.5 | 6 | 36% |
| 调度器 | euler | - | 7 | 86% |
| 重绘幅度 | simple | - | 7 | 86% |
| LoRA 模型强度 | 1 | 1 - 1 | 3 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 最常用 randomize，7 个样本，一致性 43%
- Prompt 约束强度(CFG) 中位数 6，观测区间 1 - 20，7 个样本，取值分散，一致性仅 24%
- 采样算法 中位数 1，观测区间 1 - 3.5，6 个样本，取值分散，一致性仅 36%
- 调度器 最常用 euler，7 个样本，一致性 86%
- 重绘幅度 最常用 simple，7 个样本，一致性 86%
- LoRA 模型强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
