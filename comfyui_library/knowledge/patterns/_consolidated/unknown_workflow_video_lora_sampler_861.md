---
name: unknown_workflow_video_lora_sampler_861
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.862
common_nodes: [ImageConcatMulti, ImageResizeKJv2, Int, LoadImage, SimpleMath+, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVAELoader]
problems: []
missing: [SimpleMath+]
members: [视频生成/图生视频/1967598097377497089.json, 视频生成/文生视频/1971908206685515778.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_861

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/1967598097377497089.json、视频生成/文生视频/1971908206685515778.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：86%

## 共有节点

全部 2 个 workflow 都包含：
- `ImageConcatMulti`
- `ImageResizeKJv2`
- `Int`
- `LoadImage`
- `SimpleMath+`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoTextEncodeCached`
- `WanVideoTorchCompileSettings`
- `WanVideoVACEEncode`
- `WanVideoVACEModelSelect`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 1/2 个有
- `INTConstant` —— 1/2 个有
- `JjkText` —— 1/2 个有
- `SetNode` —— 1/2 个有
- `Text` —— 1/2 个有
- `WanVideoVACEStartToEndFrame` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：SimpleMath+
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
