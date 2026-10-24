---
name: unknown_workflow_video_lora_sampler_552
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.94
common_nodes: [CreateCFGScheduleFloatList, INTConstant, ImageResizeKJv2, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/文生视频/Wan2.2-TTM-1030×PainterI2V可控大动态图到视频_1991785174904172546.json, 视频生成/文生视频/【KJ加速版】万相Wan2.2图生视频FusionX超级加速确保跑通_1958062823505088514.json, 视频生成/文生视频/【首尾帧】通义万相WAN2.2 首尾帧视频动画生成_1952990439869714434.json, 视频生成/文生视频/万相Wan2.2图生视频2025KJ加速版工作流_1975384215250448386.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_552

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/文生视频/Wan2.2-TTM-1030×PainterI2V可控大动态图到视频_1991785174904172546.json、视频生成/文生视频/【KJ加速版】万相Wan2.2图生视频FusionX超级加速确保跑通_1958062823505088514.json、视频生成/文生视频/【首尾帧】通义万相WAN2.2 首尾帧视频动画生成_1952990439869714434.json、视频生成/文生视频/万相Wan2.2图生视频2025KJ加速版工作流_1975384215250448386.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 4 个 workflow 都包含：
- `CreateCFGScheduleFloatList`
- `INTConstant`
- `ImageResizeKJv2`
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
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `GetImageSizeAndCount` —— 3/4 个有
- `easy seed` —— 3/4 个有
- `ImageToMask` —— 1/4 个有
- `String Literal` —— 1/4 个有
- `VHS_LoadVideo` —— 1/4 个有
- `WanVideoAddTTMLatents` —— 1/4 个有
- `WanVideoEncode` —— 1/4 个有
- `easy globalSeed` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
