---
name: unknown_workflow_lora_sampler_clip_107
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.9294
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, CLIPVisionLoader, CR Text Concatenate, DetailDaemonSamplerNode, DualCLIPLoader, EmptyLatentImage, FluxGuidance, ImageResizeKJ, ImageSmartSharpen+, JjkShowText, KSamplerSelect, LoadImage, LoraLoaderModelOnly, PreviewImage, RH_Captioner, RandomNoise, ReduxAdvanced, SamplerCustomAdvanced, SaveImage, StyleModelLoader, TeaCache, TextInput_, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/万物 Labubu｜人物迁移参考_1936242276983033857.json, 图片生成/图生图/万物Labubu_1930592157512683521.json, 图片生成/图生图/万物一键变成Labubu_1996474642594414594.json, 图片生成/图生图/万物生成Labubu_1996507431935025153.json, 图片生成/图生图/万物迁移Labubu_1930810031602905089.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_107

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/万物 Labubu｜人物迁移参考_1936242276983033857.json、图片生成/图生图/万物Labubu_1930592157512683521.json、图片生成/图生图/万物一键变成Labubu_1996474642594414594.json、图片生成/图生图/万物生成Labubu_1996507431935025153.json、图片生成/图生图/万物迁移Labubu_1930810031602905089.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `CR Text Concatenate`
- `DetailDaemonSamplerNode`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FluxGuidance`
- `ImageResizeKJ`
- `ImageSmartSharpen+`
- `JjkShowText`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `RH_Captioner`
- `RandomNoise`
- `ReduxAdvanced`
- `SamplerCustomAdvanced`
- `SaveImage`
- `StyleModelLoader`
- `TeaCache`
- `TextInput_`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 856 | 856 - 856 | 5 | 100% |
| 高度 | 1152 | 1152 - 1152 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 856，观测区间 856 - 856，5 个样本，取值集中（一致性 100%）
- 高度 中位数 1152，观测区间 1152 - 1152，5 个样本，取值集中（一致性 100%）
