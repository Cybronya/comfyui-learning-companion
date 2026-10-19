---
name: unknown_workflow_video_lora_sampler_92
type: Unknown Workflow
frequency: 16
level: strong
coverage: 0.921687
common_nodes: [CLIPVisionLoader, DownloadAndLoadNLFModel, INTConstant, ImageResizeKJv2, LoadImage, LoadWanVideoT5TextEncoder, NLFPredict, OnnxDetectionModelLoader, PoseDetectionVitPoseToDWPose, PreviewImage, RenderNLFPoses, SimpleMath+, VHS_LoadVideo, VHS_VideoCombine, WanVideoAddSCAILPoseEmbeds, WanVideoAddSCAILReferenceEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSamplerExtraArgs, WanVideoSamplerv2, WanVideoSchedulerv2, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/2064553319145754626.json, 视频生成/图生视频/2008441362764537857.json, 视频生成/图生视频/2048661829873831938.json, 视频生成/图生视频/2005453601126445058.json, 视频生成/图生视频/2009625455447515138.json, 视频生成/图生视频/2009854933348130817.json, 视频生成/图生视频/2071446981473562626.json, 视频生成/图生视频/2070753501143191553.json, 视频生成/图生视频/2071262215709220866.json, 视频生成/图生视频/本地开源免费，emergency_2054436990401171457.json, 视频生成/图生视频/2055881333670457346.json, 视频生成/图生视频/2055906585632878593.json, 视频生成/图生视频/本地开源免费，倒车请注意_2054373065324277762.json, 视频生成/图生视频/2055687460432171009.json, 视频生成/图生视频/2055881301147824129.json, 视频生成/图生视频/2056247693923672065.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_92

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（视频生成/图生视频/2064553319145754626.json、视频生成/图生视频/2008441362764537857.json、视频生成/图生视频/2048661829873831938.json、视频生成/图生视频/2005453601126445058.json、视频生成/图生视频/2009625455447515138.json…）

- **类型**：Unknown Workflow
- **样本数**：16
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 16 个 workflow 都包含：
- `CLIPVisionLoader`
- `DownloadAndLoadNLFModel`
- `INTConstant`
- `ImageResizeKJv2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `NLFPredict`
- `OnnxDetectionModelLoader`
- `PoseDetectionVitPoseToDWPose`
- `PreviewImage`
- `RenderNLFPoses`
- `SimpleMath+`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAddSCAILPoseEmbeds`
- `WanVideoAddSCAILReferenceEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoContextOptions`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSamplerExtraArgs`
- `WanVideoSamplerv2`
- `WanVideoSchedulerv2`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: PurgeVRAM V2` —— 11/16 个有
- `FlashVSR_SM_KSampler` —— 9/16 个有
- `FlashVSR_SM_Model` —— 9/16 个有
- `GetImageRangeFromBatch` —— 9/16 个有
- `GetImageSize` —— 9/16 个有
- `JWInteger` —— 9/16 个有
- `easy indexAnything` —— 9/16 个有
- `FloatConstant` —— 5/16 个有
- `GetImageSizeAndCount` —— 5/16 个有
- `ImageConcatMulti` —— 5/16 个有
- `LoadAudio` —— 2/16 个有
- `GetNode` —— 1/16 个有
- `HypernetworkLoader` —— 1/16 个有
- `SetNode` —— 1/16 个有
- `VHS_VideoInfo` —— 1/16 个有
- `WanAnimatePlus LoraSelect` —— 1/16 个有
- `easy showAnything` —— 1/16 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 1.12116e+09 | 2.80175e+08 - 1.91868e+09 | 9 | 56% |
| Prompt 约束强度(CFG) | randomize | - | 9 | 100% |
| 采样算法 | 2 | 2 - 2 | 9 | 100% |
| 调度器 | 3.5 | 3.5 - 3.5 | 9 | 100% |
| 重绘幅度 | 11 | 11 - 11 | 9 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 1.12116e+09，观测区间 2.80175e+08 - 1.91868e+09，9 个样本
- Prompt 约束强度(CFG) 最常用 randomize，9 个样本，一致性 100%
- 采样算法 中位数 2，观测区间 2 - 2，9 个样本，取值集中（一致性 100%）
- 调度器 中位数 3.5，观测区间 3.5 - 3.5，9 个样本，取值集中（一致性 100%）
- 重绘幅度 中位数 11，观测区间 11 - 11，9 个样本，取值集中（一致性 100%）
- 风险：采样步数 观测到 1.91868e+09，超出安全上限 60（steps 偏高收益递减且显著增加耗时）
- 风险：重绘幅度 观测到 11，超出安全上限 1（denoise 接近 1.0 时接近重新生成，初始潜空间影响被抹平）
