---
name: text_to_image_lora_sampler_clip_338
type: Text To Image
frequency: 6
level: strong
coverage: 0.888
common_nodes: [Anything Everywhere3, Anything Everywhere?, CLIPLoader, CLIPTextEncode, CheckpointLoaderSimple, EmptyImage, EmptyLatentImage, Fast Bypasser (rgthree), JjkText, KSampler, LoadImage, LoraLoaderModelOnly, Mute / Bypass Repeater (rgthree), SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAELoader, WujiCleaner, easy boolean, easy cleanGpuUsed, easy imageSwitch, easy int, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/RapidAIO图片编辑I2I V19｜千问Qwen多图中文指令编辑光天化日版_2088715810897481729.json, 图片生成/图生图/RapidAIO图片编辑I2I V23｜千问Qwen快速响应三图同时处理_2088717322675638274.json, 图片生成/图生图/千问Qwen图片编辑V19加密版 高一致性多图编辑工具_2099196211893989378.json, 图片生成/图生图/千问Qwen图片编辑V19加密版 高一致性多图编辑工具_2099577596878090242.json, 图片生成/图生图/千问Qwen图片编辑V23加密版 多图编辑本地解码工具_2099194594310320129.json, 图片生成/图生图/千问Qwen图片编辑V23加密版 多图编辑本地解码工具_2099683360460333057.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_338

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/RapidAIO图片编辑I2I V19｜千问Qwen多图中文指令编辑光天化日版_2088715810897481729.json、图片生成/图生图/RapidAIO图片编辑I2I V23｜千问Qwen快速响应三图同时处理_2088717322675638274.json、图片生成/图生图/千问Qwen图片编辑V19加密版 高一致性多图编辑工具_2099196211893989378.json、图片生成/图生图/千问Qwen图片编辑V19加密版 高一致性多图编辑工具_2099577596878090242.json、图片生成/图生图/千问Qwen图片编辑V23加密版 多图编辑本地解码工具_2099194594310320129.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 6 个 workflow 都包含：
- `Anything Everywhere3`
- `Anything Everywhere?`
- `CLIPLoader`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyImage`
- `EmptyLatentImage`
- `Fast Bypasser (rgthree)`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `Mute / Bypass Repeater (rgthree)`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `WujiCleaner`
- `easy boolean`
- `easy cleanGpuUsed`
- `easy imageSwitch`
- `easy int`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `TT_img_enc` —— 4/6 个有
- `CR Latent Input Switch` —— 2/6 个有
- `Int` —— 2/6 个有
- `easy float` —— 2/6 个有
- `easy getNode` —— 2/6 个有
- `easy imageScaleDownBy` —— 2/6 个有
- `easy imageSize` —— 2/6 个有
- `easy setNode` —— 2/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 6 | 100% |
| 高度 | 80 | 80 - 80 | 6 | 100% |
| 采样步数 | 4 | 4 - 4 | 6 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 6 | 100% |
| 采样算法 | er_sde | - | 6 | 100% |
| 调度器 | beta | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 12/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，6 个样本，一致性 100%
- 调度器 最常用 beta，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（12/6 个样本）：Steps较低可能导致细节不足
