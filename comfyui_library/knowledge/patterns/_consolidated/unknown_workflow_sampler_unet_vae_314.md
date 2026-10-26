---
name: unknown_workflow_sampler_unet_vae_314
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.864
common_nodes: [BasicScheduler, CLIPLoader, CR Text, EmptyLatentImage, KSamplerSelect, LoadImage, ModelSamplingAuraFlow, PreviewImage, RHHiddenNodes, RH_LLMAPI_Pro_Node, SamplerCustom, SaveImage, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlusAdvance_lrzjason, UNETLoader, VAEDecode, VAELoader, easy promptLine, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/V3 Boogu-Image 批量电商主图  本地可跑 适合于 情趣 养生 等类目_2068702253560717313.json, 图片生成/图生图/V3 Boogu-Image 批量详情 10张  开源本地可跑_2068718937306652673.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_314

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/V3 Boogu-Image 批量电商主图  本地可跑 适合于 情趣 养生 等类目_2068702253560717313.json、图片生成/图生图/V3 Boogu-Image 批量详情 10张  开源本地可跑_2068718937306652673.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：86%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CR Text`
- `EmptyLatentImage`
- `KSamplerSelect`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `RHHiddenNodes`
- `RH_LLMAPI_Pro_Node`
- `SamplerCustom`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy promptLine`
- `easy showAnything`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1152 | - | 2 | 78% |
| 高度 | 1500 | - | 2 | 93% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1152，样本不足，未给区间，2 个样本
- 高度 中位数 1500，样本不足，未给区间，2 个样本，取值集中（一致性 93%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
