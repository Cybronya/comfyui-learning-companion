---
name: text_to_image_lora_sampler_clip_31
type: Text To Image
frequency: 19
level: weak
coverage: 0.912632
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/SDXL文生图工作流｜经典模型稳定出图｜入门练手必备模板_2101885301458292738.json, 图片生成/文生图/SDXL极速图生图 老树开新花零费用快速出图写实风格_2094170191398789122.json, 图片生成/文生图/SDXL极速图生图｜老树开新花写实风重绘生成_2094306606434578434.json, 图片生成/文生图/Z-Image Turbo极速文生图内置身材调节Lora处理工具_2101769735858905090.json, 图片生成/文生图/Z-image-turbo极速文生图｜内置身材调节Lora免折腾_2101556554981011457.json, 图片生成/文生图/Z-image文生图工作流 不油腻超写实人像生成_2099942321948282881.json, 图片生成/文生图/Z-image文生图工作流_不油腻超写实人像生成_2100177040510115842.json, 图片生成/文生图/Z-image文生图工作流_不油腻超写实人像生成_2100552637174341633.json, 图片生成/文生图/Z-image文生图工作流_不油腻超写实人像生成_2101481634838175746.json, 图片生成/文生图/Z-image文生图工作流_不油腻超写实人像生成_2101864171859173377.json, 图片生成/文生图/Z-image文生图工作流_不油腻超写实人像生成_2102210804346085377.json, 图片生成/文生图/Z-image文生图工作流｜不油腻超写实人像生成写实风_2100811509139066882.json, 图片生成/文生图/Z-image超写实文生图工作流 写实人像生成工具_2099942556120477697.json, 图片生成/文生图/Z-image超写实文生图工作流_写实人像生成工具_2100178170963128322.json, 图片生成/文生图/Z-image超写实文生图工作流_写实人像生成工具_2100551067837751298.json, 图片生成/文生图/Z-image超写实文生图工作流_写实人像生成工具_2101864963181731842.json, 图片生成/文生图/Z-image超写实文生图工作流｜写实人像生成利器_2100814802720481282.json, 图片生成/文生图/摄影质感文生图工作流｜Z-image turbo快速出图生成_2096729113515089922.json, 图片生成/文生图/火影人气角色雏田文生图｜一键生成动漫美少女立绘_2107648182992850946.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_31

> 由 `engine/knowledge_consolidation` 从 19 个 workflow 归纳得出（图片生成/文生图/SDXL文生图工作流｜经典模型稳定出图｜入门练手必备模板_2101885301458292738.json、图片生成/文生图/SDXL极速图生图 老树开新花零费用快速出图写实风格_2094170191398789122.json、图片生成/文生图/SDXL极速图生图｜老树开新花写实风重绘生成_2094306606434578434.json、图片生成/文生图/Z-Image Turbo极速文生图内置身材调节Lora处理工具_2101769735858905090.json、图片生成/文生图/Z-image-turbo极速文生图｜内置身材调节Lora免折腾_2101556554981011457.json…）

- **类型**：Text To Image
- **样本数**：19
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 19 个 workflow 都包含：
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
- `ImageUpscaleWithModel` —— 16/19 个有
- `UpscaleModelLoader` —— 16/19 个有
- `ConditioningZeroOut` —— 15/19 个有
- `PreviewImage` —— 14/19 个有
- `ImageFromBatch` —— 13/19 个有
- `孤海注释` —— 10/19 个有
- `EmptyImage` —— 9/19 个有
- `LayerColor: BrightnessContrastV2` —— 7/19 个有
- `CheckpointLoaderSimple` —— 4/19 个有
- `LoraLoader` —— 4/19 个有
- `Int` —— 2/19 个有
- `LoadImage` —— 2/19 个有
- `VAEEncode` —— 2/19 个有
- `LayerColor: Brightness & Contrast` —— 1/19 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 19 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 19 | 100% |
| 采样算法 | er_sde | - | 19 | 100% |
| 调度器 | beta | - | 19 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 19 | 100% |
| 宽度 | 80 | 80 - 1440 | 19 | 0% |
| 高度 | 80 | 80 - 1920 | 19 | 0% |
| LoRA 模型强度 | 0.45 | 0.3 - 1 | 4 | 48% |
| LoRA 文本强度 | 0.45 | 0.3 - 1 | 4 | 48% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 23/19 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，19 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，19 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，19 个样本，一致性 100%
- 调度器 最常用 beta，19 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，19 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 1440，19 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 1920，19 个样本，取值分散，一致性仅 0%
- LoRA 模型强度 中位数 0.45，观测区间 0.3 - 1，4 个样本，取值分散，一致性仅 48%
- LoRA 文本强度 中位数 0.45，观测区间 0.3 - 1，4 个样本，取值分散，一致性仅 48%
- 高发问题（23/19 个样本）：Steps较低可能导致细节不足
