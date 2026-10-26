---
name: text_to_image_video_lora_sampler_42
type: Text To Image
frequency: 17
level: strong
coverage: 0.844294
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, ConditioningZeroOut, EmptyLatentImage, EnhancedLoadDiffusionModel, FluxKontextMultiReferenceLatentMethod, JjkText, KSampler, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, PreviewImage, PrimitiveFloat, RHHiddenNodes, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, Split String by Commas, StringReplace, Text, TextConcatenate_UTK, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine, easy MiniMaxH3ReferenceToVideoBridge, easy indexAnything, easy showAnything, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/H3加Qwen加Gemma4全开源多参视频八步加速处理_2100660131116703746.json, 视频生成/图生视频/H3加Qwen加Gemma4全开源多参视频八步加速处理_2100670884615901186.json, 视频生成/图生视频/MInimaxH3+Qwen+Gemma4全开源多参视频T1｜图生视频_2100787407342882818.json, 视频生成/图生视频/MInimaxH3+Qwen+Gemma4全开源｜多参视频八步加速生成_2106971174885482497.json, 视频生成/图生视频/MInimaxH3联手Qwen加Gemma4｜全开源多参视频8步加速_2101515958933352449.json, 视频生成/图生视频/MiniMax H3+Qwen+Gemma4 全开源多参考视频 T1｜角色一致性_2096826716000968706.json, 视频生成/图生视频/MiniMax H3+Qwen+Gemma4全开源多参视频八步加速处理工具_2101759427991920642.json, 视频生成/图生视频/MiniMax H3+Qwen+Gemma4多参视频生成处理工作流_2101009960523100162.json, 视频生成/图生视频/MiniMax H3加Qwen加Gemma4全开源多参视频八步加速，图生视频高效方案_2107175443223891969.json, 视频生成/图生视频/MiniMax_H3加Qwen加Gemma4全开源多参视频八步加速，图生视频高效方案_2109443610855960578.json, 视频生成/图生视频/Qwen+Gemma4全开源八步加速｜MInimaxH3多参图生视频_2091588120390225922.json, 视频生成/图生视频/Qwen+Gemma4全开源多参视频T2｜MInimaxH3角色一致性分镜出图图生视频_2087225496038895618.json, 视频生成/图生视频/Qwen+Gemma4全开源多参视频T4｜MInimaxH3角色一致性分镜出图图生视频_2087214415824384001.json, 视频生成/图生视频/全开源多参加速｜MinimaxH3+Qwen+Gemma4视频八步出片_2099915275339649026.json, 视频生成/图生视频/全开源多参视频T1｜MInimaxH3+Qwen+Gemma4一致性出图_2092913279109779458.json, 视频生成/图生视频/全开源多参视频八步加速｜MInimaxH3+Qwen+Gemma4图生视频_2095798673602076673.json, 视频生成/图生视频/八步加速全开源｜MinimaxH3+Qwen+Gemma4多参视频_2091754330675310593.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_42

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（视频生成/图生视频/H3加Qwen加Gemma4全开源多参视频八步加速处理_2100660131116703746.json、视频生成/图生视频/H3加Qwen加Gemma4全开源多参视频八步加速处理_2100670884615901186.json、视频生成/图生视频/MInimaxH3+Qwen+Gemma4全开源多参视频T1｜图生视频_2100787407342882818.json、视频生成/图生视频/MInimaxH3+Qwen+Gemma4全开源｜多参视频八步加速生成_2106971174885482497.json、视频生成/图生视频/MInimaxH3联手Qwen加Gemma4｜全开源多参视频8步加速_2101515958933352449.json…）

- **类型**：Text To Image
- **样本数**：17
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 17 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `EnhancedLoadDiffusionModel`
- `FluxKontextMultiReferenceLatentMethod`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `PreviewImage`
- `PrimitiveFloat`
- `RHHiddenNodes`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `Split String by Commas`
- `StringReplace`
- `Text`
- `TextConcatenate_UTK`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`
- `easy MiniMaxH3ReferenceToVideoBridge`
- `easy indexAnything`
- `easy showAnything`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `easy cleanGpuUsed` —— 13/17 个有
- `SaveImage` —— 6/17 个有
- `ImageScaleToTotalPixels` —— 4/17 个有
- `Int` —— 4/17 个有
- `JDCN_StringToList` —— 4/17 个有
- `LayerUtility: PurgeVRAM V2` —— 4/17 个有
- `RandomInt` —— 4/17 个有
- `easy batchAnything` —— 4/17 个有
- `easy forLoopEnd` —— 4/17 个有
- `easy forLoopStart` —— 4/17 个有
- `EmptyImage` —— 3/17 个有
- `MiniMaxH3BlockCacheT8` —— 2/17 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 17 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 17 | 100% |
| 采样算法 | er_sde | - | 17 | 100% |
| 调度器 | beta | - | 17 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 17 | 100% |
| 宽度 | 80 | 80 - 80 | 17 | 100% |
| 高度 | 80 | 80 - 80 | 17 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 47/17 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，17 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，17 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，17 个样本，一致性 100%
- 调度器 最常用 beta，17 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，17 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，17 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，17 个样本，取值集中（一致性 100%）
- 高发问题（47/17 个样本）：Steps较低可能导致细节不足
