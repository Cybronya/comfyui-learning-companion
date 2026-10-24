---
name: unknown_workflow_video_upscale_sampler_14
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.672
common_nodes: [CR Text, CR Text Concatenate, DownloadAndLoadGIMMVFIModel, GIMMVFI_interpolate, GetNode, ImageScaleToMegapixels, ImpactSwitch, LoadWanVideoT5TextEncoder, RH_Prompter, SetNode, ShowText|pysssss, UpscaleModelLoader, VHS_VideoCombine, WanVideoApplyNAG, WanVideoBlockSwap, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncodeSingle, WanVideoVAELoader]
problems: []
missing: []
members: [图片生成/图生图/wan2.1-fusionX-图生视频（RH自动提示词）_1934133372832632834.json, 图片生成/文生图/wan2.1-fusionX-文生视频（RH自动提示词）_1934081139910823938.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_sampler_14

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/wan2.1-fusionX-图生视频（RH自动提示词）_1934133372832632834.json、图片生成/文生图/wan2.1-fusionX-文生视频（RH自动提示词）_1934081139910823938.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：67%

## 共有节点

全部 2 个 workflow 都包含：
- `CR Text`
- `CR Text Concatenate`
- `DownloadAndLoadGIMMVFIModel`
- `GIMMVFI_interpolate`
- `GetNode`
- `ImageScaleToMegapixels`
- `ImpactSwitch`
- `LoadWanVideoT5TextEncoder`
- `RH_Prompter`
- `SetNode`
- `ShowText|pysssss`
- `UpscaleModelLoader`
- `VHS_VideoCombine`
- `WanVideoApplyNAG`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncodeSingle`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPVisionLoader` —— 1/2 个有
- `ImageResizeKJ` —— 1/2 个有
- `Int` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `RH_Captioner` —— 1/2 个有
- `WanVideoClipVisionEncode` —— 1/2 个有
- `WanVideoEmptyEmbeds` —— 1/2 个有
- `WanVideoImageToVideoEncode` —— 1/2 个有
- `WanVideoTextEncode` —— 1/2 个有
- `WanVideoTorchCompileSettings` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
