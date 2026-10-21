---
name: text_to_image_sampler_clip_unet_103
type: Text To Image
frequency: 4
level: strong
coverage: 0.733
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, Fast Groups Bypasser (rgthree), KSampler, ModelSamplingAuraFlow, PrimitiveFloat, PrimitiveInt, SaveImage, Text Multiline, UNETLoader, VAEDecode, VAELoader, llama_cpp_instruct_adv, llama_cpp_model_loader]
problems: []
missing: []
members: [图片生成/文生图/Anima三兄弟工作流_2094991229678342145.json, 图片生成/文生图/Anima全家桶工作流_2075594450092511234.json, 图片生成/文生图/Anima怀旧暗黑动漫风格工作流_2058173254162010113.json, 数字人/数字人/自用日漫_2097889656049332225.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_103

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/Anima三兄弟工作流_2094991229678342145.json、图片生成/文生图/Anima全家桶工作流_2075594450092511234.json、图片生成/文生图/Anima怀旧暗黑动漫风格工作流_2058173254162010113.json、数字人/数字人/自用日漫_2097889656049332225.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：73%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `KSampler`
- `ModelSamplingAuraFlow`
- `PrimitiveFloat`
- `PrimitiveInt`
- `SaveImage`
- `Text Multiline`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`

**可变部分**（部分 workflow 才有）：
- `JjkShowText` —— 3/4 个有
- `ComfyMathExpression` —— 2/4 个有
- `LoraLoaderModelOnly` —— 2/4 个有
- `ResolutionSelector` —— 2/4 个有
- `Text` —— 2/4 个有
- `Text to String` —— 2/4 个有
- `CheckpointLoaderSimple` —— 1/4 个有
- `easy showAnything` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 30 - 30 | 4 | 100% |
| Prompt 约束强度(CFG) | 4 | 4 - 4 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 896 | 896 - 896 | 4 | 100% |
| 高度 | 1152 | 1152 - 1152 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 30，观测区间 30 - 30，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 896，观测区间 896 - 896，4 个样本，取值集中（一致性 100%）
- 高度 中位数 1152，观测区间 1152 - 1152，4 个样本，取值集中（一致性 100%）
