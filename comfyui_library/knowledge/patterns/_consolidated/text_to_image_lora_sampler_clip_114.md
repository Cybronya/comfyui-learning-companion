---
name: text_to_image_lora_sampler_clip_114
type: Text To Image
frequency: 8
level: weak
coverage: 0.897625
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen朋友圈海报设计V1.0文生图工具_2100273790323351553.json, 图片生成/文生图/Z Image文生图标准版工作流，高质量文本到图像生成方案_2105786409570361346.json, 图片生成/文生图/Z-Image-Turbo文生图｜高速出图质量在线新体验_2105251524116041729.json, 图片生成/文生图/Z-image文生图工作流_不油腻超写实人像生成_2100552637174341633.json, 图片生成/文生图/Z-image超写实文生图工作流_写实人像生成工具_2100551067837751298.json, 图片生成/文生图/ZIT基础文生图工作流，高质量文本到图像生成方案_2106810710041911298.json, 图片生成/文生图/z-image文生图工作流（不油腻超写实）_2099402532144635906.json, 图片生成/文生图/小腰精体态曲线塑造 文生图一键生成完美身材比例_2104343399116664834.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_114

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/Qwen朋友圈海报设计V1.0文生图工具_2100273790323351553.json、图片生成/文生图/Z Image文生图标准版工作流，高质量文本到图像生成方案_2105786409570361346.json、图片生成/文生图/Z-Image-Turbo文生图｜高速出图质量在线新体验_2105251524116041729.json、图片生成/文生图/Z-image文生图工作流_不油腻超写实人像生成_2100552637174341633.json、图片生成/文生图/Z-image超写实文生图工作流_写实人像生成工具_2100551067837751298.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `JjkText` —— 7/8 个有
- `solarL_SaveImagesToZip` —— 7/8 个有
- `PreviewImage` —— 6/8 个有
- `ConditioningZeroOut` —— 5/8 个有
- `EmptySD3LatentImage` —— 5/8 个有
- `ModelSamplingAuraFlow` —— 5/8 个有
- `孤海注释` —— 5/8 个有
- `UpscaleModelLoader` —— 4/8 个有
- `ImageFromBatch` —— 3/8 个有
- `ImageUpscaleWithModel` —— 3/8 个有
- `EmptyImage` —— 2/8 个有
- `LayerColor: BrightnessContrastV2` —— 2/8 个有
- `LoraLoader` —— 2/8 个有
- `UltimateSDUpscale` —— 1/8 个有
- `ZML_LoadImage` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.8 | - | 2 | 100% |
| LoRA 文本强度 | 0.9 | - | 2 | 89% |
| 采样步数 | 4 | 4 - 10 | 8 | 58% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 8 | 72% |
| 采样算法 | er_sde | - | 8 | 88% |
| 调度器 | beta | - | 8 | 88% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |
| 宽度 | 80 | 80 - 1280 | 8 | 0% |
| 高度 | 80 | 80 - 720 | 8 | 0% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- LoRA 模型强度 中位数 0.8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 0.9，样本不足，未给区间，2 个样本，取值集中（一致性 89%）
- 采样步数 中位数 4，观测区间 4 - 10，8 个样本
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，8 个样本
- 采样算法 最常用 er_sde，8 个样本，一致性 88%
- 调度器 最常用 beta，8 个样本，一致性 88%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 1280，8 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 720，8 个样本，取值分散，一致性仅 0%
- 高发问题（10/8 个样本）：Steps较低可能导致细节不足
