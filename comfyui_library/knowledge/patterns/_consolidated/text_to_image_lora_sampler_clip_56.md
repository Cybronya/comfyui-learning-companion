---
name: text_to_image_lora_sampler_clip_56
type: Text To Image
frequency: 16
level: weak
coverage: 0.846313
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyImage, EmptyLatentImage, INTConstant, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoraLoaderModelOnly, PrimitiveStringMultiline, ResolutionSelector, SaveImage, ShowText|pysssss, Text Multiline, UNETLoader, VAEDecode, VAELoader, easy seed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Krea2超细节增强哈基米版 亚洲美人Lora加持画质提升_2098637955245101058.json, 图片生成/图生图/Krea2超细节增强洗图生图二合一 Qwen3.5自由切换构图控制_2098636397501575170.json, 图片生成/图生图/krea2 超细节增强-多样性洗图生图2合1工作流V2（哈基米自由切换版）😼_2095457143909605378.json, 图片生成/图生图/krea2 超细节增强-构图多样性 洗图生图2合1工作流V2（Qwen3.5自由切换版）😼_2095467409154072577.json, 图片生成/图生图/krea2多样性洗图生图2合1V2｜哈基米模型随心切_2098744493905375233.json, 图片生成/图生图/krea2超细节增强构图多样性｜洗图生图2合1工作流_2095573968009908226.json, 图片生成/图生图/krea2超细节增强洗图2合1V2｜Qwen3.5自由切换_2098740517784875009.json, 图片生成/图生图/krea2超细节增强｜哈基米洗图生图2合1工作流_2095578309022273537.json, 图片生成/图生图/构图多样性洗图生图2合1｜krea2超细节增强Qwen3.5切换版_2095823191347392514.json, 图片生成/文生图/Qwen 2.1超细节洗图生图二合一，支持Qwen 3.5自由切换的反推提示词工作流_2102878744355627010.json, 图片生成/文生图/krea2 超细节增强 洗图生图2合1工作流（自由切换版）_qwen3.5😼_2077340261931380738.json, 图片生成/文生图/krea2 风格之王 全能模型 Qwen3.5自动提示词文生图工作流（自由版）_2070756328192172034.json, 图片生成/文生图/krea2 风格之王 全能模型 deepseekV4自动提示词文生图工作流（自由版）_2070758812876894209.json, 图片生成/文生图/krea2 风格之王 全能模型 gemini自动提示词文生图工作流（自由版）_2070761173187907585.json, 图片生成/文生图/krea2超细节增强 洗图生图2合1工作流（自由切换版）_哈基米版😼_2077326567931473922.json, 视频生成/图生视频/Qwen_2.1超细节洗图生图二合一，支持Qwen_3.5自由切换的反推提示词工作流_2105120232384851969.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_56

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（图片生成/图生图/Krea2超细节增强哈基米版 亚洲美人Lora加持画质提升_2098637955245101058.json、图片生成/图生图/Krea2超细节增强洗图生图二合一 Qwen3.5自由切换构图控制_2098636397501575170.json、图片生成/图生图/krea2 超细节增强-多样性洗图生图2合1工作流V2（哈基米自由切换版）😼_2095457143909605378.json、图片生成/图生图/krea2 超细节增强-构图多样性 洗图生图2合1工作流V2（Qwen3.5自由切换版）😼_2095467409154072577.json、图片生成/图生图/krea2多样性洗图生图2合1V2｜哈基米模型随心切_2098744493905375233.json…）

- **类型**：Text To Image
- **样本数**：16
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：85%

## 共有节点

全部 16 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyImage`
- `EmptyLatentImage`
- `INTConstant`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoraLoaderModelOnly`
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `SaveImage`
- `ShowText|pysssss`
- `Text Multiline`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy seed`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 14/16 个有
- `LoadImage` —— 13/16 个有
- `Switch any [Crystools]` —— 13/16 个有
- `ConditioningKrea2Rebalance` —— 11/16 个有
- `LatentUpscaleBy` —— 11/16 个有
- `JjkText` —— 9/16 个有
- `llama_cpp_instruct_adv` —— 9/16 个有
- `llama_cpp_model_loader` —— 9/16 个有
- `llama_cpp_parameters` —— 9/16 个有
- `solarL_SaveImagesToZip` —— 9/16 个有
- `孤海注释` —— 8/16 个有
- `Label (rgthree)` —— 7/16 个有
- `RH_LLMAPI_Pro_Node` —— 7/16 个有
- `TextEncodeQwenImage21` —— 2/16 个有
- `TextGenerateLTX2Prompt` —— 2/16 个有
- `easy showAnything` —— 2/16 个有
- `PreviewImage` —— 1/16 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 1024 | 16 | 5% |
| 高度 | 80 | 80 - 1536 | 16 | 0% |
| 采样步数 | 4 | 3 - 8 | 16 | 63% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 16 | 42% |
| 采样算法 | er_sde | - | 16 | 56% |
| 调度器 | beta | - | 16 | 56% |
| 重绘幅度 | 1 | 0.4 - 1 | 16 | 85% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 34/16 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 1024，16 个样本，取值分散，一致性仅 5%
- 高度 中位数 80，观测区间 80 - 1536，16 个样本，取值分散，一致性仅 0%
- 采样步数 中位数 4，观测区间 3 - 8，16 个样本
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，16 个样本，取值分散，一致性仅 42%
- 采样算法 最常用 er_sde，16 个样本，一致性 56%
- 调度器 最常用 beta，16 个样本，一致性 56%
- 重绘幅度 中位数 1，观测区间 0.4 - 1，16 个样本，取值集中（一致性 85%）
- 高发问题（34/16 个样本）：Steps较低可能导致细节不足
