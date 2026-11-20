---
name: unknown_workflow_video_sampler_vae_112
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.7748
common_nodes: [AddLabel, EmptyImage, GetImageRangeFromBatch, GetImageSizeAndCount, ImageConcatMulti, ImagePadKJ, LoadWanVideoT5TextEncoder, PreviewImage, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoExperimentalArgs, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTeaCache, WanVideoVACEEncode, WanVideoVAELoader]
problems: []
missing: []
members: [平台全量/FusionX-VACE视频扩图_1934173151117139969.json, 平台全量/FusionX加速版视频扩图V1_1933936111058079746.json, 平台全量/VACE 14B视频扩图工作流_1923198805812891650.json, 平台全量/【VACE系列】视频扩展工作流实现猫咪后宫梦！_1925904698380095490.json, 视频生成/图生视频/VACE14B-视频多方位扩展编辑_1922732185021812737.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_112

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（平台全量/FusionX-VACE视频扩图_1934173151117139969.json、平台全量/FusionX加速版视频扩图V1_1933936111058079746.json、平台全量/VACE 14B视频扩图工作流_1923198805812891650.json、平台全量/【VACE系列】视频扩展工作流实现猫咪后宫梦！_1925904698380095490.json、视频生成/图生视频/VACE14B-视频多方位扩展编辑_1922732185021812737.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：77%

## 共有节点

全部 5 个 workflow 都包含：
- `AddLabel`
- `EmptyImage`
- `GetImageRangeFromBatch`
- `GetImageSizeAndCount`
- `ImageConcatMulti`
- `ImagePadKJ`
- `LoadWanVideoT5TextEncoder`
- `PreviewImage`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoExperimentalArgs`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoVACEEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `MaskPreview+` —— 4/5 个有
- `WanVideoTextEncode` —— 4/5 个有
- `WanVideoVACEModelSelect` —— 4/5 个有
- `GetNode` —— 3/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/5 个有
- `SetNode` —— 3/5 个有
- `WanVideoTorchCompileSettings` —— 3/5 个有
- `ImageResizeKJv2` —— 2/5 个有
- `CR Prompt Text` —— 1/5 个有
- `CR Text` —— 1/5 个有
- `Fast Groups Bypasser (rgthree)` —— 1/5 个有
- `JWInteger` —— 1/5 个有
- `MaskPreview` —— 1/5 个有
- `Primitive integer [Crystools]` —— 1/5 个有
- `Text Multiline` —— 1/5 个有
- `WanVideoApplyNAG` —— 1/5 个有
- `WanVideoTextEncodeSingle` —— 1/5 个有
- `easy cleanGpuUsed` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
