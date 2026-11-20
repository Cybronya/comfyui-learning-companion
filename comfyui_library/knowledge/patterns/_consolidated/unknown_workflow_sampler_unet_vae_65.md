---
name: unknown_workflow_sampler_unet_vae_65
type: Unknown Workflow
frequency: 14
level: strong
coverage: 0.889714
common_nodes: [CLIPLoader, EmptyLatentImage, KSampler, QwenImage21Cache, ResolutionSelector, SaveImage, TextEncodeQwenImage21, TextGenerateLTX2Prompt, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/【API】Qwen-Image2.1图像编辑（提示词反推）_2111987132129701889.json, 图片生成/图生图/一键扩图！电商必备！超快！_2103068831634771970.json, 图片生成/图生图/多图编辑 Multi-Image Editing Qwen+Image+2.1_2102556544050225153.json, 图片生成/图生图/多图编辑 Multi-Image Editing Qwen+Image+2.1_2105647767073935362.json, 图片生成/图生图/多图编辑 Multi-Image Editing Qwen+Image+2.1_2105680844940734465.json, 图片生成/图生图/换头换脸Face+Swap++Qwen-Image-2.1模特换头+换脸_2104737905183903746.json, 图片生成/图生图/换头换脸Face+Swap++Qwen-Image-2.1模特换头+换脸_2105235774793928705.json, 图片生成/图生图/换头换脸Face+Swap++Qwen-Image-2.1模特换头+换脸_2105274061088706562.json, 图片生成/图生图/换头换脸Face+Swap++Qwen-Image-2.1模特换头+换脸_2111625667644317697.json, 图片生成/图生图/换脸Face+Swap++Qwen-Image-2.1模特换头+换脸_2102936104516280321.json, 图片生成/图生图/模特换装 Model Outfit Changes Qwen+Image+2.1+图片换装_2105094118673309698.json, 图片生成/文生图/Qwen Image 2.1多图编辑多人合成合照单人合成_2108894186039762945.json, 图片生成/文生图/【API】Qwen-Image2.1文生图（提示词反推）_2111987215688622081.json, 视频生成/图生视频/换头换脸Face+Swap++Qwen-Image-2.1模特换头+换脸_2115289142136492033.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_65

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/图生图/【API】Qwen-Image2.1图像编辑（提示词反推）_2111987132129701889.json、图片生成/图生图/一键扩图！电商必备！超快！_2103068831634771970.json、图片生成/图生图/多图编辑 Multi-Image Editing Qwen+Image+2.1_2102556544050225153.json、图片生成/图生图/多图编辑 Multi-Image Editing Qwen+Image+2.1_2105647767073935362.json、图片生成/图生图/多图编辑 Multi-Image Editing Qwen+Image+2.1_2105680844940734465.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 14 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `QwenImage21Cache`
- `ResolutionSelector`
- `SaveImage`
- `TextEncodeQwenImage21`
- `TextGenerateLTX2Prompt`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `BatchImagesNode` —— 13/14 个有
- `ComfySwitchNode` —— 13/14 个有
- `LoadImage` —— 13/14 个有
- `JjkText` —— 12/14 个有
- `easy imageConcat` —— 4/14 个有
- `CR Prompt Text` —— 2/14 个有
- `PlaySound|pysssss` —— 2/14 个有
- `easy cleanGpuUsed` —— 2/14 个有
- `Label (rgthree)` —— 1/14 个有
- `easy showAnything` —— 1/14 个有
- `孤海注释` —— 1/14 个有
- `忽略多组孤海` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 50 | 40 - 50 | 14 | 93% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 14 | 100% |
| 采样算法 | euler | - | 14 | 100% |
| 调度器 | simple | - | 14 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 14 | 100% |
| 宽度 | 1024 | 1024 - 1024 | 14 | 100% |
| 高度 | 1024 | 1024 - 1024 | 14 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 50，观测区间 40 - 50，14 个样本，取值集中（一致性 93%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，14 个样本，一致性 100%
- 调度器 最常用 simple，14 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 1024 - 1024，14 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，14 个样本，取值集中（一致性 100%）
