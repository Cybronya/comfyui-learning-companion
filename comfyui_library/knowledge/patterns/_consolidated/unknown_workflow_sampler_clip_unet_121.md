---
name: unknown_workflow_sampler_clip_unet_121
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.958
common_nodes: [BasicScheduler, CFGGuider, CLIPTextEncode, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: [CR Upscale Image]
members: [comfyui-workflow-templates-json/image_chroma_text_to_image.json, 图片生成/文生图/1931586622008000513.json, 图片生成/文生图/1932051517409570818.json, 图片生成/文生图/1962355322230915073.json, 图片生成/文生图/1984856656842473473.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_121

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（comfyui-workflow-templates-json/image_chroma_text_to_image.json、图片生成/文生图/1931586622008000513.json、图片生成/文生图/1932051517409570818.json、图片生成/文生图/1962355322230915073.json、图片生成/文生图/1984856656842473473.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicScheduler`
- `CFGGuider`
- `CLIPTextEncode`
- `KSamplerSelect`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 4/5 个有
- `EmptySD3LatentImage` —— 4/5 个有
- `T5TokenizerOptions` —— 4/5 个有
- `LoraLoaderModelOnly` —— 3/5 个有
- `AILab_QwenVL` —— 1/5 个有
- `CR Upscale Image` —— 1/5 个有
- `DualCLIPLoader` —— 1/5 个有
- `EmptyLatentImage` —— 1/5 个有
- `LoadImage` —— 1/5 个有
- `ModelSamplingAuraFlow` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | - | 1 | 100% |
| 高度 | 1024 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：CR Upscale Image
