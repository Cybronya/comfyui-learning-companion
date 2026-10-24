---
name: unknown_workflow_upscale_lora_sampler_85
type: Unknown Workflow
frequency: 2
level: weak
coverage: 1
common_nodes: [CheckpointLoaderSimple, EmptySD3LatentImage, ImageResizeKJv2, Krea2EditGroundedEncode, Krea2EditModelPatch, LoadImage, LoraLoaderModelOnly, SaveImage, VAEEncode, WujiCleaner, WujiSampler, WujiUpscaler]
problems: []
missing: []
members: [图片生成/图生图/Krea2 四视图角色资产库，MiniMaxH3、Seedance视频参考专用_2092271423229353985.json, 图片生成/图生图/Krea2 四视图角色资产库，角色卡，人物卡片_2098983922431520769.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_85

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Krea2 四视图角色资产库，MiniMaxH3、Seedance视频参考专用_2092271423229353985.json、图片生成/图生图/Krea2 四视图角色资产库，角色卡，人物卡片_2098983922431520769.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：100%

## 共有节点

全部 2 个 workflow 都包含：
- `CheckpointLoaderSimple`
- `EmptySD3LatentImage`
- `ImageResizeKJv2`
- `Krea2EditGroundedEncode`
- `Krea2EditModelPatch`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `VAEEncode`
- `WujiCleaner`
- `WujiSampler`
- `WujiUpscaler`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
