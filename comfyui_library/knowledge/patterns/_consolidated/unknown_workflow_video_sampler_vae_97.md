---
name: unknown_workflow_video_sampler_vae_97
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9374
common_nodes: [CR Text, ImageResizeKJv2, LoadImage, LoadWanVideoT5TextEncoder, SimpleMath+, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoModelLoader, WanVideoSampler, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [图片生成/图生图/图生视频 （Rewards+Pusa+加速）Wan2.2_1967155879348985857.json, 视频生成/图生视频/Wan2.2 Fun奖励LoRA 图生视频KJ版【更好动态】_1967630576679358465.json, 视频生成/图生视频/Wan2.2-SmoothMIXv2高动态图生视频_1979786128704311297.json, 视频生成/图生视频/Wan2.2图生视频(KJ)1080P_1950372019490701313.json, 视频生成/图生视频/Wan2.2图生视频(KJ)_1949993851035541506.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_97

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/图生视频 （Rewards+Pusa+加速）Wan2.2_1967155879348985857.json、视频生成/图生视频/Wan2.2 Fun奖励LoRA 图生视频KJ版【更好动态】_1967630576679358465.json、视频生成/图生视频/Wan2.2-SmoothMIXv2高动态图生视频_1979786128704311297.json、视频生成/图生视频/Wan2.2图生视频(KJ)1080P_1950372019490701313.json、视频生成/图生视频/Wan2.2图生视频(KJ)_1949993851035541506.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 5 个 workflow 都包含：
- `CR Text`
- `ImageResizeKJv2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `SimpleMath+`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `GetImageSizeAndCount` —— 4/5 个有
- `WanVideoApplyNAG` —— 4/5 个有
- `WanVideoSetBlockSwap` —— 4/5 个有
- `WanVideoTextEncodeSingle` —— 4/5 个有
- `easy cleanGpuUsed` —— 4/5 个有
- `PrimitiveInt` —— 3/5 个有
- `WanVideoLoraSelectMulti` —— 3/5 个有
- `WanVideoTextEncode` —— 3/5 个有
- `Fast Groups Bypasser (rgthree)` —— 2/5 个有
- `INTConstant` —— 2/5 个有
- `ImpactInt` —— 2/5 个有
- `WanVideoLoraSelect` —— 2/5 个有
- `CR SDXL Aspect Ratio` —— 1/5 个有
- `CreateVideo` —— 1/5 个有
- `DownloadAndLoadGIMMVFIModel` —— 1/5 个有
- `GIMMVFI_interpolate` —— 1/5 个有
- `NumberClamp` —— 1/5 个有
- `PreViewVideo` —— 1/5 个有
- `Primitive integer [Crystools]` —— 1/5 个有
- `SeedVR2` —— 1/5 个有
- `SeedVR2BlockSwap` —— 1/5 个有
- `WanVideoSetLoRAs` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
