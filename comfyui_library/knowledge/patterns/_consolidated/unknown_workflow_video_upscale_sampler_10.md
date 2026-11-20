---
name: unknown_workflow_video_upscale_sampler_10
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.931
common_nodes: [AIO_Preprocessor, Fast Groups Bypasser (rgthree), ImageConcatMulti, ImageResizeKJ, ImageUpscaleWithModel, LoadImage, LoadWanVideoClipTextEncoder, LoadWanVideoT5TextEncoder, ReActorFaceSwap, UpscaleModelLoader, VHS_LoadVideo, VHS_SplitImages, VHS_VideoCombine, VHS_VideoInfoLoaded, WanVideoBlockSwap, WanVideoDecode, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [平台全量/VACE pose参考+自动重新构图_1908157888236560385.json, 视频生成/图生视频/Wan Fun Control精准动作+自动重新构图_1905231004943192066.json, 视频生成/图生视频/Wan2.1 Fun Control精准动作_1948402669382696962.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_sampler_10

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/VACE pose参考+自动重新构图_1908157888236560385.json、视频生成/图生视频/Wan Fun Control精准动作+自动重新构图_1905231004943192066.json、视频生成/图生视频/Wan2.1 Fun Control精准动作_1948402669382696962.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 3 个 workflow 都包含：
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
- `WanVideoDecode`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `Bbox (mtb)` —— 2/3 个有
- `INPAINT_ExpandMask` —— 2/3 个有
- `ImageCrop` —— 2/3 个有
- `LayerMask: MaskBoxDetect` —— 2/3 个有
- `LayerUtility: ColorImage V2` —— 2/3 个有
- `LayerUtility: ColorPicker` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `Uncrop (mtb)` —— 2/3 个有
- `WanVideoClipVisionEncode` —— 2/3 个有
- `WanVideoControlEmbeds` —— 2/3 个有
- `WanVideoEncode` —— 2/3 个有
- `WanVideoImageToVideoEncode` —— 2/3 个有
- `easy imageRemBg` —— 2/3 个有
- `easy indexAnything` —— 2/3 个有
- `LoadImageFromUrl` —— 1/3 个有
- `Note Plus (mtb)` —— 1/3 个有
- `WanVideoVACEEncode` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
