---
name: unknown_workflow_video_sampler_vae_158
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.74675
common_nodes: [GetImageRangeFromBatch, GetImageSizeAndCount, INTConstant, ImageBatchMulti, ImageResizeKJ, LoadImage, LoadWanVideoT5TextEncoder, PreviewImage, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoExperimentalArgs, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoVACEEncode, WanVideoVACEStartToEndFrame, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/FusionX长视频拼接工作流_1938494783562121217.json, 视频生成/图生视频/Self Forcing-多图首尾帧_1933059633864998913.json, 视频生成/图生视频/（顶配优化版）首尾帧生成视频_1958478405673107458.json, 视频生成/图生视频/（顶配版）首-中-尾三帧图生视频_1933898213298757633.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_158

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/FusionX长视频拼接工作流_1938494783562121217.json、视频生成/图生视频/Self Forcing-多图首尾帧_1933059633864998913.json、视频生成/图生视频/（顶配优化版）首尾帧生成视频_1958478405673107458.json、视频生成/图生视频/（顶配版）首-中-尾三帧图生视频_1933898213298757633.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：75%

## 共有节点

全部 4 个 workflow 都包含：
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
- `WanVideoExperimentalArgs`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoVACEEncode`
- `WanVideoVACEStartToEndFrame`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 3/4 个有
- `MaskBatchMulti` —— 3/4 个有
- `SetNode` —— 3/4 个有
- `WanVideoApplyNAG` —— 3/4 个有
- `WanVideoTextEncodeSingle` —— 3/4 个有
- `MaskPreview` —— 2/4 个有
- `WanVideoEnhanceAVideo` —— 2/4 个有
- `WanVideoTeaCache` —— 2/4 个有
- `WanVideoTorchCompileSettings` —— 2/4 个有
- `WanVideoVACEModelSelect` —— 2/4 个有
- `CR Text` —— 1/4 个有
- `ImageColorMatch+` —— 1/4 个有
- `ImageConcanate` —— 1/4 个有
- `ImpactSwitch` —— 1/4 个有
- `RH_ComfyFluxKontext` —— 1/4 个有
- `RH_LLMAPI_NODE` —— 1/4 个有
- `RH_Translator` —— 1/4 个有
- `SimpleMath+` —— 1/4 个有
- `VHS_LoadVideo` —— 1/4 个有
- `WanVideoLoraSelect` —— 1/4 个有
- `WanVideoTextEncode` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
