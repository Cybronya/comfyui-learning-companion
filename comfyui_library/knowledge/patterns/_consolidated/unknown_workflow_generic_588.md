---
name: unknown_workflow_generic_588
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.962333
common_nodes: [IDCardCorrectionAndComposition, ImageAndMaskPreview, ImageCASharpening+, LayerMask: LoadSegmentAnythingModels, LayerMask: SegmentAnythingUltra V3, LayerUtility: CropByMask, LoadImage, MaskCornerFixer, RotateImageNode, SaveImage, 图像缩放V2_孤海, 孤海图像缩放按像素, 忽略多组孤海]
problems: []
missing: []
members: [图片生成/图生图/身份证矫正+高清放大 A4纸尺寸_2084438246641201153.json, 图片生成/图生图/身份证矫正+高清放大_A4纸尺寸_2084956256191733761.json, 图片生成/图生图/身份证矫正+高清放大_A4纸尺寸_2085172786439479297.json, 图片生成/图生图/身份证自动矫正+A4拼版（懒人版）_2068051932824039426.json, 平台全量/身份证矫正+A4纸_1906134698517794817.json, 平台全量/身份证自动矫正+A4拼版_2064639428555010050.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_588

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/身份证矫正+高清放大 A4纸尺寸_2084438246641201153.json、图片生成/图生图/身份证矫正+高清放大_A4纸尺寸_2084956256191733761.json、图片生成/图生图/身份证矫正+高清放大_A4纸尺寸_2085172786439479297.json、图片生成/图生图/身份证自动矫正+A4拼版（懒人版）_2068051932824039426.json、平台全量/身份证矫正+A4纸_1906134698517794817.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 6 个 workflow 都包含：
- `IDCardCorrectionAndComposition`
- `ImageAndMaskPreview`
- `ImageCASharpening+`
- `LayerMask: LoadSegmentAnythingModels`
- `LayerMask: SegmentAnythingUltra V3`
- `LayerUtility: CropByMask`
- `LoadImage`
- `MaskCornerFixer`
- `RotateImageNode`
- `SaveImage`
- `图像缩放V2_孤海`
- `孤海图像缩放按像素`
- `忽略多组孤海`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 2/6 个有
- `孤海注释` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
