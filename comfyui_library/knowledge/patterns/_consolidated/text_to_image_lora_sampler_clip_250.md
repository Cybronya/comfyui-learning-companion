---
name: text_to_image_lora_sampler_clip_250
type: Text To Image
frequency: 7
level: weak
coverage: 0.867143
common_nodes: [AIO_Preprocessor, CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, LoadImage, LoraLoaderModelOnly, ModelPatchLoader, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/30.tonnie-Qwen image -Cn控制和重绘_2001784908882276353.json, 图片生成/图生图/87time # 36 Qwen CN 控制_1959935600843501569.json, 图片生成/图生图/Anima -深度控制动漫生成_2061785993358954498.json, 图片生成/图生图/Anima -线条控制动漫生成_2061793535317331970.json, 图片生成/图生图/Anima正式版-图生图工作流-反推提示词_2056974464365187073.json, 图片生成/图生图/Anima正式版-图生图工作流-反推提示词_2088250786076782594.json, 图片生成/图生图/Anima正式版图生图反推提示词-动漫角色美少女工作流_2087397362699427841.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_250

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/30.tonnie-Qwen image -Cn控制和重绘_2001784908882276353.json、图片生成/图生图/87time # 36 Qwen CN 控制_1959935600843501569.json、图片生成/图生图/Anima -深度控制动漫生成_2061785993358954498.json、图片生成/图生图/Anima -线条控制动漫生成_2061793535317331970.json、图片生成/图生图/Anima正式版-图生图工作流-反推提示词_2056974464365187073.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：87%

## 共有节点

全部 7 个 workflow 都包含：
- `AIO_Preprocessor`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelPatchLoader`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 6/7 个有
- `AnimaLLLiteApply` —— 5/7 个有
- `CR Prompt Text` —— 5/7 个有
- `ShowText|pysssss` —— 5/7 个有
- `Fast Groups Bypasser (rgthree)` —— 4/7 个有
- `ModelSamplingAuraFlow` —— 4/7 个有
- `Image Comparer (rgthree)` —— 3/7 个有
- `JoinStringMulti` —— 3/7 个有
- `LayerUtility: PurgeVRAM V2` —— 3/7 个有
- `PainterFluxImageEdit` —— 3/7 个有
- `RH_LLMAPI_Pro_Node` —— 3/7 个有
- `easy imageColorMatch` —— 3/7 个有
- `QwenImageDiffsynthControlnet` —— 2/7 个有
- `llama_cpp_instruct_adv` —— 2/7 个有
- `llama_cpp_model_loader` —— 2/7 个有
- `JjkText` —— 1/7 个有
- `Mask Fill Holes` —— 1/7 个有
- `solarL_SaveImagesToZip` —— 1/7 个有
- `孤海注释` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 720 | 80 - 1024 | 7 | 57% |
| 高度 | 1280 | 80 - 1536 | 7 | 51% |
| 采样步数 | 8 | 4 - 8 | 7 | 69% |
| Prompt 约束强度(CFG) | 1 | 1 - 4.5 | 7 | 18% |
| 采样算法 | er_sde | - | 7 | 43% |
| 调度器 | beta | - | 7 | 57% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 720，观测区间 80 - 1024，7 个样本
- 高度 中位数 1280，观测区间 80 - 1536，7 个样本
- 采样步数 中位数 8，观测区间 4 - 8，7 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4.5，7 个样本，取值分散，一致性仅 18%
- 采样算法 最常用 er_sde，7 个样本，一致性 43%
- 调度器 最常用 beta，7 个样本，一致性 57%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（9/7 个样本）：Steps较低可能导致细节不足
