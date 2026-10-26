---
name: unknown_workflow_lora_sampler_clip_57
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.923125
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text, EmptySD3LatentImage, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Z-image-base如梦似幻+加速Lora文生图+高清放大_2079925343082864641.json, 图片生成/文生图/Qwen-Image-LLM计算工作流-计算器_2009215925676937218.json, 图片生成/文生图/Z-image-Turbo如梦似幻 加速lora文生图+高清放大_2079024122377629697.json, 图片生成/文生图/Z-image-Turbo如梦似幻 加速lora文生图+高清放大_2079402711237353473.json, 图片生成/文生图/Z-image-Turbo（如梦似幻+瑶光lora）文生图+高清放大_2063598346006253569.json, 图片生成/文生图/Z-image-base如梦似幻+加速Lora文生图+高清放大_2079025904818409473.json, 图片生成/文生图/Z-image-base如梦似幻+加速Lora文生图+高清放大_2079877016463171586.json, 图片生成/文生图/Z-image-base（如梦似幻+瑶光lora）文生图+高清放大_2063588760020930562.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_57

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/Z-image-base如梦似幻+加速Lora文生图+高清放大_2079925343082864641.json、图片生成/文生图/Qwen-Image-LLM计算工作流-计算器_2009215925676937218.json、图片生成/文生图/Z-image-Turbo如梦似幻 加速lora文生图+高清放大_2079024122377629697.json、图片生成/文生图/Z-image-Turbo如梦似幻 加速lora文生图+高清放大_2079402711237353473.json、图片生成/文生图/Z-image-Turbo（如梦似幻+瑶光lora）文生图+高清放大_2063598346006253569.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `EmptySD3LatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: PurgeVRAM` —— 7/8 个有
- `easy getNode` —— 7/8 个有
- `easy setNode` —— 7/8 个有
- `llama_cpp_instruct_adv` —— 7/8 个有
- `llama_cpp_model_loader` —— 7/8 个有
- `Fast Groups Bypasser (rgthree)` —— 6/8 个有
- `SeedVR2LoadDiTModel` —— 6/8 个有
- `SeedVR2LoadVAEModel` —— 6/8 个有
- `SeedVR2VideoUpscaler` —— 6/8 个有
- `ModelSamplingAuraFlow` —— 5/8 个有
- `ConditioningZeroOut` —— 1/8 个有
- `RHHiddenNodes` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 1 - 8 | 8 | 68% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | res_multistep | - | 8 | 88% |
| 调度器 | simple | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 1 - 8，8 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_multistep，8 个样本，一致性 88%
- 调度器 最常用 simple，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（9/8 个样本）：Steps较低可能导致细节不足
