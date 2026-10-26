---
name: text_to_image_lora_sampler_clip_179
type: Text To Image
frequency: 10
level: moderate
coverage: 0.8946
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoader, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen朋友圈海报设计V1.0文生图工具_2100273790323351553.json, 图片生成/文生图/Qwen朋友圈海报设计文生图处理生成工作流_2101019397950361601.json, 图片生成/文生图/SDXL图生图极速版 零成本快速图片风格转换_2098114830124281858.json, 图片生成/文生图/SDXL文生图工作流｜经典模型稳定出图｜入门练手必备模板_2101885301458292738.json, 图片生成/文生图/SDXL极速图生图 老树开新花零费用快速出图写实风格_2094170191398789122.json, 图片生成/文生图/SDXL极速图生图｜老树开新花写实风重绘生成_2094306606434578434.json, 图片生成/文生图/图生图老树开新花SDXL图生图极速版 快速出图方案_2109035097302327297.json, 图片生成/文生图/小腰精体态曲线塑造 文生图一键生成完美身材比例_2104343399116664834.json, 图片生成/文生图/老树开新花极速写实｜SDXL图生图零成本出图_2090826700719476738.json, 图片生成/文生图/老树开新花极速版｜SDXL图生图写实生成_2090531557399420929.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_179

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/文生图/Qwen朋友圈海报设计V1.0文生图工具_2100273790323351553.json、图片生成/文生图/Qwen朋友圈海报设计文生图处理生成工作流_2101019397950361601.json、图片生成/文生图/SDXL图生图极速版 零成本快速图片风格转换_2098114830124281858.json、图片生成/文生图/SDXL文生图工作流｜经典模型稳定出图｜入门练手必备模板_2101885301458292738.json、图片生成/文生图/SDXL极速图生图 老树开新花零费用快速出图写实风格_2094170191398789122.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
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
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `CheckpointLoaderSimple` —— 7/10 个有
- `LoadImage` —— 6/10 个有
- `VAEEncode` —— 6/10 个有
- `EmptySD3LatentImage` —— 3/10 个有
- `ModelSamplingAuraFlow` —— 3/10 个有
- `PreviewImage` —— 3/10 个有
- `UpscaleModelLoader` —— 3/10 个有
- `UltimateSDUpscale` —— 2/10 个有
- `ImageUpscaleWithModel` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.3 | 0.3 - 1 | 10 | 47% |
| LoRA 文本强度 | 0.3 | 0.3 - 1 | 10 | 44% |
| 采样步数 | 4 | 4 - 4 | 10 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 10 | 100% |
| 采样算法 | er_sde | - | 10 | 100% |
| 调度器 | beta | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |
| 宽度 | 80 | 80 - 80 | 10 | 100% |
| 高度 | 80 | 80 - 80 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- LoRA 模型强度 中位数 0.3，观测区间 0.3 - 1，10 个样本，取值分散，一致性仅 47%
- LoRA 文本强度 中位数 0.3，观测区间 0.3 - 1，10 个样本，取值分散，一致性仅 44%
- 采样步数 中位数 4，观测区间 4 - 4，10 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，10 个样本，一致性 100%
- 调度器 最常用 beta，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 高发问题（11/10 个样本）：Steps较低可能导致细节不足
