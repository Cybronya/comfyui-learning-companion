---
name: unknown_workflow_video_sampler_28
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.7548
common_nodes: [DiffuEraserLoader, DiffuEraserSampler, MaskToImage, SAM3Segment, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, easy cleanGpuUsed]
problems: []
missing: []
members: [平台全量/seedance2.0小云雀豆包视频一键去除水印_2033713008693747714.json, 平台全量/小云雀seedance2.0水印去除_2025291039346532354.json, 平台全量/小云雀seedance2.0水印去除_2033469559058993154.json, 平台全量/小云雀超能视频2.0水印去除_2020554185825067010.json, 平台全量/（工具流）sam3自动识别视频去水印工具-全类型通用版_2021478582417104897.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_28

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（平台全量/seedance2.0小云雀豆包视频一键去除水印_2033713008693747714.json、平台全量/小云雀seedance2.0水印去除_2025291039346532354.json、平台全量/小云雀seedance2.0水印去除_2033469559058993154.json、平台全量/小云雀超能视频2.0水印去除_2020554185825067010.json、平台全量/（工具流）sam3自动识别视频去水印工具-全类型通用版_2021478582417104897.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：75%

## 共有节点

全部 5 个 workflow 都包含：
- `DiffuEraserLoader`
- `DiffuEraserSampler`
- `MaskToImage`
- `SAM3Segment`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 4/5 个有
- `RepeatImageBatch` —— 4/5 个有
- `VHS_SelectImages` —— 4/5 个有
- `VHS_SelectMasks` —— 4/5 个有
- `ImageConcatMulti` —— 1/5 个有
- `easy float` —— 1/5 个有
- `easy int` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
