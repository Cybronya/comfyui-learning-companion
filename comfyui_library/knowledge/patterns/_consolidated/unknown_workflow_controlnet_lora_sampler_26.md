---
name: unknown_workflow_controlnet_lora_sampler_26
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.841
common_nodes: [AIO_Preprocessor, BasicGuider, BasicScheduler, CLIPTextEncode, CR Text, ConditioningZeroOut, ControlNetApplyAdvanced, ControlNetLoader, DualCLIPLoader, EmptyLatentImage, FluxGuidance, GetImageSize+, Image Comparer (rgthree), ImitationHueNode, JWImageResizeByLongerSide, KSamplerSelect, LayerFilter: AddGrain, LayerMask: Shadow & Highlight Mask, LayerUtility: ImageBlend, LoadImage, LoraLoaderModelOnly, PreviewImage, RH_LLMAPI_NODE, RandomNoise, SamplerCustomAdvanced, SaveImage, SetUnionControlNetType, StringFunction|pysssss, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/【洗图】网红一键洗图-提升真实感_1942064097208987649.json, 图片生成/图生图/人物洗图_1958372133011406849.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_lora_sampler_26

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/【洗图】网红一键洗图-提升真实感_1942064097208987649.json、图片生成/图生图/人物洗图_1958372133011406849.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：84%

## 共有节点

全部 2 个 workflow 都包含：
- `AIO_Preprocessor`
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `CR Text`
- `ConditioningZeroOut`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FluxGuidance`
- `GetImageSize+`
- `Image Comparer (rgthree)`
- `ImitationHueNode`
- `JWImageResizeByLongerSide`
- `KSamplerSelect`
- `LayerFilter: AddGrain`
- `LayerMask: Shadow & Highlight Mask`
- `LayerUtility: ImageBlend`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `RH_LLMAPI_NODE`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SetUnionControlNetType`
- `StringFunction|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.68 | - | 2 | 100% |
| 宽度 | 768 | - | 2 | 100% |
| 高度 | 1024 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.68，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 768，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
