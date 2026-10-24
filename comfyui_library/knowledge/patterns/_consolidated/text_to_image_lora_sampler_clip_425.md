---
name: text_to_image_lora_sampler_clip_425
type: Text To Image
frequency: 4
level: strong
coverage: 0.90525
common_nodes: [AI_Ollama, CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, Int, KSampler, LoraLoaderModelOnly, QwenImagePromptStyler, RH_Translator, SaveImage, Switch, TextBox, VAEDecode, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/可调控尺寸lora-动漫二次元-文生图_2076995810960691201.json, 图片生成/图生图/可调控尺寸lora-动漫二次元-文生图_2080520972146405377.json, 图片生成/文生图/IL-XL-waiNS加可调控尺寸lora-支持中文提示词翻译-动漫-文生图（出图自选）款_2028882775184510977.json, 图片生成/文生图/二次元-文生图_2077425296835432449.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_425

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/可调控尺寸lora-动漫二次元-文生图_2076995810960691201.json、图片生成/图生图/可调控尺寸lora-动漫二次元-文生图_2080520972146405377.json、图片生成/文生图/IL-XL-waiNS加可调控尺寸lora-支持中文提示词翻译-动漫-文生图（出图自选）款_2028882775184510977.json、图片生成/文生图/二次元-文生图_2077425296835432449.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 4 个 workflow 都包含：
- `AI_Ollama`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `Int`
- `KSampler`
- `LoraLoaderModelOnly`
- `QwenImagePromptStyler`
- `RH_Translator`
- `SaveImage`
- `Switch`
- `TextBox`
- `VAEDecode`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `DuckHideNode` —— 3/4 个有
- `PreviewImage` —— 3/4 个有
- `ImageScaleToTotalPixels` —— 2/4 个有
- `SeedVR2LoadDiTModel` —— 2/4 个有
- `SeedVR2LoadVAEModel` —— 2/4 个有
- `SeedVR2VideoUpscaler` —— 2/4 个有
- `HAIGC_SaveImagesToZip` —— 1/4 个有
- `TT_img_enc_v2` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 25 - 25 | 4 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4 - 5 | 4 | 89% |
| 采样算法 | euler_ancestral | - | 4 | 100% |
| 调度器 | karras | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 768 | 768 - 768 | 4 | 100% |
| 高度 | 1024 | 1024 - 1024 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 25 - 25，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4 - 5，4 个样本，取值集中（一致性 89%）
- 采样算法 最常用 euler_ancestral，4 个样本，一致性 100%
- 调度器 最常用 karras，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 768，观测区间 768 - 768，4 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，4 个样本，取值集中（一致性 100%）
