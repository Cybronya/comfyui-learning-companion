---
name: unknown_workflow_sampler_unet_vae_34
type: Unknown Workflow
frequency: 18
level: strong
coverage: 0.905111
common_nodes: [CLIPLoader, ComfySwitchNode, EmptyLatentImage, KSampler, LoadImage, QwenImage21Cache, ResolutionSelector, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Qwen Image 2.1多图编辑_2102401818163765249.json, 图片生成/图生图/Qwen Image 2.1多图编辑_2107745252730826754.json, 图片生成/图生图/Qwen Image 2.1多图编辑_2108519033753653250.json, 图片生成/图生图/Qwen Image 2.1多图编辑！B站艾橘溪_2102245556734218241.json, 图片生成/图生图/Qwen image 2.1 3图编辑_2101904839130312705.json, 图片生成/图生图/Qwen image 2.1单图编辑_2101881268609830914.json, 图片生成/图生图/Qwen image 2.1双图编辑_2101903016357097474.json, 图片生成/图生图/Qwen image 2.1图片编辑_2101800014677897217.json, 图片生成/图生图/Qwen image 2.1图片编辑_2101884328585285634.json, 图片生成/图生图/Qwen image 2.1图片编辑_2101946565576454146.json, 图片生成/图生图/Qwen image 2.1图片编辑_2101981525330976770.json, 图片生成/图生图/Qwen image 2.1图片编辑_2102013628437319682.json, 图片生成/图生图/Qwen image 2.1图片编辑_2102212076977606658.json, 图片生成/图生图/Qwen image 2.1图片编辑_2102302751672848386.json, 图片生成/图生图/Qwen image 2.1图片编辑_2111737939410640897.json, 图片生成/图生图/Qwen image 2.1图片编辑【自动提示词版】_2101837155051073537.json, 图片生成/图生图/Qwen image 2.1图片编辑（双图）_2101862560432746498.json, 图片生成/图生图/Qwen image 2.1透明背景抠图_2101914691361660930.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_34

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（图片生成/图生图/Qwen Image 2.1多图编辑_2102401818163765249.json、图片生成/图生图/Qwen Image 2.1多图编辑_2107745252730826754.json、图片生成/图生图/Qwen Image 2.1多图编辑_2108519033753653250.json、图片生成/图生图/Qwen Image 2.1多图编辑！B站艾橘溪_2102245556734218241.json、图片生成/图生图/Qwen image 2.1 3图编辑_2101904839130312705.json…）

- **类型**：Unknown Workflow
- **样本数**：18
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 18 个 workflow 都包含：
- `CLIPLoader`
- `ComfySwitchNode`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `QwenImage21Cache`
- `ResolutionSelector`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `BatchImagesNode` —— 17/18 个有
- `TextGenerateLTX2Prompt` —— 17/18 个有
- `SaveImageAdvanced` —— 14/18 个有
- `easy showAnything` —— 14/18 个有
- `ImageConcatMulti` —— 12/18 个有
- `JjkText` —— 8/18 个有
- `easy cleanGpuUsed` —— 4/18 个有
- `easy imageConcat` —— 2/18 个有
- `CompressImages` —— 1/18 个有
- `GetImageSize` —— 1/18 个有
- `Int` —— 1/18 个有
- `Label (rgthree)` —— 1/18 个有
- `TextCombinerTwo` —— 1/18 个有
- `TextInput_` —— 1/18 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 50 | 50 - 50 | 18 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 18 | 100% |
| 采样算法 | euler | - | 18 | 100% |
| 调度器 | simple | - | 18 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 18 | 100% |
| 宽度 | 1024 | 1024 - 1024 | 18 | 100% |
| 高度 | 1024 | 1024 - 1024 | 18 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 50，观测区间 50 - 50，18 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，18 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，18 个样本，一致性 100%
- 调度器 最常用 simple，18 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，18 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 1024 - 1024，18 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，18 个样本，取值集中（一致性 100%）
