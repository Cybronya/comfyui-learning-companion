---
name: unknown_workflow_video_upscale_sampler_17
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.941
common_nodes: [AIO_Preprocessor, Fast Groups Bypasser (rgthree), ImageConcatMulti, ImageResizeKJ, ImageUpscaleWithModel, LoadImage, LoadWanVideoClipTextEncoder, LoadWanVideoT5TextEncoder, ReActorFaceSwap, UpscaleModelLoader, VHS_LoadVideo, VHS_SplitImages, VHS_VideoCombine, VHS_VideoInfoLoaded, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoControlEmbeds, WanVideoDecode, WanVideoEncode, WanVideoImageToVideoEncode, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Wan Fun Control精准动作+自动重新构图_1905231004943192066.json, 视频生成/图生视频/Wan2.1 Fun Control精准动作_1948402669382696962.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_sampler_17

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/Wan Fun Control精准动作+自动重新构图_1905231004943192066.json、视频生成/图生视频/Wan2.1 Fun Control精准动作_1948402669382696962.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：94%

## 共有节点

全部 2 个 workflow 都包含：
- `AIO_Preprocessor`
- `Fast Groups Bypasser (rgthree)`
- `ImageConcatMulti`
- `ImageResizeKJ`
- `ImageUpscaleWithModel`
- `LoadImage`
- `LoadWanVideoClipTextEncoder`
- `LoadWanVideoT5TextEncoder`
- `ReActorFaceSwap`
- `UpscaleModelLoader`
- `VHS_LoadVideo`
- `VHS_SplitImages`
- `VHS_VideoCombine`
- `VHS_VideoInfoLoaded`
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
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `Bbox (mtb)` —— 1/2 个有
- `INPAINT_ExpandMask` —— 1/2 个有
- `ImageCrop` —— 1/2 个有
- `LayerMask: MaskBoxDetect` —— 1/2 个有
- `LayerUtility: ColorImage V2` —— 1/2 个有
- `LayerUtility: ColorPicker` —— 1/2 个有
- `LoadImageFromUrl` —— 1/2 个有
- `Note Plus (mtb)` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `Uncrop (mtb)` —— 1/2 个有
- `easy imageRemBg` —— 1/2 个有
- `easy indexAnything` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
