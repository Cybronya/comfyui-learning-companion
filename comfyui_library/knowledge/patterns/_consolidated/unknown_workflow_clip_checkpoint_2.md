---
name: unknown_workflow_clip_checkpoint_2
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.5665
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, DeepTranslatorTextNode, DrawMaskOnImage, LoadImage, SAM3_Detect, SaveImage]
problems: []
missing: []
members: [图片生成/图生图/SAM-3.1图像语义分割提取遮罩+全节点注释_2052975663912628226.json, 平台全量/SAM-3.1图像语义分割提取遮罩+全节点注释_2054391711895441410.json]
source: knowledge_consolidation
---

# unknown_workflow_clip_checkpoint_2

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/SAM-3.1图像语义分割提取遮罩+全节点注释_2052975663912628226.json、平台全量/SAM-3.1图像语义分割提取遮罩+全节点注释_2054391711895441410.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：57%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `DeepTranslatorTextNode`
- `DrawMaskOnImage`
- `LoadImage`
- `SAM3_Detect`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `JjkText` —— 1/2 个有
- `MaskToImage` —— 1/2 个有
- `PreviewAny` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
