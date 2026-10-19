---
name: unknown_workflow_video_lora_sampler_577
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.670333
common_nodes: [Anything Everywhere, CR Prompt Text, CreateCFGScheduleFloatList, Fast Groups Muter (rgthree), FloatConstant, GetNode, INTConstant, LayerUtility: PurgeVRAM V2, LoadImage, SetNode, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoScheduler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSigmaToStep, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1991509572473069569.json, 视频生成/图生视频/1990968837673787394.json, 视频生成/图生视频/1991503138804998145.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_577

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/1991509572473069569.json、视频生成/图生视频/1990968837673787394.json、视频生成/图生视频/1991503138804998145.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：67%

## 共有节点

全部 3 个 workflow 都包含：
- `Anything Everywhere`
- `CR Prompt Text`
- `CreateCFGScheduleFloatList`
- `Fast Groups Muter (rgthree)`
- `FloatConstant`
- `GetNode`
- `INTConstant`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `SetNode`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoScheduler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSigmaToStep`
- `WanVideoTextEncodeCached`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJv2` —— 2/3 个有
- `ADE_CameraPoseCombo` —— 1/3 个有
- `CameraPoseVisualizer` —— 1/3 个有
- `DWPreprocessor` —— 1/3 个有
- `DepthAnythingV2Preprocessor` —— 1/3 个有
- `GetImageSizeAndCount` —— 1/3 个有
- `ImageBlend` —— 1/3 个有
- `ImageResize+` —— 1/3 个有
- `ImpactSwitch` —— 1/3 个有
- `LoadWanVideoClipTextEncoder` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `VHS_LoadVideo` —— 1/3 个有
- `WanVideoClipVisionEncode` —— 1/3 个有
- `WanVideoControlEmbeds` —— 1/3 个有
- `WanVideoEmptyEmbeds` —— 1/3 个有
- `WanVideoEncode` —— 1/3 个有
- `WanVideoFunCameraEmbeds` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
