---
name: unknown_workflow_video_lora_sampler_457
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.8384
common_nodes: [ApplyFaceProcessor, FaceProcessorLoader, ImageResizeKJv2, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoAddStandInLatent, WanVideoBlockSwap, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVACEModelSelect, WanVideoVAELoader, easy imageRemBg]
problems: []
missing: []
members: [视频生成/图生视频/1956266863963590657.json, 视频生成/文生视频/03-12-01-WAN2.1-脸部参考文生视频-Standin_1989933889823100930.json, 视频生成/文生视频/1956789708207394817.json, 视频生成/文生视频/1956768845814796289.json, 视频生成/文生视频/1957446441918722049.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_457

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/1956266863963590657.json、视频生成/文生视频/03-12-01-WAN2.1-脸部参考文生视频-Standin_1989933889823100930.json、视频生成/文生视频/1956789708207394817.json、视频生成/文生视频/1956768845814796289.json、视频生成/文生视频/1957446441918722049.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 5 个 workflow 都包含：
- `ApplyFaceProcessor`
- `FaceProcessorLoader`
- `ImageResizeKJv2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoAddStandInLatent`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoVACEModelSelect`
- `WanVideoVAELoader`
- `easy imageRemBg`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 4/5 个有
- `ImageConcanate` —— 4/5 个有
- `ImpactInt` —— 4/5 个有
- `INTConstant` —— 3/5 个有
- `JWInteger` —— 2/5 个有
- `SimpleMath+` —— 2/5 个有
- `WanVideoTorchCompileSettings` —— 2/5 个有
- `GetNode` —— 1/5 个有
- `JjkText` —— 1/5 个有
- `Note Plus (mtb)` —— 1/5 个有
- `SetNode` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
