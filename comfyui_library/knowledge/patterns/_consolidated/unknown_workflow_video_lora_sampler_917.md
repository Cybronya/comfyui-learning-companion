---
name: unknown_workflow_video_lora_sampler_917
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8375
common_nodes: [GetImageSizeAndCount, GetNode, INTConstant, ImageResizeKJv2, LoadImage, LoadWanVideoT5TextEncoder, MathExpression|pysssss, SetNode, SimpleMath+, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVAELoader, easy batchAnything, easy forLoopEnd, easy forLoopStart, easy seed]
problems: []
missing: []
members: [视频生成/图生视频/1981043696474931201.json, 视频生成/文生视频/svi-film-转绘循环-8帧重叠_1983865424628613121.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_917

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/1981043696474931201.json、视频生成/文生视频/svi-film-转绘循环-8帧重叠_1983865424628613121.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：84%

## 共有节点

全部 2 个 workflow 都包含：
- `GetImageSizeAndCount`
- `GetNode`
- `INTConstant`
- `ImageResizeKJv2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MathExpression|pysssss`
- `SetNode`
- `SimpleMath+`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVACEEncode`
- `WanVideoVACEModelSelect`
- `WanVideoVAELoader`
- `easy batchAnything`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy seed`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 1/2 个有
- `DWPreprocessor` —— 1/2 个有
- `GetImageRangeFromBatch` —— 1/2 个有
- `ImageBatch` —— 1/2 个有
- `ImageFromBatch` —— 1/2 个有
- `ImpactInt` —— 1/2 个有
- `ImpactSwitch` —— 1/2 个有
- `Int` —— 1/2 个有
- `JWInteger` —— 1/2 个有
- `VHS_BatchManager` —— 1/2 个有
- `VHS_VideoInfoLoaded` —— 1/2 个有
- `WanVideoSLG` —— 1/2 个有
- `WanVideoVACEStartToEndFrame` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
