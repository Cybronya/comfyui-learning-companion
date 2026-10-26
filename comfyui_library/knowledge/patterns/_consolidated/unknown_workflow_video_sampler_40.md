---
name: unknown_workflow_video_sampler_40
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8875
common_nodes: [Compare, DiffuEraserLoader, DiffuEraserSampler, GetVideoComponents, ImageResizeKJv2, JWInteger, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, RH_Translator, RepeatImageBatch, SaveVideo, Text, VHS_GetImageCount, VHS_VideoCombine, easy cleanGpuUsed, easy ifElse]
problems: []
missing: []
members: [视频生成/图生视频/全能视频S图生视频加去水印一体_1975073237912694785.json, 视频生成/文生视频/全能视频S文生视频加去水印一体_1974820757119348737.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_40

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/全能视频S图生视频加去水印一体_1975073237912694785.json、视频生成/文生视频/全能视频S文生视频加去水印一体_1974820757119348737.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：89%

## 共有节点

全部 2 个 workflow 都包含：
- `Compare`
- `DiffuEraserLoader`
- `DiffuEraserSampler`
- `GetVideoComponents`
- `ImageResizeKJv2`
- `JWInteger`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `RH_Translator`
- `RepeatImageBatch`
- `SaveVideo`
- `Text`
- `VHS_GetImageCount`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`
- `easy ifElse`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Muter (rgthree)` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `RH_Sora2_I2V` —— 1/2 个有
- `RH_Sora2_T2V` —— 1/2 个有
- `SaveText|pysssss` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
