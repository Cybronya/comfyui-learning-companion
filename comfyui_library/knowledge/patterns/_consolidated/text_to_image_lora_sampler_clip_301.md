---
name: text_to_image_lora_sampler_clip_301
type: Text To Image
frequency: 7
level: moderate
coverage: 0.929429
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, ImageBatchMulti, KSampler, LoadImage, RunningHub_ImageQwenI2L_LoraGenerator, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/I2L图生LoraCFB细节版工作流_1999759560254648321.json, 图片生成/文生图/I2L图生Lora风格版工作流_1999722337903800321.json, 图片生成/文生图/Qwen image I2L 模型训练成lora 后生图工作流_2015679486120960001.json, 图片生成/文生图/RH_ImageQwenI2L-图片转LoRA_1999434195766214657.json, 图片生成/文生图/RH_ImageQwenI2L-图片转LoRA文生图_2001570529641394177.json, 图片生成/文生图/风格即时定制，ImageQwen I2L 图片转LoRA_2000578050028863489.json, 平台全量/Qwen-I2L风格训练-5张图片一个LoRA_1999642719985205249.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_301

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/I2L图生LoraCFB细节版工作流_1999759560254648321.json、图片生成/文生图/I2L图生Lora风格版工作流_1999722337903800321.json、图片生成/文生图/Qwen image I2L 模型训练成lora 后生图工作流_2015679486120960001.json、图片生成/文生图/RH_ImageQwenI2L-图片转LoRA_1999434195766214657.json、图片生成/文生图/RH_ImageQwenI2L-图片转LoRA文生图_2001570529641394177.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：93%

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
- `easy showAnything` —— 5/7 个有
- `JjkText` —— 3/7 个有
- `RH_Captioner` —— 3/7 个有
- `ShowText` —— 3/7 个有
- `TextCombinerTwo` —— 3/7 个有
- `LoraLoader` —— 1/7 个有
- `RunningHub_ImageQwenI2L_Loader(CFB)` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 20 | 7 | 77% |
| Prompt 约束强度(CFG) | 8 | 1 - 8 | 7 | 52% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| 宽度 | 768 | 512 - 1104 | 7 | 75% |
| 高度 | 1280 | 768 - 1920 | 7 | 72% |
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 20，7 个样本
- Prompt 约束强度(CFG) 中位数 8，观测区间 1 - 8，7 个样本
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 宽度 中位数 768，观测区间 512 - 1104，7 个样本
- 高度 中位数 1280，观测区间 768 - 1920，7 个样本
