---
name: unknown_workflow_lora_sampler_clip_40
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.695429
common_nodes: [BasicScheduler, BerniniConditioning, CLIPLoader, CLIPTextEncode, KSamplerSelect, LoraLoaderModelOnly, PrimitiveInt, PrimitiveStringMultiline, SamplerCustom, SplitSigmas, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/bernini_宝藏模型_T2I 文生图_2066848208415969281.json, 视频生成/图生视频/2082419589669015553.json, 视频生成/图生视频/2082414642227404801.json, 视频生成/图生视频/2080281287134367745.json, 视频生成/图生视频/2066854228743778305.json, 视频生成/图生视频/2066854283353612289.json, 视频生成/文生视频/Bernini 文生视频_2082360670233911297.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_40

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/bernini_宝藏模型_T2I 文生图_2066848208415969281.json、视频生成/图生视频/2082419589669015553.json、视频生成/图生视频/2082414642227404801.json、视频生成/图生视频/2080281287134367745.json、视频生成/图生视频/2066854228743778305.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：70%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicScheduler`
- `BerniniConditioning`
- `CLIPLoader`
- `CLIPTextEncode`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `SamplerCustom`
- `SplitSigmas`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `SimpleComparison+` —— 6/7 个有
- `VHS_VideoCombine` —— 6/7 个有
- `easy ifElse` —— 6/7 个有
- `LoadImage` —— 5/7 个有
- `ComfySwitchNode` —— 3/7 个有
- `PrimitiveBoolean` —— 3/7 个有
- `PrimitiveFloat` —— 3/7 个有
- `BatchImagesNode` —— 2/7 个有
- `ImageResizeKJv2` —— 1/7 个有
- `SaveImage` —— 1/7 个有
- `VHS_LoadVideo` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
