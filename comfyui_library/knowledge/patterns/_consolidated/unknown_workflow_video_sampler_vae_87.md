---
name: unknown_workflow_video_sampler_vae_87
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.652333
common_nodes: [AddLabel, EmptyImage, GetImageSizeAndCount, GetNode, ImageConcatMulti, LoadWanVideoT5TextEncoder, SetNode, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoExperimentalArgs, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1922732185021812737.json, 视频生成/图生视频/1922723230275223554.json, 视频生成/图生视频/1923032081754935297.json, 视频生成/图生视频/1923004449781182465.json, 视频生成/图生视频/1922996913308954625.json, 视频生成/图生视频/1913467020191461377.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_87

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/1922732185021812737.json、视频生成/图生视频/1922723230275223554.json、视频生成/图生视频/1923032081754935297.json、视频生成/图生视频/1923004449781182465.json、视频生成/图生视频/1922996913308954625.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：65%

## 共有节点

全部 6 个 workflow 都包含：
- `AddLabel`
- `EmptyImage`
- `GetImageSizeAndCount`
- `GetNode`
- `ImageConcatMulti`
- `LoadWanVideoT5TextEncoder`
- `SetNode`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoExperimentalArgs`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVACEEncode`
- `WanVideoVACEModelSelect`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 5/6 个有
- `GetImageRangeFromBatch` —— 5/6 个有
- `ImagePadKJ` —— 5/6 个有
- `ImageResizeKJ` —— 5/6 个有
- `LoadImage` —— 5/6 个有
- `Primitive integer [Crystools]` —— 5/6 个有
- `Text Multiline` —— 5/6 个有
- `VHS_LoadVideo` —— 5/6 个有
- `DepthAnything_V2` —— 4/6 个有
- `DownloadAndLoadDepthAnythingV2Model` —— 4/6 个有
- `AIO_Preprocessor` —— 3/6 个有
- `MaskPreview+` —— 3/6 个有
- `PreviewImage` —— 3/6 个有
- `RH_Captioner` —— 3/6 个有
- `ShowText|pysssss` —— 3/6 个有
- `Text Concatenate` —— 3/6 个有
- `WanVideoVACEStartToEndFrame` —— 2/6 个有
- `easy imageRemBg` —— 2/6 个有
- `Fast Groups Muter (rgthree)` —— 1/6 个有
- `ImageResizeKJv2` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
