---
name: unknown_workflow_upscale_32
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.6675
common_nodes: [BiRefNet_ModelLoader_Zho, BiRefNet_Zho, InspyrenetRembg, LayerMask: BiRefNetUltra, LayerMask: SegmentAnythingUltra V2, LoadImage, PreviewImage, SaveImage, easy imageRemBg]
problems: []
missing: []
members: [图片生成/图生图/Image Masking Collection7合1抠图+抠图去除背景_2097859749982334977.json, 图片生成/图生图/抠图_2062353508631928833.json, 平台全量/7合1抠图 抠图大合集 +抠图去除背景+一键在线抠图+万能抠图+自动抠图+智能识别+抠发丝级_2045736524297277441.json, 平台全量/抠图大合集  7合1抠图 抠图去除背景 一键在线抠图 万能抠图 自动抠图 智能识别 抠发丝级_2043530094085414913.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_32

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Image Masking Collection7合1抠图+抠图去除背景_2097859749982334977.json、图片生成/图生图/抠图_2062353508631928833.json、平台全量/7合1抠图 抠图大合集 +抠图去除背景+一键在线抠图+万能抠图+自动抠图+智能识别+抠发丝级_2045736524297277441.json、平台全量/抠图大合集  7合1抠图 抠图去除背景 一键在线抠图 万能抠图 自动抠图 智能识别 抠发丝级_2043530094085414913.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：67%

## 共有节点

全部 4 个 workflow 都包含：
- `BiRefNet_ModelLoader_Zho`
- `BiRefNet_Zho`
- `InspyrenetRembg`
- `LayerMask: BiRefNetUltra`
- `LayerMask: SegmentAnythingUltra V2`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `easy imageRemBg`

**可变部分**（部分 workflow 才有）：
- `ImageUpscaleWithModel` —— 1/4 个有
- `Upscale Model Loader` —— 1/4 个有
- `YUAN_TXTConvertAny` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
