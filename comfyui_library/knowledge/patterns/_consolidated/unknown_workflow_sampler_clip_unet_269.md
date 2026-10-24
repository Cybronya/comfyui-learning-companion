---
name: unknown_workflow_sampler_clip_unet_269
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.864
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, DPRandomGenerator, EmptyLatentImage, FlowMatchEulerDiscreteScheduler (Custom), KSamplerSelect, ModelSamplingAuraFlow, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader, easy batchAnything, easy forLoopEnd, easy forLoopStart, easy mathInt]
problems: []
missing: []
members: [图片生成/文生图/z_image_turbo_官方调度器_随机Prompt_浴缸写真_2005950136666779650.json, 图片生成/文生图/z_image_turbo_官方调度器_随机Prompt_清冷古装_2005664737729933313.json, 图片生成/文生图/z_image_turbo_官方调度器_随机Prompt_雨巷旗袍_2005949064745287682.json, 图片生成/文生图/z_image_turbo_官方调度器_随机Prompt_黑白气质美女_2005667147495993346.json, 图片生成/文生图/一键写真z_image_turbo_官方调度器_2005298289731928066.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_269

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/z_image_turbo_官方调度器_随机Prompt_浴缸写真_2005950136666779650.json、图片生成/文生图/z_image_turbo_官方调度器_随机Prompt_清冷古装_2005664737729933313.json、图片生成/文生图/z_image_turbo_官方调度器_随机Prompt_雨巷旗袍_2005949064745287682.json、图片生成/文生图/z_image_turbo_官方调度器_随机Prompt_黑白气质美女_2005667147495993346.json、图片生成/文生图/一键写真z_image_turbo_官方调度器_2005298289731928066.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DPRandomGenerator`
- `EmptyLatentImage`
- `FlowMatchEulerDiscreteScheduler (Custom)`
- `KSamplerSelect`
- `ModelSamplingAuraFlow`
- `PrimitiveInt`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy batchAnything`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy mathInt`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1080 | 1080 - 1080 | 5 | 100% |
| 高度 | 1920 | 1080 - 1920 | 5 | 74% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1080，观测区间 1080 - 1080，5 个样本，取值集中（一致性 100%）
- 高度 中位数 1920，观测区间 1080 - 1920，5 个样本
