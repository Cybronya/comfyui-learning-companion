---
name: unknown_workflow_sampler_96
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.69
common_nodes: [DF_Get_image_size, ImageCompositeMasked, ImageResize+, ImageResizeKJv2, JjkText, LBMSampler, LoadImage, LoadLBMModel, PreviewImage, RH_ComfyFluxKontext, RH_Translator, RMBG, SaveImage, ShowText, TextCombinerSix, easy imageConcat]
problems: []
missing: []
members: [图片生成/文生图/Flux Kontext一键换产品_1947854784697090050.json, 平台全量/Flux Kontext一键融图打光_1942844679140347905.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_96

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/Flux Kontext一键换产品_1947854784697090050.json、平台全量/Flux Kontext一键融图打光_1942844679140347905.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：69%

## 共有节点

全部 2 个 workflow 都包含：
- `DF_Get_image_size`
- `ImageCompositeMasked`
- `ImageResize+`
- `ImageResizeKJv2`
- `JjkText`
- `LBMSampler`
- `LoadImage`
- `LoadLBMModel`
- `PreviewImage`
- `RH_ComfyFluxKontext`
- `RH_Translator`
- `RMBG`
- `SaveImage`
- `ShowText`
- `TextCombinerSix`
- `easy imageConcat`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
