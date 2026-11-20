---
name: text_to_image_upscale_latent_upscale_lora_19
type: Text To Image
frequency: 2
level: weak
coverage: 0.8145
common_nodes: [CLIPSetLastLayer, CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, HAIGC_SaveImagesToZip, KSampler, LatentUpscaleBy, LoraLoader, PrimitiveFloat, SaveImage, VAEDecode]
problems: []
missing: []
members: [图片生成/文生图/LLM酒馆2D角色卡封面生成_2004390873263734786.json, 图片生成/文生图/酒馆2D角色卡封面生成_2002452758932385793.json]
source: knowledge_consolidation
---

# text_to_image_upscale_latent_upscale_lora_19

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/LLM酒馆2D角色卡封面生成_2004390873263734786.json、图片生成/文生图/酒馆2D角色卡封面生成_2002452758932385793.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：81%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPSetLastLayer`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `HAIGC_SaveImagesToZip`
- `KSampler`
- `LatentUpscaleBy`
- `LoraLoader`
- `PrimitiveFloat`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 1/2 个有
- `CR Text Concatenate` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `OpenAI_Chat_API` —— 1/2 个有
- `PrimitiveStringMultiline` —— 1/2 个有
- `RegexStringReplace` —— 1/2 个有
- `ShowText` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.6 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |
| 采样步数 | 20 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 7 | - | 2 | 100% |
| 采样算法 | euler_ancestral | - | 2 | 100% |
| 调度器 | normal | - | 2 | 100% |
| 重绘幅度 | 0.6 | - | 2 | 100% |
| 宽度 | 608 | - | 2 | 100% |
| 高度 | 912 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 0.6，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 20，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 7，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，2 个样本，一致性 100%
- 调度器 最常用 normal，2 个样本，一致性 100%
- 重绘幅度 中位数 0.6，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 608，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 912，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
