---
name: text_to_image_video_upscale_lora_4
type: Text To Image
frequency: 3
level: strong
coverage: 0.811
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, CR Prompt Text, CR Text, ComfyMathExpression, ComfySwitchNode, EmptyLatentImage, Fast Groups Bypasser (rgthree), INTConstant, Image Comparer (rgthree), ImageScaleToTotalPixels, KSampler, KSamplerSelect, LoadImage, LoraLoaderBypassModelOnly, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, ModelAttentionBackend, PreviewImage, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SolAttnMiniMax, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine, 忽略多组孤海]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/【Gensor】AI短剧制作工具合集工作流_2111079570249183234.json, 视频生成/图生视频/【Work-Fisher】AI短剧制作全流程_2109735475824123905.json, 视频生成/图生视频/【创客训练营】AI短剧制作全流程_2110597688004792322.json]
source: knowledge_consolidation
---

# text_to_image_video_upscale_lora_4

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/【Gensor】AI短剧制作工具合集工作流_2111079570249183234.json、视频生成/图生视频/【Work-Fisher】AI短剧制作全流程_2109735475824123905.json、视频生成/图生视频/【创客训练营】AI短剧制作全流程_2110597688004792322.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `CR Text`
- `ComfyMathExpression`
- `ComfySwitchNode`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `INTConstant`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderBypassModelOnly`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `ModelAttentionBackend`
- `PreviewImage`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SolAttnMiniMax`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`
- `忽略多组孤海`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1080 | 1080 - 1080 | 3 | 100% |
| 高度 | 1920 | 1920 - 1920 | 3 | 100% |
| 采样步数 | 8 | 8 - 8 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | res_2s_ode | - | 3 | 100% |
| 调度器 | kl_optimal | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1080，观测区间 1080 - 1080，3 个样本，取值集中（一致性 100%）
- 高度 中位数 1920，观测区间 1920 - 1920，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 8，观测区间 8 - 8，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_2s_ode，3 个样本，一致性 100%
- 调度器 最常用 kl_optimal，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（6/3 个样本）：Steps较低可能导致细节不足
