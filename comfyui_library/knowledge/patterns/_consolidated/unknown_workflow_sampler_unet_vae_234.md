---
name: unknown_workflow_sampler_unet_vae_234
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.6935
common_nodes: [CFGGuider, CLIPLoader, ComfySwitchNode, EmptyLatentImage, KSamplerSelect, LoadImage, ManualSigmas, QwenImage21Cache, RandomNoise, SamplerCustomAdvanced, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Image 2.1 Turbo 图像编辑_2113964550642036738.json, 图片生成/图生图/Qwen Image 2.1 Turbo：图像编辑_2110487180635365378.json, 图片生成/图生图/Qwen Image 2.1-PE-图像编辑-加速版_2108817312836055042.json, 图片生成/图生图/image_qwen_image_2_1_turbo_多参考图加速版版_2113568692574449665.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_234

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Qwen Image 2.1 Turbo 图像编辑_2113964550642036738.json、图片生成/图生图/Qwen Image 2.1 Turbo：图像编辑_2110487180635365378.json、图片生成/图生图/Qwen Image 2.1-PE-图像编辑-加速版_2108817312836055042.json、图片生成/图生图/image_qwen_image_2_1_turbo_多参考图加速版版_2113568692574449665.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：69%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `ComfySwitchNode`
- `EmptyLatentImage`
- `KSamplerSelect`
- `LoadImage`
- `ManualSigmas`
- `QwenImage21Cache`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PrimitiveStringMultiline` —— 3/4 个有
- `SaveImageAdvanced` —— 3/4 个有
- `BatchImagesNode` —— 2/4 个有
- `ImageCompare` —— 2/4 个有
- `PreviewAny` —— 2/4 个有
- `PrimitiveBoolean` —— 2/4 个有
- `TextGenerate` —— 2/4 个有
- `GetNode` —— 1/4 个有
- `JjkText` —— 1/4 个有
- `KSampler` —— 1/4 个有
- `LoraLoaderModelOnly` —— 1/4 个有
- `PathchSageAttentionKJ` —— 1/4 个有
- `PreviewImage` —— 1/4 个有
- `RH_QwenImagePromptEnhancer` —— 1/4 个有
- `ResolutionSelector` —— 1/4 个有
- `SetNode` —— 1/4 个有
- `easy showAnything` —— 1/4 个有
- `忽略多组孤海` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 4 | 100% |
| 高度 | 1024 | 1024 - 1024 | 4 | 100% |
| 采样步数 | 8 | - | 1 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 1 | 100% |
| 采样算法 | euler | - | 1 | 100% |
| 调度器 | simple | - | 1 | 100% |
| 重绘幅度 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，4 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，4 个样本，取值集中（一致性 100%）
