---
name: text_to_image_video_lora_sampler_60
type: Text To Image
frequency: 11
level: strong
coverage: 0.860818
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3MultiRateSamplerEXPT8, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/int8文生视频4步加速｜MiniMax H3提示词优化工作流_2090868519985565697.json, 图片生成/文生图/int8文生视频4步加速｜MiniMax H3提示词优化流_2090563536077545474.json, 视频生成/图生视频/H3单图生视频｜MINIMAX工作流8-20新版_2090869883713179650.json, 视频生成/图生视频/H3高保真图生视频 静止图像动态化运镜重构_2099924808850042881.json, 视频生成/图生视频/MiniMax H3全能参考工作流｜文生视频单图生视频图生视频_2090446719375990786.json, 视频生成/图生视频/MiniMax h3开源版H3图生视频短剧广告片创意视频口播MV跳舞视频生成数字人加速四倍_2087143209582546946.json, 视频生成/图生视频/MiniMax h3开源版H3图生视频短剧广告片创意视频口播MV跳舞视频生成数字人加速四倍_2087154037660672001.json, 视频生成/图生视频/h3开源加速版MINIMAX-H3合集｜单图生多图参考4步lora加速_2097965293799825409.json, 视频生成/图生视频/全能参考工作流｜MiniMax H3图生视频一键生成_2090270213274165249.json, 视频生成/图生视频/多参考图生视频4步加速｜MiniMax H3提示词自动优化美少女_2091298868020473857.json, 视频生成/图生视频/高质量自动化多参视频流｜动漫人物特效图生视频_2092738709815906306.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_60

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/文生图/int8文生视频4步加速｜MiniMax H3提示词优化工作流_2090868519985565697.json、图片生成/文生图/int8文生视频4步加速｜MiniMax H3提示词优化流_2090563536077545474.json、视频生成/图生视频/H3单图生视频｜MINIMAX工作流8-20新版_2090869883713179650.json、视频生成/图生视频/H3高保真图生视频 静止图像动态化运镜重构_2099924808850042881.json、视频生成/图生视频/MiniMax H3全能参考工作流｜文生视频单图生视频图生视频_2090446719375990786.json…）

- **类型**：Text To Image
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 11 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3MultiRateSamplerEXPT8`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 9/11 个有
- `孤海注释` —— 9/11 个有
- `LoraLoaderBypassModelOnly` —— 8/11 个有
- `LoadAudio` —— 6/11 个有
- `UniBlockSwap` —— 4/11 个有
- `Any To String (mtb)` —— 3/11 个有
- `BatchImagesNode` —— 3/11 个有
- `Fast Groups Bypasser (rgthree)` —— 3/11 个有
- `JoinStringMulti` —— 3/11 个有
- `StringConcatenate` —— 3/11 个有
- `easy showAnything` —— 3/11 个有
- `llama_cpp_instruct_adv` —— 3/11 个有
- `llama_cpp_model_loader` —— 3/11 个有
- `llama_cpp_parameters` —— 3/11 个有
- `PreviewAny` —— 2/11 个有
- `RH_LLMAPI_Pro_Node` —— 2/11 个有
- `MemoryCleaner` —— 1/11 个有
- `MiniMaxH3SigmaShift` —— 1/11 个有
- `RHLLMChatNode` —— 1/11 个有
- `SaveImage` —— 1/11 个有
- `VHS_LoadVideo` —— 1/11 个有
- `WujiCleaner` —— 1/11 个有
- `XB_ROCmMemCleaner` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 11 | 100% |
| 高度 | 80 | 80 - 80 | 11 | 100% |
| 采样步数 | 4 | 4 - 4 | 11 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 11 | 100% |
| 采样算法 | er_sde | - | 11 | 100% |
| 调度器 | beta | - | 11 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，11 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，11 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，11 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，11 个样本，一致性 100%
- 调度器 最常用 beta，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 高发问题（11/11 个样本）：Steps较低可能导致细节不足
