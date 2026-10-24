---
name: text_to_image_video_upscale_lora_4
type: Text To Image
frequency: 6
level: weak
coverage: 0.824333
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, CR Prompt Text, CR Text, ComfyMathExpression, ComfySwitchNode, EmptyLatentImage, Fast Groups Bypasser (rgthree), INTConstant, Image Comparer (rgthree), ImageScaleToTotalPixels, KSampler, KSamplerSelect, LoadImage, LoraLoaderBypassModelOnly, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, ModelAttentionBackend, PreviewImage, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SolAttnMiniMax, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Work-Fisher出品AI短剧制作全流程｜热门IP一键改编_2111070378704596993.json, 图片生成/文生图/AI短剧制作全流程工作流｜文生图到图生视频一条龙｜短剧创作省心方案_2112118425899323393.json, 图片生成/文生图/AI短剧制作全流程视频_2111655145577734145.json, 视频生成/图生视频/【Gensor】AI短剧制作工具合集工作流_2111079570249183234.json, 视频生成/图生视频/【Work-Fisher】AI短剧制作全流程_2109735475824123905.json, 视频生成/图生视频/【创客训练营】AI短剧制作全流程_2110597688004792322.json]
source: knowledge_consolidation
---

# text_to_image_video_upscale_lora_4

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Work-Fisher出品AI短剧制作全流程｜热门IP一键改编_2111070378704596993.json、图片生成/文生图/AI短剧制作全流程工作流｜文生图到图生视频一条龙｜短剧创作省心方案_2112118425899323393.json、图片生成/文生图/AI短剧制作全流程视频_2111655145577734145.json、视频生成/图生视频/【Gensor】AI短剧制作工具合集工作流_2111079570249183234.json、视频生成/图生视频/【Work-Fisher】AI短剧制作全流程_2109735475824123905.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：82%

## 共有节点

全部 6 个 workflow 都包含：
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

**可变部分**（部分 workflow 才有）：
- `忽略多组孤海` —— 4/6 个有
- `JjkText` —— 2/6 个有
- `solarL_SaveImagesToZip` —— 2/6 个有
- `孤海注释` —— 2/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1080 | 80 - 1080 | 6 | 37% |
| 高度 | 1920 | 80 - 1920 | 6 | 34% |
| 采样步数 | 8 | 4 - 8 | 6 | 72% |
| Prompt 约束强度(CFG) | 1 | 1 - 4.5 | 6 | 24% |
| 采样算法 | res_2s_ode | - | 6 | 67% |
| 调度器 | kl_optimal | - | 6 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 14/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1080，观测区间 80 - 1080，6 个样本，取值分散，一致性仅 37%
- 高度 中位数 1920，观测区间 80 - 1920，6 个样本，取值分散，一致性仅 34%
- 采样步数 中位数 8，观测区间 4 - 8，6 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4.5，6 个样本，取值分散，一致性仅 24%
- 采样算法 最常用 res_2s_ode，6 个样本，一致性 67%
- 调度器 最常用 kl_optimal，6 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（14/6 个样本）：Steps较低可能导致细节不足
