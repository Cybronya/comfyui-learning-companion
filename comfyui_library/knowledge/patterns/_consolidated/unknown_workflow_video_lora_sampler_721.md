---
name: unknown_workflow_video_lora_sampler_721
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.828667
common_nodes: [CR Text Replace, CreateCFGScheduleFloatList, GetImageSizeAndCount, INTConstant, LoadImage, LoadWanVideoT5TextEncoder, PrimitiveBoolean, RH_Captioner, TextBox, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVAELoader, easy ifElse, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/Wan2.2-720P 高速版｜图生视频_1952617990284087298.json, 视频生成/图生视频/Wan2.2-JK高速版-高清1920 -自动提示词_1952604203145474049.json, 视频生成/图生视频/【视频】Wan2.2首尾帧一键生成视频_1952674570933309442.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_721

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/Wan2.2-720P 高速版｜图生视频_1952617990284087298.json、视频生成/图生视频/Wan2.2-JK高速版-高清1920 -自动提示词_1952604203145474049.json、视频生成/图生视频/【视频】Wan2.2首尾帧一键生成视频_1952674570933309442.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 3 个 workflow 都包含：
- `CR Text Replace`
- `CreateCFGScheduleFloatList`
- `GetImageSizeAndCount`
- `INTConstant`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `PrimitiveBoolean`
- `RH_Captioner`
- `TextBox`
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
- `easy ifElse`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CR Text Concatenate` —— 2/3 个有
- `GetNode` —— 2/3 个有
- `ImageFromBatch+` —— 2/3 个有
- `ImageResizeKJ` —— 2/3 个有
- `ImpactSwitch` —— 2/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/3 个有
- `LayerUtility: PurgeVRAM` —— 2/3 个有
- `Primitive integer [Crystools]` —— 2/3 个有
- `RHHiddenNodes` —— 2/3 个有
- `SetNode` —— 2/3 个有
- `SimpleMath+` —— 2/3 个有
- `VAELoader` —— 2/3 个有
- `ImageResizeKJv2` —— 1/3 个有
- `WanVideoTorchCompileSettings` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
