---
name: text_to_image_lora_sampler_clip_124
type: Text To Image
frequency: 9
level: strong
coverage: 0.872444
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, CreateVideo, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadAudio, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MINIMAX H3多参生视频，文生视频图生视频双模式_2110819887017975810.json, 视频生成/图生视频/MINIMAX H3多图参考生视频 多张参考图输入角色一致性更强_2104657812193370114.json, 视频生成/图生视频/MINIMAX H3多图参考生视频 多模态输入视频生成_2109333013833273345.json, 视频生成/图生视频/MINIMAX H3多图参考生视频工作流，视频生视频图生视频处理方案_2108265068692598785.json, 视频生成/图生视频/MINIMAX H3多图参考生视频工作流，视频生视频图生视频方案_2106813670759157761.json, 视频生成/图生视频/MINIMAX-H3多图参考生视频｜多图输入角色一致生成_2094860073762902017.json, 视频生成/图生视频/MINIMAX-H3多图参考生视频｜视频生视频图生视频_2090436400712863745.json, 视频生成/图生视频/MINIMAX-H3多图参考｜多张图片参考生成连贯视频_2101575258661806082.json, 视频生成/图生视频/MImax H3超强开源视频加速-图生视频工作流_2087344640801464322.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_124

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/MINIMAX H3多参生视频，文生视频图生视频双模式_2110819887017975810.json、视频生成/图生视频/MINIMAX H3多图参考生视频 多张参考图输入角色一致性更强_2104657812193370114.json、视频生成/图生视频/MINIMAX H3多图参考生视频 多模态输入视频生成_2109333013833273345.json、视频生成/图生视频/MINIMAX H3多图参考生视频工作流，视频生视频图生视频处理方案_2108265068692598785.json、视频生成/图生视频/MINIMAX H3多图参考生视频工作流，视频生视频图生视频方案_2106813670759157761.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 9 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `CreateVideo`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `ComfyMathExpression` —— 8/9 个有
- `PrimitiveFloat` —— 8/9 个有
- `PrimitiveStringMultiline` —— 8/9 个有
- `SaveImage` —— 5/9 个有
- `ApplyFaceProcessor` —— 1/9 个有
- `CompressImages` —— 1/9 个有
- `FaceProcessorLoader` —— 1/9 个有
- `GetVideoComponents` —— 1/9 个有
- `ImageFromBatch` —— 1/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/9 个有
- `MathExpression|pysssss` —— 1/9 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 1/9 个有
- `PreviewAny` —— 1/9 个有
- `PreviewImage` —— 1/9 个有
- `RH_Astra` —— 1/9 个有
- `SaveMP4` —— 1/9 个有
- `SeedVR2` —— 1/9 个有
- `SeedVR2BlockSwap` —— 1/9 个有
- `VHS_VideoCombine` —— 1/9 个有
- `easy float` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 9 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 9 | 100% |
| 采样算法 | er_sde | - | 9 | 100% |
| 调度器 | beta | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |
| 宽度 | 80 | 80 - 80 | 9 | 100% |
| 高度 | 80 | 80 - 80 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，9 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，9 个样本，一致性 100%
- 调度器 最常用 beta，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高发问题（9/9 个样本）：Steps较低可能导致细节不足
