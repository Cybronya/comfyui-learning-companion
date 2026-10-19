---
name: unknown_workflow_video_lora_sampler_390
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.774833
common_nodes: [DownloadAndLoadHyVideoTextEncoder, HyVideoBlockSwap, HyVideoDecode, HyVideoEncodeKeyframes, HyVideoEnhanceAVideo, HyVideoLoraSelect, HyVideoModelLoader, HyVideoSampler, HyVideoTeaCache, HyVideoTextEncode, HyVideoVAELoader, LoadImage, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/1905259795853529090.json, 视频生成/图生视频/1898964861882454017.json, 视频生成/文生视频/1902236284432359426.json, 视频生成/文生视频/混元前后关键帧控制-图生视频工作流_2041411541697830913.json, 视频生成/文生视频/1899158148928720898.json, 视频生成/文生视频/1937073069645271041.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_390

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/1905259795853529090.json、视频生成/图生视频/1898964861882454017.json、视频生成/文生视频/1902236284432359426.json、视频生成/文生视频/混元前后关键帧控制-图生视频工作流_2041411541697830913.json、视频生成/文生视频/1899158148928720898.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：77%

## 共有节点

全部 6 个 workflow 都包含：
- `DownloadAndLoadHyVideoTextEncoder`
- `HyVideoBlockSwap`
- `HyVideoDecode`
- `HyVideoEncodeKeyframes`
- `HyVideoEnhanceAVideo`
- `HyVideoLoraSelect`
- `HyVideoModelLoader`
- `HyVideoSampler`
- `HyVideoTeaCache`
- `HyVideoTextEncode`
- `HyVideoVAELoader`
- `LoadImage`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `GetImageSizeAndCount` —— 5/6 个有
- `HyVideoTorchCompileSettings` —— 5/6 个有
- `INTConstant` —— 5/6 个有
- `ImageScale` —— 5/6 个有
- `GetNode` —— 4/6 个有
- `SetNode` —— 4/6 个有
- `AddLabel` —— 2/6 个有
- `EmptyImage` —— 2/6 个有
- `ImageConcatMulti` —— 2/6 个有
- `LayerUtility: PurgeVRAM` —— 2/6 个有
- `ColorMatch` —— 1/6 个有
- `ImageResizeKJ` —— 1/6 个有
- `Int` —— 1/6 个有
- `Note Plus (mtb)` —— 1/6 个有
- `TextInput_` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
