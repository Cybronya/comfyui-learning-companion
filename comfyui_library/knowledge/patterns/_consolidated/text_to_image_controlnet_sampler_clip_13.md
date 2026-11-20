---
name: text_to_image_controlnet_sampler_clip_13
type: Text To Image
frequency: 4
level: strong
coverage: 0.86575
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, ControlNetLoader, EmptyLatentImage, KSampler, LoadImage, PreviewImage, SaveImage, VAEDecode]
problems: []
missing: []
members: [图片生成/图生图/【遇见AI】SDXL基础文生图+SDXL版ControlNet_2011599378745663490.json, 图片生成/图生图/【遇见AI】SDXL基础文生图+SDXL版Union多合一ControlNet_2012828647471718402.json, 图片生成/图生图/姿态+线条工作流_2001846231892672514.json, 图片生成/图生图/线稿上色_2000880333153333250.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_sampler_clip_13

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/【遇见AI】SDXL基础文生图+SDXL版ControlNet_2011599378745663490.json、图片生成/图生图/【遇见AI】SDXL基础文生图+SDXL版Union多合一ControlNet_2012828647471718402.json、图片生成/图生图/姿态+线条工作流_2001846231892672514.json、图片生成/图生图/线稿上色_2000880333153333250.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ControlNetLoader`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `AIO_Preprocessor` —— 2/4 个有
- `ControlNetApplyAdvanced` —— 2/4 个有
- `ControlNetApplySD3` —— 2/4 个有
- `LineartStandardPreprocessor` —— 2/4 个有
- `DF_Get_image_size` —— 1/4 个有
- `DWPreprocessor` —— 1/4 个有
- `PD_GetImageSize` —— 1/4 个有
- `VAELoader` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 22.5 | 20 - 25 | 4 | 89% |
| Prompt 约束强度(CFG) | 7.25 | 6.5 - 8 | 4 | 90% |
| 采样算法 | euler | - | 4 | 50% |
| 调度器 | normal | - | 4 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 512 | 512 - 512 | 4 | 100% |
| 高度 | 768 | 512 - 1024 | 4 | 67% |
| ControlNet 权重 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 22.5，观测区间 20 - 25，4 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 7.25，观测区间 6.5 - 8，4 个样本，取值集中（一致性 90%）
- 采样算法 最常用 euler，4 个样本，一致性 50%
- 调度器 最常用 normal，4 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 512，观测区间 512 - 512，4 个样本，取值集中（一致性 100%）
- 高度 中位数 768，观测区间 512 - 1024，4 个样本
- ControlNet 权重 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
