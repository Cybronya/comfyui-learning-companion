---
name: unknown_workflow_sampler_unet_vae_243
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.91125
common_nodes: [CLIPLoader, KSampler, LoadImage, QwenImage21Cache, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Qwen2.1图像编辑【透明图专用】_2103544673385140226.json, 图片生成/图生图/Qwen_2.1_角色替换_换人_2114261197271953410.json, 图片生成/图生图/qwen-image-2.1一键抠图_PNG通道_2102319407006572545.json, 图片生成/图生图/qwen-image-2.1多图编辑_2102013603833532417.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_243

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Qwen2.1图像编辑【透明图专用】_2103544673385140226.json、图片生成/图生图/Qwen_2.1_角色替换_换人_2114261197271953410.json、图片生成/图生图/qwen-image-2.1一键抠图_PNG通道_2102319407006572545.json、图片生成/图生图/qwen-image-2.1多图编辑_2102013603833532417.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 4 个 workflow 都包含：
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
- `PreviewImage` —— 2/4 个有
- `SaveImageAdvanced` —— 2/4 个有
- `EmptyImage` —— 1/4 个有
- `LoraLoaderModelOnly` —— 1/4 个有
- `StringConcatenate` —— 1/4 个有
- `StringConstantMultiline` —— 1/4 个有
- `easy seed` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 32.5 | 25 - 40 | 4 | 77% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 32.5，观测区间 25 - 40，4 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
