---
name: unknown_workflow_video_lora_sampler_210
type: Unknown Workflow
frequency: 9
level: strong
coverage: 0.905556
common_nodes: [AudioCropProcessUTK, AudioEncoderEncode, AudioEncoderLoader, CLIPLoader, CLIPTextEncode, CR Float To Integer, KSampler, LoadAudio, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, SimpleMath+, VAEDecode, VAELoader, VHS_VideoCombine, WanSoundImageToVideo, wanBlockSwap]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/1961096934272471041.json, 视频生成/图生视频/1961064649582120962.json, 视频生成/图生视频/1961096971735994369.json, 视频生成/图生视频/1961257200578707457.json, 视频生成/图生视频/1962687799453462530.json, 视频生成/图生视频/1962685286419415042.json, 视频生成/图生视频/1960895773552644098.json, 视频生成/图生视频/1961341007348568066.json, 视频生成/图生视频/1965758281866219521.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_210

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/1961096934272471041.json、视频生成/图生视频/1961064649582120962.json、视频生成/图生视频/1961096971735994369.json、视频生成/图生视频/1961257200578707457.json、视频生成/图生视频/1962687799453462530.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 9 个 workflow 都包含：
- `AudioCropProcessUTK`
- `AudioEncoderEncode`
- `AudioEncoderLoader`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Float To Integer`
- `KSampler`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `SimpleMath+`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanSoundImageToVideo`
- `wanBlockSwap`

**可变部分**（部分 workflow 才有）：
- `PreviewAudio` —— 8/9 个有
- `UNETLoader` —— 8/9 个有
- `VHS_LoadVideo` —— 8/9 个有
- `PreviewImage` —— 7/9 个有
- `ContextWindowsManual` —— 5/9 个有
- `ImageFromBatch+` —— 5/9 个有
- `JWFloat` —— 5/9 个有
- `JWInteger` —— 5/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/9 个有
- `ImageResizeKJv2` —— 4/9 个有
- `Display Any (rgthree)` —— 3/9 个有
- `SaveLatent` —— 3/9 个有
- `CR Prompt Text` —— 2/9 个有
- `SaveImage` —— 2/9 个有
- `LayerUtility: PurgeVRAM V2` —— 1/9 个有
- `OpenposePreprocessor` —— 1/9 个有
- `UnetLoaderGGUF` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 9 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | uni_pc | - | 9 | 100% |
| 调度器 | simple | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，9 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 uni_pc，9 个样本，一致性 100%
- 调度器 最常用 simple，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（9/9 个样本）：Steps较低可能导致细节不足
