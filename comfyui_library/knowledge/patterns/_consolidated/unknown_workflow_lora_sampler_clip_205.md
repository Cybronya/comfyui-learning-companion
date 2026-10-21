---
name: unknown_workflow_lora_sampler_clip_205
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.936
common_nodes: [CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, ConditioningZeroOut, DualCLIPLoader, FramePackFindNearestBucket, FramePackLoraSelect, FramePackSingleFrameSampler, ImageConcatMulti, ImageResize+, LoadFramePackModel, LoadImage, PreviewImage, SaveImage, VAEDecodeTiled, VAEEncode, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/2073213299981905922.json, 视频生成/图生视频/1935136983549157377.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_205

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/2073213299981905922.json、视频生成/图生视频/1935136983549157377.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：94%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FramePackFindNearestBucket`
- `FramePackLoraSelect`
- `FramePackSingleFrameSampler`
- `ImageConcatMulti`
- `ImageResize+`
- `LoadFramePackModel`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 1/2 个有
- `FramePackTorchCompileSettings` —— 1/2 个有
- `GODMT_CreateList` —— 1/2 个有
- `Image Rembg (Remove Background)` —— 1/2 个有
- `JWInteger` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
