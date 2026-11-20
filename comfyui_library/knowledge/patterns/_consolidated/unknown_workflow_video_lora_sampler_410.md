---
name: unknown_workflow_video_lora_sampler_410
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.973857
common_nodes: [INTConstant, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [图片生成/图生图/【gen全能视频Si】wan2.2图生视频（极简加速版）_1963812148127551490.json, 平台全量/Wan2.2首尾帧视频 KJ版_1952619482592284674.json, 平台全量/wan2.2Fun-VACE+Controlnet_1967843717660966913.json, 视频生成/图生视频/8-图转视频 Wan2.2 14b Optional Last Frame_2053486047740350466.json, 视频生成/图生视频/Wan2.2 Fun Vace视频驱动图片——动作迁移_1966850900927057922.json, 视频生成/图生视频/wan2.2Fun-VACE 动作迁移_1966739330226139137.json, 视频生成/图生视频/wan2.2官方 VACE 人物姿态迁移 KJ流【推荐】_1967834051866406914.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_410

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/【gen全能视频Si】wan2.2图生视频（极简加速版）_1963812148127551490.json、平台全量/Wan2.2首尾帧视频 KJ版_1952619482592284674.json、平台全量/wan2.2Fun-VACE+Controlnet_1967843717660966913.json、视频生成/图生视频/8-图转视频 Wan2.2 14b Optional Last Frame_2053486047740350466.json、视频生成/图生视频/Wan2.2 Fun Vace视频驱动图片——动作迁移_1966850900927057922.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 7 个 workflow 都包含：
- `INTConstant`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `CreateCFGScheduleFloatList` —— 6/7 个有
- `ImageResizeKJv2` —— 6/7 个有
- `VHS_LoadVideo` —— 4/7 个有
- `VHS_VideoInfo` —— 4/7 个有
- `WanVideoVACEEncode` —— 4/7 个有
- `WanVideoVACEModelSelect` —— 4/7 个有
- `DWPreprocessor` —— 3/7 个有
- `ImageConcatMulti` —— 3/7 个有
- `WanVideoImageToVideoEncode` —— 3/7 个有
- `GetImageSizeAndCount` —— 2/7 个有
- `PurgeVRAM_UTK` —— 2/7 个有
- `CR Text` —— 1/7 个有
- `DepthAnythingV2Preprocessor` —— 1/7 个有
- `Fast Groups Bypasser (rgthree)` —— 1/7 个有
- `ImageScaleByAspectRatio_UTK` —— 1/7 个有
- `Label (rgthree)` —— 1/7 个有
- `Note Plus (mtb)` —— 1/7 个有
- `RIFE VFI` —— 1/7 个有
- `Seed (rgthree)` —— 1/7 个有
- `SimpleMath+` —— 1/7 个有
- `easy int` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
