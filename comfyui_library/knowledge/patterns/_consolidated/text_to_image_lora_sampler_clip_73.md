---
name: text_to_image_lora_sampler_clip_73
type: Text To Image
frequency: 12
level: strong
coverage: 0.667333
common_nodes: [CLIPTextEncode, CR Text, CR Text Concatenate, CheckpointLoaderSimple, EmptyLatentImage, KSampler, LoraLoader, SaveImage, VAEDecode]
problems: []
missing: [CR Text, CR Text Concatenate, SDXL Empty Latent Image (rgthree)]
members: [图片生成/文生图/1912776705101234178.json, 图片生成/文生图/1978632798712041473.json, 图片生成/文生图/1985255103059927041.json, 图片生成/文生图/1986741424010031105.json, 图片生成/文生图/SDXL-文生图_2057359733673254913.json, 图片生成/文生图/SDXL文生图260814_2088171447368900610.json, 图片生成/文生图/SDXL文生图工作流1_2019407761120956418.json, 图片生成/文生图/SDXL文生图工作流_2007995686184296449.json, 图片生成/文生图/SDXL文生图工作流_2008828192865390594.json, 图片生成/文生图/SDXL文生图工作流_2086796769467396098.json, 图片生成/文生图/sdxl文生图工作流_2106366129026457602.json, 图片生成/文生图/z-image-图生图_2060257717163487234.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_73

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/文生图/1912776705101234178.json、图片生成/文生图/1978632798712041473.json、图片生成/文生图/1985255103059927041.json、图片生成/文生图/1986741424010031105.json、图片生成/文生图/SDXL-文生图_2057359733673254913.json…）

- **类型**：Text To Image
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：67%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPTextEncode`
- `CR Text`
- `CR Text Concatenate`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `KSampler`
- `LoraLoader`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `ShowText|pysssss` —— 11/12 个有
- `SDXL Empty Latent Image (rgthree)` —— 10/12 个有
- `TextInputBasic` —— 10/12 个有
- `PreviewImage` —— 2/12 个有
- `Seed (rgthree)` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 768 | 512 - 1024 | 12 | 86% |
| 高度 | 1024 | 768 - 1024 | 12 | 93% |
| LoRA 模型强度 | 0.8 | 0.8 - 1 | 12 | 91% |
| LoRA 文本强度 | 1 | 1 - 1 | 12 | 100% |
| 采样步数 | 30 | 20 - 30 | 12 | 91% |
| Prompt 约束强度(CFG) | 5 | 5 - 7 | 12 | 86% |
| 采样算法 | dpmpp_2m | - | 12 | 83% |
| 调度器 | sgm_uniform | - | 12 | 83% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 768，观测区间 512 - 1024，12 个样本，取值集中（一致性 86%）
- 高度 中位数 1024，观测区间 768 - 1024，12 个样本，取值集中（一致性 93%）
- LoRA 模型强度 中位数 0.8，观测区间 0.8 - 1，12 个样本，取值集中（一致性 91%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 采样步数 中位数 30，观测区间 20 - 30，12 个样本，取值集中（一致性 91%）
- Prompt 约束强度(CFG) 中位数 5，观测区间 5 - 7，12 个样本，取值集中（一致性 86%）
- 采样算法 最常用 dpmpp_2m，12 个样本，一致性 83%
- 调度器 最常用 sgm_uniform，12 个样本，一致性 83%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：CR Text、CR Text Concatenate、SDXL Empty Latent Image (rgthree)
