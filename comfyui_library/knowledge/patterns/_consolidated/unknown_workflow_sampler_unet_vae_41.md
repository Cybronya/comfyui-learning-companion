---
name: unknown_workflow_sampler_unet_vae_41
type: Unknown Workflow
frequency: 15
level: strong
coverage: 0.8912
common_nodes: [CLIPLoader, ComfySwitchNode, EmptyLatentImage, KSampler, LoadImage, QwenImage21Cache, ResolutionSelector, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Qwen Image 2.1图片透明分层！ 生成透明图层！艾橘溪_2102196823371898882.json, 图片生成/图生图/Qwen Image 2.1多图编辑_2102313870550462466.json, 图片生成/图生图/Qwen Image 2.1多图编辑_2102401818163765249.json, 图片生成/图生图/Qwen Image 2.1多图编辑_2107745252730826754.json, 图片生成/图生图/Qwen Image 2.1多图编辑_2108519033753653250.json, 图片生成/图生图/Qwen Image 2.1多图编辑！B站艾橘溪_2102245556734218241.json, 图片生成/图生图/Qwen image 2.1 3图编辑_2101904839130312705.json, 图片生成/图生图/Qwen image 2.1单图编辑_2101881268609830914.json, 图片生成/图生图/Qwen image 2.1双图编辑_2101903016357097474.json, 图片生成/图生图/Qwen image 2.1图片编辑_2101800014677897217.json, 图片生成/图生图/Qwen image 2.1图片编辑_2101884328585285634.json, 图片生成/图生图/Qwen image 2.1图片编辑_2111737939410640897.json, 图片生成/图生图/Qwen image 2.1图片编辑【自动提示词版】_2101837155051073537.json, 图片生成/图生图/Qwen image 2.1图片编辑（双图）_2101862560432746498.json, 图片生成/图生图/Qwen image 2.1透明背景抠图_2101914691361660930.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_41

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（图片生成/图生图/Qwen Image 2.1图片透明分层！ 生成透明图层！艾橘溪_2102196823371898882.json、图片生成/图生图/Qwen Image 2.1多图编辑_2102313870550462466.json、图片生成/图生图/Qwen Image 2.1多图编辑_2102401818163765249.json、图片生成/图生图/Qwen Image 2.1多图编辑_2107745252730826754.json、图片生成/图生图/Qwen Image 2.1多图编辑_2108519033753653250.json…）

- **类型**：Unknown Workflow
- **样本数**：15
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 15 个 workflow 都包含：
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
- `BatchImagesNode` —— 14/15 个有
- `TextGenerateLTX2Prompt` —— 14/15 个有
- `JjkText` —— 10/15 个有
- `ImageConcatMulti` —— 9/15 个有
- `SaveImageAdvanced` —— 9/15 个有
- `easy showAnything` —— 9/15 个有
- `easy cleanGpuUsed` —— 4/15 个有
- `easy imageConcat` —— 2/15 个有
- `CompressImages` —— 1/15 个有
- `Int` —— 1/15 个有
- `Label (rgthree)` —— 1/15 个有
- `PreviewAny` —— 1/15 个有
- `Text Multiline` —— 1/15 个有
- `TextCombinerSix` —— 1/15 个有
- `TextCombinerTwo` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 15 | 100% |
| 高度 | 1024 | 1024 - 1024 | 15 | 100% |
| 采样步数 | 50 | 50 - 50 | 15 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 15 | 100% |
| 采样算法 | euler | - | 15 | 100% |
| 调度器 | simple | - | 15 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 15 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，15 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，15 个样本，取值集中（一致性 100%）
- 采样步数 中位数 50，观测区间 50 - 50，15 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，15 个样本，一致性 100%
- 调度器 最常用 simple，15 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
