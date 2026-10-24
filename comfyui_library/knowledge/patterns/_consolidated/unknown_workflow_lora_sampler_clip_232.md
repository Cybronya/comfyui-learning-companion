---
name: unknown_workflow_lora_sampler_clip_232
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.3525
common_nodes: [AddLabel, BasicScheduler, CFGOverride, CLIPLoader, CLIPTextEncode, EmptyLatentImage, GetNode, ImageConcatMulti, ImageResizeKJv2, KSamplerSelect, Krea2OstrisEditModelPatch, LoadImage, LoraLoaderModelOnly, ModelSamplingFlux, PrimitiveInt, PrimitiveStringMultiline, SamplerCustom, SaveImage, SeedNode, SetNode, ShowText|pysssss, TextEncodeKrea2OstrisEdit, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Krea2 风格迁移_2081076963816591362.json, 图片生成/图生图/图片风格转换krea2_2078850728155766786.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_232

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Krea2 风格迁移_2081076963816591362.json、图片生成/图生图/图片风格转换krea2_2078850728155766786.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：35%

## 共有节点

全部 2 个 workflow 都包含：
- `AddLabel`
- `BasicScheduler`
- `CFGOverride`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `GetNode`
- `ImageConcatMulti`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `Krea2OstrisEditModelPatch`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingFlux`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `SamplerCustom`
- `SaveImage`
- `SeedNode`
- `SetNode`
- `ShowText|pysssss`
- `TextEncodeKrea2OstrisEdit`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 1/2 个有
- `StringConcatenate` —— 1/2 个有
- `TTResolutionSelector` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 832 | - | 2 | 100% |
| 高度 | 1216 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 832，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1216，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
