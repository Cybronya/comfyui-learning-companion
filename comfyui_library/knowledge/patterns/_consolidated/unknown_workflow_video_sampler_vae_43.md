---
name: unknown_workflow_video_sampler_vae_43
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.9715
common_nodes: [CreateCFGScheduleFloatList, GetImageSizeAndCount, INTConstant, LoadImage, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoModelLoader, WanVideoSampler, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1978778369921847298.json, 视频生成/图生视频/1950839891598966785.json, 视频生成/图生视频/1972692156160888834.json, 视频生成/图生视频/1959587431169339394.json, 视频生成/图生视频/1955274783857393666.json, 视频生成/图生视频/1954784687051857922.json, 视频生成/图生视频/2071492329428570114.json, 视频生成/图生视频/2005731300571049986.json, 视频生成/图生视频/2019289555643408385.json, 视频生成/图生视频/2067311490910220289.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_43

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/1978778369921847298.json、视频生成/图生视频/1950839891598966785.json、视频生成/图生视频/1972692156160888834.json、视频生成/图生视频/1959587431169339394.json、视频生成/图生视频/1955274783857393666.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 10 个 workflow 都包含：
- `CreateCFGScheduleFloatList`
- `GetImageSizeAndCount`
- `INTConstant`
- `LoadImage`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadWanVideoT5TextEncoder` —— 9/10 个有
- `WanVideoLoraSelect` —— 9/10 个有
- `WanVideoTextEncode` —— 9/10 个有
- `WanVideoSetBlockSwap` —— 8/10 个有
- `WanVideoSetLoRAs` —— 8/10 个有
- `WanVideoTorchCompileSettings` —— 7/10 个有
- `ImageResizeKJv2` —— 5/10 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/10 个有
- `CR Prompt Text` —— 4/10 个有
- `JWInteger` —— 4/10 个有
- `WanVideoSetRadialAttention` —— 2/10 个有
- `CM_IntToFloat` —— 1/10 个有
- `GetImageSize` —— 1/10 个有
- `LazySwitch2way` —— 1/10 个有
- `SimpleMath+` —— 1/10 个有
- `WanVideoTextEncodeCached` —— 1/10 个有
- `easy compare` —— 1/10 个有
- `easy imageSize` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
