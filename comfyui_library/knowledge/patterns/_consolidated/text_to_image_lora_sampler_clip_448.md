---
name: text_to_image_lora_sampler_clip_448
type: Text To Image
frequency: 4
level: strong
coverage: 0.85725
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/H3_MAX智能运镜AI看图自动运镜图生图处理工作流_2101761496228388866.json, 图片生成/图生图/Image2.5高精度图生图处理生成工具_2100287923240398849.json, 图片生成/图生图/MOSS Text to Image 2K Turbo 文生图图生图极速工具_2114119482594648066.json, 图片生成/图生图/Qwen Image 2.1 IN 极速版全能编辑，2K超清透明通道十图极限融合_2103213714240528385.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_448

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/H3_MAX智能运镜AI看图自动运镜图生图处理工作流_2101761496228388866.json、图片生成/图生图/Image2.5高精度图生图处理生成工具_2100287923240398849.json、图片生成/图生图/MOSS Text to Image 2K Turbo 文生图图生图极速工具_2114119482594648066.json、图片生成/图生图/Qwen Image 2.1 IN 极速版全能编辑，2K超清透明通道十图极限融合_2103213714240528385.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `EmptyImage` —— 3/4 个有
- `LoadImage` —— 3/4 个有
- `ResolutionSelector` —— 2/4 个有
- `EmptyFlux2LatentImage` —— 1/4 个有
- `ImageCompositeMasked` —— 1/4 个有
- `ImageResizeKJv2` —— 1/4 个有
- `PrimitiveStringMultiline` —— 1/4 个有
- `RH_MinimaxHailuoH3ContextIrMultimodal` —— 1/4 个有
- `RH_MinimaxHailuoH3MaxImageToVideo` —— 1/4 个有
- `RH_RhartImageG25SunburstImageToImage` —— 1/4 个有
- `SaveVideo` —— 1/4 个有
- `TextEncodeQwenImage21` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 4 | 100% |
| 采样算法 | er_sde | - | 4 | 100% |
| 调度器 | beta | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 80 | 80 - 80 | 4 | 100% |
| 高度 | 80 | 80 - 80 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，4 个样本，一致性 100%
- 调度器 最常用 beta，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高发问题（5/4 个样本）：Steps较低可能导致细节不足
