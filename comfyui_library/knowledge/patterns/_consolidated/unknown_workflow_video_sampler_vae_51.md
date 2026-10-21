---
name: unknown_workflow_video_sampler_vae_51
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.713
common_nodes: [GetNode, INTConstant, ImageResizeKJv2, LoadWanVideoT5TextEncoder, PreviewImage, SetNode, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1922913039635419137.json, 视频生成/图生视频/1927920381506797569.json, 视频生成/图生视频/1922904256758648834.json, 视频生成/图生视频/1930513841942118401.json, 视频生成/图生视频/1924699214469918722.json, 视频生成/图生视频/1922890736801386498.json, 视频生成/图生视频/1931161804242923521.json, 视频生成/图生视频/1922918753066172418.json, 视频生成/图生视频/1929011681165262850.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_51

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/1922913039635419137.json、视频生成/图生视频/1927920381506797569.json、视频生成/图生视频/1922904256758648834.json、视频生成/图生视频/1930513841942118401.json、视频生成/图生视频/1924699214469918722.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：71%

## 共有节点

全部 9 个 workflow 都包含：
- `GetNode`
- `INTConstant`
- `ImageResizeKJv2`
- `LoadWanVideoT5TextEncoder`
- `PreviewImage`
- `SetNode`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVACEEncode`
- `WanVideoVACEModelSelect`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 8/9 个有
- `WanVideoEnhanceAVideo` —— 8/9 个有
- `WanVideoExperimentalArgs` —— 8/9 个有
- `WanVideoSLG` —— 8/9 个有
- `Label (rgthree)` —— 7/9 个有
- `RMBG` —— 6/9 个有
- `VHS_LoadVideo` —— 6/9 个有
- `WanVideoTeaCache` —— 4/9 个有
- `ImageResizeKJ` —— 3/9 个有
- `MaskToImage` —— 3/9 个有
- `Mix Color By Mask` —— 3/9 个有
- `DownloadAndLoadSAM2Model` —— 2/9 个有
- `GrowMaskWithBlur` —— 2/9 个有
- `OpenposePreprocessor` —— 2/9 个有
- `PointsEditor` —— 2/9 个有
- `Sam2Segmentation` —— 2/9 个有
- `WanVideoLoraSelect` —— 2/9 个有
- `DWPreprocessor` —— 1/9 个有
- `DepthAnythingV2Preprocessor` —— 1/9 个有
- `ImageBatchGet` —— 1/9 个有
- `InvertMask` —— 1/9 个有
- `SAMLoader` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
