---
name: unknown_workflow_sampler_vae_59
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.77575
common_nodes: [LoadImage, LoadLotusModel, LotusSampler, PreviewImage, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Lotus_深度+法线预测_BY_ZERO_1940232640807223298.json, 图片生成/图生图/图片转法线深度贴图工作流_2034509684610174978.json, 平台全量/图片转法线深度贴图工作流_2032773935200210945.json, 平台全量/法线与深度图生成_1858914488073293825.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_vae_59

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Lotus_深度+法线预测_BY_ZERO_1940232640807223298.json、图片生成/图生图/图片转法线深度贴图工作流_2034509684610174978.json、平台全量/图片转法线深度贴图工作流_2032773935200210945.json、平台全量/法线与深度图生成_1858914488073293825.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：78%

## 共有节点

全部 4 个 workflow 都包含：
- `LoadImage`
- `LoadLotusModel`
- `LotusSampler`
- `PreviewImage`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageInvert` —— 3/4 个有
- `Image Comparer (rgthree)` —— 2/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
