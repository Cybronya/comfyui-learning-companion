---
name: unknown_workflow_sampler_unet_vae_202
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.8448
common_nodes: [Anything Everywhere3, CLIPLoader, KSampler, LoadImage, SaveImage, Text, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/qwen2.1去除卡片_2104046325158469633.json, 图片生成/图生图/qwen2.1去除文字_2108072161025019906.json, 图片生成/图生图/qwen2.1去除油腻_2103758229087014913.json, 图片生成/图生图/qwen2.1替换主体_2103386241126457346.json, 图片生成/图生图/qwen2.1自定义修改_2103385944303951873.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_202

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/qwen2.1去除卡片_2104046325158469633.json、图片生成/图生图/qwen2.1去除文字_2108072161025019906.json、图片生成/图生图/qwen2.1去除油腻_2103758229087014913.json、图片生成/图生图/qwen2.1替换主体_2103386241126457346.json、图片生成/图生图/qwen2.1自定义修改_2103385944303951873.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 5 个 workflow 都包含：
- `Anything Everywhere3`
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `Text`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 4/5 个有
- `ImageToMask` —— 3/5 个有
- `PixaromaInpaintCrop` —— 3/5 个有
- `PixaromaUncrop` —— 3/5 个有
- `Image Remove Alpha JK` —— 2/5 个有
- `ImageColorMatch+` —— 2/5 个有
- `LoraLoaderModelOnly` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 25 - 25 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 25 - 25，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
