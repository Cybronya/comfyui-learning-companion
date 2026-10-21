---
name: text_to_image_lora_sampler_clip_172
type: Text To Image
frequency: 7
level: strong
coverage: 0.871714
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/RH工作流封面生成_2085451153541779457.json, 图片生成/文生图/SDXL图生图极速版 零成本快速图片风格转换_2098114830124281858.json, 图片生成/文生图/SDXL文生图工作流，高质量文本到图像生成方案_2106904544729985026.json, 图片生成/文生图/SDXL文生图工作流，高质量文本到图像生成方案_2108380198407327746.json, 图片生成/文生图/sdxl文生图工作流｜输入描述文字直接生成图片_2106604632175890434.json, 图片生成/文生图/老树开新花极速写实｜SDXL图生图零成本出图_2090826700719476738.json, 图片生成/文生图/老树开新花极速版｜SDXL图生图写实生成_2090531557399420929.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_172

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/RH工作流封面生成_2085451153541779457.json、图片生成/文生图/SDXL图生图极速版 零成本快速图片风格转换_2098114830124281858.json、图片生成/文生图/SDXL文生图工作流，高质量文本到图像生成方案_2106904544729985026.json、图片生成/文生图/SDXL文生图工作流，高质量文本到图像生成方案_2108380198407327746.json、图片生成/文生图/sdxl文生图工作流｜输入描述文字直接生成图片_2106604632175890434.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `CheckpointLoaderSimple` —— 6/7 个有
- `LoraLoader` —— 6/7 个有
- `孤海注释` —— 6/7 个有
- `CR Text` —— 4/7 个有
- `ShowText|pysssss` —— 4/7 个有
- `CR Text Concatenate` —— 3/7 个有
- `LoadImage` —— 3/7 个有
- `SDXL Empty Latent Image (rgthree)` —— 3/7 个有
- `TextInputBasic` —— 3/7 个有
- `VAEEncode` —— 3/7 个有
- `RH_LLMAPI_NODE` —— 1/7 个有
- `RH_RhartImageG2TextToImage` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 7 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 7 | 100% |
| 采样算法 | er_sde | - | 7 | 100% |
| 调度器 | beta | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| 宽度 | 80 | 80 - 80 | 7 | 100% |
| 高度 | 80 | 80 - 80 | 7 | 100% |
| LoRA 模型强度 | 0.55 | 0.3 - 0.8 | 6 | 55% |
| LoRA 文本强度 | 0.65 | 0.3 - 1 | 6 | 46% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，7 个样本，一致性 100%
- 调度器 最常用 beta，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.55，观测区间 0.3 - 0.8，6 个样本
- LoRA 文本强度 中位数 0.65，观测区间 0.3 - 1，6 个样本，取值分散，一致性仅 46%
- 高发问题（7/7 个样本）：Steps较低可能导致细节不足
