---
name: unknown_workflow_sampler_clip_checkpoint_20
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.6685
common_nodes: [BasicScheduler, CLIPTextEncode, CheckpointLoaderSimple, ComfyMathExpression, ComfySwitchNode, EmptyHiDreamO1LatentImage, GetImageSize, HiDreamO1ReferenceImages, ImageScaleToTotalPixels, LoadImage, ModelNoiseScale, PreviewAny, PrimitiveBoolean, PrimitiveStringMultiline, SamplerCustom, SaveImage, VAEDecode]
problems: []
missing: []
members: [comfyui-workflow-templates-json/image_hidream_o1.json, comfyui-workflow-templates-json/image_hidream_o1_dev.json, 图片生成/图生图/HiDream O1图生图满血版_2064530660454391810.json, 图片生成/文生图/hidream_o1_full_2099207835962929153.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_checkpoint_20

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（comfyui-workflow-templates-json/image_hidream_o1.json、comfyui-workflow-templates-json/image_hidream_o1_dev.json、图片生成/图生图/HiDream O1图生图满血版_2064530660454391810.json、图片生成/文生图/hidream_o1_full_2099207835962929153.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：67%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicScheduler`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ComfyMathExpression`
- `ComfySwitchNode`
- `EmptyHiDreamO1LatentImage`
- `GetImageSize`
- `HiDreamO1ReferenceImages`
- `ImageScaleToTotalPixels`
- `LoadImage`
- `ModelNoiseScale`
- `PreviewAny`
- `PrimitiveBoolean`
- `PrimitiveStringMultiline`
- `SamplerCustom`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `HiDreamO1PatchSeamSmoothing` —— 3/4 个有
- `KSamplerSelect` —— 3/4 个有
- `CLIPLoader` —— 2/4 个有
- `JsonExtractString` —— 2/4 个有
- `RegexReplace` —— 2/4 个有
- `StringConcatenate` —— 2/4 个有
- `StringReplace` —— 2/4 个有
- `TextGenerate` —— 2/4 个有
- `fa7296b5-c974-4466-bfe3-a1f05f43b880` —— 2/4 个有
- `PrimitiveInt` —— 1/4 个有
- `ResolutionSelector` —— 1/4 个有
- `SamplerLCM` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
