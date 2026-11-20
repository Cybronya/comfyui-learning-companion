---
name: text_to_image_upscale_sampler_clip_29
type: Text To Image
frequency: 5
level: moderate
coverage: 0.8924
common_nodes: [CLIPTextEncode, EmptyLatentImage, ImageUpscaleWithModel, KSampler, PreviewImage, SaveImage, UpscaleModelLoader, VAEDecode]
problems: []
missing: []
members: [平台全量/提示词反推（WD14)-图片生成放大_1832980051804475393.json, 平台全量/是毛团子啊！_1792827865239179265.json, 平台全量/果冻色宠物盲盒_1792785283100495874.json, 平台全量/毛团子鸭子_1839849817907351554.json, 平台全量/真实场景_1792507820214636545.json]
source: knowledge_consolidation
---

# text_to_image_upscale_sampler_clip_29

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（平台全量/提示词反推（WD14)-图片生成放大_1832980051804475393.json、平台全量/是毛团子啊！_1792827865239179265.json、平台全量/果冻色宠物盲盒_1792785283100495874.json、平台全量/毛团子鸭子_1839849817907351554.json、平台全量/真实场景_1792507820214636545.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPTextEncode`
- `EmptyLatentImage`
- `ImageUpscaleWithModel`
- `KSampler`
- `PreviewImage`
- `SaveImage`
- `UpscaleModelLoader`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `CheckpointLoaderSimple` —— 4/5 个有
- `LoraLoader` —— 4/5 个有
- `ConditionText` —— 1/5 个有
- `VAELoader` —— 1/5 个有
- `workflow/提示词获取` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 768 - 1280 | 5 | 82% |
| 高度 | 1024 | 1024 - 1920 | 5 | 70% |
| 采样步数 | 20 | 20 - 20 | 5 | 100% |
| Prompt 约束强度(CFG) | 3.8 | 3.8 - 8 | 5 | 64% |
| 采样算法 | dpmpp_2m | - | 5 | 80% |
| 调度器 | karras | - | 5 | 80% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| LoRA 模型强度 | 0.6 | 0.6 - 1 | 4 | 75% |
| LoRA 文本强度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 768 - 1280，5 个样本，取值集中（一致性 82%）
- 高度 中位数 1024，观测区间 1024 - 1920，5 个样本
- 采样步数 中位数 20，观测区间 20 - 20，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 3.8，观测区间 3.8 - 8，5 个样本
- 采样算法 最常用 dpmpp_2m，5 个样本，一致性 80%
- 调度器 最常用 karras，5 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.6，观测区间 0.6 - 1，4 个样本
- LoRA 文本强度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
