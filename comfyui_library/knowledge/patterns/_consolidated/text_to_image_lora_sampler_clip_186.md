---
name: text_to_image_lora_sampler_clip_186
type: Text To Image
frequency: 7
level: strong
coverage: 0.767286
common_nodes: [AudioCrop, BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadAudio, LoadImage, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SoundFlow_GetLength, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/Minimax数字人V3｜自动提词加速语音自驱图生视频数字人_2089690692552581121.json, 视频生成/图生视频/数字人V3流程｜Minimax自动提词加速 语音自驱图生视频_2089421450242514945.json, 视频生成/文生视频/minimaxH3数字人唱歌｜音频驱动口播视频生成_2095236856601468930.json, 视频生成/文生视频/minimaxH3数字人音频驱动｜音频生成口播视频工作流_2094870008924041217.json, 视频生成/文生视频/图片音频生成口播数字人｜MinimaxH3全节点注释_2091178749877379073.json, 视频生成/文生视频/数字人唱歌视频生成｜minimaxH3文生视频一键直出_2095506914233905153.json, 视频生成/文生视频/音频图片变口播数字人｜MinimaxH3全节点注释版_2090887027813343234.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_186

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/Minimax数字人V3｜自动提词加速语音自驱图生视频数字人_2089690692552581121.json、视频生成/图生视频/数字人V3流程｜Minimax自动提词加速 语音自驱图生视频_2089421450242514945.json、视频生成/文生视频/minimaxH3数字人唱歌｜音频驱动口播视频生成_2095236856601468930.json、视频生成/文生视频/minimaxH3数字人音频驱动｜音频生成口播视频工作流_2094870008924041217.json、视频生成/文生视频/图片音频生成口播数字人｜MinimaxH3全节点注释_2091178749877379073.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：77%

## 共有节点

全部 7 个 workflow 都包含：
- `AudioCrop`
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SoundFlow_GetLength`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 5/7 个有
- `GetNode` —— 5/7 个有
- `MiniMaxH3ReferenceToVideo` —— 5/7 个有
- `ModelPreviewOverrideKJ` —— 5/7 个有
- `PrimitiveStringMultiline` —— 5/7 个有
- `SaveVideo` —— 5/7 个有
- `SetNode` —— 5/7 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 5/7 个有
- `CR Text` —— 4/7 个有
- `ModelAttentionBackend` —— 4/7 个有
- `PathchSageAttentionKJ` —— 3/7 个有
- `MiniMaxH3AudioConditioningT8` —— 2/7 个有
- `PreviewAudio` —— 2/7 个有
- `RH_LLMAPI_Pro_Node` —— 2/7 个有
- `RunningHub_VoxCPM_LoadModel` —— 2/7 个有
- `RunningHub_VoxCPM_MultiSpeaker` —— 2/7 个有
- `StringFunction|pysssss` —— 2/7 个有
- `VHS_VideoCombine` —— 2/7 个有
- `easy showAnything` —— 2/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 7 | 100% |
| 高度 | 80 | 80 - 80 | 7 | 100% |
| 采样步数 | 4 | 4 - 4 | 7 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 7 | 100% |
| 采样算法 | er_sde | - | 7 | 100% |
| 调度器 | beta | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，7 个样本，一致性 100%
- 调度器 最常用 beta，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（7/7 个样本）：Steps较低可能导致细节不足
