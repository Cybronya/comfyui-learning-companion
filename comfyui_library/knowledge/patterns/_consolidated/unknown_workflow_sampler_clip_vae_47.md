---
name: unknown_workflow_sampler_clip_vae_47
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.915
common_nodes: [CLIPTextEncode, DualCLIPLoader, LoadImage, PreviewImage, SaveImage, VAEDecode, VAELoader, WithAnyoneModelLoaderNode, WithAnyoneSamplerNode, WithAnyoneSinglePersonConditioningNode]
problems: []
missing: []
members: [图片生成/图生图/WithAnyone多人合影工作流_1986924641862266881.json, 图片生成/图生图/WithAnyone多人合影工作流_2049672518990041089.json, 图片生成/文生图/BBox 画布 快捷定位 WithAnyone多人合影_1987625825740763137.json, 图片生成/文生图/WithAnyone-2人合照_1988162313423339521.json, 图片生成/文生图/WithAnyone-4人合照_1988322980231036930.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_47

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/WithAnyone多人合影工作流_1986924641862266881.json、图片生成/图生图/WithAnyone多人合影工作流_2049672518990041089.json、图片生成/文生图/BBox 画布 快捷定位 WithAnyone多人合影_1987625825740763137.json、图片生成/文生图/WithAnyone-2人合照_1988162313423339521.json、图片生成/文生图/WithAnyone-4人合照_1988322980231036930.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 5 个 workflow 都包含：
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

**可变部分**（部分 workflow 才有）：
- `ycBBoxBridge` —— 3/5 个有
- `ycCanvasBBox` —— 3/5 个有
- `WithAnyoneBBoxNode` —— 2/5 个有
- `LayerUtility: PurgeVRAM V2` —— 1/5 个有
- `SeedVR2` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
