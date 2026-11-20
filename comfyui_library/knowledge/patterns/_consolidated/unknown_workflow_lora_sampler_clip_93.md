---
name: unknown_workflow_lora_sampler_clip_93
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.897
common_nodes: [BasicScheduler, BatchImagesNode, BerniniConditioning, CLIPLoader, CLIPTextEncode, CreateVideo, GetVideoComponents, KSamplerSelect, LoadVideo, LoraLoaderModelOnly, PathchSageAttentionKJ, SamplerCustom, SaveVideo, SplitSigmas, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [平台全量/Bernini参考图主体更换_2062157335388319746.json, 平台全量/Bernini参考视频更换指定画面_2062178027064356866.json, 平台全量/Bernini视频编辑_2062220064002236418.json, 平台全量/wan2.2 bernini 视频编辑、人物替换、动作迁移_2062367684234407937.json, 视频生成/图生视频/Bernini多模态视频编辑_2062112812658417666.json, 视频生成/图生视频/wan-Bernini 单人视频编辑+动作迁移 V4_2062167785479950338.json, 视频生成/图生视频/wan-Bernini 单人视频编辑+动作迁移 V4_2066715725934448641.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_93

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（平台全量/Bernini参考图主体更换_2062157335388319746.json、平台全量/Bernini参考视频更换指定画面_2062178027064356866.json、平台全量/Bernini视频编辑_2062220064002236418.json、平台全量/wan2.2 bernini 视频编辑、人物替换、动作迁移_2062367684234407937.json、视频生成/图生视频/Bernini多模态视频编辑_2062112812658417666.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicScheduler`
- `BatchImagesNode`
- `BerniniConditioning`
- `CLIPLoader`
- `CLIPTextEncode`
- `CreateVideo`
- `GetVideoComponents`
- `KSamplerSelect`
- `LoadVideo`
- `LoraLoaderModelOnly`
- `PathchSageAttentionKJ`
- `SamplerCustom`
- `SaveVideo`
- `SplitSigmas`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 6/7 个有
- `CR Text` —— 3/7 个有
- `ImageFromBatch` —— 3/7 个有
- `Int` —— 3/7 个有
- `VHS_VideoCombine` —— 3/7 个有
- `Fast Groups Bypasser (rgthree)` —— 2/7 个有
- `GetImageSize` —— 2/7 个有
- `PrimitiveInt` —— 2/7 个有
- `TextInput_` —— 2/7 个有
- `easy imageScaleDownToSize` —— 2/7 个有
- `ttN seed` —— 2/7 个有
- `INTConstant` —— 1/7 个有
- `ImageConcanate` —— 1/7 个有
- `SimpleMath+` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
