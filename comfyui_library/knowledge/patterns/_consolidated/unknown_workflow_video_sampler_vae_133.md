---
name: unknown_workflow_video_sampler_vae_133
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.85475
common_nodes: [ImageResizeKJv2, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoExperimentalArgs, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/VACE首尾帧+深度控制工作流_1953668787440635905.json, 视频生成/图生视频/VACE首尾帧工作流_1923019731547115522.json, 视频生成/图生视频/直播让图片跳舞_1926646859241263106.json, 视频生成/图生视频/自己用：VACE首尾帧_1940794920766697474.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_133

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/VACE首尾帧+深度控制工作流_1953668787440635905.json、视频生成/图生视频/VACE首尾帧工作流_1923019731547115522.json、视频生成/图生视频/直播让图片跳舞_1926646859241263106.json、视频生成/图生视频/自己用：VACE首尾帧_1940794920766697474.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 4 个 workflow 都包含：
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
- `MaskPreview+` —— 3/4 个有
- `PreviewImage` —— 3/4 个有
- `String Literal` —— 3/4 个有
- `WanVideoVACEStartToEndFrame` —— 3/4 个有
- `ttN int` —— 3/4 个有
- `DepthAnything_V2` —— 2/4 个有
- `DownloadAndLoadDepthAnythingV2Model` —— 2/4 个有
- `VHS_LoadVideo` —— 2/4 个有
- `ImageFromBatch+` —— 1/4 个有
- `ImageListToBatch_` —— 1/4 个有
- `ImageRepeat` —— 1/4 个有
- `OpenposePreprocessor` —— 1/4 个有
- `VHS_MergeImages` —— 1/4 个有
- `WanVideoEnhanceAVideo` —— 1/4 个有
- `easy showAnything` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
