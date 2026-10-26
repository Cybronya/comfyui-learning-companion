---
name: text_to_image_lora_sampler_clip_331
type: Text To Image
frequency: 6
level: strong
coverage: 0.908167
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoraLoaderModelOnly, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/LLaDA Image Base图像编辑 一句话改图方案_2108973949999730689.json, 图片生成/图生图/Qwen image 2.1多参考生图 短剧分镜8步加速处理工具_2113027948751183873.json, 图片生成/图生图/Qwen image 2.1多参考生图｜短剧分镜制作专用8步加速版_2112827913790906370.json, 图片生成/文生图/LLaDA Image文生图全扩散架构 全参数扩散模型图像生成_2098692650353385474.json, 图片生成/文生图/Qwen Image 2.1 Turbo文生图工作流，指令生图速度快质量高_2114481503345405954.json, 图片生成/文生图/Qwen Image 2.1 Turbo文生图｜一句话生成高质量图片_2114173392453722113.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_331

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/LLaDA Image Base图像编辑 一句话改图方案_2108973949999730689.json、图片生成/图生图/Qwen image 2.1多参考生图 短剧分镜8步加速处理工具_2113027948751183873.json、图片生成/图生图/Qwen image 2.1多参考生图｜短剧分镜制作专用8步加速版_2112827913790906370.json、图片生成/文生图/LLaDA Image文生图全扩散架构 全参数扩散模型图像生成_2098692650353385474.json、图片生成/文生图/Qwen Image 2.1 Turbo文生图工作流，指令生图速度快质量高_2114481503345405954.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 6 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `QwenImage21Cache` —— 4/6 个有
- `TextEncodeQwenImage21` —— 4/6 个有
- `LoadImage` —— 3/6 个有
- `BasicScheduler` —— 2/6 个有
- `ExtendIntermediateSigmas` —— 2/6 个有
- `ManualSigmas` —— 2/6 个有
- `ResolutionSelector` —— 2/6 个有
- `T8LLaDAImageCheckpointLoader` —— 2/6 个有
- `T8LLaDAImageScheduler` —— 2/6 个有
- `EmptyFlux2LatentImage` —— 1/6 个有
- `FluxKontextImageScale` —— 1/6 个有
- `PrimitiveInt` —— 1/6 个有
- `PrimitiveStringMultiline` —— 1/6 个有
- `T8LLaDAImageEditConditioning` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 6 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 6 | 100% |
| 采样算法 | er_sde | - | 6 | 100% |
| 调度器 | beta | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 80 | 80 - 80 | 6 | 100% |
| 高度 | 80 | 80 - 80 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，6 个样本，一致性 100%
- 调度器 最常用 beta，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足
