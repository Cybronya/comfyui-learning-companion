---
name: unknown_workflow_lora_sampler_13
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7915
common_nodes: [CR Text, FluxTextDrawGlyph, FluxTextLoraLoader, FluxTextPipeLine, FluxTextSampler, ImageConcanate, ImageResizeKJv2, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, MaskToImage, PreviewImage, SaveImage]
problems: []
missing: []
members: [图片生成/图生图/最强FluxText文字编辑，支持中文，字体风格自动匹配_1942904378175217666.json, 平台全量/👺【中文更换】FluxText中文字体更换【面霸版】~👺_1943254794603819010.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_13

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/最强FluxText文字编辑，支持中文，字体风格自动匹配_1942904378175217666.json、平台全量/👺【中文更换】FluxText中文字体更换【面霸版】~👺_1943254794603819010.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：79%

## 共有节点

全部 2 个 workflow 都包含：
- `CR Text`
- `FluxTextDrawGlyph`
- `FluxTextLoraLoader`
- `FluxTextPipeLine`
- `FluxTextSampler`
- `ImageConcanate`
- `ImageResizeKJv2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `MaskToImage`
- `PreviewImage`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `ColorMatch` —— 1/2 个有
- `ImitationHueNode` —— 1/2 个有
- `Mask Fill Holes` —— 1/2 个有
- `easy imageSize` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
