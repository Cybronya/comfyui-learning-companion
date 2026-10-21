---
name: text_to_image_lora_sampler_clip_168
type: Text To Image
frequency: 7
level: moderate
coverage: 0.917
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, ImageBatchMulti, KSampler, LoadImage, RunningHub_ImageQwenI2L_LoraGenerator, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/I2L图生LoraCFB细节版工作流_1999759560254648321.json, 图片生成/文生图/I2L图生Lora风格版工作流_1999722337903800321.json, 图片生成/文生图/Qwen image I2L 模型训练成lora 后生图工作流_2015679486120960001.json, 图片生成/文生图/RH_ImageQwenI2L-图片转LoRA_1999434195766214657.json, 图片生成/文生图/RH_ImageQwenI2L-图片转LoRA文生图_2001570529641394177.json, 图片生成/文生图/【超快速LoRA训练】Qwen Image i2L模型：只需6张相同风格图片，1分钟训练出对应风格LoRA！_2001117117581754370.json, 图片生成/文生图/风格即时定制，ImageQwen I2L 图片转LoRA_2000578050028863489.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_168

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/I2L图生LoraCFB细节版工作流_1999759560254648321.json、图片生成/文生图/I2L图生Lora风格版工作流_1999722337903800321.json、图片生成/文生图/Qwen image I2L 模型训练成lora 后生图工作流_2015679486120960001.json、图片生成/文生图/RH_ImageQwenI2L-图片转LoRA_1999434195766214657.json、图片生成/文生图/RH_ImageQwenI2L-图片转LoRA文生图_2001570529641394177.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `ImageBatchMulti`
- `KSampler`
- `LoadImage`
- `RunningHub_ImageQwenI2L_LoraGenerator`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 6/7 个有
- `RunningHub_ImageQwenI2L_Loader(Style)` —— 6/7 个有
- `easy showAnything` —— 6/7 个有
- `JjkText` —— 3/7 个有
- `RH_Captioner` —— 3/7 个有
- `ShowText` —— 3/7 个有
- `TextCombinerTwo` —— 3/7 个有
- `Label (rgthree)` —— 1/7 个有
- `LoraLoader` —— 1/7 个有
- `RunningHub_ImageQwenI2L_Loader(CFB)` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 7 | 100% |
| Prompt 约束强度(CFG) | 8 | 2 - 8 | 7 | 71% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| 宽度 | 768 | 512 - 1104 | 7 | 71% |
| 高度 | 1024 | 512 - 1920 | 7 | 62% |
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 8，观测区间 2 - 8，7 个样本
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 宽度 中位数 768，观测区间 512 - 1104，7 个样本
- 高度 中位数 1024，观测区间 512 - 1920，7 个样本
