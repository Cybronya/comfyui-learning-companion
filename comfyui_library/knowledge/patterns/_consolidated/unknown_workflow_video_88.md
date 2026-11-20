---
name: unknown_workflow_video_88
type: Unknown Workflow
frequency: 2
level: weak
coverage: 1
common_nodes: [CR Prompt Text, Comfly_Doubao_Seedance2_0_Asset, Comfly_api_set, CreateVideo, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, SaveVideo, ShellAgentPluginOutputText, ShowAnything|Mie, VHS_LoadVideo, VHS_VideoInfoLoaded]
problems: []
missing: []
members: [图片生成/反推提示词/（视频资产）Seedance2.0 真人ID资产库提取(贞贞的AI工坊)_2043136169650692097.json, 视频生成/图生视频/(脱敏版-支持真人)Seedance2.0满血视频参考生视频V1（贞贞的AI工坊）_2043168596234342402.json]
source: knowledge_consolidation
---

# unknown_workflow_video_88

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/反推提示词/（视频资产）Seedance2.0 真人ID资产库提取(贞贞的AI工坊)_2043136169650692097.json、视频生成/图生视频/(脱敏版-支持真人)Seedance2.0满血视频参考生视频V1（贞贞的AI工坊）_2043168596234342402.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：100%

## 共有节点

全部 2 个 workflow 都包含：
- `CR Prompt Text`
- `Comfly_Doubao_Seedance2_0_Asset`
- `Comfly_api_set`
- `CreateVideo`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `SaveVideo`
- `ShellAgentPluginOutputText`
- `ShowAnything|Mie`
- `VHS_LoadVideo`
- `VHS_VideoInfoLoaded`

**可变部分**（部分 workflow 才有）：
- `Comfly_Doubao_Seedance2_0` —— 1/2 个有
- `Comfly_Doubao_Seedance2_0_AssetIdBundle` —— 1/2 个有
- `GetVideoComponents` —— 1/2 个有
- `ImageConcanate` —— 1/2 个有
- `SaveImage` —— 1/2 个有
- `VHS_VideoCombine` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
