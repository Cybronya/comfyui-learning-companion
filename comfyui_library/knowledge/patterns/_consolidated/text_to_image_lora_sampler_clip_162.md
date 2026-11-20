---
name: text_to_image_lora_sampler_clip_162
type: Text To Image
frequency: 11
level: strong
coverage: 0.771545
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [数字人/数字人/写英文工作流｜数字人英文口播视频生成专用流_2114020800511696898.json, 视频生成/图生视频/10步+3步Latent Upscaler｜H3参考模式图生视频_2091180204667531265.json, 视频生成/图生视频/BUNNY_H3单采er_sde手动Sigma，文生视频节奏随心控_2110519304910364674.json, 视频生成/图生视频/H3 Taomate 3步加速 中远距离不崩脸视频生成_2099588330131382273.json, 视频生成/图生视频/H3全能参考短剧工作流 多模态输入视频生成_2109027495902277633.json, 视频生成/图生视频/MiniMax H3 FastVideo极速多参 视频生成加速方案_2109013584503201793.json, 视频生成/图生视频/MiniMax H3人物演技提升 文生视频图生视频处理工具_2113333463540658178.json, 视频生成/图生视频/MiniMax H3角色替换 指定角色视频编辑换脸处理工具_2113766570131542018.json, 视频生成/图生视频/MiniMax H3角色替换单人指定版｜视频编辑换脸一步完成_2113541615401918466.json, 视频生成/图生视频/MiniMax H3角色替换｜单人指定角色+视频编辑多合一_2110716972131512322.json, 视频生成/图生视频/MiniMax-H3高速大动态，无劣化抗形变模糊文生视频_2111233041338298369.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_162

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（数字人/数字人/写英文工作流｜数字人英文口播视频生成专用流_2114020800511696898.json、视频生成/图生视频/10步+3步Latent Upscaler｜H3参考模式图生视频_2091180204667531265.json、视频生成/图生视频/BUNNY_H3单采er_sde手动Sigma，文生视频节奏随心控_2110519304910364674.json、视频生成/图生视频/H3 Taomate 3步加速 中远距离不崩脸视频生成_2099588330131382273.json、视频生成/图生视频/H3全能参考短剧工作流 多模态输入视频生成_2109027495902277633.json…）

- **类型**：Text To Image
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：77%

## 共有节点

全部 11 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `ModelAttentionBackend` —— 10/11 个有
- `ModelPreviewOverrideKJ` —— 10/11 个有
- `PrimitiveFloat` —— 10/11 个有
- `PrimitiveStringMultiline` —— 10/11 个有
- `ManualSigmas` —— 8/11 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 8/11 个有
- `VHS_VideoCombine` —— 8/11 个有
- `BlockSparseAttention` —— 7/11 个有
- `MiniMaxH3SigmaShift` —— 7/11 个有
- `SaveImage` —— 7/11 个有
- `Fast Groups Bypasser (rgthree)` —— 6/11 个有
- `BasicScheduler` —— 5/11 个有
- `CreateVideo` —— 5/11 个有
- `ConditioningZeroOut` —— 4/11 个有
- `GetNode` —— 4/11 个有
- `MiniMaxH3Unified` —— 4/11 个有
- `SaveVideo` —— 4/11 个有
- `SetNode` —— 4/11 个有
- `VHS_LoadVideo` —— 4/11 个有
- `LoadAudio` —— 3/11 个有
- `MiniMaxChunkFeedForward` —— 3/11 个有
- `MiniMaxLowVRAMAttention` —— 3/11 个有
- `SplitSigmas` —— 2/11 个有
- `CR Prompt Text` —— 1/11 个有
- `CR Text Concatenate` —— 1/11 个有
- `Fast Bypasser (rgthree)` —— 1/11 个有
- `GetVideoComponents` —— 1/11 个有
- `Label (rgthree)` —— 1/11 个有
- `MiniMaxH3LearnedLatentUpscaleT8Advanced` —— 1/11 个有
- `MiniMaxH3SemanticBridgeApplyT8` —— 1/11 个有
- `MiniMaxH3SemanticBridgeConfigT8` —— 1/11 个有
- `PrimitiveBoolean` —— 1/11 个有
- `QZ_ResolutionPreset` —— 1/11 个有
- `RH_Astra` —— 1/11 个有
- `RunningHub Deepcleaner` —— 1/11 个有
- `VRAM_Debug` —— 1/11 个有
- `easy float` —— 1/11 个有
- `easy ifElse` —— 1/11 个有
- `布尔孤海` —— 1/11 个有

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
