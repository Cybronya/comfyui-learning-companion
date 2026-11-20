---
name: unknown_workflow_lora_sampler_clip_150
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9562
common_nodes: [CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, ConditioningZeroOut, DualCLIPLoader, FramePackLoraSelect, FramePackSingleFrameSampler, LoadFramePackModel, LoadImage, SaveImage, VAEDecodeTiled, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/最强姿势迁移_1958854845690228738.json, 平台全量/灵魂画手姿势迁移_1982730262549282817.json, 平台全量/超强姿势迁移_1959890797044903937.json, 数字人/数字人/动作迁移_1970863650342899713.json, 视频生成/图生视频/动作迁移Oneframe_kisekae_V2_2073213299981905922.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_150

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/最强姿势迁移_1958854845690228738.json、平台全量/灵魂画手姿势迁移_1982730262549282817.json、平台全量/超强姿势迁移_1959890797044903937.json、数字人/数字人/动作迁移_1970863650342899713.json、视频生成/图生视频/动作迁移Oneframe_kisekae_V2_2073213299981905922.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 5 个 workflow 都包含：
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
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/5 个有
- `FramePackFindNearestBucket` —— 2/5 个有
- `INTConstant` —— 2/5 个有
- `PreviewImage` —— 2/5 个有
- `GODMT_CreateList` —— 1/5 个有
- `ImageConcatMulti` —— 1/5 个有
- `ImageResize+` —— 1/5 个有
- `ImageResizeKJv2` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
