---
name: unknown_workflow_video_sampler_vae_39
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.8476
common_nodes: [GetImageSizeAndCount, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoExperimentalArgs, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTextEncode, WanVideoVACEEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/FusionX-VACE加速高细节最强首尾帧_1934640445391872001.json, 视频生成/图生视频/FusionX-VACE首尾帧_1934644328725684226.json, 视频生成/图生视频/FusionX高细节双图首尾帧视频生成_1943227565869842433.json, 视频生成/图生视频/VACE 14B-首尾帧图生视频_1925111334327754753.json, 视频生成/图生视频/VACE 14B视频扩图稳定版V1_1922724321020579841.json, 视频生成/图生视频/VACE-视频扩图工作流_1923332542534250497.json, 视频生成/图生视频/Vace首尾帧工作流修复版_1913425967614783490.json, 视频生成/图生视频/wanvideo_1_3B_VACE_examples_02_1913467020191461377.json, 视频生成/图生视频/【10秒生成】Causvid模型实现AI跳舞视频_1926507512189624322.json, 视频生成/图生视频/【VACE系列】Causvid模型实现10秒生成AI跳舞视频_1926119230994018305.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_39

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/FusionX-VACE加速高细节最强首尾帧_1934640445391872001.json、视频生成/图生视频/FusionX-VACE首尾帧_1934644328725684226.json、视频生成/图生视频/FusionX高细节双图首尾帧视频生成_1943227565869842433.json、视频生成/图生视频/VACE 14B-首尾帧图生视频_1925111334327754753.json、视频生成/图生视频/VACE 14B视频扩图稳定版V1_1922724321020579841.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 10 个 workflow 都包含：
- `GetImageSizeAndCount`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoExperimentalArgs`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVACEEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 8/10 个有
- `WanVideoTeaCache` —— 8/10 个有
- `WanVideoVACEStartToEndFrame` —— 8/10 个有
- `AddLabel` —— 7/10 个有
- `EmptyImage` —— 7/10 个有
- `ImageConcatMulti` —— 7/10 个有
- `ImageResizeKJ` —— 7/10 个有
- `PreviewImage` —— 7/10 个有
- `WanVideoVACEModelSelect` —— 6/10 个有
- `MaskPreview+` —— 5/10 个有
- `VHS_LoadVideo` —— 5/10 个有
- `GetNode` —— 4/10 个有
- `SetNode` —— 4/10 个有
- `DepthAnything_V2` —— 3/10 个有
- `DownloadAndLoadDepthAnythingV2Model` —— 3/10 个有
- `GetImageRangeFromBatch` —— 3/10 个有
- `ImagePadKJ` —— 3/10 个有
- `LayerUtility: PurgeVRAM V2` —— 3/10 个有
- `WanVideoTorchCompileSettings` —— 3/10 个有
- `easy int` —— 3/10 个有
- `ImageFromBatch+` —— 2/10 个有
- `ImageResizeKJv2` —— 2/10 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/10 个有
- `MaskPreview` —— 2/10 个有
- `RH_Translator` —— 2/10 个有
- `WanVideoLoraSelect` —— 2/10 个有
- `WanVideoMagCache` —— 2/10 个有
- `Fast Groups Muter (rgthree)` —— 1/10 个有
- `Text` —— 1/10 个有
- `easy cleanGpuUsed` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
