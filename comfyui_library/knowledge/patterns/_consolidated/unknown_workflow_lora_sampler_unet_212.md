---
name: unknown_workflow_lora_sampler_unet_212
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.923667
common_nodes: [CLIPLoader, CR Prompt Text, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelAttentionBackend, PathchSageAttentionKJ, PixaromaLabel, PreviewImage, QwenImage21Cache, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Qwen Image 2.1 扩图专用工作流_2106034671938260993.json, 图片生成/图生图/Qwen Image 2.1 透明图层抠图    手动标记改图专属工作流_2107175001689513986.json, 图片生成/图生图/Qwen Image 2.1 透明图层抠图改图_2108778898052968449.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_212

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Qwen Image 2.1 扩图专用工作流_2106034671938260993.json、图片生成/图生图/Qwen Image 2.1 透明图层抠图    手动标记改图专属工作流_2107175001689513986.json、图片生成/图生图/Qwen Image 2.1 透明图层抠图改图_2108778898052968449.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CR Prompt Text`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelAttentionBackend`
- `PathchSageAttentionKJ`
- `PixaromaLabel`
- `PreviewImage`
- `QwenImage21Cache`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `SaveImageAdvanced` —— 2/3 个有
- `EmptyLatentImage` —— 1/3 个有
- `GetImageSize` —— 1/3 个有
- `ImagePadKJ` —— 1/3 个有
- `TextGenerateLTX2Prompt` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 40 | 40 - 40 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 1024 | - | 1 | 100% |
| 高度 | 1024 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 40，观测区间 40 - 40，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
