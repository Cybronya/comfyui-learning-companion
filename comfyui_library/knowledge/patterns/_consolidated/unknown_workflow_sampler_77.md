---
name: unknown_workflow_sampler_77
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.867
common_nodes: [AIO_Preprocessor, GetImageSizeAndCount, ImageConcanate, LayerUtility: TextJoin, LoadImage, PreviewImage, RH_Captioner, RunningHub QwenImage Canny Pipeline, RunningHub QwenImage Canny Sampler, SaveImage, Text Multiline, easy imageScaleDownToSize, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/QwenImage深度控制-Depth深度_1958211256522051585.json, 图片生成/文生图/QwenImage线稿控制-Canny_1956777535356985346.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_77

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/QwenImage深度控制-Depth深度_1958211256522051585.json、图片生成/文生图/QwenImage线稿控制-Canny_1956777535356985346.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：87%

## 共有节点

全部 2 个 workflow 都包含：
- `AIO_Preprocessor`
- `GetImageSizeAndCount`
- `ImageConcanate`
- `LayerUtility: TextJoin`
- `LoadImage`
- `PreviewImage`
- `RH_Captioner`
- `RunningHub QwenImage Canny Pipeline`
- `RunningHub QwenImage Canny Sampler`
- `SaveImage`
- `Text Multiline`
- `easy imageScaleDownToSize`
- `easy showAnything`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
