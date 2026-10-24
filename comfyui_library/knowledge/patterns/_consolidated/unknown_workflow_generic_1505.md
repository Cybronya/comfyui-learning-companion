---
name: unknown_workflow_generic_1505
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.906
common_nodes: [CR Text, Fast Groups Bypasser (rgthree), Image Batch, ImageConcanate, ImageResizeKJv2, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, PreviewImage, Text List, ToString]
problems: []
missing: []
members: [图片生成/文生图/可乐-小说剧本生成分镜提示词_2008160689906520065.json, 视频生成/图生视频/可乐-漫剧分镜生成视频_2008539333560639489.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1505

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/可乐-小说剧本生成分镜提示词_2008160689906520065.json、视频生成/图生视频/可乐-漫剧分镜生成视频_2008539333560639489.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 2 个 workflow 都包含：
- `CR Text`
- `Fast Groups Bypasser (rgthree)`
- `Image Batch`
- `ImageConcanate`
- `ImageResizeKJv2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `PreviewImage`
- `Text List`
- `ToString`

**可变部分**（部分 workflow 才有）：
- `PreviewAny` —— 1/2 个有
- `RHHiddenNodes` —— 1/2 个有
- `RH_LLMAPI_NODE` —— 1/2 个有
- `RH_Sora2_I2V` —— 1/2 个有
- `SaveVideo` —— 1/2 个有
- `easy saveText` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
