---
name: unknown_workflow_video_lora_sampler_76
type: Unknown Workflow
frequency: 19
level: strong
coverage: 0.892789
common_nodes: [CLIPVisionLoader, DownloadAndLoadNLFModel, ImageResizeKJv2, LoadImage, LoadWanVideoT5TextEncoder, NLFPredict, OnnxDetectionModelLoader, PoseDetectionVitPoseToDWPose, RenderNLFPoses, SimpleMath+, VHS_LoadVideo, VHS_VideoCombine, WanVideoAddSCAILPoseEmbeds, WanVideoAddSCAILReferenceEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSamplerExtraArgs, WanVideoSamplerv2, WanVideoSchedulerv2, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/cosplay度量の広いお姉さん_2064553319145754626.json, 视频生成/图生视频/scail 多人跳舞_2008441362764537857.json, 视频生成/图生视频/【AI小王子】85.Scail+一键跳舞！骨骼完美驱动！(视频和图片需要选择自己本地的）_2048661829873831938.json, 视频生成/图生视频/【最推荐，完美动作迁移】Scail 一键跳舞！骨骼完美驱动！_2009625455447515138.json, 视频生成/图生视频/【最推荐，完美动作迁移，动态增强】Scail 一键跳舞！骨骼完美驱动！_2009854933348130817.json, 视频生成/图生视频/人类动作迁移到动物_2071446981473562626.json, 视频生成/图生视频/卡通人物动作迁移_2070753501143191553.json, 视频生成/图生视频/搞笑动物跳舞视频_2071262215709220866.json, 视频生成/图生视频/最新SCAIL动作迁移美女跳舞，支持双人对战_2001125534966874113.json, 视频生成/图生视频/本地开源免费，emergency_2054436990401171457.json, 视频生成/图生视频/本地开源免费，tiktok dancing_2055881333670457346.json, 视频生成/图生视频/本地开源免费，tiktok dancing_2055906585632878593.json, 视频生成/图生视频/本地开源免费，倒车请注意_2054373065324277762.json, 视频生成/图生视频/本地开源免费，倒车请注意_2055687460432171009.json, 视频生成/图生视频/本地开源免费，好汉歌_2055881301147824129.json, 视频生成/图生视频/本地开源免费，道士小曲_2056247693923672065.json, 视频生成/图生视频/适配各种风格也适合双人动作迁移丝滑_2002389202262212609.json, 视频生成/图生视频/🕺丝滑动作迁移-SCAIL无限人数版🕺_2001377941516845057.json, 视频生成/图生视频/🕺丝滑动作迁移-SCAIL适配各种风格也适合双人🕺_2000762623283036162.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_76

> 由 `engine/knowledge_consolidation` 从 19 个 workflow 归纳得出（视频生成/图生视频/cosplay度量の広いお姉さん_2064553319145754626.json、视频生成/图生视频/scail 多人跳舞_2008441362764537857.json、视频生成/图生视频/【AI小王子】85.Scail+一键跳舞！骨骼完美驱动！(视频和图片需要选择自己本地的）_2048661829873831938.json、视频生成/图生视频/【最推荐，完美动作迁移】Scail 一键跳舞！骨骼完美驱动！_2009625455447515138.json、视频生成/图生视频/【最推荐，完美动作迁移，动态增强】Scail 一键跳舞！骨骼完美驱动！_2009854933348130817.json…）

- **类型**：Unknown Workflow
- **样本数**：19
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 19 个 workflow 都包含：
- `CLIPVisionLoader`
- `DownloadAndLoadNLFModel`
- `ImageResizeKJv2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `NLFPredict`
- `OnnxDetectionModelLoader`
- `PoseDetectionVitPoseToDWPose`
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
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `WanVideoTorchCompileSettings` —— 16/19 个有
- `INTConstant` —— 15/19 个有
- `PreviewImage` —— 15/19 个有
- `LayerUtility: PurgeVRAM V2` —— 11/19 个有
- `FlashVSR_SM_KSampler` —— 9/19 个有
- `FlashVSR_SM_Model` —— 9/19 个有
- `GetImageRangeFromBatch` —— 9/19 个有
- `GetImageSize` —— 9/19 个有
- `JWInteger` —— 9/19 个有
- `easy indexAnything` —— 9/19 个有
- `FloatConstant` —— 8/19 个有
- `GetImageSizeAndCount` —— 8/19 个有
- `ImageConcatMulti` —— 8/19 个有
- `CR Text` —— 4/19 个有
- `WanVideoEncode` —— 4/19 个有
- `WanVideoUni3C_ControlnetLoader` —— 4/19 个有
- `WanVideoUni3C_embeds` —— 4/19 个有
- `easy int` —— 4/19 个有
- `GetNode` —— 3/19 个有
- `SetNode` —— 3/19 个有
- `Fast Bypasser (rgthree)` —— 2/19 个有
- `LoadAudio` —— 2/19 个有
- `Mute / Bypass Repeater (rgthree)` —— 2/19 个有
- `Note Plus (mtb)` —— 2/19 个有
- `HypernetworkLoader` —— 1/19 个有
- `VHS_VideoInfo` —— 1/19 个有
- `WanAnimatePlus LoraSelect` —— 1/19 个有
- `WanVideoLoraSelectMulti` —— 1/19 个有
- `easy showAnything` —— 1/19 个有

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
