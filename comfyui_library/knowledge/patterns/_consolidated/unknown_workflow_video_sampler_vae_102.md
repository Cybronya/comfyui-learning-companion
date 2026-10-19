---
name: unknown_workflow_video_sampler_vae_102
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.8596
common_nodes: [ImageResizeKJv2, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoExperimentalArgs, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1953668787440635905.json, 视频生成/图生视频/1923019731547115522.json, 视频生成/图生视频/1926646859241263106.json, 视频生成/图生视频/1940794920766697474.json, 视频生成/图生视频/1948659044000104450.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_102

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/1953668787440635905.json、视频生成/图生视频/1923019731547115522.json、视频生成/图生视频/1926646859241263106.json、视频生成/图生视频/1940794920766697474.json、视频生成/图生视频/1948659044000104450.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 5 个 workflow 都包含：
- `ImageResizeKJv2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoExperimentalArgs`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoVACEEncode`
- `WanVideoVACEModelSelect`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 4/5 个有
- `DepthAnything_V2` —— 3/5 个有
- `DownloadAndLoadDepthAnythingV2Model` —— 3/5 个有
- `MaskPreview+` —— 3/5 个有
- `String Literal` —— 3/5 个有
- `VHS_LoadVideo` —— 3/5 个有
- `WanVideoVACEStartToEndFrame` —— 3/5 个有
- `ttN int` —— 3/5 个有
- `ImageFromBatch+` —— 2/5 个有
- `ImageRepeat` —— 2/5 个有
- `VHS_MergeImages` —— 2/5 个有
- `WanVideoEnhanceAVideo` —— 2/5 个有
- `Fast Groups Muter (rgthree)` —— 1/5 个有
- `ImageFromBatch` —— 1/5 个有
- `ImageListToBatch_` —— 1/5 个有
- `JjkText` —— 1/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/5 个有
- `OpenposePreprocessor` —— 1/5 个有
- `SaveImage` —— 1/5 个有
- `WanVideoFreeInitArgs` —— 1/5 个有
- `WanVideoLoraSelect` —— 1/5 个有
- `easy showAnything` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
