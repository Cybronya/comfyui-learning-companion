---
name: text_to_image_sampler_clip_unet_64
type: Text To Image
frequency: 10
level: moderate
coverage: 0.9882
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAELoader]
problems: [Steps较低可能导致细节不足, 发现KSampler但没有VAEDecode]
missing: []
members: [图片生成/文生图/Krea2-raw+turbo两次采样对比单采样turbo-_2074526672380063745.json, 图片生成/文生图/Krea2基础文生图_2070504244750405634.json, 图片生成/文生图/Moody Krea 2 Mix -文生图_2084479377294843906.json, 图片生成/文生图/Ovis-image文生图工作流_1996530154350452738.json, 图片生成/文生图/Qwen-Image-通义千问-文生图_海报设计_1953818850963935234.json, 图片生成/文生图/Qwen-Image官方工作流-满血版BF16_1953997948080279554.json, 图片生成/文生图/Qwen-image 图片生成基础工作流_1957086467483734017.json, 图片生成/文生图/Qwen-千问文生图工作流+LORA（电商运营海报）_1993309631191728130.json, 图片生成/文生图/Qwen_Image基础加速工作流_1973965175168569346.json, 图片生成/文生图/Z-Image VS Z-Image-turbo VS Qwen image 2512_2016491036381552641.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_64

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/文生图/Krea2-raw+turbo两次采样对比单采样turbo-_2074526672380063745.json、图片生成/文生图/Krea2基础文生图_2070504244750405634.json、图片生成/文生图/Moody Krea 2 Mix -文生图_2084479377294843906.json、图片生成/文生图/Ovis-image文生图工作流_1996530154350452738.json、图片生成/文生图/Qwen-Image-通义千问-文生图_海报设计_1953818850963935234.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：99%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 9/10 个有
- `VAEDecode` —— 9/10 个有
- `ModelSamplingAuraFlow` —— 7/10 个有
- `KSamplerAdvanced` —— 2/10 个有
- `LoraLoader` —— 2/10 个有
- `LoraLoaderModelOnly` —— 2/10 个有
- `TTResolutionSelector` —— 2/10 个有
- `AddLabel` —— 1/10 个有
- `Fast Groups Bypasser (rgthree)` —— 1/10 个有
- `ImageConcanate` —— 1/10 个有
- `QwenEditResolution` —— 1/10 个有
- `VAEDecodeTiled` —— 1/10 个有
- `easy promptList` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 12 | 8 - 50 | 9 | 28% |
| Prompt 约束强度(CFG) | 1.75 | 1 - 8 | 10 | 18% |
| 采样算法 | euler | - | 10 | 60% |
| 调度器 | simple | - | 10 | 70% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |
| 宽度 | 1024 | 512 - 1328 | 10 | 77% |
| 高度 | 1280 | 512 - 1920 | 10 | 71% |
| LoRA 模型强度 | 0.9 | - | 2 | 89% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |
| 发现KSampler但没有VAEDecode | 1/10 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 12，观测区间 8 - 50，9 个样本，取值分散，一致性仅 28%
- Prompt 约束强度(CFG) 中位数 1.75，观测区间 1 - 8，10 个样本，取值分散，一致性仅 18%
- 采样算法 最常用 euler，10 个样本，一致性 60%
- 调度器 最常用 simple，10 个样本，一致性 70%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 512 - 1328，10 个样本
- 高度 中位数 1280，观测区间 512 - 1920，10 个样本
- LoRA 模型强度 中位数 0.9，样本不足，未给区间，2 个样本，取值集中（一致性 89%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
