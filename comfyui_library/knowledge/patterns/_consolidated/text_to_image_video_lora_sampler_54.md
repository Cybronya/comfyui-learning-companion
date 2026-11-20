---
name: text_to_image_video_lora_sampler_54
type: Text To Image
frequency: 14
level: strong
coverage: 0.751357
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/int8文生视频4步加速｜MiniMax H3提示词优化工作流_2090868519985565697.json, 图片生成/文生图/int8文生视频4步加速｜MiniMax H3提示词优化流_2090563536077545474.json, 数字人/数字人/AI短剧人物开口说话V1.1｜8秒有声测试版先睹为快_2112399633505939458.json, 数字人/数字人/探店商品视频无滤镜版｜MiniMax+H3数字人生成_2093789772853633025.json, 视频生成/图生视频/MiniMax H3图片加音色生视频 自动提示词优化工具_2114132113485287426.json, 视频生成/图生视频/V1.2两次采样8步加速MiniMax H3参考生视频音频参考自动提示词优化_2088370421749080065.json, 视频生成/图生视频/两次采样8步加速音频参考自动提示词优化V1.2｜MiniMax H3参考生视频图生视频_2088337657226153985.json, 视频生成/图生视频/多参考图生视频4步加速｜MiniMax H3提示词自动优化美少女_2091298868020473857.json, 视频生成/图生视频/绘影MiniMax H3参考生视频in 混合模型，720P加速LoRA四步出图方案_2103224330846031873.json, 视频生成/图生视频/绘影打造｜MiniMax H3参考生视频fl2va int8量化720P V1_2103021430949629954.json, 视频生成/文生视频/H3全能多参提示词优化｜4步加速文生视频图生视频_2089386017529880578.json, 视频生成/文生视频/MiniMax H3 全能参考_自动提示词_2085967794637729794.json, 视频生成/文生视频/MiniMaxH3加速版尾帧做参考｜4步加速 文生视频视频生视频快出片_2104097352675057665.json, 视频生成/文生视频/尾帧参考4步加速 MiniMaxH3极速生视频省时方案_2104330470908579842.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_54

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/文生图/int8文生视频4步加速｜MiniMax H3提示词优化工作流_2090868519985565697.json、图片生成/文生图/int8文生视频4步加速｜MiniMax H3提示词优化流_2090563536077545474.json、数字人/数字人/AI短剧人物开口说话V1.1｜8秒有声测试版先睹为快_2112399633505939458.json、数字人/数字人/探店商品视频无滤镜版｜MiniMax+H3数字人生成_2093789772853633025.json、视频生成/图生视频/MiniMax H3图片加音色生视频 自动提示词优化工具_2114132113485287426.json…）

- **类型**：Text To Image
- **样本数**：14
- **可信度**：强结论
- **平均知识覆盖**：75%

## 共有节点

全部 14 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
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
- `JoinStringMulti` —— 13/14 个有
- `StringConcatenate` —— 13/14 个有
- `easy showAnything` —— 13/14 个有
- `llama_cpp_instruct_adv` —— 13/14 个有
- `llama_cpp_model_loader` —— 13/14 个有
- `llama_cpp_parameters` —— 13/14 个有
- `孤海注释` —— 13/14 个有
- `LoadImage` —— 12/14 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 12/14 个有
- `Fast Groups Bypasser (rgthree)` —— 11/14 个有
- `LoadAudio` —— 11/14 个有
- `Any Switch (rgthree)` —— 10/14 个有
- `BasicScheduler` —— 10/14 个有
- `GetNode` —— 10/14 个有
- `KSamplerSelect` —— 10/14 个有
- `MiniMaxH3ReferenceToVideo` —— 10/14 个有
- `PurgeVRAM_UTK` —— 10/14 个有
- `SetNode` —— 10/14 个有
- `ToString` —— 10/14 个有
- `VAEDecodeAudio` —— 10/14 个有
- `BatchImagesNode` —— 9/14 个有
- `MiniMaxH3AVDecodeT8` —— 6/14 个有
- `MiniMaxH3AudioConditioningT8` —— 4/14 个有
- `MiniMaxH3MultiRateSamplerEXPT8` —— 4/14 个有
- `ModelAttentionBackend` —— 4/14 个有
- `UniBlockSwap` —— 4/14 个有
- `Any To String (mtb)` —— 3/14 个有
- `LoadVideo` —— 3/14 个有
- `MiniMaxH3SigmaShift` —— 3/14 个有
- `SaveImage` —— 3/14 个有
- `GetLastFrameNode` —— 2/14 个有
- `H3SigmaRefiner` —— 2/14 个有
- `ImageResizeKJv2` —— 2/14 个有
- `LTXVConcatAVLatent` —— 2/14 个有
- `LoraLoaderBypassModelOnly` —— 2/14 个有
- `MiniMaxChunkFeedForward` —— 2/14 个有
- `MiniMaxLowVRAMAttention` —— 2/14 个有
- `ModelPreviewOverrideKJ` —— 2/14 个有
- `PathchSageAttentionKJ` —— 2/14 个有
- `VAEEncode` —— 2/14 个有
- `ZNGB_ImageBatchMulti` —— 2/14 个有
- `workflow>2` —— 2/14 个有
- `StringFormat` —— 1/14 个有
- `TrimAudioDuration` —— 1/14 个有
- `YuanCustomCombo` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 14 | 100% |
| 高度 | 80 | 80 - 80 | 14 | 100% |
| 采样步数 | 4 | 4 - 4 | 14 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 14 | 100% |
| 采样算法 | er_sde | - | 14 | 100% |
| 调度器 | beta | - | 14 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 14 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 14/14 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，14 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，14 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，14 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，14 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，14 个样本，一致性 100%
- 调度器 最常用 beta，14 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 高发问题（14/14 个样本）：Steps较低可能导致细节不足
