---
name: unknown_workflow_generic_674
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.7722
common_nodes: [BBoxesToSAM2, DownloadAndLoadQwenModel, LayerMask: LoadSAM2Model, LayerMask: SAM2UltraV2, LoadImage, MaskToImage, QwenVLDetection, SaveImage, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/Qwen VL语义识别智能抠像_1943508935598874625.json, 平台全量/Qwen VL语义识别抠像_1934256680953929730.json, 平台全量/Qwen2.5 Vl及Florence Sam2分割_1934072503814021121.json, 平台全量/Qwen2.5 Vl物体分割_1966160675510849537.json, 平台全量/一句话分割图片_1934633057640980482.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_674

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Qwen VL语义识别智能抠像_1943508935598874625.json、平台全量/Qwen VL语义识别抠像_1934256680953929730.json、平台全量/Qwen2.5 Vl及Florence Sam2分割_1934072503814021121.json、平台全量/Qwen2.5 Vl物体分割_1966160675510849537.json、平台全量/一句话分割图片_1934633057640980482.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：77%

## 共有节点

全部 5 个 workflow 都包含：
- `BBoxesToSAM2`
- `DownloadAndLoadQwenModel`
- `LayerMask: LoadSAM2Model`
- `LayerMask: SAM2UltraV2`
- `LoadImage`
- `MaskToImage`
- `QwenVLDetection`
- `SaveImage`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 3/5 个有
- `LayerUtility: PurgeVRAM` —— 3/5 个有
- `PreviewImage` —— 3/5 个有
- `JjkText` —— 2/5 个有
- `LayerMask: LoadFlorence2Model` —— 2/5 个有
- `LayerMask: ObjectDetectorFL2` —— 2/5 个有
- `ImageConcanate` —— 1/5 个有
- `easy cleanGpuUsed` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
