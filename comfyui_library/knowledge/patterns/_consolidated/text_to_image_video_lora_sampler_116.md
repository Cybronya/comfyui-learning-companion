---
name: text_to_image_video_lora_sampler_116
type: Text To Image
frequency: 6
level: strong
coverage: 0.877
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, CR Text, ComfyMathExpression, EmptyLatentImage, Fast Groups Bypasser (rgthree), ImageConcatMulti, ImageResizeKJv2, JjkText, KSampler, KSamplerSelect, LayerUtility: PurgeVRAM V2, LoadImage, LoraLoaderModelOnly, MiniMaxChunkFeedForward, MiniMaxH3AVDecodeT8, MiniMaxH3DualClockSamplerT8, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxLowVRAMAttention, ModelAttentionBackend, ModelPreviewOverrideKJ, PT_H3ConcatAVLatent, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, ShowText|pysssss, Switch any [Crystools], UNETLoader, VAEDecode, VAEEncode, VAELoader, VHS_VideoCombine, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMax_H3_Fl2va双时钟采样Turbo_LORA｜视频风格转换加速双引擎_2107470865632948225.json, 视频生成/文生视频/MiniMax H3 Fl2va双时钟采样Turbo LORA｜视频风格转换加速双引擎_2107295461982949378.json, 视频生成/文生视频/MiniMax H3 Fl2va双时钟采样Turbo LoRA工作流，文生视频图生视频方案_2107530132549357569.json, 视频生成/文生视频/MiniMax H3 Fl2va双时钟采样Turbo Lora图生视频工具_2101398805836025858.json, 视频生成/文生视频/MiniMax H3双时钟采样Turbo Lora双采多模态视频工具_2101400762055217154.json, 视频生成/文生视频/双时钟采样Turbo LORA加持 MiniMax H3双采多模态工作流_2104826155835682817.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_116

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/MiniMax_H3_Fl2va双时钟采样Turbo_LORA｜视频风格转换加速双引擎_2107470865632948225.json、视频生成/文生视频/MiniMax H3 Fl2va双时钟采样Turbo LORA｜视频风格转换加速双引擎_2107295461982949378.json、视频生成/文生视频/MiniMax H3 Fl2va双时钟采样Turbo LoRA工作流，文生视频图生视频方案_2107530132549357569.json、视频生成/文生视频/MiniMax H3 Fl2va双时钟采样Turbo Lora图生视频工具_2101398805836025858.json、视频生成/文生视频/MiniMax H3双时钟采样Turbo Lora双采多模态视频工具_2101400762055217154.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `ImageConcatMulti`
- `ImageResizeKJv2`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxChunkFeedForward`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3DualClockSamplerT8`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxLowVRAMAttention`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `PT_H3ConcatAVLatent`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `ShowText|pysssss`
- `Switch any [Crystools]`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `VHS_VideoCombine`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: TextJoin` —— 5/6 个有
- `孤海注释` —— 5/6 个有
- `MiniMaxH3ImageToVideo` —— 4/6 个有
- `Primitive boolean [Crystools]` —— 4/6 个有
- `SaveImage` —— 3/6 个有
- `AudioConcat` —— 2/6 个有
- `LoadAudio` —— 2/6 个有
- `LoadVideoUI` —— 2/6 个有
- `MiniMaxH3ReferenceToVideo` —— 2/6 个有
- `TrimAudioDuration` —— 2/6 个有
- `VAEEncodeAudio` —— 2/6 个有
- `easy boolean` —— 2/6 个有
- `easy cleanGpuUsed` —— 2/6 个有
- `easy seed` —— 2/6 个有
- `EmptyImage` —— 1/6 个有
- `PreviewImage` —— 1/6 个有
- `RHHiddenNodes` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 6 | 100% |
| 高度 | 80 | 80 - 80 | 6 | 100% |
| 采样步数 | 4 | 4 - 4 | 6 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 6 | 100% |
| 采样算法 | er_sde | - | 6 | 100% |
| 调度器 | beta | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，6 个样本，一致性 100%
- 调度器 最常用 beta，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足
