---
name: unknown_workflow_sampler_unet_vae_236
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.879
common_nodes: [CLIPLoader, EmptyLatentImage, KSampler, ResolutionSelector, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/透明素材生成丨Qwen Image 2.1丨文生图·透明PNG_2112093151107305474.json, 平台全量/09-image2.1文生图系列图_2119365576085827586.json, 平台全量/Qwen Image 2.1 文生图标准版_2119323345215901697.json, 平台全量/封面设计自用_2117821998381486082.json, 平台全量/封面设计自用_2117897593035513858.json, 数字人/数字人/qwen_image_2_1_角色三视图生成(自定义服装)_2108073982967762946.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_236

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/透明素材生成丨Qwen Image 2.1丨文生图·透明PNG_2112093151107305474.json、平台全量/09-image2.1文生图系列图_2119365576085827586.json、平台全量/Qwen Image 2.1 文生图标准版_2119323345215901697.json、平台全量/封面设计自用_2117821998381486082.json、平台全量/封面设计自用_2117897593035513858.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `ResolutionSelector`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `JjkText` —— 3/6 个有
- `LoraLoaderModelOnly` —— 2/6 个有
- `LoadImage` —— 1/6 个有
- `MaskToImage` —— 1/6 个有
- `PrimitiveStringMultiline` —— 1/6 个有
- `SplitImageWithAlpha` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1088 | 6 | 98% |
| 高度 | 1024 | 1024 - 1920 | 6 | 72% |
| 采样步数 | 25 | 25 - 50 | 6 | 70% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1088，6 个样本，取值集中（一致性 98%）
- 高度 中位数 1024，观测区间 1024 - 1920，6 个样本
- 采样步数 中位数 25，观测区间 25 - 50，6 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
