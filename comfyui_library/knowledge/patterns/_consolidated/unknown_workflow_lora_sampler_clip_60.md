---
name: unknown_workflow_lora_sampler_clip_60
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.667333
common_nodes: [BasicScheduler, BerniniConditioning, CLIPLoader, CLIPTextEncode, KSamplerSelect, LoraLoaderModelOnly, PrimitiveInt, PrimitiveStringMultiline, SamplerCustom, SplitSigmas, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/bernini_宝藏模型_T2I 文生图_2066848208415969281.json, 平台全量/Bernini_宝藏模型_视频编辑+参考图_2073700701599002626.json, 平台全量/Bernini_宝藏模型给_视频编辑_2066854264764461057.json, 视频生成/图生视频/Bernini 三图参考生视频_2082419589669015553.json, 视频生成/图生视频/Bernini 双图参考生视频_2082414642227404801.json, 视频生成/图生视频/Bernini 图生视频_2080281287134367745.json, 视频生成/图生视频/Bernini_宝藏模型_参考生视频_2066854228743778305.json, 视频生成/图生视频/Bernini_宝藏模型_视频编辑+参考图_2066854283353612289.json, 视频生成/文生视频/Bernini 文生视频_2082360670233911297.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_60

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/文生图/bernini_宝藏模型_T2I 文生图_2066848208415969281.json、平台全量/Bernini_宝藏模型_视频编辑+参考图_2073700701599002626.json、平台全量/Bernini_宝藏模型给_视频编辑_2066854264764461057.json、视频生成/图生视频/Bernini 三图参考生视频_2082419589669015553.json、视频生成/图生视频/Bernini 双图参考生视频_2082414642227404801.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：67%

## 共有节点

全部 9 个 workflow 都包含：
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
- `VHS_VideoCombine` —— 8/9 个有
- `SimpleComparison+` —— 7/9 个有
- `easy ifElse` —— 7/9 个有
- `LoadImage` —— 6/9 个有
- `ComfySwitchNode` —— 5/9 个有
- `PrimitiveBoolean` —— 5/9 个有
- `PrimitiveFloat` —— 5/9 个有
- `BatchImagesNode` —— 3/9 个有
- `ImageResizeKJv2` —— 3/9 个有
- `VHS_LoadVideo` —— 3/9 个有
- `SaveImage` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
