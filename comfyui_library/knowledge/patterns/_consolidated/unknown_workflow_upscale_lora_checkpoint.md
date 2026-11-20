---
name: unknown_workflow_upscale_lora_checkpoint
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.443
common_nodes: [Bookmark (rgthree), CR Apply LoRA Stack, CR LoRA Stack, CR Simple Text Watermark, CheckpointLoaderSimple, ColorMatch, Fast Groups Bypasser (rgthree), GetImageSize+, GetNode, Image Comparer (rgthree), Image Resize, ImageResize+, ImageUpscaleWithModel, JWFloat, LoadImage, PlaySound|pysssss, PreviewImage, SUPIR_conditioner, SUPIR_decode, SUPIR_encode, SUPIR_first_stage, SUPIR_model_loader_v2, SUPIR_sample, SaveImage, SetNode, UpscaleModelLoader, WD14Tagger|pysssss, easy cleanGpuUsed]
problems: []
missing: []
members: [平台全量/【大师流】SUPIR - v2  放大_1819010591100153857.json, 平台全量/【大师流】SUPIR - v2  放大_1829502886480105473.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_checkpoint

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/【大师流】SUPIR - v2  放大_1819010591100153857.json、平台全量/【大师流】SUPIR - v2  放大_1829502886480105473.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：44%

## 共有节点

全部 2 个 workflow 都包含：
- `Bookmark (rgthree)`
- `CR Apply LoRA Stack`
- `CR LoRA Stack`
- `CR Simple Text Watermark`
- `CheckpointLoaderSimple`
- `ColorMatch`
- `Fast Groups Bypasser (rgthree)`
- `GetImageSize+`
- `GetNode`
- `Image Comparer (rgthree)`
- `Image Resize`
- `ImageResize+`
- `ImageUpscaleWithModel`
- `JWFloat`
- `LoadImage`
- `PlaySound|pysssss`
- `PreviewImage`
- `SUPIR_conditioner`
- `SUPIR_decode`
- `SUPIR_encode`
- `SUPIR_first_stage`
- `SUPIR_model_loader_v2`
- `SUPIR_sample`
- `SaveImage`
- `SetNode`
- `UpscaleModelLoader`
- `WD14Tagger|pysssss`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `Calculation [Dream]` —— 1/2 个有
- `Display Int (rgthree)` —— 1/2 个有
- `ShowText|pysssss` —— 1/2 个有
- `SimpleMath+` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
