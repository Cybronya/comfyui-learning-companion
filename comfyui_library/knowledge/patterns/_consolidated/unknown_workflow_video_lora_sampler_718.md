---
name: unknown_workflow_video_lora_sampler_718
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.929667
common_nodes: [CreateCFGScheduleFloatList, GetImageSizeAndCount, LoadImage, LoadWanVideoT5TextEncoder, SimpleMath+, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Wan2.2 Smooth Mix高动态 文生视频_1979029148482048001.json, 视频生成/图生视频/Wan2_2_I2V_A14B_高质量加速工作流_1980926100463337474.json, 视频生成/图生视频/wan2.2 图生视频+首尾帧_1956285826319699969.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_718

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/Wan2.2 Smooth Mix高动态 文生视频_1979029148482048001.json、视频生成/图生视频/Wan2_2_I2V_A14B_高质量加速工作流_1980926100463337474.json、视频生成/图生视频/wan2.2 图生视频+首尾帧_1956285826319699969.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 3 个 workflow 都包含：
- `CreateCFGScheduleFloatList`
- `GetImageSizeAndCount`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `SimpleMath+`
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
- `INTConstant` —— 2/3 个有
- `ImageResizeKJv2` —— 2/3 个有
- `PrimitiveFloat` —— 2/3 个有
- `WanVideoImageToVideoEncode` —— 2/3 个有
- `JjkText` —— 1/3 个有
- `Primitive integer [Crystools]` —— 1/3 个有
- `PrimitiveStringMultiline` —— 1/3 个有
- `WanVideoEmptyEmbeds` —— 1/3 个有
- `WanVideoScheduler` —— 1/3 个有
- `WanVideoSigmaToStep` —— 1/3 个有
- `easy cleanGpuUsed` —— 1/3 个有
- `easy float` —— 1/3 个有
- `easy int` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
