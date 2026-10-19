---
name: unknown_workflow_video_lora_sampler_353
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.72
common_nodes: [BasicScheduler, BerniniConditioning, CLIPLoader, CLIPTextEncode, KSamplerSelect, LoraLoaderModelOnly, PrimitiveInt, PrimitiveStringMultiline, SamplerCustom, SimpleComparison+, SplitSigmas, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, easy ifElse]
problems: []
missing: []
members: [视频生成/图生视频/2082419589669015553.json, 视频生成/图生视频/2082414642227404801.json, 视频生成/图生视频/2080281287134367745.json, 视频生成/图生视频/2066854228743778305.json, 视频生成/图生视频/2066854283353612289.json, 视频生成/文生视频/Bernini 文生视频_2082360670233911297.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_353

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/2082419589669015553.json、视频生成/图生视频/2082414642227404801.json、视频生成/图生视频/2080281287134367745.json、视频生成/图生视频/2066854228743778305.json、视频生成/图生视频/2066854283353612289.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：72%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicScheduler`
- `BerniniConditioning`
- `CLIPLoader`
- `CLIPTextEncode`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `SamplerCustom`
- `SimpleComparison+`
- `SplitSigmas`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `easy ifElse`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 5/6 个有
- `BatchImagesNode` —— 2/6 个有
- `ComfySwitchNode` —— 2/6 个有
- `PrimitiveBoolean` —— 2/6 个有
- `PrimitiveFloat` —— 2/6 个有
- `ImageResizeKJv2` —— 1/6 个有
- `VHS_LoadVideo` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
