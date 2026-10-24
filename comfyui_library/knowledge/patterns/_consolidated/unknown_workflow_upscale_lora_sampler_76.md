---
name: unknown_workflow_upscale_lora_sampler_76
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.771
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptySD3LatentImage, FloatConstant, GetImageSize, INTConstant, Image Comparer (rgthree), ImageScaleToTotalPixels, JoinStrings, KSampler, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, RunningHub Deepcleaner, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SimpleMath+, Text, UNETLoader, UltimateSDUpscale, UpscaleModelLoader, VAEDecode, VAELoader, WujiCleaner, ttN seed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/【楚心钟陌】Zimage base lora 另外一个少女_2034684945469284353.json, 图片生成/文生图/【楚心钟陌】Zimage base lora 好看的少女_2034022373820735489.json, 图片生成/文生图/【楚心钟陌】Zimage base lora 这个脸不错，这个脸确实不错_2034708254667841537.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_76

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/【楚心钟陌】Zimage base lora 另外一个少女_2034684945469284353.json、图片生成/文生图/【楚心钟陌】Zimage base lora 好看的少女_2034022373820735489.json、图片生成/文生图/【楚心钟陌】Zimage base lora 这个脸不错，这个脸确实不错_2034708254667841537.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：77%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptySD3LatentImage`
- `FloatConstant`
- `GetImageSize`
- `INTConstant`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `JoinStrings`
- `KSampler`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `RunningHub Deepcleaner`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SimpleMath+`
- `Text`
- `UNETLoader`
- `UltimateSDUpscale`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAELoader`
- `WujiCleaner`
- `ttN seed`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler_ancestral_cfg_pp | - | 3 | 100% |
| 调度器 | bong_tangent | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral_cfg_pp，3 个样本，一致性 100%
- 调度器 最常用 bong_tangent，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
