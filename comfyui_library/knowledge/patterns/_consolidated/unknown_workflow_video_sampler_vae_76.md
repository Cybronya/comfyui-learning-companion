---
name: unknown_workflow_video_sampler_vae_76
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.533286
common_nodes: [EmptyImage, GetImageSize, GetNode, ImageComposite+, ImageResizeKJv2, InspyrenetRembg, LoadImage, LoadWanVideoT5TextEncoder, MaskGenerator, PreviewImage, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoExperimentalArgs, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1926613325860474881.json, 视频生成/图生视频/1927603815992954882.json, 视频生成/图生视频/1928492165083639810.json, 视频生成/图生视频/1928759873897664514.json, 视频生成/图生视频/1928782340749737985.json, 视频生成/图生视频/1928806775427076098.json, 视频生成/图生视频/1928820592806412290.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_76

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/1926613325860474881.json、视频生成/图生视频/1927603815992954882.json、视频生成/图生视频/1928492165083639810.json、视频生成/图生视频/1928759873897664514.json、视频生成/图生视频/1928782340749737985.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：53%

## 共有节点

全部 7 个 workflow 都包含：
- `EmptyImage`
- `GetImageSize`
- `GetNode`
- `ImageComposite+`
- `ImageResizeKJv2`
- `InspyrenetRembg`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MaskGenerator`
- `PreviewImage`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoExperimentalArgs`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVACEEncode`
- `WanVideoVACEModelSelect`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `INTConstant` —— 6/7 个有
- `LoadAudio` —— 6/7 个有
- `Bjornulf_ShowInt` —— 1/7 个有
- `DWPreprocessor` —— 1/7 个有
- `Fast Groups Bypasser (rgthree)` —— 1/7 个有
- `GetImageRangeFromBatch` —— 1/7 个有
- `GetImageSizeAndCount` —— 1/7 个有
- `ImageBatchMulti` —— 1/7 个有
- `ImageFromBatch` —— 1/7 个有
- `ImageFromBatch+` —— 1/7 个有
- `IntMathOperation` —— 1/7 个有
- `LayerColor: ColorAdapter` —— 1/7 个有
- `MaskBatchMulti` —— 1/7 个有
- `WanVideoLoraSelect` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
