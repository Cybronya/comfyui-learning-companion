---
name: unknown_workflow_sampler_unet_vae_153
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.881571
common_nodes: [CLIPLoader, JjkText, KSampler, LoadImage, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Qwen Image 2.1动作模仿+动作迁移 图片动作迁移模仿_2109586459991826434.json, 图片生成/图生图/Qwen Image 2.1动作模仿+动作迁移 图片动作迁移模仿_2109607770860384257.json, 图片生成/图生图/Qwen Image 2.1动作模仿+动作迁移！B站艾橘溪_2109520790583595009.json, 图片生成/图生图/Qwen2.1_漫转真_2108743375179567106.json, 图片生成/图生图/Qwen2.1_漫转真_2110186652676222978.json, 图片生成/文生图/主体去背景丨Qwen Image 2.1丨透明PNG·遮罩预览_2112093034207858689.json, 图片生成/文生图/人物动作迁移丨Qwen Image 2.1丨双图参考·姿态引导_2112093122409885697.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_153

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/Qwen Image 2.1动作模仿+动作迁移 图片动作迁移模仿_2109586459991826434.json、图片生成/图生图/Qwen Image 2.1动作模仿+动作迁移 图片动作迁移模仿_2109607770860384257.json、图片生成/图生图/Qwen Image 2.1动作模仿+动作迁移！B站艾橘溪_2109520790583595009.json、图片生成/图生图/Qwen2.1_漫转真_2108743375179567106.json、图片生成/图生图/Qwen2.1_漫转真_2110186652676222978.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `JjkText`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 6/7 个有
- `EmptyLatentImage` —— 5/7 个有
- `ImageResizeKJv2` —— 5/7 个有
- `PrimitiveInt` —— 5/7 个有
- `DWPreprocessor` —— 4/7 个有
- `ImageStitch` —— 4/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/7 个有
- `ComfySwitchNode` —— 1/7 个有
- `ImageScale` —— 1/7 个有
- `MaskToImage` —— 1/7 个有
- `QwenImage21Cache` —— 1/7 个有
- `SplitImageWithAlpha` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 960 - 1280 | 5 | 89% |
| 高度 | 1024 | 960 - 1280 | 5 | 89% |
| 采样步数 | 30 | 25 - 40 | 7 | 84% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 960 - 1280，5 个样本，取值集中（一致性 89%）
- 高度 中位数 1024，观测区间 960 - 1280，5 个样本，取值集中（一致性 89%）
- 采样步数 中位数 30，观测区间 25 - 40，7 个样本，取值集中（一致性 84%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
