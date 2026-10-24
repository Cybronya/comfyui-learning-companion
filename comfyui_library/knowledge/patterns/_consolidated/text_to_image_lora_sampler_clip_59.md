---
name: text_to_image_lora_sampler_clip_59
type: Text To Image
frequency: 17
level: moderate
coverage: 0.911059
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen朋友圈海报设计V1.0文生图工具_2100273790323351553.json, 图片生成/文生图/Qwen朋友圈海报设计文生图处理生成工作流_2101019397950361601.json, 图片生成/文生图/SDXL文生图工作流｜经典模型稳定出图｜入门练手必备模板_2101885301458292738.json, 图片生成/文生图/Z Image文生图标准版工作流，高质量文本到图像生成方案_2105786409570361346.json, 图片生成/文生图/Z-image文生图工作流 不油腻超写实人像生成_2099942321948282881.json, 图片生成/文生图/Z-image文生图工作流_不油腻超写实人像生成_2100177040510115842.json, 图片生成/文生图/Z-image文生图工作流_不油腻超写实人像生成_2100552637174341633.json, 图片生成/文生图/Z-image文生图工作流_不油腻超写实人像生成_2101481634838175746.json, 图片生成/文生图/Z-image文生图工作流_不油腻超写实人像生成_2101864171859173377.json, 图片生成/文生图/Z-image文生图工作流_不油腻超写实人像生成_2102210804346085377.json, 图片生成/文生图/Z-image文生图工作流｜不油腻超写实人像生成写实风_2100811509139066882.json, 图片生成/文生图/Z-image超写实文生图工作流 写实人像生成工具_2099942556120477697.json, 图片生成/文生图/Z-image超写实文生图工作流_写实人像生成工具_2100178170963128322.json, 图片生成/文生图/Z-image超写实文生图工作流_写实人像生成工具_2100551067837751298.json, 图片生成/文生图/Z-image超写实文生图工作流_写实人像生成工具_2101864963181731842.json, 图片生成/文生图/Z-image超写实文生图工作流｜写实人像生成利器_2100814802720481282.json, 图片生成/文生图/火影人气角色雏田文生图｜一键生成动漫美少女立绘_2107648182992850946.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_59

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（图片生成/文生图/Qwen朋友圈海报设计V1.0文生图工具_2100273790323351553.json、图片生成/文生图/Qwen朋友圈海报设计文生图处理生成工作流_2101019397950361601.json、图片生成/文生图/SDXL文生图工作流｜经典模型稳定出图｜入门练手必备模板_2101885301458292738.json、图片生成/文生图/Z Image文生图标准版工作流，高质量文本到图像生成方案_2105786409570361346.json、图片生成/文生图/Z-image文生图工作流 不油腻超写实人像生成_2099942321948282881.json…）

- **类型**：Text To Image
- **样本数**：17
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 17 个 workflow 都包含：
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
- `PreviewImage` —— 15/17 个有
- `UpscaleModelLoader` —— 15/17 个有
- `ImageUpscaleWithModel` —— 13/17 个有
- `ConditioningZeroOut` —— 12/17 个有
- `ImageFromBatch` —— 12/17 个有
- `EmptyImage` —— 9/17 个有
- `孤海注释` —— 8/17 个有
- `LayerColor: BrightnessContrastV2` —— 7/17 个有
- `LoraLoader` —— 4/17 个有
- `EmptySD3LatentImage` —— 3/17 个有
- `ModelSamplingAuraFlow` —— 3/17 个有
- `CheckpointLoaderSimple` —— 2/17 个有
- `UltimateSDUpscale` —— 2/17 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.8 | 0.6 - 1 | 4 | 82% |
| LoRA 文本强度 | 0.8 | 0.6 - 1 | 4 | 82% |
| 采样步数 | 4 | 4 - 4 | 17 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 17 | 100% |
| 采样算法 | er_sde | - | 17 | 100% |
| 调度器 | beta | - | 17 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 17 | 100% |
| 宽度 | 80 | 80 - 1440 | 17 | 0% |
| 高度 | 80 | 80 - 1920 | 17 | 0% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 19/17 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- LoRA 模型强度 中位数 0.8，观测区间 0.6 - 1，4 个样本，取值集中（一致性 82%）
- LoRA 文本强度 中位数 0.8，观测区间 0.6 - 1，4 个样本，取值集中（一致性 82%）
- 采样步数 中位数 4，观测区间 4 - 4，17 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，17 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，17 个样本，一致性 100%
- 调度器 最常用 beta，17 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，17 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 1440，17 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 1920，17 个样本，取值分散，一致性仅 0%
- 高发问题（19/17 个样本）：Steps较低可能导致细节不足
