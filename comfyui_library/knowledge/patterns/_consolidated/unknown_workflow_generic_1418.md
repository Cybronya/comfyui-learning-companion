---
name: unknown_workflow_generic_1418
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7775
common_nodes: [Fast Groups Bypasser (rgthree), ImageConcanate, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadVideo, QwenImageEditNode, QwenImageNode, QwenVideoNode, QwenVisionNode, SaveImage, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/qwen大模型api调用 Qwen3-VL视觉理解模型反推提示词+api调用图片生成_1992064649529192450.json, 图片生成/文生图/【阡陌】Qwen3-VL图片_视频反推Qwen-Image-Edit-2509调用免费API_1983868724254048258.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1418

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/qwen大模型api调用 Qwen3-VL视觉理解模型反推提示词+api调用图片生成_1992064649529192450.json、图片生成/文生图/【阡陌】Qwen3-VL图片_视频反推Qwen-Image-Edit-2509调用免费API_1983868724254048258.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：78%

## 共有节点

全部 2 个 workflow 都包含：
- `Fast Groups Bypasser (rgthree)`
- `ImageConcanate`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoadVideo`
- `QwenImageEditNode`
- `QwenImageNode`
- `QwenVideoNode`
- `QwenVisionNode`
- `SaveImage`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `GetImageSize+` —— 1/2 个有
- `ImageConcatMulti` —— 1/2 个有
- `ShowText|pysssss` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
