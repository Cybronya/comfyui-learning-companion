---
name: image_to_image_upscale_lora_sampler_38
type: Image To Image
frequency: 4
level: strong
coverage: 0.6265
common_nodes: [AILab_QwenVL, AILab_QwenVL_PromptEnhancer, Any Switch (rgthree), BasicScheduler, CLIPLoader, CLIPTextEncode, CheckpointLoaderSimple, ConditioningZeroOut, EmptyHiDreamO1LatentImage, Fast Groups Bypasser (rgthree), GetNode, HiDreamO1ReferenceImages, KSampler, LoadImage, LoraLoaderModelOnly, ModelNoiseScale, ModelSamplingAuraFlow, PreviewImage, PrimitiveStringMultiline, SamplerCustom, SamplerLCM, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SetNode, ShowText|pysssss, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Hi-Dream_O1_图生图-图像编辑-9张参考图传入 工作流_2058236406446780418.json, 图片生成/图生图/Hi-Dream_O1_文生图-图像编辑-多参考图（虚拟试穿）三合一 工作流_2057276659350458369.json, 图片生成/文生图/Hi-Dream_O1_文生图-图像编辑-多参考图虚拟试穿三合一_工作流_2098916831623991297.json, 图片生成/文生图/Hi-Dream_O1_文生图-图像编辑-多参考图虚拟试穿三合一_工作流_2098974634644434945.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_38

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Hi-Dream_O1_图生图-图像编辑-9张参考图传入 工作流_2058236406446780418.json、图片生成/图生图/Hi-Dream_O1_文生图-图像编辑-多参考图（虚拟试穿）三合一 工作流_2057276659350458369.json、图片生成/文生图/Hi-Dream_O1_文生图-图像编辑-多参考图虚拟试穿三合一_工作流_2098916831623991297.json、图片生成/文生图/Hi-Dream_O1_文生图-图像编辑-多参考图虚拟试穿三合一_工作流_2098974634644434945.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：63%

## 共有节点

全部 4 个 workflow 都包含：
- `AILab_QwenVL`
- `AILab_QwenVL_PromptEnhancer`
- `Any Switch (rgthree)`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `EmptyHiDreamO1LatentImage`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `HiDreamO1ReferenceImages`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelNoiseScale`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `PrimitiveStringMultiline`
- `SamplerCustom`
- `SamplerLCM`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SetNode`
- `ShowText|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `EmptyImage` —— 2/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | res_2s | - | 4 | 100% |
| 调度器 | bong_tangent | - | 4 | 100% |
| 重绘幅度 | 0.4 | 0.4 - 0.4 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_2s，4 个样本，一致性 100%
- 调度器 最常用 bong_tangent，4 个样本，一致性 100%
- 重绘幅度 中位数 0.4，观测区间 0.4 - 0.4，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
