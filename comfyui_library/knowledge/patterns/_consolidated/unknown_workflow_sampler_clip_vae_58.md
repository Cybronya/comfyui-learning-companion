---
name: unknown_workflow_sampler_clip_vae_58
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.947
common_nodes: [CLIPTextEncode, CLIPVisionEncode, DownloadAndLoadFlorence2Model, Florence2Run, FluxSamplerParams+, LoadImage, SDXLEmptyLatentSizePicker+, SaveImage, StyleModelApply, Text List, Text List to Text, VAEDecode]
problems: []
missing: []
members: [图片生成/图生图/室内设计家具置办_1882019817501941762.json, 平台全量/Flux 室内设计 _ Flux Redux Roomdesigner_1864869212488683521.json, 平台全量/产品迁移+图片融合_1891794989884583938.json, 平台全量/多图融合室内设计 Flux Redux RoomDesigner_1860229849133748226.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_58

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/室内设计家具置办_1882019817501941762.json、平台全量/Flux 室内设计 _ Flux Redux Roomdesigner_1864869212488683521.json、平台全量/产品迁移+图片融合_1891794989884583938.json、平台全量/多图融合室内设计 Flux Redux RoomDesigner_1860229849133748226.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：95%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `DownloadAndLoadFlorence2Model`
- `Florence2Run`
- `FluxSamplerParams+`
- `LoadImage`
- `SDXLEmptyLatentSizePicker+`
- `SaveImage`
- `StyleModelApply`
- `Text List`
- `Text List to Text`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `CLIPVisionLoader` —— 3/4 个有
- `DualCLIPLoaderGGUF` —— 3/4 个有
- `StyleModelLoader` —— 3/4 个有
- `UnetLoaderGGUF` —— 3/4 个有
- `VAELoader` —— 3/4 个有
- `PreviewImage` —— 2/4 个有
- `workflow/模型组` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024x1024 (1.0) | - | 4 | 75% |
| 高度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 最常用 1024x1024 (1.0)，4 个样本，一致性 75%
- 高度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
