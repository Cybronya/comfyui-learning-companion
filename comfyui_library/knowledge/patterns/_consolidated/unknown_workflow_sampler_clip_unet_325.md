---
name: unknown_workflow_sampler_clip_unet_325
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.987333
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, Florence2ModelLoader, Florence2Run, ImageResize+, KSamplerSelect, LoadImage, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/3d 卡通渲染 风格转绘_1913947619196923905.json, 图片生成/图生图/TC-常用图生图_1924377750059012097.json, 图片生成/图生图/复古迪士尼AI滤镜_1923669273305411585.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_325

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/3d 卡通渲染 风格转绘_1913947619196923905.json、图片生成/图生图/TC-常用图生图_1924377750059012097.json、图片生成/图生图/复古迪士尼AI滤镜_1923669273305411585.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：99%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `Florence2ModelLoader`
- `Florence2Run`
- `ImageResize+`
- `KSamplerSelect`
- `LoadImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text Replace` —— 2/3 个有
- `FluxGuidance` —— 2/3 个有
- `LoraLoader` —— 2/3 个有
- `String Literal` —— 2/3 个有
- `Text List` —— 2/3 个有
- `Text List to Text` —— 2/3 个有
- `CLIPVisionLoader` —— 1/3 个有
- `CR Latent Batch Size` —— 1/3 个有
- `JjkShowText` —— 1/3 个有
- `ReduxAdvanced` —— 1/3 个有
- `ShowText|pysssss` —— 1/3 个有
- `StyleModelLoader` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1.025 | - | 2 | 93% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 1.025，样本不足，未给区间，2 个样本，取值集中（一致性 93%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
