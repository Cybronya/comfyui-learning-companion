---
name: unknown_workflow_video_sampler_vae_163
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.863333
common_nodes: [ADE_CameraPoseBasic, CameraPoseVisualizer, INTConstant, ImageConcatMulti, LoadImage, LoadWanVideoT5TextEncoder, PreviewImage, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoExperimentalArgs, WanVideoFunCameraEmbeds, WanVideoImageToVideoEncode, WanVideoModelLoader, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1917932586730196994.json, 视频生成/图生视频/1924473517754994690.json, 视频生成/文生视频/1929007015320829954.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_163

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/1917932586730196994.json、视频生成/图生视频/1924473517754994690.json、视频生成/文生视频/1929007015320829954.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 3 个 workflow 都包含：
- `ADE_CameraPoseBasic`
- `CameraPoseVisualizer`
- `INTConstant`
- `ImageConcatMulti`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `PreviewImage`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoExperimentalArgs`
- `WanVideoFunCameraEmbeds`
- `WanVideoImageToVideoEncode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/3 个有
- `WanVideoTorchCompileSettings` —— 2/3 个有
- `Any Switch (rgthree)` —— 1/3 个有
- `DownloadAndLoadGIMMVFIModel` —— 1/3 个有
- `Fast Groups Muter (rgthree)` —— 1/3 个有
- `GIMMVFI_interpolate` —— 1/3 个有
- `ImageResizeKJ` —— 1/3 个有
- `LayerUtility: TextBox` —— 1/3 个有
- `Text Multiline` —— 1/3 个有
- `WanVideoLoraSelect` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
