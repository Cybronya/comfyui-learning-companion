---
name: unknown_workflow_sampler_unet_vae_97
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.9031
common_nodes: [CLIPLoader, EmptyLatentImage, KSampler, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/自用qwen_image_2.1_image_edit接超分放大工作流_2102129332872372226.json, 图片生成/图生图/角色三视图_Qwen image 2.1_2107299006337601538.json, 图片生成/图生图/角色三视图__2112738425802682369.json, 图片生成/图生图/（短剧）人物3视图_2111246118960062466.json, 图片生成/文生图/BF16小字不崩-Qwen image 2.1图片编辑_2102769559072763906.json, 图片生成/文生图/BF16版小字不崩Qwen image 2.1 文生图_2102282917081862146.json, 图片生成/文生图/QWEN-IMAGE-2.1_2104540875895431170.json, 图片生成/文生图/Qwen Image 2.1去除ai感_2101954709987872770.json, 图片生成/文生图/Qwen-Image-2.1-图生图_2101854452645978114.json, 图片生成/文生图/Qwen_image_2_1_多图编辑_2101885250807877634.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_97

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/自用qwen_image_2.1_image_edit接超分放大工作流_2102129332872372226.json、图片生成/图生图/角色三视图_Qwen image 2.1_2107299006337601538.json、图片生成/图生图/角色三视图__2112738425802682369.json、图片生成/图生图/（短剧）人物3视图_2111246118960062466.json、图片生成/文生图/BF16小字不崩-Qwen image 2.1图片编辑_2102769559072763906.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 9/10 个有
- `ComfySwitchNode` —— 8/10 个有
- `QwenImage21Cache` —— 8/10 个有
- `ResolutionSelector` —— 7/10 个有
- `SaveImageAdvanced` —— 6/10 个有
- `CR Prompt Text` —— 3/10 个有
- `ImageScaleToTotalPixels` —— 3/10 个有
- `ImageStitch` —— 3/10 个有
- `CM_IntToFloat` —— 1/10 个有
- `LoraLoaderModelOnly` —— 1/10 个有
- `PrimitiveInt` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 768 - 1536 | 10 | 83% |
| 高度 | 1024 | 1024 - 2048 | 10 | 71% |
| 采样步数 | 25 | 25 - 50 | 10 | 66% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 10 | 100% |
| 采样算法 | euler | - | 10 | 100% |
| 调度器 | simple | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 768 - 1536，10 个样本，取值集中（一致性 83%）
- 高度 中位数 1024，观测区间 1024 - 2048，10 个样本
- 采样步数 中位数 25，观测区间 25 - 50，10 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，10 个样本，一致性 100%
- 调度器 最常用 simple，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
