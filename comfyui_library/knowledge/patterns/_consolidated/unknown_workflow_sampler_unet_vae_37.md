---
name: unknown_workflow_sampler_unet_vae_37
type: Unknown Workflow
frequency: 15
level: moderate
coverage: 0.815
common_nodes: [CLIPLoader, ComfySwitchNode, EmptyLatentImage, KSampler, LoadImage, QwenImage21Cache, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/AI图像创作丨Qwen-Image丨参考图生成_2113093276168450049.json, 图片生成/图生图/Action Transfer人物替换+人物换装 Qwen+Image+2.1_2109808936437243905.json, 图片生成/图生图/CGD_qwen-image-2.1-rh-background-removal_2104833999733616641.json, 图片生成/图生图/Qwen Image 2.1 人物替换+图片换人_2109588672441049090.json, 图片生成/图生图/Qwen Image 2.1 人物替换+图片换人_2109604944461520897.json, 图片生成/图生图/Qwen Image 2.1 人物替换+图片换人！B站艾橘溪_2109524734416351233.json, 图片生成/图生图/Qwen Image 2.1 双参考图换装编辑｜本地 GGUF 提示词增强_2101976709301096450.json, 图片生成/图生图/Qwen Image 2.1 多参考图生图标准版_2105099788420210690.json, 图片生成/图生图/Qwen Image 2.1 ｜生图及编辑_2101865008786395137.json, 图片生成/图生图/Qwen Image 2.1_人物替换+图片换人_2109576795904372737.json, 图片生成/图生图/Qwen image 2.1图像编辑_2101926899231584257.json, 图片生成/图生图/Qwen_Image_2.1_｜生图及编辑_2109445975751352321.json, 图片生成/图生图/人物替换+图片换人_2109643939279106049.json, 图片生成/图生图/图片换人丨Qwen_Image_2.1丨双图替换·保留姿态_2113801696882282497.json, 图片生成/文生图/图片换人丨Qwen Image 2.1丨双图替换·保留姿态_2112093115338280962.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_37

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（图片生成/图生图/AI图像创作丨Qwen-Image丨参考图生成_2113093276168450049.json、图片生成/图生图/Action Transfer人物替换+人物换装 Qwen+Image+2.1_2109808936437243905.json、图片生成/图生图/CGD_qwen-image-2.1-rh-background-removal_2104833999733616641.json、图片生成/图生图/Qwen Image 2.1 人物替换+图片换人_2109588672441049090.json、图片生成/图生图/Qwen Image 2.1 人物替换+图片换人_2109604944461520897.json…）

- **类型**：Unknown Workflow
- **样本数**：15
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 15 个 workflow 都包含：
- `CLIPLoader`
- `ComfySwitchNode`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `QwenImage21Cache`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `JjkText` —— 10/15 个有
- `ImageResizeKJv2` —— 9/15 个有
- `PrimitiveInt` —— 9/15 个有
- `easy imageConcat` —— 9/15 个有
- `ResolutionSelector` —— 5/15 个有
- `SaveImageAdvanced` —— 4/15 个有
- `PreviewImage` —— 3/15 个有
- `EmptyImage` —— 2/15 个有
- `ImageScale` —— 2/15 个有
- `LoraLoaderModelOnly` —— 2/15 个有
- `ImageCompare` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 25 - 50 | 15 | 70% |
| Prompt 约束强度(CFG) | 1 | 1 - 3.5 | 15 | 36% |
| 采样算法 | euler | - | 15 | 87% |
| 调度器 | beta | - | 15 | 60% |
| 重绘幅度 | 1 | 1 - 1 | 15 | 100% |
| 宽度 | 1024 | 960 - 1024 | 15 | 98% |
| 高度 | 1024 | 1024 - 1280 | 15 | 92% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 25 - 50，15 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3.5，15 个样本，取值分散，一致性仅 36%
- 采样算法 最常用 euler，15 个样本，一致性 87%
- 调度器 最常用 beta，15 个样本，一致性 60%
- 重绘幅度 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 960 - 1024，15 个样本，取值集中（一致性 98%）
- 高度 中位数 1024，观测区间 1024 - 1280，15 个样本，取值集中（一致性 92%）
