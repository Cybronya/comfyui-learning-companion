---
name: unknown_workflow_lora_sampler_clip_200
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.972333
common_nodes: [CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, ConditioningZeroOut, DualCLIPLoader, FramePackLoraSelect, FramePackSingleFrameSampler, LoadFramePackModel, LoadImage, SaveImage, VAEDecodeTiled, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/最强姿势迁移_1958854845690228738.json, 数字人/数字人/动作迁移_1970863650342899713.json, 视频生成/图生视频/动作迁移Oneframe_kisekae_V2_2073213299981905922.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_200

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/最强姿势迁移_1958854845690228738.json、数字人/数字人/动作迁移_1970863650342899713.json、视频生成/图生视频/动作迁移Oneframe_kisekae_V2_2073213299981905922.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 3 个 workflow 都包含：
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
- `FramePackFindNearestBucket` —— 2/3 个有
- `GODMT_CreateList` —— 1/3 个有
- `ImageConcatMulti` —— 1/3 个有
- `ImageResize+` —— 1/3 个有
- `ImageResizeKJv2` —— 1/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有
- `PreviewImage` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
