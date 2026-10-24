---
name: unknown_workflow_video_inpaint_sampler_5
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8175
common_nodes: [Fast Groups Bypasser (rgthree), GrowMaskWithBlur, ImageConcanate, ImageResizeKJ, InpaintPreprocessor, LayerMask: LoadSegmentAnythingModels, LayerMask: SegmentAnythingUltra V3, LoadImage, LoadWanVideoT5TextEncoder, MaskToImage, PreviewImage, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoModelLoader, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoVACEEncode, WanVideoVAELoader, easy imageRemBg]
problems: []
missing: []
members: [视频生成/图生视频/VACE14B自动遮罩局部视频修改_1922808096656343042.json, 视频生成/图生视频/VACE普通控制+双图可控构图参考+局部编辑_1909233072066469889.json]
source: knowledge_consolidation
---

# unknown_workflow_video_inpaint_sampler_5

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/VACE14B自动遮罩局部视频修改_1922808096656343042.json、视频生成/图生视频/VACE普通控制+双图可控构图参考+局部编辑_1909233072066469889.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：82%

## 共有节点

全部 2 个 workflow 都包含：
- `Fast Groups Bypasser (rgthree)`
- `GrowMaskWithBlur`
- `ImageConcanate`
- `ImageResizeKJ`
- `InpaintPreprocessor`
- `LayerMask: LoadSegmentAnythingModels`
- `LayerMask: SegmentAnythingUltra V3`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MaskToImage`
- `PreviewImage`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoVACEEncode`
- `WanVideoVAELoader`
- `easy imageRemBg`

**可变部分**（部分 workflow 才有）：
- `AIO_Preprocessor` —— 1/2 个有
- `Compositor3` —— 1/2 个有
- `CompositorConfig3` —— 1/2 个有
- `GetNode` —— 1/2 个有
- `Images to RGB` —— 1/2 个有
- `SetNode` —— 1/2 个有
- `Text Multiline` —— 1/2 个有
- `WanVideoEnhanceAVideo` —— 1/2 个有
- `WanVideoExperimentalArgs` —— 1/2 个有
- `WanVideoTorchCompileSettings` —— 1/2 个有
- `WanVideoVACEModelSelect` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
