---
name: unknown_workflow_sampler_unet_vae_314
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.596333
common_nodes: [Any Switch (rgthree), CFGGuider, CLIPLoader, ComfySwitchNode, EmptyLatentImage, Fast Groups Bypasser (rgthree), Fast Groups Muter (rgthree), Image Comparer (rgthree), ImageConcanate, ImageConcatMulti, ImageScaleToTotalPixels, KSamplerSelect, LoadImage, ManualSigmas, PrimitiveStringMultiline, QwenImage21Cache, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveImage, Seed (rgthree), TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Qwen-Image_2.1_一键_表情_动作_多视图_生成_2116345900653178881.json, 平台全量/Qwen image 2.1 Turbo 多合一图像编辑工作流 V1_2111129116396318722.json, 平台全量/Qwen-Image 2.1 一键 表情_动作_多视图 生成_2116017427275411457.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_314

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Qwen-Image_2.1_一键_表情_动作_多视图_生成_2116345900653178881.json、平台全量/Qwen image 2.1 Turbo 多合一图像编辑工作流 V1_2111129116396318722.json、平台全量/Qwen-Image 2.1 一键 表情_动作_多视图 生成_2116017427275411457.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：60%

## 共有节点

全部 3 个 workflow 都包含：
- `Any Switch (rgthree)`
- `CFGGuider`
- `CLIPLoader`
- `ComfySwitchNode`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Muter (rgthree)`
- `Image Comparer (rgthree)`
- `ImageConcanate`
- `ImageConcatMulti`
- `ImageScaleToTotalPixels`
- `KSamplerSelect`
- `LoadImage`
- `ManualSigmas`
- `PrimitiveStringMultiline`
- `QwenImage21Cache`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveImage`
- `Seed (rgthree)`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text Replace` —— 2/3 个有
- `ImageFromBatch` —— 2/3 个有
- `PrimitiveBoolean` —— 2/3 个有
- `SimpleComparison+` —— 2/3 个有
- `easy anythingIndexSwitch` —— 2/3 个有
- `easy imageListToImageBatch` —— 2/3 个有
- `easy int` —— 2/3 个有
- `easy mathInt` —— 2/3 个有
- `easy promptList` —— 2/3 个有
- `PathchSageAttentionKJ` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 3 | 100% |
| 高度 | 1024 | 1024 - 1024 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，3 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，3 个样本，取值集中（一致性 100%）
