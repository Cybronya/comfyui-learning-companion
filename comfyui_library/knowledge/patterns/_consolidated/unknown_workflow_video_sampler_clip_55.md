---
name: unknown_workflow_video_sampler_clip_55
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.547333
common_nodes: [CLIPLoader, CLIPTextEncode, INTConstant, KSamplerAdvanced, LoadImage, ModelPatchTorchSettings, ModelSamplingSD3, PathchSageAttentionKJ, PreviewImage, RIFE VFI, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, easy cleanGpuUsed]
problems: []
missing: []
members: [视频生成/图生视频/2011699908318859265.json, 视频生成/图生视频/1981353708422348802.json, 视频生成/图生视频/1996506562493554690.json, 视频生成/图生视频/2009254393203396610.json, 视频生成/图生视频/1996163879166263297.json, 视频生成/图生视频/2017121557004423170.json, 视频生成/图生视频/2001276328982740993.json, 视频生成/图生视频/1998328006265438210.json, 视频生成/图生视频/1997659149460770818.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_55

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/2011699908318859265.json、视频生成/图生视频/1981353708422348802.json、视频生成/图生视频/1996506562493554690.json、视频生成/图生视频/2009254393203396610.json、视频生成/图生视频/1996163879166263297.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：55%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `INTConstant`
- `KSamplerAdvanced`
- `LoadImage`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `RIFE VFI`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJv2` —— 7/9 个有
- `Int` —— 7/9 个有
- `wanBlockSwap` —— 7/9 个有
- `GetNode` —— 6/9 个有
- `LoraLoaderModelOnly` —— 6/9 个有
- `SetNode` —— 6/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/9 个有
- `CLIPVisionEncode` —— 4/9 个有
- `CLIPVisionLoader` —— 4/9 个有
- `Fast Groups Bypasser (rgthree)` —— 4/9 个有
- `easy clearCacheAll` —— 4/9 个有
- `PainterI2V` —— 3/9 个有
- `WanFirstLastFrameToVideo` —— 3/9 个有
- `WanImageToVideo` —— 3/9 个有
- `ImageConcatMulti` —— 2/9 个有
- `GetImagesFromBatchIndexed` —— 1/9 个有
- `MultiTextConcatenate` —— 1/9 个有
- `MuyeTextEditOutput` —— 1/9 个有
- `Qwen3_VQA` —— 1/9 个有
- `SaveImage` —— 1/9 个有
- `TT_img_enc` —— 1/9 个有
- `TextInput_` —— 1/9 个有
- `easy showAnything` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 9 | 89% |
| Prompt 约束强度(CFG) | 6 | 4 - 20 | 9 | 28% |
| 采样算法 | 1 | 1 - 1 | 9 | 100% |
| 调度器 | euler | - | 9 | 56% |
| 重绘幅度 | simple | - | 9 | 56% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，9 个样本，一致性 89%
- Prompt 约束强度(CFG) 中位数 6，观测区间 4 - 20，9 个样本，取值分散，一致性仅 28%
- 采样算法 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，9 个样本，一致性 56%
- 重绘幅度 最常用 simple，9 个样本，一致性 56%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
