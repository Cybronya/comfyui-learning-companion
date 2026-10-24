---
name: unknown_workflow_video_sampler_vae_156
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.812667
common_nodes: [GetImageRangeFromBatch, GetImageSizeAndCount, INTConstant, ImageBatchMulti, ImageResizeKJ, LoadImage, LoadWanVideoT5TextEncoder, PreviewImage, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTeaCache, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVACEStartToEndFrame, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/FusionX长视频拼接工作流_1938494783562121217.json, 视频生成/图生视频/Self Forcing-多图首尾帧_1933059633864998913.json, 视频生成/图生视频/lightx2v-高质量加速模型测试_1935325590822256642.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_156

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/FusionX长视频拼接工作流_1938494783562121217.json、视频生成/图生视频/Self Forcing-多图首尾帧_1933059633864998913.json、视频生成/图生视频/lightx2v-高质量加速模型测试_1935325590822256642.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 3 个 workflow 都包含：
- `GetImageRangeFromBatch`
- `GetImageSizeAndCount`
- `INTConstant`
- `ImageBatchMulti`
- `ImageResizeKJ`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `PreviewImage`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoVACEEncode`
- `WanVideoVACEModelSelect`
- `WanVideoVACEStartToEndFrame`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `MaskBatchMulti` —— 2/3 个有
- `VHS_LoadVideo` —— 2/3 个有
- `WanVideoTextEncode` —— 2/3 个有
- `WanVideoTorchCompileSettings` —— 2/3 个有
- `DWPreprocessor` —— 1/3 个有
- `GetImageSize+` —— 1/3 个有
- `GetNode` —— 1/3 个有
- `ImageColorMatch+` —— 1/3 个有
- `ImageResizeKJv2` —— 1/3 个有
- `RH_ComfyFluxKontext` —— 1/3 个有
- `RH_Translator` —— 1/3 个有
- `SetNode` —— 1/3 个有
- `SimpleMath+` —— 1/3 个有
- `String Literal` —— 1/3 个有
- `WanVideoApplyNAG` —— 1/3 个有
- `WanVideoLoraSelect` —— 1/3 个有
- `WanVideoTextEncodeSingle` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
