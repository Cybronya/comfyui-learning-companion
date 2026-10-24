---
name: unknown_workflow_sampler_unet_vae_50
type: Unknown Workflow
frequency: 14
level: moderate
coverage: 0.950357
common_nodes: [CLIPLoader, KSampler, LoadImage, QwenImage21Cache, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Qwe Image 2.1 多维运镜与构图变换（附控制指南）_2110310238359478273.json, 图片生成/图生图/Qwen 2.1 角色替换_换人_2104554592607494145.json, 图片生成/图生图/Qwen 2.1改头换面_换头术_2104553221795696641.json, 图片生成/图生图/Qwen Image 2.1 图片清晰度增强与细节修复 V1_2108522729849843713.json, 图片生成/图生图/Qwen Image 2.1 图片清晰度增强与细节修复 V2_2108531794294435842.json, 图片生成/图生图/Qwen Image 2.1 导演下一个镜头i_2108579867628494850.json, 图片生成/图生图/Qwen-Image-2.1 一键抠图｜透明背景｜自动识别主体 _ 电商产品照_2103702044094853121.json, 图片生成/图生图/Qwen-Image-2.1 图像编辑（最新模型）_2112762662135353346.json, 图片生成/图生图/qwen-image-2.1图生图_2101823764827828226.json, 图片生成/图生图/qwen-image-2.1图生图（三套夏装)_2107744199545278466.json, 图片生成/图生图/（10图）qwen-image-2.1多图编辑_2107971848804855810.json, 图片生成/文生图/AI生图编辑丨Qwen-Image 2.1丨多图参考·智能提示词老邵_2108408117536059393.json, 图片生成/文生图/AI生图编辑丨Qwen-Image 2.1丨多图参考·智能提示词老邵_2108416050982375426.json, 图片生成/文生图/Qwen Image2.1 图生图任意角度转换双图版_2105241162926878722.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_50

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/图生图/Qwe Image 2.1 多维运镜与构图变换（附控制指南）_2110310238359478273.json、图片生成/图生图/Qwen 2.1 角色替换_换人_2104554592607494145.json、图片生成/图生图/Qwen 2.1改头换面_换头术_2104553221795696641.json、图片生成/图生图/Qwen Image 2.1 图片清晰度增强与细节修复 V1_2108522729849843713.json、图片生成/图生图/Qwen Image 2.1 图片清晰度增强与细节修复 V2_2108531794294435842.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 14 个 workflow 都包含：
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
- `CR Text` —— 9/14 个有
- `LoraLoaderModelOnly` —— 7/14 个有
- `Image Comparer (rgthree)` —— 4/14 个有
- `SeedNode` —— 4/14 个有
- `SplitImageWithAlpha` —— 4/14 个有
- `RHHiddenNodes` —— 2/14 个有
- `TextInput_` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 20 - 40 | 14 | 78% |
| Prompt 约束强度(CFG) | 1 | 1 - 3 | 14 | 43% |
| 采样算法 | euler | - | 14 | 100% |
| 调度器 | simple | - | 14 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 14 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 20 - 40，14 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3，14 个样本，取值分散，一致性仅 43%
- 采样算法 最常用 euler，14 个样本，一致性 100%
- 调度器 最常用 simple，14 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
