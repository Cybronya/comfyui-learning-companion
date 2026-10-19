---
name: unknown_workflow_sampler_clip_unet_80
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.915667
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, DualCFGGuider, EmptySD3LatentImage, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [comfyui-workflow-templates-json/image_omnigen2_image_edit.json, 图片生成/文生图/1939949487580160001.json, 图片生成/文生图/1943503078144286722.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_80

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（comfyui-workflow-templates-json/image_omnigen2_image_edit.json、图片生成/文生图/1939949487580160001.json、图片生成/文生图/1943503078144286722.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `DualCFGGuider`
- `EmptySD3LatentImage`
- `KSamplerSelect`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `GetImageSize` —— 1/3 个有
- `ImageScaleToTotalPixels` —— 1/3 个有
- `LoadImage` —— 1/3 个有
- `ReferenceLatent` —— 1/3 个有
- `VAEEncode` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
