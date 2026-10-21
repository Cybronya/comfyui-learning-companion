---
name: unknown_workflow_sampler_clip_unet_140
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.77575
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, EmptySD3LatentImage, FluxGuidance, KSamplerSelect, ModelSamplingFlux, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: [ImageCrop+]
members: [comfyui-workflow-templates-json/flux_redux_model_example.json, 图片生成/文生图/06.Flux_Redux_Advanced_1993297476142694401.json, 图片生成/文生图/1911275546050002945.json, 图片生成/文生图/Redux角色一致性_1901277660763275265.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_140

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（comfyui-workflow-templates-json/flux_redux_model_example.json、图片生成/文生图/06.Flux_Redux_Advanced_1993297476142694401.json、图片生成/文生图/1911275546050002945.json、图片生成/文生图/Redux角色一致性_1901277660763275265.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：78%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptySD3LatentImage`
- `FluxGuidance`
- `KSamplerSelect`
- `ModelSamplingFlux`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPVisionLoader` —— 3/4 个有
- `LoadImage` —— 3/4 个有
- `StyleModelLoader` —— 3/4 个有
- `CLIPVisionEncode` —— 2/4 个有
- `StyleModelApply` —— 2/4 个有
- `Image Comparer (rgthree)` —— 1/4 个有
- `ImageCrop+` —— 1/4 个有
- `ImpactInt` —— 1/4 个有
- `LoraLoader` —— 1/4 个有
- `ReduxAdvanced` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：ImageCrop+
