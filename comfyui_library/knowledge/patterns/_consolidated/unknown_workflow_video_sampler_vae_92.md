---
name: unknown_workflow_video_sampler_vae_92
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.873333
common_nodes: [LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTextEncode, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/电商商品展示_1924016884511854593.json, 视频生成/图生视频/电商首尾帧丝滑转场特效（加速版）_1991857702083293186.json, 视频生成/图生视频/直播图生视频（加速版）_1928609349776654338.json, 视频生成/图生视频/直播首尾帧图生视频（加速版）_1930066639159508993.json, 视频生成/图生视频/直播首尾帧生成人物换装视频（加速版）_1946416276699013121.json, 视频生成/图生视频/进阶版直播真实视频转动漫_1948659044000104450.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_92

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/电商商品展示_1924016884511854593.json、视频生成/图生视频/电商首尾帧丝滑转场特效（加速版）_1991857702083293186.json、视频生成/图生视频/直播图生视频（加速版）_1928609349776654338.json、视频生成/图生视频/直播首尾帧图生视频（加速版）_1930066639159508993.json、视频生成/图生视频/直播首尾帧生成人物换装视频（加速版）_1946416276699013121.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 6 个 workflow 都包含：
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVACEEncode`
- `WanVideoVACEModelSelect`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageRepeat` —— 5/6 个有
- `JjkText` —— 5/6 个有
- `WanVideoLoraSelect` —— 5/6 个有
- `ImageAndMaskPreview` —— 4/6 个有
- `Int` —— 4/6 个有
- `WanVideoVACEStartToEndFrame` —— 4/6 个有
- `PreviewImage` —— 3/6 个有
- `ImageResizeKJv2` —— 2/6 个有
- `WanVideoFreeInitArgs` —— 2/6 个有
- `WanVideoTeaCache` —— 2/6 个有
- `DepthAnything_V2` —— 1/6 个有
- `DownloadAndLoadDepthAnythingV2Model` —— 1/6 个有
- `Fast Groups Muter (rgthree)` —— 1/6 个有
- `ImageFromBatch` —— 1/6 个有
- `ImageFromBatch+` —— 1/6 个有
- `SaveImage` —— 1/6 个有
- `VHS_LoadVideo` —— 1/6 个有
- `VHS_MergeImages` —— 1/6 个有
- `easy imageConcat` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
