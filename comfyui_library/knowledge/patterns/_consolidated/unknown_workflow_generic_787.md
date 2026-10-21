---
name: unknown_workflow_generic_787
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.893
common_nodes: [LoadImage, SaveImage, SeeThrough_GenerateDepth, SeeThrough_GenerateLayers, SeeThrough_LoadDepthModel, SeeThrough_LoadLayerDiffModel, SeeThrough_PostProcess, SeeThrough_SavePSD]
problems: []
missing: []
members: [图片生成/文生图/seethrough-动漫人物图层拆分_2073317814898876418.json, 视频生成/图生视频/2051130633145073665.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_787

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/seethrough-动漫人物图层拆分_2073317814898876418.json、视频生成/图生视频/2051130633145073665.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：89%

## 共有节点

全部 2 个 workflow 都包含：
- `LoadImage`
- `SaveImage`
- `SeeThrough_GenerateDepth`
- `SeeThrough_GenerateLayers`
- `SeeThrough_LoadDepthModel`
- `SeeThrough_LoadLayerDiffModel`
- `SeeThrough_PostProcess`
- `SeeThrough_SavePSD`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
