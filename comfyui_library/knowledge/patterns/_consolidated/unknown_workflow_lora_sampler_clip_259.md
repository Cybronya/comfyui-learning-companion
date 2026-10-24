---
name: unknown_workflow_lora_sampler_clip_259
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9585
common_nodes: [CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, ConditioningZeroOut, DualCLIPLoader, FramePackLoraSelect, FramePackSingleFrameSampler, LoadFramePackModel, LoadImage, SaveImage, VAEDecodeTiled, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/最强姿势迁移_1958854845690228738.json, 视频生成/图生视频/动作迁移Oneframe_kisekae_V2_2073213299981905922.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_259

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/最强姿势迁移_1958854845690228738.json、视频生成/图生视频/动作迁移Oneframe_kisekae_V2_2073213299981905922.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：96%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FramePackLoraSelect`
- `FramePackSingleFrameSampler`
- `LoadFramePackModel`
- `LoadImage`
- `SaveImage`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `FramePackFindNearestBucket` —— 1/2 个有
- `GODMT_CreateList` —— 1/2 个有
- `ImageConcatMulti` —— 1/2 个有
- `ImageResize+` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `PreviewImage` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
