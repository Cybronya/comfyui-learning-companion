---
name: unknown_workflow_sampler_clip_vae_41
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.933167
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, FluxGuidance, KSamplerSelect, LoadImage, ModelSamplingFlux, RandomNoise, SamplerCustomAdvanced, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/吉卜力风格化_1905893406915088385.json, 图片生成/图生图/图片一键转灵魂画手风格_2024788264820936705.json, 图片生成/图生图/提取物品_1947232272145666049.json, 图片生成/图生图/文字编辑图片 Flux kontext dev_1938542570844938242.json, 图片生成/图生图/电商服装去除图片人物_1943097905094025218.json, 图片生成/图生图/移除物品_1947235737038168065.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_41

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/吉卜力风格化_1905893406915088385.json、图片生成/图生图/图片一键转灵魂画手风格_2024788264820936705.json、图片生成/图生图/提取物品_1947232272145666049.json、图片生成/图生图/文字编辑图片 Flux kontext dev_1938542570844938242.json、图片生成/图生图/电商服装去除图片人物_1943097905094025218.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSamplerSelect`
- `LoadImage`
- `ModelSamplingFlux`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptySD3LatentImage` —— 5/6 个有
- `FluxKontextImageScale` —— 5/6 个有
- `ReferenceLatent` —— 5/6 个有
- `CheckpointLoaderSimple` —— 4/6 个有
- `RepeatLatentBatch` —— 3/6 个有
- `GetImageSize` —— 2/6 个有
- `LoraLoader` —— 2/6 个有
- `PrimitiveString` —— 2/6 个有
- `StringReplace` —— 2/6 个有
- `UNETLoader` —— 2/6 个有
- `easy imageSize` —— 2/6 个有
- `ImageResize+` —— 1/6 个有
- `JjkText` —— 1/6 个有
- `RH_Translator` —— 1/6 个有
- `Text` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
