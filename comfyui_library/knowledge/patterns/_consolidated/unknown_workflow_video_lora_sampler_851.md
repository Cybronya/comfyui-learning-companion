---
name: unknown_workflow_video_lora_sampler_851
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.795
common_nodes: [CreateCFGScheduleFloatList, GetImageSizeAndCount, GetNode, INTConstant, ImageResizeKJv2, Int, JjkText, LoadImage, LoadWanVideoT5TextEncoder, SetNode, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/wan21+wan22_指定运镜工作流，精确控制运镜_2014932478938587137.json, 视频生成/图生视频/wan22+uni3C运镜控制工作流，精准运镜控制_2014737203347333121.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_851

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/wan21+wan22_指定运镜工作流，精确控制运镜_2014932478938587137.json、视频生成/图生视频/wan22+uni3C运镜控制工作流，精准运镜控制_2014737203347333121.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：80%

## 共有节点

全部 2 个 workflow 都包含：
- `CreateCFGScheduleFloatList`
- `GetImageSizeAndCount`
- `GetNode`
- `INTConstant`
- `ImageResizeKJv2`
- `Int`
- `JjkText`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `SetNode`
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
- `ImageConcanate` —— 1/2 个有
- `RHHiddenNodes` —— 1/2 个有
- `ThreeJSActionCombiner` —— 1/2 个有
- `ThreeJSCameraAction` —— 1/2 个有
- `ThreeJSCameraConfig` —— 1/2 个有
- `ThreeJSEnvironment` —— 1/2 个有
- `ThreeJSFigureAction` —— 1/2 个有
- `ThreeJSFigureConfig` —— 1/2 个有
- `ThreeJSRenderNode` —— 1/2 个有
- `VHS_LoadVideo` —— 1/2 个有
- `WanVideoEncode` —— 1/2 个有
- `WanVideoUni3C_ControlnetLoader` —— 1/2 个有
- `WanVideoUni3C_embeds` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
