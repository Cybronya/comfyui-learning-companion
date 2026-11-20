---
name: unknown_workflow_lora_sampler_unet_87
type: Unknown Workflow
frequency: 9
level: strong
coverage: 0.854
common_nodes: [CLIPLoader, Image Comparer (rgthree), KSampler, LoadImage, LoraLoaderModelOnly, QwenImage21Cache, SaveImage, Seed (rgthree), Text Concatenate, Text Multiline, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, XinbaoImageStandardizer, XinbaoLightingCompanion, easy cleanGpuUsed]
problems: []
missing: []
members: [图片生成/图生图/Qwen image 2.1心宝全能溶图打光｜18种光效组合｜11种光照方向_2111632736069963777.json, 图片生成/图生图/Qwen_image_2.1全能溶图打光｜18种光效组合｜11种光照方向_2116014715209084929.json, 图片生成/图生图/Qwen_image_2.1心宝全能溶图打光｜18种光效组合｜11种光照方向_2115617568051523585.json, 图片生成/图生图/Qwen_image_2.1心宝全能溶图打光｜18种光效组合｜11种光照方向_2115665535491985410.json, 图片生成/图生图/Qwen_image_2.1心宝全能溶图打光｜18种光效组合｜11种光照方向_2115965092289409026.json, 图片生成/图生图/心宝全能打光，18种光效组合，11种光照方向，可溶图，可打光_2111070300279492610.json, 平台全量/全能打光-18种光效组合-11种光照方向-可溶图-可打光_2109558391852060673.json, 平台全量/全能打光——18种光效组合丨11种光照方向丨可溶图+可打光_2108729231567052801.json, 平台全量/心宝全能打光，18种光效组合，11种光照方向，可溶图，可打光_2108448477058527233.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_87

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/Qwen image 2.1心宝全能溶图打光｜18种光效组合｜11种光照方向_2111632736069963777.json、图片生成/图生图/Qwen_image_2.1全能溶图打光｜18种光效组合｜11种光照方向_2116014715209084929.json、图片生成/图生图/Qwen_image_2.1心宝全能溶图打光｜18种光效组合｜11种光照方向_2115617568051523585.json、图片生成/图生图/Qwen_image_2.1心宝全能溶图打光｜18种光效组合｜11种光照方向_2115665535491985410.json、图片生成/图生图/Qwen_image_2.1心宝全能溶图打光｜18种光效组合｜11种光照方向_2115965092289409026.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `Image Comparer (rgthree)`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `QwenImage21Cache`
- `SaveImage`
- `Seed (rgthree)`
- `Text Concatenate`
- `Text Multiline`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `XinbaoImageStandardizer`
- `XinbaoLightingCompanion`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 5/9 个有
- `SetNode` —— 5/9 个有
- `孤海注释` —— 5/9 个有
- `Float` —— 4/9 个有
- `MuyeTextEditOutput` —— 4/9 个有
- `easy imageConcat` —— 3/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 25 - 25 | 9 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler | - | 9 | 100% |
| 调度器 | simple | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 25 - 25，9 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，9 个样本，一致性 100%
- 调度器 最常用 simple，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
