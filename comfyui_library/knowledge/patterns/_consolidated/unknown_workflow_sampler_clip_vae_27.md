---
name: unknown_workflow_sampler_clip_vae_27
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.882667
common_nodes: [CLIPTextEncode, DualCLIPLoader, LoadImage, PreviewImage, SaveImage, VAEDecode, VAELoader, WithAnyoneModelLoaderNode, WithAnyoneSamplerNode, WithAnyoneSinglePersonConditioningNode, ycBBoxBridge, ycCanvasBBox]
problems: []
missing: [LayerUtility: PurgeVRAM V2]
members: [图片生成/文生图/1987625825740763137.json, 图片生成/文生图/1988162313423339521.json, 图片生成/文生图/1988322980231036930.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_27

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/1987625825740763137.json、图片生成/文生图/1988162313423339521.json、图片生成/文生图/1988322980231036930.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `VAEDecode`
- `VAELoader`
- `WithAnyoneModelLoaderNode`
- `WithAnyoneSamplerNode`
- `WithAnyoneSinglePersonConditioningNode`
- `ycBBoxBridge`
- `ycCanvasBBox`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: PurgeVRAM V2` —— 1/3 个有
- `SeedVR2` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: PurgeVRAM V2
