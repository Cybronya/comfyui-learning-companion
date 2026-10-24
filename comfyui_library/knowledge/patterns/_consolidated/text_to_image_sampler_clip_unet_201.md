---
name: text_to_image_sampler_clip_unet_201
type: Text To Image
frequency: 2
level: weak
coverage: 0.894
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, EmptyLatentImage, FluxGuidance, FluxKontextImageScale, FluxResolutionNode, ImageStitch, KSampler, LayerUtility: Boolean, LayerUtility: If , LayerUtility: ImageScaleRestore, LayerUtility: ZhipuGLM4, LoadImage, MathExpression|pysssss, PreviewImage, PrimitiveStringMultiline, RH_Translator, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader, workflow>抠图3, workflow>抠图4, workflow>抠图5]
problems: []
missing: []
members: [图片生成/图生图/Context_极简超舒适界面+32种提示词预设_1943126196676943874.json, 图片生成/图生图/Context_极简超舒适界面、支持3图混合修改_1938513720891105281.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_201

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Context_极简超舒适界面+32种提示词预设_1943126196676943874.json、图片生成/图生图/Context_极简超舒适界面、支持3图混合修改_1938513720891105281.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：89%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FluxGuidance`
- `FluxKontextImageScale`
- `FluxResolutionNode`
- `ImageStitch`
- `KSampler`
- `LayerUtility: Boolean`
- `LayerUtility: If `
- `LayerUtility: ImageScaleRestore`
- `LayerUtility: ZhipuGLM4`
- `LoadImage`
- `MathExpression|pysssss`
- `PreviewImage`
- `PrimitiveStringMultiline`
- `RH_Translator`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `workflow>抠图3`
- `workflow>抠图4`
- `workflow>抠图5`

**可变部分**（部分 workflow 才有）：
- `Bjornulf_ShowStringText` —— 1/2 个有
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `ImpactInt` —— 1/2 个有
- `LayerUtility: BooleanOperator` —— 1/2 个有
- `LoraLoader` —— 1/2 个有
- `ShowText|pysssss` —— 1/2 个有
- `SomethingToString` —— 1/2 个有
- `StringConcatenate` —— 1/2 个有
- `Text Multiline` —— 1/2 个有
- `workflow>抠图` —— 1/2 个有
- `workflow>抠图2` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | - | 2 | 100% |
| 高度 | 1280 | - | 2 | 100% |
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |
| 采样步数 | 40 | - | 2 | 50% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1280，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 40，样本不足，未给区间，2 个样本
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
