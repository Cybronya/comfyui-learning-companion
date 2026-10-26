---
name: unknown_workflow_video_lora_sampler_652
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.881333
common_nodes: [AudioSeparation, DWPreprocessor, DownloadAndLoadWav2VecModel, GetImageSizeAndCount, ImagePadKJ, ImageResizeKJv2, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, WanVideoBlockSwap, WanVideoDecode, WanVideoExperimentalArgs, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVACEStartToEndFrame, WanVideoVAELoader, easy imageRemBg]
problems: []
missing: []
members: [数字人/数字人/Multitalk数字人+复刻视频动作及声音_1949328620750811138.json, 视频生成/图生视频/Aiwood-VACE复刻RunwayAct2_1949185140044570626.json, 视频生成/图生视频/VACE+Multitalk数字人加速版_1949385467585822721.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_652

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（数字人/数字人/Multitalk数字人+复刻视频动作及声音_1949328620750811138.json、视频生成/图生视频/Aiwood-VACE复刻RunwayAct2_1949185140044570626.json、视频生成/图生视频/VACE+Multitalk数字人加速版_1949385467585822721.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 3 个 workflow 都包含：
- `AudioSeparation`
- `DWPreprocessor`
- `DownloadAndLoadWav2VecModel`
- `GetImageSizeAndCount`
- `ImagePadKJ`
- `ImageResizeKJv2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoExperimentalArgs`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVACEEncode`
- `WanVideoVACEModelSelect`
- `WanVideoVACEStartToEndFrame`
- `WanVideoVAELoader`
- `easy imageRemBg`

**可变部分**（部分 workflow 才有）：
- `AddLabel` —— 2/3 个有
- `EmptyImage` —— 2/3 个有
- `ImageConcatMulti` —— 2/3 个有
- `MaskPreview` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `CR Text` —— 1/3 个有
- `GetNode` —— 1/3 个有
- `Int` —— 1/3 个有
- `SetNode` —— 1/3 个有
- `WanVideoEasyCache` —— 1/3 个有
- `WanVideoEnhanceAVideo` —— 1/3 个有
- `WanVideoFreeInitArgs` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
