---
name: text_to_image_lora_sampler_clip_303
type: Text To Image
frequency: 7
level: moderate
coverage: 0.799429
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyImage, EmptyLatentImage, INTConstant, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoraLoaderModelOnly, ResolutionSelector, SaveImage, UNETLoader, VAEDecode, VAELoader, easy seed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/MOSS image超细节 生图工作流😼_2111769823528181762.json, 图片生成/文生图/krea2 风格之王 全能模型 deepseekV4自动提示词文生图工作流（自由版）_2070758812876894209.json, 图片生成/文生图/krea2 风格之王 全能模型 gemini自动提示词文生图工作流（自由版）_2070761173187907585.json, 图片生成/文生图/krea2 风格之王 全能模型 文生图工作流（自由版）_2070673954079068162.json, 图片生成/文生图/krea2+Qwen3VL提示词优化文生图_2071171990551097346.json, 平台全量/MOSS image超细节 反推洗图生图工作流😼(qwen3.8版)_2117205252813451265.json, 平台全量/MOSS image超细节 反推洗图生图工作流😼(小鲸鱼版)_2117266045516996609.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_303

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/MOSS image超细节 生图工作流😼_2111769823528181762.json、图片生成/文生图/krea2 风格之王 全能模型 deepseekV4自动提示词文生图工作流（自由版）_2070758812876894209.json、图片生成/文生图/krea2 风格之王 全能模型 gemini自动提示词文生图工作流（自由版）_2070761173187907585.json、图片生成/文生图/krea2 风格之王 全能模型 文生图工作流（自由版）_2070673954079068162.json、图片生成/文生图/krea2+Qwen3VL提示词优化文生图_2071171990551097346.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：80%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyImage`
- `EmptyLatentImage`
- `INTConstant`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoraLoaderModelOnly`
- `ResolutionSelector`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy seed`

**可变部分**（部分 workflow 才有）：
- `PrimitiveStringMultiline` —— 6/7 个有
- `ConditioningZeroOut` —— 5/7 个有
- `Text Multiline` —— 5/7 个有
- `Label (rgthree)` —— 4/7 个有
- `ShowText|pysssss` —— 4/7 个有
- `RH_LLMAPI_Pro_Node` —— 3/7 个有
- `SkipLayerGuidanceDiTSimple` —— 3/7 个有
- `Lable (DaSiWa)` —— 2/7 个有
- `LoadImage` —— 2/7 个有
- `XB_CanvasLabel` —— 2/7 个有
- `llama_cpp_instruct_adv` —— 2/7 个有
- `llama_cpp_model_loader` —— 2/7 个有
- `llama_cpp_parameters` —— 2/7 个有
- `PreviewAny` —— 1/7 个有
- `PreviewImage` —— 1/7 个有
- `Switch any [Crystools]` —— 1/7 个有
- `TextGenerate` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 7 | 100% |
| 高度 | 1536 | 1024 - 1536 | 7 | 81% |
| 采样步数 | 8 | 8 - 25 | 7 | 47% |
| Prompt 约束强度(CFG) | 1 | 1 - 3 | 7 | 43% |
| 采样算法 | dpmpp_2s_ancestral | - | 7 | 43% |
| 调度器 | simple | - | 7 | 57% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，7 个样本，取值集中（一致性 100%）
- 高度 中位数 1536，观测区间 1024 - 1536，7 个样本，取值集中（一致性 81%）
- 采样步数 中位数 8，观测区间 8 - 25，7 个样本，取值分散，一致性仅 47%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3，7 个样本，取值分散，一致性仅 43%
- 采样算法 最常用 dpmpp_2s_ancestral，7 个样本，一致性 43%
- 调度器 最常用 simple，7 个样本，一致性 57%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（4/7 个样本）：Steps较低可能导致细节不足
