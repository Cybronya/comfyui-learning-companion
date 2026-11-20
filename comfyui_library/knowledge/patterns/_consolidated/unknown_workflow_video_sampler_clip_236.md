---
name: unknown_workflow_video_sampler_clip_236
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.938
common_nodes: [ImageConcanate, ImageResizeKJ, LayerUtility: PurgeVRAM, LoadImage, LoadWanVideoClipTextEncoder, LoadWanVideoT5TextEncoder, Note Plus (mtb), VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoControlEmbeds, WanVideoDecode, WanVideoEncode, WanVideoImageToVideoEncode, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [平台全量/【大炮视频】FUN control超稳定视频姿势控制视频生成_1914925720416546817.json, 视频生成/文生视频/WAN FAN首尾帧工作流_1906315512241131522.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_236

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/【大炮视频】FUN control超稳定视频姿势控制视频生成_1914925720416546817.json、视频生成/文生视频/WAN FAN首尾帧工作流_1906315512241131522.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：94%

## 共有节点

全部 2 个 workflow 都包含：
- `ImageConcanate`
- `ImageResizeKJ`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoadWanVideoClipTextEncoder`
- `LoadWanVideoT5TextEncoder`
- `Note Plus (mtb)`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoControlEmbeds`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoImageToVideoEncode`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `AIO_Preprocessor` —— 1/2 个有
- `CR Text` —— 1/2 个有
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `GetImageSizeAndCount` —— 1/2 个有
- `LTXVPromptEnhancer` —— 1/2 个有
- `LTXVPromptEnhancerLoader` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `Seed (rgthree)` —— 1/2 个有
- `Text Concatenate` —— 1/2 个有
- `WanVideoEnhanceAVideo` —— 1/2 个有
- `WanVideoExperimentalArgs` —— 1/2 个有
- `WanVideoTorchCompileSettings` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
