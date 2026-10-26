---
name: unknown_workflow_sampler_unet_vae_78
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.864182
common_nodes: [CLIPLoader, EmptyLatentImage, KSampler, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/image_qwen_image_2_1_t2i_2101968376938717186.json, 图片生成/文生图/image_qwen_image_2_1_t2i_2102665438198059010.json, 图片生成/文生图/qwen image 2.1文生图_2094967170106216450.json, 图片生成/文生图/qwen-image-2.1文生图_2102011026517614593.json, 图片生成/文生图/qwen-image-2.1文生图｜高效创作，一键生图_2105572911326261250.json, 图片生成/文生图/qwen-image2.1-文生图_2101865085642825729.json, 图片生成/文生图/qwen-image2.1-文生图_2105123427295252481.json, 图片生成/文生图/qwen-image2.1-文生图_2105500926474801154.json, 图片生成/文生图/qwen2.1 文生图_2102025901952299009.json, 图片生成/文生图/文生图_qwenimage2.1_2101826399211446273.json, 数字人/数字人/Qwen Image 2.1 文生图 T2I_2101822255830495234.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_78

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/文生图/image_qwen_image_2_1_t2i_2101968376938717186.json、图片生成/文生图/image_qwen_image_2_1_t2i_2102665438198059010.json、图片生成/文生图/qwen image 2.1文生图_2094967170106216450.json、图片生成/文生图/qwen-image-2.1文生图_2102011026517614593.json、图片生成/文生图/qwen-image-2.1文生图｜高效创作，一键生图_2105572911326261250.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ResolutionSelector` —— 9/11 个有
- `TextGenerateLTX2Prompt` —— 8/11 个有
- `SaveImageAdvanced` —— 7/11 个有
- `PreviewAny` —— 4/11 个有
- `PrimitiveStringMultiline` —— 4/11 个有
- `easy showAnything` —— 3/11 个有
- `ComfySwitchNode` —— 1/11 个有
- `RH_LLMAPI_Pro_Node` —— 1/11 个有
- `Text Multiline` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 768 - 2048 | 11 | 72% |
| 高度 | 1024 | 1024 - 2048 | 11 | 69% |
| 采样步数 | 25 | 25 - 50 | 11 | 69% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 11 | 100% |
| 采样算法 | euler | - | 11 | 100% |
| 调度器 | simple | - | 11 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 768 - 2048，11 个样本
- 高度 中位数 1024，观测区间 1024 - 2048，11 个样本
- 采样步数 中位数 25，观测区间 25 - 50，11 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，11 个样本，一致性 100%
- 调度器 最常用 simple，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
