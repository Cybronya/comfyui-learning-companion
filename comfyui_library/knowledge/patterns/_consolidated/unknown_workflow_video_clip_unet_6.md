---
name: unknown_workflow_video_clip_unet_6
type: Unknown Workflow
frequency: 10
level: strong
coverage: 0.5821
common_nodes: [CLIPLoader, CLIPTextEncode, INTConstant, ModelPatchTorchSettings, PathchSageAttentionKJ, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, easy cleanGpuUsed]
problems: []
missing: [RIFE VFI, easy cleanGpuUsed]
members: [图片生成/文生图/1979072068958457857.json, 视频生成/图生视频/2035278593374298113.json, 视频生成/图生视频/1985933619749367810.json, 视频生成/图生视频/1992224912406368258.json, 视频生成/图生视频/2011699908318859265.json, 视频生成/图生视频/1981353708422348802.json, 视频生成/图生视频/1996506562493554690.json, 视频生成/图生视频/2009254393203396610.json, 视频生成/图生视频/WAN2.2图生视频终极版_2083953699881316354.json, 视频生成/图生视频/1981254959582928897.json]
source: knowledge_consolidation
---

# unknown_workflow_video_clip_unet_6

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/文生图/1979072068958457857.json、视频生成/图生视频/2035278593374298113.json、视频生成/图生视频/1985933619749367810.json、视频生成/图生视频/1992224912406368258.json、视频生成/图生视频/2011699908318859265.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：58%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `INTConstant`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `Int` —— 9/10 个有
- `KSamplerAdvanced` —— 9/10 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 9/10 个有
- `LoadImage` —— 9/10 个有
- `ModelSamplingSD3` —— 9/10 个有
- `WanImageToVideo` —— 9/10 个有
- `PreviewImage` —— 8/10 个有
- `RIFE VFI` —— 8/10 个有
- `Fast Groups Bypasser (rgthree)` —— 7/10 个有
- `LoraLoaderModelOnly` —— 7/10 个有
- `wanBlockSwap` —— 7/10 个有
- `CR Text` —— 2/10 个有
- `ImageResizeKJv2` —— 2/10 个有
- `SetNode` —— 2/10 个有
- `CompressImages` —— 1/10 个有
- `CreateVideo` —— 1/10 个有
- `Fast Groups Muter (rgthree)` —— 1/10 个有
- `GetImagesFromBatchIndexed` —— 1/10 个有
- `GetNode` —— 1/10 个有
- `PainterI2V` —— 1/10 个有
- `RHHiddenNodes` —— 1/10 个有
- `UnetLoaderGGUF` —— 1/10 个有
- `WanMoeKSampler` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 10 | 80% |
| Prompt 约束强度(CFG) | 4 | 4 - 6 | 10 | 86% |
| 采样算法 | 1 | 1 - 1 | 10 | 100% |
| 调度器 | euler | - | 10 | 90% |
| 重绘幅度 | normal | - | 10 | 80% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，10 个样本，一致性 80%
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 6，10 个样本，取值集中（一致性 86%）
- 采样算法 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，10 个样本，一致性 90%
- 重绘幅度 最常用 normal，10 个样本，一致性 80%
- 这些节点还没有知识卡，系统对它们的理解有限：RIFE VFI、easy cleanGpuUsed
