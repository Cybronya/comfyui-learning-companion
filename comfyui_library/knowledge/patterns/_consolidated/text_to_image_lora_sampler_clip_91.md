---
name: text_to_image_lora_sampler_clip_91
type: Text To Image
frequency: 10
level: strong
coverage: 0.8074
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoraLoaderModelOnly, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/开源版文生视频｜MiniMax-H3提示词一键出片_2089012717008023553.json, 视频生成/文生视频/开源版文生视频｜MiniMax-H3纯文本生成视频开源工作流_2088773720985923585.json, 视频生成/文生视频/快速文生视频｜Fastvideo H3角色表演ComfyUI工作流_2095559517340790785.json, 视频生成/文生视频/战斗双采首尾帧模式｜文生视频特效视频生成_2094537849541578753.json, 视频生成/文生视频/打斗强化三件套｜MiniMax_H3二采+打斗lora+动作修复_2092876212183068673.json, 视频生成/文生视频/打斗强化二采修复｜MiniMax H3打斗lora文生图生视频_2092687490728681474.json, 视频生成/文生视频/文生+首尾帧全能｜MiniMax H3 FL2VA视频生成_2093227972433104897.json, 视频生成/文生视频/极速版二采潜空间直接放大 minimaxh3 去油画质提升_2094233661909585921.json, 视频生成/文生视频/武戏专用参考｜MiniMax H3提示词手输自动可选_2096598519665750017.json, 视频生成/文生视频/高清人脸｜海螺H3 sigma强化潜空间放大视频生成_2089812873718624257.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_91

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/文生视频/开源版文生视频｜MiniMax-H3提示词一键出片_2089012717008023553.json、视频生成/文生视频/开源版文生视频｜MiniMax-H3纯文本生成视频开源工作流_2088773720985923585.json、视频生成/文生视频/快速文生视频｜Fastvideo H3角色表演ComfyUI工作流_2095559517340790785.json、视频生成/文生视频/战斗双采首尾帧模式｜文生视频特效视频生成_2094537849541578753.json、视频生成/文生视频/打斗强化三件套｜MiniMax_H3二采+打斗lora+动作修复_2092876212183068673.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 10 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `PrimitiveFloat`
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
- `CreateVideo` —— 8/10 个有
- `PrimitiveStringMultiline` —— 8/10 个有
- `SaveVideo` —— 8/10 个有
- `LoadImage` —— 7/10 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 7/10 个有
- `LTXVConcatAVLatent` —— 6/10 个有
- `LTXVSeparateAVLatent` —— 6/10 个有
- `MiniMaxH3ImageToVideo` —— 5/10 个有
- `MiniMaxH3ReferenceToVideo` —— 5/10 个有
- `MinimaxH3LatentUpscaler3D` —— 5/10 个有
- `ExtendIntermediateSigmas` —— 4/10 个有
- `GetNode` —— 4/10 个有
- `H3SigmaRefiner` —— 4/10 个有
- `MiniMaxH3SigmaShift` —— 4/10 个有
- `SetNode` —— 4/10 个有
- `DisableNoise` —— 3/10 个有
- `ModelAttentionBackend` —— 3/10 个有
- `ModelPreviewOverrideKJ` —— 3/10 个有
- `SplitSigmas` —— 3/10 个有
- `SplitSigmasDenoise` —— 3/10 个有
- `easy cleanGpuUsed` —— 3/10 个有
- `LoadAudio` —— 2/10 个有
- `VHS_VideoCombine` —— 2/10 个有
- `Any Switch (rgthree)` —— 1/10 个有
- `CR Prompt Text` —— 1/10 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/10 个有
- `MinimaxH3LatentUpscalerNode3D` —— 1/10 个有
- `MuyeTextEditOutput` —— 1/10 个有
- `PathchSageAttentionKJ` —— 1/10 个有
- `PreviewImage` —— 1/10 个有
- `RH_LLMAPI_Pro_Node` —— 1/10 个有
- `SolAttnMiniMax` —— 1/10 个有
- `StringConcatenate` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 10 | 100% |
| 高度 | 80 | 80 - 80 | 10 | 100% |
| 采样步数 | 4 | 4 - 4 | 10 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 10 | 100% |
| 采样算法 | er_sde | - | 10 | 100% |
| 调度器 | beta | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，10 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，10 个样本，一致性 100%
- 调度器 最常用 beta，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 高发问题（10/10 个样本）：Steps较低可能导致细节不足
