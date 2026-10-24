---
name: unknown_workflow_controlnet_lora_clip_2
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.75
common_nodes: [CLIPTextEncode, CR Combine Prompt, CR Text, CheckpointLoaderSimple, ControlNetApplyAdvanced, ControlNetLoader, DepthAnythingPreprocessor, EmptyLatentImage, ExtractSubstring, Image Comparer (rgthree), LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, PreviewImage, PrimitiveFloat, RHHiddenNodes, RH_LLMAPI_NODE, SaveImage, SetUnionControlNetType, TextBox, VAEDecode, WD14Tagger|pysssss, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/【图生图】高质量动漫壁纸一键生成_1934879715553681410.json, 图片生成/文生图/高质量动漫壁纸一键生成_1934457942890672129.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_lora_clip_2

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/【图生图】高质量动漫壁纸一键生成_1934879715553681410.json、图片生成/文生图/高质量动漫壁纸一键生成_1934457942890672129.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：75%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CR Combine Prompt`
- `CR Text`
- `CheckpointLoaderSimple`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `DepthAnythingPreprocessor`
- `EmptyLatentImage`
- `ExtractSubstring`
- `Image Comparer (rgthree)`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `PrimitiveFloat`
- `RHHiddenNodes`
- `RH_LLMAPI_NODE`
- `SaveImage`
- `SetUnionControlNetType`
- `TextBox`
- `VAEDecode`
- `WD14Tagger|pysssss`
- `easy showAnything`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1536 | - | 2 | 100% |
| 高度 | 1024 | - | 2 | 100% |
| ControlNet 权重 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1536，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
