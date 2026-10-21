---
name: unknown_workflow_video_sampler_vae_122
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.88025
common_nodes: [DownloadAndLoadHyVideoTextEncoder, HyVideoBlockSwap, HyVideoDecode, HyVideoEncode, HyVideoModelLoader, HyVideoSampler, HyVideoTorchCompileSettings, HyVideoVAELoader, ImageResizeKJ, LoadImage, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/1891816391639740418.json, 视频生成/图生视频/1892941621485580289.json, 视频生成/图生视频/1892483487939923969.json, 视频生成/图生视频/1900195867180281858.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_122

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/1891816391639740418.json、视频生成/图生视频/1892941621485580289.json、视频生成/图生视频/1892483487939923969.json、视频生成/图生视频/1900195867180281858.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 4 个 workflow 都包含：
- `DownloadAndLoadHyVideoTextEncoder`
- `HyVideoBlockSwap`
- `HyVideoDecode`
- `HyVideoEncode`
- `HyVideoModelLoader`
- `HyVideoSampler`
- `HyVideoTorchCompileSettings`
- `HyVideoVAELoader`
- `ImageResizeKJ`
- `LoadImage`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `ColorMatch` —— 3/4 个有
- `HyVideoCFG` —— 3/4 个有
- `HyVideoEnhanceAVideo` —— 3/4 个有
- `HyVideoTextEncode` —— 3/4 个有
- `DownloadAndLoadFlorence2Model` —— 2/4 个有
- `Florence2Run` —— 2/4 个有
- `HyVideoLoraSelect` —— 2/4 个有
- `HyVideoTeaCache` —— 2/4 个有
- `PreviewImage` —— 2/4 个有
- `ShowText|pysssss` —— 2/4 个有
- `StringFunction|pysssss` —— 2/4 个有
- `HyVideoI2VEncode` —— 1/4 个有
- `ImageConcatMulti` —— 1/4 个有
- `Int` —— 1/4 个有
- `LayerUtility: PurgeVRAM` —— 1/4 个有
- `String Replace (mtb)` —— 1/4 个有
- `TextInput_` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
