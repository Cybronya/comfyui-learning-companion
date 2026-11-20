---
name: unknown_workflow_sampler_clip_unet_477
type: Unknown Workflow
frequency: 2
level: weak
coverage: 1
common_nodes: [CLIPTextEncode, CR Seed, DualCLIPLoader, FluxSamplerParams+, Image Compare (mtb), Int2String, LoadImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/FLUX图生图工作流（大全）_2048759695099301889.json, 平台全量/FLUX图生图工作流（大全）_2048437283350646785.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_477

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/FLUX图生图工作流（大全）_2048759695099301889.json、平台全量/FLUX图生图工作流（大全）_2048437283350646785.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：100%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CR Seed`
- `DualCLIPLoader`
- `FluxSamplerParams+`
- `Image Compare (mtb)`
- `Int2String`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
