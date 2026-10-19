---
name: text_to_image_lora_sampler_clip_175
type: Text To Image
frequency: 5
level: weak
coverage: 0.8756
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text, EmptyLatentImage, KSampler, LoraLoaderModelOnly, PreviewAny, SaveImage, UNETLoader, VAEDecode, VAELoader, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Anima base v1.0 文生图 提示词扩写 自动匹配画师_2100427692003913729.json, 图片生成/文生图/Krea2 文生图_2096503316002983938.json, 图片生成/文生图/Krea2模型文生图工作流，高质量文本到图像生成方案_2102885318025371650.json, 图片生成/文生图/Krea2模型文生图工作流，高质量文本到图像生成方案_2105111992758530050.json, 视频生成/文生视频/Krea2模型文生图工作流，高质量文本到图像生成方案_2105111992758530050.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_175

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/Anima base v1.0 文生图 提示词扩写 自动匹配画师_2100427692003913729.json、图片生成/文生图/Krea2 文生图_2096503316002983938.json、图片生成/文生图/Krea2模型文生图工作流，高质量文本到图像生成方案_2102885318025371650.json、图片生成/文生图/Krea2模型文生图工作流，高质量文本到图像生成方案_2105111992758530050.json、视频生成/文生视频/Krea2模型文生图工作流，高质量文本到图像生成方案_2105111992758530050.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：88%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `EmptyLatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `PreviewAny`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 4/5 个有
- `DF_Latent_Scale_to_side` —— 4/5 个有
- `Fast Groups Bypasser (rgthree)` —— 4/5 个有
- `TTResolutionSelector` —— 4/5 个有
- `easy cleanGpuUsed` —— 4/5 个有
- `JjkText` —— 3/5 个有
- `solarL_SaveImagesToZip` —— 3/5 个有
- `EmptyImage` —— 2/5 个有
- `PreviewImage` —— 2/5 个有
- `LayerUtility: ImageReel` —— 1/5 个有
- `LayerUtility: ImageReelComposit` —— 1/5 个有
- `Seed_` —— 1/5 个有
- `孤海注释` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 12 | 5 | 50% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 5 | 45% |
| 采样算法 | er_sde | - | 5 | 100% |
| 调度器 | beta | - | 5 | 60% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 80 | 80 - 1536 | 5 | 0% |
| 高度 | 80 | 80 - 1536 | 5 | 0% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 12，5 个样本
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，5 个样本，取值分散，一致性仅 45%
- 采样算法 最常用 er_sde，5 个样本，一致性 100%
- 调度器 最常用 beta，5 个样本，一致性 60%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 1536，5 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 1536，5 个样本，取值分散，一致性仅 0%
- 高发问题（7/5 个样本）：Steps较低可能导致细节不足
