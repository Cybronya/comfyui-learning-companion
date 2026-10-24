---
name: text_to_image_lora_sampler_clip_418
type: Text To Image
frequency: 4
level: strong
coverage: 0.89425
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, EmptyLatentImage, FluxGuidance, KSampler, LoadImage, LoraLoaderModelOnly, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/kontext _ 提取服装_1941053081952088066.json, 图片生成/图生图/kontext dev服装产品照提取_1959946240127610881.json, 图片生成/图生图/提取服装产品照 kontext dev_1944752299111534594.json, 图片生成/图生图/服饰提取工作流_1960698267938041857.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_418

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/kontext _ 提取服装_1941053081952088066.json、图片生成/图生图/kontext dev服装产品照提取_1959946240127610881.json、图片生成/图生图/提取服装产品照 kontext dev_1944752299111534594.json、图片生成/图生图/服饰提取工作流_1960698267938041857.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FluxGuidance`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `GetImageSize` —— 3/4 个有
- `ImageResize+` —— 3/4 个有
- `PrimitiveStringMultiline` —— 3/4 个有
- `RH_Translator` —— 3/4 个有
- `Text Find and Replace` —— 3/4 个有
- `DF_Get_image_size` —— 2/4 个有
- `PreviewImage` —— 2/4 个有
- `FluxKontextImageScale` —— 1/4 个有
- `GoogleTranslateTextNode` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | 512 - 512 | 4 | 100% |
| 高度 | 512 | 512 - 512 | 4 | 100% |
| 采样步数 | 20 | 20 - 20 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 512，观测区间 512 - 512，4 个样本，取值集中（一致性 100%）
- 高度 中位数 512，观测区间 512 - 512，4 个样本，取值集中（一致性 100%）
- 采样步数 中位数 20，观测区间 20 - 20，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
