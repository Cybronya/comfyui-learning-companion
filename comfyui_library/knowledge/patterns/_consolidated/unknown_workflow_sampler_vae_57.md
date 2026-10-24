---
name: unknown_workflow_sampler_vae_57
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.764
common_nodes: [ImageInvert, LoadImage, LoadLotusModel, LotusSampler, PreviewImage, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Lotus_深度+法线预测_BY_ZERO_1940232640807223298.json, 图片生成/图生图/图片转法线深度贴图工作流_2034509684610174978.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_vae_57

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Lotus_深度+法线预测_BY_ZERO_1940232640807223298.json、图片生成/图生图/图片转法线深度贴图工作流_2034509684610174978.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：76%

## 共有节点

全部 2 个 workflow 都包含：
- `ImageInvert`
- `LoadImage`
- `LoadLotusModel`
- `LotusSampler`
- `PreviewImage`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
