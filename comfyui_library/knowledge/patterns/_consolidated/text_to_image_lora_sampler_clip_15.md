---
name: text_to_image_lora_sampler_clip_15
type: Text To Image
frequency: 29
level: strong
coverage: 0.807724
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/FL2VA开源动作迁移｜MiniMax H3生成视频工作流_2094056951331254274.json, 视频生成/图生视频/FL2VA开源单图生视频｜MiniMax H3图生视频工作流_2093094312534962178.json, 视频生成/图生视频/FastVideo FastH3图生视频 8步加速视频生成工具_2100636893338759170.json, 视频生成/图生视频/FastVideo FastH3图生视频工作流，图生视频高效视频生成方案_2107904076905275394.json, 视频生成/图生视频/FastVideo FastH3图生视频｜快速通道高效产出视频_2107686292824879105.json, 视频生成/图生视频/H3图生视频 官方通用视频生成处理工具_2100635406244081666.json, 视频生成/图生视频/MiniMax H3 FL2VA开源人物模仿，动作迁移图生视频_2110821478810873857.json, 视频生成/图生视频/MiniMax H3 FL2VA开源版 用动作迁移直接生成视频_2095072427146571777.json, 视频生成/图生视频/MiniMax H3 FL2VA开源版 用动作迁移直接生成视频_2097466631751561218.json, 视频生成/图生视频/MiniMax H3 FL2VA开源版工作流 视频动作迁移人物图生视频方案_2094031469198008322.json, 视频生成/图生视频/MiniMax H3 FL2VA开源版工作流 视频动作迁移人物图生视频方案_2097111204803203073.json, 视频生成/图生视频/MiniMax H3 FL2VA开源版工作流 视频动作迁移人物图生视频方案_2098922083215564801.json, 视频生成/图生视频/MiniMax H3全能参考三图版｜三图输入视频生成_2094516324448948226.json, 视频生成/图生视频/MiniMax H3全能参考双图版｜双图输入视频生成_2094519227574218754.json, 视频生成/图生视频/MiniMax H3全能参考四图版｜多图输入视频生成_2094508021375397889.json, 视频生成/图生视频/MiniMax H3参考生视频 官方全能多模态创作工具_2098824046145269762.json, 视频生成/图生视频/MiniMax H3参考生视频加速版图生视频处理工具_2101358023905206274.json, 视频生成/图生视频/MiniMax H3参考生视频图生视频多模态处理工具_2101356055950356482.json, 视频生成/图生视频/MiniMax H3参考生视频｜多图参考保持主角一致性稳定输出_2099169349520150529.json, 视频生成/图生视频/MiniMax H3图生视频 官方全模态立体声视频生成_2098814736157728769.json, 视频生成/图生视频/MiniMax H3图生视频fastH3基础版 trim加速快速直出_2110253662495928321.json, 视频生成/图生视频/MiniMax H3图生视频fastH3基础版 trim加速快速直出_2110368880341377026.json, 视频生成/图生视频/Minimax H3 Veda稀疏注意力8步极速版参考生视频 快速出片_2108988281630314498.json, 视频生成/图生视频/Minimax H3参考图和参考视音频生成视频满血版 多模态输入_2105039400945147906.json, 视频生成/图生视频/Minimax图生视频I2V工作流含首尾帧，图生视频高效创作工具_2106873837555113985.json, 视频生成/图生视频/Minimax图生视频I2V工作流含首尾帧，图生视频高效创作工具_2109810746019373058.json, 视频生成/图生视频/Minimax图生视频I2V工作流，图生视频官方图生视频处理工具_2107908610960486402.json, 视频生成/图生视频/Minimax图生视频I2V方案，图生视频高效直出_2111192151311872002.json, 视频生成/图生视频/Minimax图生视频I2V方案｜图片动起来就这么简单_2107697471907516418.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_15

> 由 `engine/knowledge_consolidation` 从 29 个 workflow 归纳得出（视频生成/图生视频/FL2VA开源动作迁移｜MiniMax H3生成视频工作流_2094056951331254274.json、视频生成/图生视频/FL2VA开源单图生视频｜MiniMax H3图生视频工作流_2093094312534962178.json、视频生成/图生视频/FastVideo FastH3图生视频 8步加速视频生成工具_2100636893338759170.json、视频生成/图生视频/FastVideo FastH3图生视频工作流，图生视频高效视频生成方案_2107904076905275394.json、视频生成/图生视频/FastVideo FastH3图生视频｜快速通道高效产出视频_2107686292824879105.json…）

- **类型**：Text To Image
- **样本数**：29
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 29 个 workflow 都包含：
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
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `孤海注释` —— 28/29 个有
- `CreateVideo` —— 27/29 个有
- `SaveVideo` —— 27/29 个有
- `ComfySwitchNode` —— 24/29 个有
- `PrimitiveBoolean` —— 24/29 个有
- `PrimitiveInt` —— 24/29 个有
- `VAEDecodeAudio` —— 22/29 个有
- `GetImageSize` —— 18/29 个有
- `ResolutionSelector` —— 18/29 个有
- `MiniMaxH3ReferenceToVideo` —— 16/29 个有
- `SaveImage` —— 16/29 个有
- `MiniMaxH3ImageToVideo` —— 13/29 个有
- `LoadAudio` —— 11/29 个有
- `PrimitiveStringMultiline` —— 11/29 个有
- `ImageScaleToTotalPixels` —— 10/29 个有
- `GetVideoComponents` —— 9/29 个有
- `LoadVideo` —— 9/29 个有
- `ImageScale` —— 8/29 个有
- `SetNode` —— 7/29 个有
- `Video Slice` —— 7/29 个有
- `VideoFrameSample` —— 7/29 个有
- `BlockSparseAttention` —— 6/29 个有
- `MiniMaxH3SigmaShift` —— 6/29 个有
- `ModelAttentionBackend` —— 6/29 个有
- `AudioCrop` —— 5/29 个有
- `GetNode` —— 5/29 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 3/29 个有
- `easy minimaxH3AudioLock` —— 3/29 个有
- `MiniMaxH3AudioLock` —— 2/29 个有
- `VHS_VideoCombine` —— 2/29 个有
- `CR Text` —— 1/29 个有
- `EmptyImage` —— 1/29 个有
- `MiniMaxH3SaveLatent` —— 1/29 个有
- `PreviewImage` —— 1/29 个有
- `VedaSparseAttention` —— 1/29 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 29 | 100% |
| 高度 | 80 | 80 - 80 | 29 | 100% |
| 采样步数 | 4 | 4 - 4 | 29 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 29 | 100% |
| 采样算法 | er_sde | - | 29 | 100% |
| 调度器 | beta | - | 29 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 29 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 30/29 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，29 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，29 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，29 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，29 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，29 个样本，一致性 100%
- 调度器 最常用 beta，29 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，29 个样本，取值集中（一致性 100%）
- 高发问题（30/29 个样本）：Steps较低可能导致细节不足
