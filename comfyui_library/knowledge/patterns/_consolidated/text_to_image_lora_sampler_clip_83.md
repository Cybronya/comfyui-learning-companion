---
name: text_to_image_lora_sampler_clip_83
type: Text To Image
frequency: 15
level: weak
coverage: 0.912133
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/千问2.1文生图_2103829231951241218.json, 图片生成/文生图/千问2.1文生图官方原生架构｜一键出图带海报制作｜新手友好_2104813513557504002.json, 图片生成/文生图/千问2.1文生图自动优化版｜一句话提示词直出精美图片_2103726338984210433.json, 图片生成/文生图/千问2.1文生图｜轻量好上手 文生图出图稳定效果在线_2104035483096539138.json, 图片生成/文生图/千问2.1白底商品图｜商业摄影级纯白底｜电商主图批量生成_2104808797784072193.json, 图片生成/文生图/千问Qwen Image 2.1文生图工作流，人像写真美少女风格出图_2114504263949963266.json, 图片生成/文生图/千问Qwen-Image-2.1文生图 中文提示词图像生成工具_2113397688858398722.json, 图片生成/文生图/千问Qwen_Image_2.1文生图工作流，人像写真美少女风格出图_2115963188691955713.json, 图片生成/文生图/千问Qwen_Image_2.1文生图工作流，人像写真美少女风格出图_2116017876267257857.json, 图片生成/文生图/千问iamge2.1文生图工作流｜官方同款画质一键直出_2103062439452569601.json, 图片生成/文生图/千问qwen image 2.1文生图官方架构一键出图 高质量画面直出_2108706393980227586.json, 图片生成/文生图/千问qwen image 2.1文生图工作流 高质量画面直出_2104994907697012737.json, 数字人/数字人/Qwen Image 2.1文生图处理生成工具_2102554303809544193.json, 视频生成/文生视频/Qwen_Image_2.1文生图工作流，最强开源模型中文提示词直接出图_2105513820637716482.json, 视频生成/文生视频/Qwen_image_2.1文生图美少女特调｜写实风格出图细腻｜二次元真人两相宜_2104048080306917377.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_83

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（图片生成/文生图/千问2.1文生图_2103829231951241218.json、图片生成/文生图/千问2.1文生图官方原生架构｜一键出图带海报制作｜新手友好_2104813513557504002.json、图片生成/文生图/千问2.1文生图自动优化版｜一句话提示词直出精美图片_2103726338984210433.json、图片生成/文生图/千问2.1文生图｜轻量好上手 文生图出图稳定效果在线_2104035483096539138.json、图片生成/文生图/千问2.1白底商品图｜商业摄影级纯白底｜电商主图批量生成_2104808797784072193.json…）

- **类型**：Text To Image
- **样本数**：15
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 15 个 workflow 都包含：
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
- `PreviewImage` —— 12/15 个有
- `孤海注释` —— 10/15 个有
- `TextEncodeQwenImage21` —— 9/15 个有
- `TextGenerateLTX2Prompt` —— 7/15 个有
- `easy showAnything` —— 7/15 个有
- `ConditioningZeroOut` —— 6/15 个有
- `ResolutionSelector` —— 5/15 个有
- `FastGroupsBypassSwitch` —— 4/15 个有
- `CM_FloatToInt` —— 2/15 个有
- `EmptyImage` —— 2/15 个有
- `SaveImageAdvanced` —— 2/15 个有
- `CR Text` —— 1/15 个有
- `ImpactSwitch` —— 1/15 个有
- `Text` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 1024 | 15 | 0% |
| 高度 | 80 | 80 - 1024 | 15 | 0% |
| 采样步数 | 4 | 4 - 50 | 15 | 0% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 15 | 80% |
| 采样算法 | er_sde | - | 15 | 93% |
| 调度器 | beta | - | 15 | 93% |
| 重绘幅度 | 1 | 1 - 1 | 15 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 27/15 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 1024，15 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 1024，15 个样本，取值分散，一致性仅 0%
- 采样步数 中位数 4，观测区间 4 - 50，15 个样本，取值分散，一致性仅 0%
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，15 个样本
- 采样算法 最常用 er_sde，15 个样本，一致性 93%
- 调度器 最常用 beta，15 个样本，一致性 93%
- 重绘幅度 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 高发问题（27/15 个样本）：Steps较低可能导致细节不足
