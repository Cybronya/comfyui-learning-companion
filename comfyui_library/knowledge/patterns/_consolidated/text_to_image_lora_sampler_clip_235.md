---
name: text_to_image_lora_sampler_clip_235
type: Text To Image
frequency: 5
level: strong
coverage: 0.82
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyImage, EmptyLatentImage, INTConstant, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoraLoaderModelOnly, ResolutionSelector, SaveImage, Text Multiline, UNETLoader, VAEDecode, VAELoader, easy seed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/krea2 风格之王 全能模型 deepseekV4自动提示词文生图工作流（自由版）_2070758812876894209.json, 图片生成/文生图/krea2 风格之王 全能模型 gemini自动提示词文生图工作流（自由版）_2070761173187907585.json, 图片生成/文生图/krea2 风格之王 全能模型 文生图工作流（自由版）_2070673954079068162.json, 图片生成/文生图/krea2+Qwen3VL提示词优化文生图_2071171990551097346.json, 图片生成/文生图/krea2超细节增强 洗图生图2合1工作流（自由切换版）_哈基米版😼_2077326567931473922.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_235

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/krea2 风格之王 全能模型 deepseekV4自动提示词文生图工作流（自由版）_2070758812876894209.json、图片生成/文生图/krea2 风格之王 全能模型 gemini自动提示词文生图工作流（自由版）_2070761173187907585.json、图片生成/文生图/krea2 风格之王 全能模型 文生图工作流（自由版）_2070673954079068162.json、图片生成/文生图/krea2+Qwen3VL提示词优化文生图_2071171990551097346.json、图片生成/文生图/krea2超细节增强 洗图生图2合1工作流（自由切换版）_哈基米版😼_2077326567931473922.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyImage`
- `EmptyLatentImage`
- `INTConstant`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoraLoaderModelOnly`
- `ResolutionSelector`
- `SaveImage`
- `Text Multiline`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy seed`

**可变部分**（部分 workflow 才有）：
- `Label (rgthree)` —— 4/5 个有
- `PrimitiveStringMultiline` —— 4/5 个有
- `RH_LLMAPI_Pro_Node` —— 3/5 个有
- `ShowText|pysssss` —— 3/5 个有
- `ConditioningKrea2Rebalance` —— 1/5 个有
- `LatentUpscaleBy` —— 1/5 个有
- `LoadImage` —— 1/5 个有
- `Switch any [Crystools]` —— 1/5 个有
- `llama_cpp_instruct_adv` —— 1/5 个有
- `llama_cpp_model_loader` —— 1/5 个有
- `llama_cpp_parameters` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 5 | 100% |
| 高度 | 1536 | 1536 - 1536 | 5 | 100% |
| 采样步数 | 8 | 6 - 8 | 5 | 89% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | dpmpp_2s_ancestral | - | 5 | 60% |
| 调度器 | bong_tangent | - | 5 | 60% |
| 重绘幅度 | 1 | 0.4 - 1 | 5 | 73% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，5 个样本，取值集中（一致性 100%）
- 高度 中位数 1536，观测区间 1536 - 1536，5 个样本，取值集中（一致性 100%）
- 采样步数 中位数 8，观测区间 6 - 8，5 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_2s_ancestral，5 个样本，一致性 60%
- 调度器 最常用 bong_tangent，5 个样本，一致性 60%
- 重绘幅度 中位数 1，观测区间 0.4 - 1，5 个样本
- 高发问题（6/5 个样本）：Steps较低可能导致细节不足
