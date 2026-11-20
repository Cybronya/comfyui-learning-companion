---
name: unknown_workflow_video_upscale_lora_32
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.606
common_nodes: [ControlNextGetPoses, CreateCFGScheduleFloatList, GetImageSizeAndCount, GetNode, INTConstant, ImageResize+, ImageUpscaleWithModel, ImpactInt, JWInteger, LoadImage, LoadWanVideoT5TextEncoder, MathExpression|pysssss, RIFE VFI, SetNode, UpscaleModelLoader, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoSource, WanVideoBlockSwap, WanVideoControlEmbeds, WanVideoDecode, WanVideoEncode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader, easy positive, easy seed]
problems: []
missing: []
members: [视频生成/图生视频/Wan2.2-FunControl美女跳舞_1971091047734484993.json, 视频生成/图生视频/【放大补帧】Wan2.2-FunControl 视频动作迁移 美女跳舞_1975040693611663361.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_lora_32

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/Wan2.2-FunControl美女跳舞_1971091047734484993.json、视频生成/图生视频/【放大补帧】Wan2.2-FunControl 视频动作迁移 美女跳舞_1975040693611663361.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：61%

## 共有节点

全部 2 个 workflow 都包含：
- `ControlNextGetPoses`
- `CreateCFGScheduleFloatList`
- `GetImageSizeAndCount`
- `GetNode`
- `INTConstant`
- `ImageResize+`
- `ImageUpscaleWithModel`
- `ImpactInt`
- `JWInteger`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MathExpression|pysssss`
- `RIFE VFI`
- `SetNode`
- `UpscaleModelLoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfoSource`
- `WanVideoBlockSwap`
- `WanVideoControlEmbeds`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `easy positive`
- `easy seed`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
