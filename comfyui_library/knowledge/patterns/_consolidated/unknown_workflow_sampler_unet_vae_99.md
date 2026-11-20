---
name: unknown_workflow_sampler_unet_vae_99
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.699364
common_nodes: [CLIPLoader, KSampler, QwenImage21Cache, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Qwen image 2.1图片编辑-1图_2112357928580763649.json, 图片生成/图生图/Qwen image 2.1图片编辑-2图_2112352357722972162.json, 图片生成/图生图/Qwen image 2.1图片编辑-3图_2112358020758990850.json, 图片生成/图生图/Qwen image 2.1图片编辑-4图_2112358074219581441.json, 图片生成/图生图/Qwen image 2.1图片编辑-5图_2112359254878412802.json, 图片生成/图生图/Qwen image 2.1图片编辑-6图_2112359295756099586.json, 图片生成/图生图/Qwen-Image 2.1 重磅升级：一键抠图直出 PNG，无缝重塑图像工作流！_2106021474862723074.json, 图片生成/图生图/Qwen-Image 2.1：生图、改图、拼图，一个模型全搞定_2102215048675545090.json, 图片生成/图生图/Qwen-Image-2.1 图像编辑，最多 10 张参考图，图生图_2103753279908966401.json, 图片生成/图生图/QwenImage2.1-图像编辑换头_2101872643862523905.json, 图片生成/图生图/qwen image 2.1 编辑_2101987550209593345.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_99

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/Qwen image 2.1图片编辑-1图_2112357928580763649.json、图片生成/图生图/Qwen image 2.1图片编辑-2图_2112352357722972162.json、图片生成/图生图/Qwen image 2.1图片编辑-3图_2112358020758990850.json、图片生成/图生图/Qwen image 2.1图片编辑-4图_2112358074219581441.json、图片生成/图生图/Qwen image 2.1图片编辑-5图_2112359254878412802.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：70%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
- `KSampler`
- `QwenImage21Cache`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ComfySwitchNode` —— 10/11 个有
- `EmptyLatentImage` —— 10/11 个有
- `PrimitiveStringMultiline` —— 9/11 个有
- `SaveImageAdvanced` —— 9/11 个有
- `Int` —— 6/11 个有
- `SDVN Load Image Url` —— 6/11 个有
- `LoadImage` —— 5/11 个有
- `ResolutionSelector` —— 4/11 个有
- `BatchImagesNode` —— 3/11 个有
- `Fast Groups Bypasser (rgthree)` —— 3/11 个有
- `TextGenerateLTX2Prompt` —— 3/11 个有
- `GetNode` —— 2/11 个有
- `SetNode` —— 2/11 个有
- `ImageConcatMulti` —— 1/11 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/11 个有
- `Text` —— 1/11 个有
- `孤海注释` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 50 | 25 - 50 | 11 | 74% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 11 | 100% |
| 采样算法 | euler | - | 11 | 100% |
| 调度器 | simple | - | 11 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |
| 宽度 | 16 | 16 - 1024 | 10 | 0% |
| 高度 | 1024 | 1024 - 1024 | 10 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 50，观测区间 25 - 50，11 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，11 个样本，一致性 100%
- 调度器 最常用 simple，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 宽度 中位数 16，观测区间 16 - 1024，10 个样本，取值分散，一致性仅 0%
- 高度 中位数 1024，观测区间 1024 - 1024，10 个样本，取值集中（一致性 100%）
