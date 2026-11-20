---
name: unknown_workflow_video_sampler_vae_162
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.701667
common_nodes: [GetImageSizeAndCount, GetNode, ImageResizeKJv2, LoadImage, LoadWanVideoT5TextEncoder, MaskPreview, PreviewImage, SetNode, VHS_VideoCombine, WanVideoApplyNAG, WanVideoBlockSwap, WanVideoDecode, WanVideoExperimentalArgs, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTextEncodeSingle, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVACEStartToEndFrame, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Wan 2.1 FusionX VACE+Control_1949680224212000770.json, 视频生成/图生视频/Wan2.1 FusionX  VACE首尾帧_1949681611131506689.json, 视频生成/图生视频/万象FusionX VACE+NAG 首尾帧_1934079084030775298.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_162

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/Wan 2.1 FusionX VACE+Control_1949680224212000770.json、视频生成/图生视频/Wan2.1 FusionX  VACE首尾帧_1949681611131506689.json、视频生成/图生视频/万象FusionX VACE+NAG 首尾帧_1934079084030775298.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：70%

## 共有节点

全部 3 个 workflow 都包含：
- `GetImageSizeAndCount`
- `GetNode`
- `ImageResizeKJv2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MaskPreview`
- `PreviewImage`
- `SetNode`
- `VHS_VideoCombine`
- `WanVideoApplyNAG`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoExperimentalArgs`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTextEncodeSingle`
- `WanVideoVACEEncode`
- `WanVideoVACEModelSelect`
- `WanVideoVACEStartToEndFrame`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptyImage` —— 2/3 个有
- `ImageConcatMulti` —— 2/3 个有
- `Int` —— 2/3 个有
- `LoadImageFromUrl` —— 2/3 个有
- `Note Plus (mtb)` —— 2/3 个有
- `AIO_Preprocessor` —— 1/3 个有
- `ImageBlend` —— 1/3 个有
- `ImagePadKJ` —— 1/3 个有
- `ImageScale` —— 1/3 个有
- `VHS_LoadVideo` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
