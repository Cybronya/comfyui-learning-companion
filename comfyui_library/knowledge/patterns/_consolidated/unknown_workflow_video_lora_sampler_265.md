---
name: unknown_workflow_video_lora_sampler_265
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.924
common_nodes: [LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Wan2.2 图生视频超级加速KJ版_1950100729937747969.json, 视频生成/图生视频/Wan2.2 图生视频首尾帧 万能工作流_1954848772384710658.json, 视频生成/图生视频/Wan2.2建筑变圣诞树特效图生视频V1（Lora版）_1953405056387305473.json, 视频生成/图生视频/Wanmove_轨迹运动_图生视频_1999179098159185922.json, 视频生成/图生视频/ai动画_1988552709458542593.json, 视频生成/图生视频/wan2.2图生视频加速，kj版_1951106522648653826.json, 视频生成/图生视频/大明动画风格 图生视频_1962000212275478530.json, 视频生成/文生视频/(KJ版)Wan2.2图生视频超级加速版V3（大幅度提高速度）_1950046289267441666.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_265

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/Wan2.2 图生视频超级加速KJ版_1950100729937747969.json、视频生成/图生视频/Wan2.2 图生视频首尾帧 万能工作流_1954848772384710658.json、视频生成/图生视频/Wan2.2建筑变圣诞树特效图生视频V1（Lora版）_1953405056387305473.json、视频生成/图生视频/Wanmove_轨迹运动_图生视频_1999179098159185922.json、视频生成/图生视频/ai动画_1988552709458542593.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 8 个 workflow 都包含：
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 7/8 个有
- `CreateCFGScheduleFloatList` —— 7/8 个有
- `GetImageSizeAndCount` —— 7/8 个有
- `INTConstant` —— 7/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 7/8 个有
- `ImageFromBatch+` —— 5/8 个有
- `JWInteger` —— 5/8 个有
- `LayerUtility: PurgeVRAM` —— 5/8 个有
- `WanVideoTorchCompileSettings` —— 4/8 个有
- `CLIPVisionLoader` —— 2/8 个有
- `WanVideoClipVisionEncode` —— 2/8 个有
- `ConcatTextOfUtils` —— 1/8 个有
- `Display Int (rgthree)` —— 1/8 个有
- `LayerUtility: ImageMaskScaleAsV2` —— 1/8 个有
- `SplineEditor` —— 1/8 个有
- `WanVideoAddWanMoveTracks` —— 1/8 个有
- `YC Color Match` —— 1/8 个有
- `easy mathInt` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
