---
name: unknown_workflow_video_lora_sampler_213
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.702889
common_nodes: [AddLabel, DownloadAndLoadHyVideoTextEncoder, EmptyImage, GetImageSizeAndCount, GetNode, HyVideoBlockSwap, HyVideoDecode, HyVideoEncodeKeyframes, HyVideoLoraSelect, HyVideoModelLoader, HyVideoSampler, HyVideoTeaCache, HyVideoTextEncode, HyVideoVAELoader, INTConstant, ImageConcatMulti, ImageScale, LoadImage, SetNode, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/1898786623557947394.json, 视频生成/图生视频/1901229353970057217.json, 视频生成/图生视频/1912693250090594306.json, 视频生成/图生视频/1912569135262330881.json, 视频生成/图生视频/2042055349607337985.json, 视频生成/图生视频/1898632329806434306.json, 视频生成/图生视频/1898873358178537473.json, 视频生成/图生视频/1898536833251233794.json, 视频生成/文生视频/1898757029459382273.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_213

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/1898786623557947394.json、视频生成/图生视频/1901229353970057217.json、视频生成/图生视频/1912693250090594306.json、视频生成/图生视频/1912569135262330881.json、视频生成/图生视频/2042055349607337985.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：70%

## 共有节点

全部 9 个 workflow 都包含：
- `AddLabel`
- `DownloadAndLoadHyVideoTextEncoder`
- `EmptyImage`
- `GetImageSizeAndCount`
- `GetNode`
- `HyVideoBlockSwap`
- `HyVideoDecode`
- `HyVideoEncodeKeyframes`
- `HyVideoLoraSelect`
- `HyVideoModelLoader`
- `HyVideoSampler`
- `HyVideoTeaCache`
- `HyVideoTextEncode`
- `HyVideoVAELoader`
- `INTConstant`
- `ImageConcatMulti`
- `ImageScale`
- `LoadImage`
- `SetNode`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `HyVideoEnhanceAVideo` —— 8/9 个有
- `HyVideoTorchCompileSettings` —— 8/9 个有
- `LayerUtility: PurgeVRAM` —— 7/9 个有
- `ColorMatch` —— 6/9 个有
- `Note Plus (mtb)` —— 5/9 个有
- `PreviewImage` —— 5/9 个有
- `Note _O` —— 4/9 个有
- `easy cleanGpuUsed` —— 4/9 个有
- `PMRF` —— 3/9 个有
- `Primitive string [Crystools]` —— 1/9 个有
- `TextInput_` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
