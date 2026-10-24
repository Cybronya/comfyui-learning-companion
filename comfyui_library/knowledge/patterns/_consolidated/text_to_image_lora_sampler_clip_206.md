---
name: text_to_image_lora_sampler_clip_206
type: Text To Image
frequency: 9
level: moderate
coverage: 0.895889
common_nodes: [CLIPLoader, CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, JjkText, KSampler, LoraLoader, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/SDXL文生图工作流，高质量文本到图像生成方案_2106904544729985026.json, 图片生成/文生图/SDXL文生图工作流，高质量文本到图像生成方案_2108380198407327746.json, 图片生成/文生图/SDXL极速图生图 老树开新花零费用快速出图写实风格_2094170191398789122.json, 图片生成/文生图/SDXL极速图生图｜老树开新花写实风重绘生成_2094306606434578434.json, 图片生成/文生图/sdxl文生图工作流｜输入描述文字直接生成图片_2106604632175890434.json, 图片生成/文生图/光辉绘画工作流｜光效氛围感唯美插画一键直出_2112426661630275588.json, 图片生成/文生图/图生图老树开新花SDXL图生图极速版 快速出图方案_2109035097302327297.json, 图片生成/文生图/老树开新花极速写实｜SDXL图生图零成本出图_2090826700719476738.json, 图片生成/文生图/老树开新花极速版｜SDXL图生图写实生成_2090531557399420929.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_206

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/文生图/SDXL文生图工作流，高质量文本到图像生成方案_2106904544729985026.json、图片生成/文生图/SDXL文生图工作流，高质量文本到图像生成方案_2108380198407327746.json、图片生成/文生图/SDXL极速图生图 老树开新花零费用快速出图写实风格_2094170191398789122.json、图片生成/文生图/SDXL极速图生图｜老树开新花写实风重绘生成_2094306606434578434.json、图片生成/文生图/sdxl文生图工作流｜输入描述文字直接生成图片_2106604632175890434.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoader`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `孤海注释` —— 8/9 个有
- `LoadImage` —— 5/9 个有
- `VAEEncode` —— 5/9 个有
- `CR Text` —— 3/9 个有
- `CR Text Concatenate` —— 3/9 个有
- `SDXL Empty Latent Image (rgthree)` —— 3/9 个有
- `ShowText|pysssss` —— 3/9 个有
- `TextInputBasic` —— 3/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 9 | 100% |
| 高度 | 80 | 80 - 80 | 9 | 100% |
| LoRA 模型强度 | 0.3 | 0.3 - 1 | 9 | 49% |
| LoRA 文本强度 | 0.3 | 0.3 - 1 | 9 | 43% |
| 采样步数 | 4 | 4 - 4 | 9 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 9 | 100% |
| 采样算法 | er_sde | - | 9 | 100% |
| 调度器 | beta | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.3，观测区间 0.3 - 1，9 个样本，取值分散，一致性仅 49%
- LoRA 文本强度 中位数 0.3，观测区间 0.3 - 1，9 个样本，取值分散，一致性仅 43%
- 采样步数 中位数 4，观测区间 4 - 4，9 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，9 个样本，一致性 100%
- 调度器 最常用 beta，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（9/9 个样本）：Steps较低可能导致细节不足
