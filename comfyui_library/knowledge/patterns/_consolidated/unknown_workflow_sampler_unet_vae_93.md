---
name: unknown_workflow_sampler_unet_vae_93
type: Unknown Workflow
frequency: 10
level: strong
coverage: 0.9467
common_nodes: [CLIPLoader, KSampler, LoadImage, QwenImage21Cache, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Qwe Image 2.1 多维运镜与构图变换（附控制指南）_2110310238359478273.json, 图片生成/图生图/Qwen 2.1 角色替换_换人_2104554592607494145.json, 图片生成/图生图/Qwen 2.1改头换面_换头术_2104553221795696641.json, 图片生成/图生图/Qwen Image 2.1 图片清晰度增强与细节修复 V1_2108522729849843713.json, 图片生成/图生图/Qwen Image 2.1 图片清晰度增强与细节修复 V2_2108531794294435842.json, 图片生成/图生图/Qwen Image 2.1 导演下一个镜头i_2108579867628494850.json, 图片生成/图生图/Qwen-Image 2.1 重磅升级：一键抠图直出 PNG，无缝重塑图像工作流！_2106021474862723074.json, 图片生成/图生图/Qwen-Image-2.1 一键抠图｜透明背景｜自动识别主体 _ 电商产品照_2103702044094853121.json, 图片生成/图生图/Qwen-Image-2.1 图像编辑（最新模型）_2112762662135353346.json, 图片生成/图生图/Qwen-Image-2.1 图像编辑（最新模型）_2113099904515137538.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_93

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/Qwe Image 2.1 多维运镜与构图变换（附控制指南）_2110310238359478273.json、图片生成/图生图/Qwen 2.1 角色替换_换人_2104554592607494145.json、图片生成/图生图/Qwen 2.1改头换面_换头术_2104553221795696641.json、图片生成/图生图/Qwen Image 2.1 图片清晰度增强与细节修复 V1_2108522729849843713.json、图片生成/图生图/Qwen Image 2.1 图片清晰度增强与细节修复 V2_2108531794294435842.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：95%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `QwenImage21Cache`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 6/10 个有
- `Image Comparer (rgthree)` —— 5/10 个有
- `CR Text` —— 4/10 个有
- `SeedNode` —— 4/10 个有
- `SplitImageWithAlpha` —— 4/10 个有
- `RHHiddenNodes` —— 3/10 个有
- `TextInput_` —— 2/10 个有
- `SaveImageAdvanced` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 25 - 40 | 10 | 79% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 10 | 100% |
| 采样算法 | euler | - | 10 | 100% |
| 调度器 | simple | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 25 - 40，10 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，10 个样本，一致性 100%
- 调度器 最常用 simple，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
