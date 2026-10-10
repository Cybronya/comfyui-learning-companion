---
key: comfyui-workflow-templates-json/basic_mask_operations_and_compositing.json
name: basic_mask_operations_and_compositing
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/basic_mask_operations_and_compositing.json
hash: 8873d1f10ab21708
official: true
coverage: 0.804878
learned_at: 2026-10-10 22:47:05
nodes: [PreviewImage, MaskPreview, PreviewImage, PreviewImage, EmptyImage, LoadImage, MaskComposite, MaskPreview, SolidMask, MaskPreview, MaskComposite, MaskPreview, MaskComposite, MaskPreview, MaskComposite, MaskPreview, MaskComposite, MaskPreview, MarkdownNote, MarkdownNote, MarkdownNote, MaskComposite, MaskPreview, MaskComposite, MaskPreview, FeatherMask, MaskPreview, SolidMask, ImageToMask, MaskPreview, ThresholdMask, MaskPreview, MaskPreview, MaskToImage, InvertMask, FeatherMask, MaskPreview, ImageCompositeMasked, EmptyImage, PreviewImage, MarkdownNote]
patterns: []
missing: []
---

# comfyui-workflow-templates-json/basic_mask_operations_and_compositing.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/basic_mask_operations_and_compositing.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（41 个）：
- `PreviewImage`
- `MaskPreview`
- `PreviewImage`
- `PreviewImage`
- `EmptyImage`
- `LoadImage`
- `MaskComposite`
- `MaskPreview`
- `SolidMask`
- `MaskPreview`
- `MaskComposite`
- `MaskPreview`
- `MaskComposite`
- `MaskPreview`
- `MaskComposite`
- `MaskPreview`
- `MaskComposite`
- `MaskPreview`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `MaskComposite`
- `MaskPreview`
- `MaskComposite`
- `MaskPreview`
- `FeatherMask`
- `MaskPreview`
- `SolidMask`
- `ImageToMask`
- `MaskPreview`
- `ThresholdMask`
- `MaskPreview`
- `MaskPreview`
- `MaskToImage`
- `InvertMask`
- `FeatherMask`
- `MaskPreview`
- `ImageCompositeMasked`
- `EmptyImage`
- `PreviewImage`
- `MarkdownNote`

## 知识

覆盖率 **80%**（33/41）

**有卡**：`MaskPreview`、`EmptyImage`、`LoadImage`、`MaskComposite`、`SolidMask`、`FeatherMask`、`ImageToMask`、`ThresholdMask`、`MaskToImage`、`InvertMask`、`ImageCompositeMasked`

**用到的条目**：LoadImage、MaskPreview、EmptyImage、InvertMask、ImageCompositeMasked、ImageToMask、ImageToMask、MaskToImage
