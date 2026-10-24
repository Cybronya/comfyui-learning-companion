---
name: text_to_image_lora_sampler_clip_148
type: Text To Image
frequency: 11
level: strong
coverage: 0.866
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMaxH3参考图生视频｜角色一致性视频生成_2095091404421820417.json, 视频生成/图生视频/Minimax H3冻结时间360环绕｜首尾画面循环闭环｜HyperFlow 8步LoRA加持_2104830891699822594.json, 视频生成/图生视频/Minimax H3首尾帧生视频In8加速版图生视频生成_2088209952254021634.json, 视频生成/图生视频/Minimax-H3-图生视频（Lightx2v加速）_2086209989152174082.json, 视频生成/图生视频/MinimaxH3lightx2vlora图生视频工作流多重提速ENG加速ENG4步海螺ENG_2087126062730924033.json, 视频生成/图生视频/MinimaxH3海螺4步lightx2v加速lora-多重提速转场运镜图生视频_2087374035620556802.json, 视频生成/图生视频/R2V参考生视频加速版｜5060Ti 16G本地极速跑_2103045635455938561.json, 视频生成/图生视频/三图版全能参考｜MiniMax H3图生视频一键生成_2094737971634335745.json, 视频生成/图生视频/参考图生视频生成｜MiniMaxH3高质量出片工作流_2095049456667414529.json, 视频生成/图生视频/双图版全能参考｜MiniMax H3图生视频高质量生成_2094740772443738114.json, 视频生成/图生视频/提速不减质｜MiniMax H3图生视频加速通道_2096569545073971201.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_148

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/MiniMaxH3参考图生视频｜角色一致性视频生成_2095091404421820417.json、视频生成/图生视频/Minimax H3冻结时间360环绕｜首尾画面循环闭环｜HyperFlow 8步LoRA加持_2104830891699822594.json、视频生成/图生视频/Minimax H3首尾帧生视频In8加速版图生视频生成_2088209952254021634.json、视频生成/图生视频/Minimax-H3-图生视频（Lightx2v加速）_2086209989152174082.json、视频生成/图生视频/MinimaxH3lightx2vlora图生视频工作流多重提速ENG加速ENG4步海螺ENG_2087126062730924033.json…）

- **类型**：Text To Image
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 11 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `ComfyMathExpression` —— 9/11 个有
- `PrimitiveFloat` —— 9/11 个有
- `ResolutionSelector` —— 9/11 个有
- `CreateVideo` —— 8/11 个有
- `SaveVideo` —— 8/11 个有
- `MiniMaxH3ImageToVideo` —— 6/11 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 5/11 个有
- `PrimitiveInt` —— 5/11 个有
- `ModelAttentionBackend` —— 4/11 个有
- `PrimitiveStringMultiline` —— 4/11 个有
- `ComfySwitchNode` —— 3/11 个有
- `MiniMaxH3ReferenceToVideo` —— 3/11 个有
- `PrimitiveBoolean` —— 3/11 个有
- `VHS_VideoCombine` —— 3/11 个有
- `ImageResizeKJv2` —— 2/11 个有
- `MiniMaxH3Easy` —— 2/11 个有
- `MiniMaxH3EasyLoader` —— 2/11 个有
- `MiniMaxH3EasyOutput` —— 2/11 个有
- `RTXVideoSuperResolution` —— 2/11 个有
- `TextInput_` —— 2/11 个有
- `MiniMaxH3QwenReferencePrefixCacheT8Advanced` —— 1/11 个有
- `RHHiddenNodes` —— 1/11 个有
- `Seed (rgthree)` —— 1/11 个有
- `XB_ReferenceAny` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 11 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 11 | 100% |
| 采样算法 | er_sde | - | 11 | 100% |
| 调度器 | beta | - | 11 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |
| 宽度 | 80 | 80 - 80 | 11 | 100% |
| 高度 | 80 | 80 - 80 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，11 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，11 个样本，一致性 100%
- 调度器 最常用 beta，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，11 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，11 个样本，取值集中（一致性 100%）
- 高发问题（11/11 个样本）：Steps较低可能导致细节不足
