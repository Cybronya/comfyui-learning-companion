---
name: unknown_workflow_sampler_unet_vae_62
type: Unknown Workflow
frequency: 14
level: strong
coverage: 0.845786
common_nodes: [CLIPLoader, EmptyLatentImage, KSampler, LoadImage, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/AI图像创作丨Qwen-Image丨参考图生成_2113093276168450049.json, 图片生成/图生图/Action Transfer人物替换+人物换装 Qwen+Image+2.1_2109808936437243905.json, 图片生成/图生图/Action_Transfer人物替换+人物换装_Qwen+Image+2.1_2115601886672936962.json, 图片生成/图生图/CGD_qwen-image-2.1-rh-background-removal_2104833999733616641.json, 图片生成/图生图/Qwen Image 2.1 人物替换+图片换人_2109588672441049090.json, 图片生成/图生图/Qwen Image 2.1 人物替换+图片换人_2109604944461520897.json, 图片生成/图生图/Qwen Image 2.1 人物替换+图片换人！B站艾橘溪_2109524734416351233.json, 图片生成/图生图/Qwen Image 2.1_人物替换+图片换人_2109576795904372737.json, 图片生成/图生图/Qwen Image 2.1动作模仿+动作迁移 图片动作迁移模仿_2109586459991826434.json, 图片生成/图生图/Qwen Image 2.1动作模仿+动作迁移 图片动作迁移模仿_2109607770860384257.json, 图片生成/图生图/Qwen Image 2.1动作模仿+动作迁移！B站艾橘溪_2109520790583595009.json, 图片生成/图生图/人物替换+图片换人_2109643939279106049.json, 图片生成/图生图/图片换人丨Qwen_Image_2.1丨双图替换·保留姿态_2113801696882282497.json, 图片生成/文生图/人物动作迁移丨Qwen Image 2.1丨双图参考·姿态引导_2112093122409885697.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_62

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/图生图/AI图像创作丨Qwen-Image丨参考图生成_2113093276168450049.json、图片生成/图生图/Action Transfer人物替换+人物换装 Qwen+Image+2.1_2109808936437243905.json、图片生成/图生图/Action_Transfer人物替换+人物换装_Qwen+Image+2.1_2115601886672936962.json、图片生成/图生图/CGD_qwen-image-2.1-rh-background-removal_2104833999733616641.json、图片生成/图生图/Qwen Image 2.1 人物替换+图片换人_2109588672441049090.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 14 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJv2` —— 13/14 个有
- `JjkText` —— 13/14 个有
- `PrimitiveInt` —— 13/14 个有
- `ComfySwitchNode` —— 10/14 个有
- `QwenImage21Cache` —— 10/14 个有
- `easy imageConcat` —— 9/14 个有
- `DWPreprocessor` —— 4/14 个有
- `ImageStitch` —— 4/14 个有
- `LoraLoaderModelOnly` —— 4/14 个有
- `ImageScale` —— 2/14 个有
- `EmptyImage` —— 1/14 个有
- `ImageCompare` —— 1/14 个有
- `PreviewImage` —— 1/14 个有
- `SaveImageAdvanced` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 25 - 30 | 14 | 91% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 14 | 100% |
| 采样算法 | euler | - | 14 | 100% |
| 调度器 | beta | - | 14 | 64% |
| 重绘幅度 | 1 | 1 - 1 | 14 | 100% |
| 宽度 | 1024 | 960 - 1280 | 14 | 93% |
| 高度 | 1024 | 960 - 1280 | 14 | 93% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 25 - 30，14 个样本，取值集中（一致性 91%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，14 个样本，一致性 100%
- 调度器 最常用 beta，14 个样本，一致性 64%
- 重绘幅度 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 960 - 1280，14 个样本，取值集中（一致性 93%）
- 高度 中位数 1024，观测区间 960 - 1280，14 个样本，取值集中（一致性 93%）
