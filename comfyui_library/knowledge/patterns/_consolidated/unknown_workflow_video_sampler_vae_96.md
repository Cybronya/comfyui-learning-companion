---
name: unknown_workflow_video_sampler_vae_96
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9838
common_nodes: [CreateCFGScheduleFloatList, INTConstant, ImageResizeKJv2, LoadImage, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoTorchCompileSettings, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/47.tonnie-Wan2.2 VACE 视频动作迁移_2007574568222859266.json, 视频生成/图生视频/Wan2.2 Fun Vace视频驱动图片——动作迁移_1966850900927057922.json, 视频生成/图生视频/wan2.2Fun-VACE 动作迁移_1966739330226139137.json, 视频生成/图生视频/wan2.2官方 VACE 人物姿态迁移 KJ流【推荐】_1967834051866406914.json, 视频生成/图生视频/wan2.2官方 VACE 首尾帧 KJ流_1967815071856472066.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_96

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/47.tonnie-Wan2.2 VACE 视频动作迁移_2007574568222859266.json、视频生成/图生视频/Wan2.2 Fun Vace视频驱动图片——动作迁移_1966850900927057922.json、视频生成/图生视频/wan2.2Fun-VACE 动作迁移_1966739330226139137.json、视频生成/图生视频/wan2.2官方 VACE 人物姿态迁移 KJ流【推荐】_1967834051866406914.json、视频生成/图生视频/wan2.2官方 VACE 首尾帧 KJ流_1967815071856472066.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 5 个 workflow 都包含：
- `CreateCFGScheduleFloatList`
- `INTConstant`
- `ImageResizeKJv2`
- `LoadImage`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoTorchCompileSettings`
- `WanVideoVACEEncode`
- `WanVideoVACEModelSelect`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `DWPreprocessor` —— 4/5 个有
- `LoadWanVideoT5TextEncoder` —— 4/5 个有
- `VHS_LoadVideo` —— 4/5 个有
- `WanVideoLoraSelect` —— 4/5 个有
- `WanVideoSetLoRAs` —— 4/5 个有
- `WanVideoTextEncode` —— 4/5 个有
- `ImageConcatMulti` —— 3/5 个有
- `SimpleMath+` —— 3/5 个有
- `VHS_VideoInfo` —— 3/5 个有
- `CR Text` —— 2/5 个有
- `Note Plus (mtb)` —— 2/5 个有
- `ColorMatch` —— 1/5 个有
- `ImpactInt` —— 1/5 个有
- `PixelPerfectResolution` —— 1/5 个有
- `WanVideoLoraSelectMulti` —— 1/5 个有
- `WanVideoTextEncodeCached` —— 1/5 个有
- `WanVideoVACEStartToEndFrame` —— 1/5 个有
- `easy int` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
