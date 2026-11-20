---
name: unknown_workflow_video_sampler_27
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.796333
common_nodes: [DiffuEraserLoader, DiffuEraserSampler, ImageResizeKJv2, ImageToMask, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LoadImage, MaskToImage, RepeatImageBatch, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, easy compare, easy ifElse, easy int]
problems: []
missing: []
members: [平台全量/DG(26.3.23)_手动遮罩去水印+diffueraser_2035909951046029314.json, 平台全量/DG(26.4.13)_手动遮罩去水印+diffueraser_2043921356739317761.json, 平台全量/dg(已整理)：全能视频S竖版去水印（11-26日））_1993581828894294017.json, 平台全量/全能视频S去水印（11月17日更新）_1981208923220992001.json, 平台全量/全能视频S去水印（11月1日更新）_1985324521928466433.json, 平台全量/视频水印去除_2046458229718257665.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_27

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（平台全量/DG(26.3.23)_手动遮罩去水印+diffueraser_2035909951046029314.json、平台全量/DG(26.4.13)_手动遮罩去水印+diffueraser_2043921356739317761.json、平台全量/dg(已整理)：全能视频S竖版去水印（11-26日））_1993581828894294017.json、平台全量/全能视频S去水印（11月17日更新）_1981208923220992001.json、平台全量/全能视频S去水印（11月1日更新）_1985324521928466433.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：80%

## 共有节点

全部 6 个 workflow 都包含：
- `DiffuEraserLoader`
- `DiffuEraserSampler`
- `ImageResizeKJv2`
- `ImageToMask`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `MaskToImage`
- `RepeatImageBatch`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `easy compare`
- `easy ifElse`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `ImageConcanate` —— 3/6 个有
- `LayerMask: MaskPreview` —— 3/6 个有
- `PreviewImage` —— 3/6 个有
- `easy showAnything` —— 3/6 个有
- `Getter` —— 2/6 个有
- `Setter` —— 2/6 个有
- `GetNode` —— 1/6 个有
- `SetNode` —— 1/6 个有
- `easy anythingIndexSwitch` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
