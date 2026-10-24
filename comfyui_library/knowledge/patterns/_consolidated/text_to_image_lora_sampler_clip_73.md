---
name: text_to_image_lora_sampler_clip_73
type: Text To Image
frequency: 16
level: strong
coverage: 0.696875
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/深度视频参考动作迁移｜H3视频图生视频直出_2091029816312156162.json, 视频生成/图生视频/深度视频参考动作迁移｜H3视频生视频生成_2091213094801465345.json, 视频生成/图生视频/满血FP16+剪枝int8二采｜MinimaxH3浅空间放大v4_2093250532080185346.json, 视频生成/图生视频/满血FP16剪枝int8加速｜MinimaxH3浅空间放大二采v4_2093092897481650178.json, 视频生成/图生视频/满血int8单采八步加速｜MinimaxH3 Sigma版V4生成_2093254483198439425.json, 视频生成/图生视频/潜空间放大｜H3图生视频高清画质增强老八版_2090166759558045698.json, 视频生成/图生视频/电影级人物视频｜MiniMax H3完美解决脸部崩坏人物特效图生视频_2090066539633528834.json, 视频生成/图生视频/自然去油不磨皮｜MiniMax H3强化二采放大_2096579288177926145.json, 视频生成/图生视频/（最强一致性Singularity）Minimax H3多参考双采生视频王牌版_2104560310488223746.json, 视频生成/文生视频/0906 万象AI+Singularity 新模型｜12秒横屏960分辨率_2096858352113512449.json, 视频生成/文生视频/0906 万象AI+Singularity 新模型｜12秒竖屏960分辨率_2096856463141588993.json, 视频生成/文生视频/FL2VA首尾帧文生全能｜MiniMax H3视频生成工作流_2093069819640901634.json, 视频生成/文生视频/H3数字人口播工作流｜人物场景图加音频生成 自然Vlog口播视频_2104049801779306497.json, 视频生成/文生视频/MINImax-H3单人音乐MV制作｜文生视频音乐生成_2094927265846091778.json, 视频生成/文生视频/单人音乐MV制作｜MINImax-H3三模视频生成工作流_2095106732040220673.json, 视频生成/文生视频/小脸不崩运动不糊｜H3高清优化版文生图生视频_2089773922295304193.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_73

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（视频生成/图生视频/深度视频参考动作迁移｜H3视频图生视频直出_2091029816312156162.json、视频生成/图生视频/深度视频参考动作迁移｜H3视频生视频生成_2091213094801465345.json、视频生成/图生视频/满血FP16+剪枝int8二采｜MinimaxH3浅空间放大v4_2093250532080185346.json、视频生成/图生视频/满血FP16剪枝int8加速｜MinimaxH3浅空间放大二采v4_2093092897481650178.json、视频生成/图生视频/满血int8单采八步加速｜MinimaxH3 Sigma版V4生成_2093254483198439425.json…）

- **类型**：Text To Image
- **样本数**：16
- **可信度**：强结论
- **平均知识覆盖**：70%

## 共有节点

全部 16 个 workflow 都包含：
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
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `LTXVConcatAVLatent` —— 15/16 个有
- `LTXVSeparateAVLatent` —— 15/16 个有
- `MiniMaxH3ReferenceToVideo` —— 15/16 个有
- `GetNode` —— 13/16 个有
- `SetNode` —— 13/16 个有
- `SplitSigmas` —— 13/16 个有
- `VAEDecodeAudio` —— 13/16 个有
- `ModelAttentionBackend` —— 12/16 个有
- `MinimaxH3LatentUpscaler3D` —— 11/16 个有
- `H3SigmaRefiner` —— 10/16 个有
- `ModelPreviewOverrideKJ` —— 10/16 个有
- `LoadAudio` —— 9/16 个有
- `VHS_VideoCombine` —— 9/16 个有
- `SolAttnMiniMax` —— 8/16 个有
- `VHS_LoadVideo` —— 8/16 个有
- `CreateVideo` —— 7/16 个有
- `PrimitiveStringMultiline` —— 7/16 个有
- `SaveVideo` —— 7/16 个有
- `Text` —— 6/16 个有
- `easy float` —— 6/16 个有
- `MiniMaxH3SigmaShift` —— 5/16 个有
- `Lora Loader Stack (rgthree)` —— 3/16 个有
- `MinimaxH3LatentUpscalerNode3D` —— 3/16 个有
- `PathchSageAttentionKJ` —— 3/16 个有
- `Text Multiline` —— 3/16 个有
- `easy cleanGpuUsed` —— 3/16 个有
- `Fast Groups Bypasser (rgthree)` —— 2/16 个有
- `INTConstant` —— 2/16 个有
- `Label (rgthree)` —— 2/16 个有
- `PreviewAudio` —— 2/16 个有
- `ResizeShortestToNode` —— 2/16 个有
- `SoundFlow_GetLength` —— 2/16 个有
- `TrimAudioDuration` —— 2/16 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 2/16 个有
- `MiniMaxH3ImageToVideo` —— 1/16 个有
- `PlaySound|pysssss` —— 1/16 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 16 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 16 | 100% |
| 采样算法 | er_sde | - | 16 | 100% |
| 调度器 | beta | - | 16 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 16 | 100% |
| 宽度 | 80 | 80 - 80 | 16 | 100% |
| 高度 | 80 | 80 - 80 | 16 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 16/16 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，16 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，16 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，16 个样本，一致性 100%
- 调度器 最常用 beta，16 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，16 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，16 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，16 个样本，取值集中（一致性 100%）
- 高发问题（16/16 个样本）：Steps较低可能导致细节不足
