---
name: text_to_image_video_lora_sampler_61
type: Text To Image
frequency: 11
level: strong
coverage: 0.851636
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/I2V lora加速｜MiniMax H3首帧图生视频3分40秒_2091174539307872258.json, 视频生成/图生视频/MInimaxH3首尾帧官方提示词指南自动扩写_2086206535667109889.json, 视频生成/图生视频/MInimaxH3首尾帧官方提示词指南｜自动扩写T2分镜更稳_2106263717989150721.json, 视频生成/图生视频/MInimaxH3首尾帧官方提示词指南｜自动扩写T3分镜出图_2106974045374869506.json, 视频生成/图生视频/MiniMax H3 I2V图生视频｜Fused ACC八步极速出片_2097147575894888449.json, 视频生成/图生视频/MiniMax H3全参官方指南自动扩展提示词T6工作流，角色一致性图生视频_2106097208906043393.json, 视频生成/图生视频/MiniMax H3全参官方指南自动扩展提示词，角色表演图生视频工作流_2103588976929099778.json, 视频生成/图生视频/MiniMax H3全参连续帧提示词自动优化工作流，图生视频高效创作方案_2106094286554099714.json, 视频生成/图生视频/T6全参官方指南｜minimaxh3自动扩展提示词分镜出图_2094333256052334594.json, 视频生成/图生视频/minimaxh3全参官方指南自动扩展提示词_2086537843907846146.json, 视频生成/图生视频/全参连续帧优化｜minimaxh3提示词自动图生视频生成_2094719853226717186.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_61

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/I2V lora加速｜MiniMax H3首帧图生视频3分40秒_2091174539307872258.json、视频生成/图生视频/MInimaxH3首尾帧官方提示词指南自动扩写_2086206535667109889.json、视频生成/图生视频/MInimaxH3首尾帧官方提示词指南｜自动扩写T2分镜更稳_2106263717989150721.json、视频生成/图生视频/MInimaxH3首尾帧官方提示词指南｜自动扩写T3分镜出图_2106974045374869506.json、视频生成/图生视频/MiniMax H3 I2V图生视频｜Fused ACC八步极速出片_2097147575894888449.json…）

- **类型**：Text To Image
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 11 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `Text` —— 10/11 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 8/11 个有
- `RHHiddenNodes` —— 7/11 个有
- `ResolutionSelector` —— 7/11 个有
- `PreviewImage` —— 6/11 个有
- `easy MiniMaxH3ReferenceToVideoBridge` —— 6/11 个有
- `easy showAnything` —— 6/11 个有
- `MiniMaxH3ImageToVideo` —— 5/11 个有
- `ImageConcatenateMulti_UTK` —— 4/11 个有
- `ImageResizeKJv2` —— 3/11 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/11 个有
- `SaveImage` —— 3/11 个有
- `LoadAudio` —— 2/11 个有
- `RH_Captioner` —— 2/11 个有
- `TextConcatenate_UTK` —— 2/11 个有
- `easy imageSplitGrid` —— 2/11 个有
- `easy indexAnything` —— 2/11 个有
- `GetNode` —— 1/11 个有
- `MiniMaxChunkFeedForward` —— 1/11 个有
- `MiniMaxLowVRAMAttention` —— 1/11 个有
- `PrimitiveStringMultiline` —— 1/11 个有
- `SetNode` —— 1/11 个有
- `SolAttnPatch` —— 1/11 个有
- `ZNGB_ResizeImage` —— 1/11 个有

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
