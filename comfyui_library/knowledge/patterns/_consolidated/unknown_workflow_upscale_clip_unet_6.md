---
name: unknown_workflow_upscale_clip_unet_6
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.946
common_nodes: [CLIPLoader, CLIPTextEncode, ComfyMathExpression, DetailerForEach, GetImageSize, ImageUpscaleWithModel, ImpactMakeTileSEGS, ImpactSEGSLabelAssign, PrimitiveFloat, ResizeImageMaskNode, SEGSPreview, SaveImage, StringConcatenate, StringListToString, UNETLoader, UpscaleModelLoader, VAELoader, WD14Tagger|pysssss, WildcardPromptFromString]
problems: []
missing: []
members: [图片生成/图生图/Anima最强分块放大超分_2062393942229995522.json, 图片生成/文生图/Anima AIO 生图+超分_2067513375885713409.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_clip_unet_6

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Anima最强分块放大超分_2062393942229995522.json、图片生成/文生图/Anima AIO 生图+超分_2067513375885713409.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：95%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `DetailerForEach`
- `GetImageSize`
- `ImageUpscaleWithModel`
- `ImpactMakeTileSEGS`
- `ImpactSEGSLabelAssign`
- `PrimitiveFloat`
- `ResizeImageMaskNode`
- `SEGSPreview`
- `SaveImage`
- `StringConcatenate`
- `StringListToString`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAELoader`
- `WD14Tagger|pysssss`
- `WildcardPromptFromString`

**可变部分**（部分 workflow 才有）：
- `KSampler` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `ResolutionMaster` —— 1/2 个有
- `VAEDecode` —— 1/2 个有
- `孤海注释` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | - | 1 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 1 | 100% |
| 采样算法 | euler_ancestral | - | 1 | 100% |
| 调度器 | simple | - | 1 | 100% |
| 重绘幅度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
