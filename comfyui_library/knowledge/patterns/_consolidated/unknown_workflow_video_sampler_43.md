---
name: unknown_workflow_video_sampler_43
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.6945
common_nodes: [DiffuEraserLoader, DiffuEraserSampler, Fast Groups Muter (rgthree), FlashVSRNode, ImageResizeKJv2, Int, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, MaskToImage, RepeatImageBatch, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, VHS_VideoInfoLoaded, easy compare, easy ifElse, easy showAnything]
problems: []
missing: []
members: [平台全量/新版全能视频S高清修复+去水印基于wan2.2_1992297040050974721.json, 平台全量/（12月20更新）全能视频S高清修复+去水印_1981178677461417986.json, 视频生成/图生视频/全能视频S高清修复加去水印（最新版）_1993299080321368065.json, 视频生成/图生视频/全能视频S高清修复去水印（最强优化）_1993311600947953666.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_43

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/新版全能视频S高清修复+去水印基于wan2.2_1992297040050974721.json、平台全量/（12月20更新）全能视频S高清修复+去水印_1981178677461417986.json、视频生成/图生视频/全能视频S高清修复加去水印（最新版）_1993299080321368065.json、视频生成/图生视频/全能视频S高清修复去水印（最强优化）_1993311600947953666.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：69%

## 共有节点

全部 4 个 workflow 都包含：
- `DiffuEraserLoader`
- `DiffuEraserSampler`
- `Fast Groups Muter (rgthree)`
- `FlashVSRNode`
- `ImageResizeKJv2`
- `Int`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `MaskToImage`
- `RepeatImageBatch`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `VHS_VideoInfoLoaded`
- `easy compare`
- `easy ifElse`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `ImageConcanate` —— 3/4 个有
- `LayerUtility: PurgeVRAM V2` —— 3/4 个有
- `ImageToMask` —— 1/4 个有
- `RunningHub Deepcleaner` —— 1/4 个有
- `easy int` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
