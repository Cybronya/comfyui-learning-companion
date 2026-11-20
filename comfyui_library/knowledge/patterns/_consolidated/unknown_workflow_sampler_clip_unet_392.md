---
name: unknown_workflow_sampler_clip_unet_392
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.950667
common_nodes: [BasicScheduler, CLIPAttentionMultiply, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, KSamplerSelect, LoadAndResizeImage, MaskHoleFiller, SamplerCustom, SaveImage, Seed (rgthree), SigmasEditor, UNETLoader, VAEDecode, VAELoader, ZImageTimestepNoise]
problems: []
missing: []
members: [图片生成/文生图/Z-IMAGE批次随机性增强_2026919909292249089.json, 图片生成/文生图/【LG】Z-IMAGE批次随机性增强_2004095661245120513.json, 图片生成/文生图/指定区域Z-image-随机性增强出图-蒙版_2004367556561563649.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_392

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Z-IMAGE批次随机性增强_2026919909292249089.json、图片生成/文生图/【LG】Z-IMAGE批次随机性增强_2004095661245120513.json、图片生成/文生图/指定区域Z-image-随机性增强出图-蒙版_2004367556561563649.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicScheduler`
- `CLIPAttentionMultiply`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `KSamplerSelect`
- `LoadAndResizeImage`
- `MaskHoleFiller`
- `SamplerCustom`
- `SaveImage`
- `Seed (rgthree)`
- `SigmasEditor`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `ZImageTimestepNoise`

**可变部分**（部分 workflow 才有）：
- `SizeNode` —— 2/3 个有
- `CR Text` —— 1/3 个有
- `LayerMask: MaskPreview` —— 1/3 个有
- `MuyeSizeSelector` —— 1/3 个有
- `MuyeTextEditOutput` —— 1/3 个有
- `easy float` —— 1/3 个有
- `easy int` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
