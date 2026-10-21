---
name: unknown_workflow_lora_sampler_clip_22
type: Unknown Workflow
frequency: 10
level: strong
coverage: 0.793
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, INTConstant, JoinStrings, KSampler, LoadImage, LoraLoaderModelOnly, PreviewImage, SaveImage, Text, UNETLoader, VAEDecode, VAELoader, easy cleanGpuUsed, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_unload_model]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/【楚心钟陌】BBBS风格，懒人图片提示词反推_2025122219109650434.json, 图片生成/文生图/【楚心钟陌】Leo画风，文生_2024094855894405121.json, 图片生成/文生图/【楚心钟陌】Matcha_风格，懒人图片元素提取反推_2022316505475584002.json, 图片生成/文生图/【楚心钟陌】Y易青Y风格风格，懒人图片提示词反推_2025129534554644482.json, 图片生成/文生图/【楚心钟陌】fgo风格，懒人图片提示词反推_2025137070485803009.json, 图片生成/文生图/【楚心钟陌】potg风格，懒人图片提示词反推_2024535930769514497.json, 图片生成/文生图/【楚心钟陌】rinotuna风格，懒人图片提示词反推_2025238242332774401.json, 图片生成/文生图/【楚心钟陌】はむねずこ风格，懒人图片提示词反推_2025233719291813889.json, 图片生成/文生图/【楚心钟陌】塔罗牌文生_2026313813309526018.json, 图片生成/文生图/【楚心钟陌】夢ノ内风格，懒人图片元素提取反推_2022312874340782081.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_22

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/文生图/【楚心钟陌】BBBS风格，懒人图片提示词反推_2025122219109650434.json、图片生成/文生图/【楚心钟陌】Leo画风，文生_2024094855894405121.json、图片生成/文生图/【楚心钟陌】Matcha_风格，懒人图片元素提取反推_2022316505475584002.json、图片生成/文生图/【楚心钟陌】Y易青Y风格风格，懒人图片提示词反推_2025129534554644482.json、图片生成/文生图/【楚心钟陌】fgo风格，懒人图片提示词反推_2025137070485803009.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：79%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `INTConstant`
- `JoinStrings`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SaveImage`
- `Text`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy cleanGpuUsed`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_unload_model`

**可变部分**（部分 workflow 才有）：
- `RunningHub Deepcleaner` —— 8/10 个有
- `TextPreview` —— 8/10 个有
- `ttN seed` —— 5/10 个有
- `AIO_Preprocessor` —— 3/10 个有
- `ImageScaleToTotalPixels` —— 3/10 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/10 个有
- `ModelPatchLoader` —— 3/10 个有
- `QwenImageDiffsynthControlnet` —— 3/10 个有
- `llama_cpp_parameters` —— 3/10 个有
- `LayerUtility: ImageReel` —— 2/10 个有
- `LayerUtility: ImageReelComposit` —— 2/10 个有
- `ModelscopeApiImageCaptionNode` —— 2/10 个有
- `ShowText|pysssss` —— 2/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 6 - 8 | 10 | 90% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 10 | 100% |
| 采样算法 | euler_ancestral_cfg_pp | - | 10 | 80% |
| 调度器 | bong_tangent | - | 10 | 80% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 6 - 8，10 个样本，取值集中（一致性 90%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral_cfg_pp，10 个样本，一致性 80%
- 调度器 最常用 bong_tangent，10 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 高发问题（10/10 个样本）：Steps较低可能导致细节不足
