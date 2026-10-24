---
name: unknown_workflow_video_lora_sampler_370
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.500333
common_nodes: [AudioEncoderEncode, AudioEncoderLoader, CLIPLoader, CLIPTextEncode, CR Text, ColorMatch, Fast Groups Bypasser (rgthree), GetNode, INTConstant, ImageFromBatch, ImageResizeKJv2, JWInteger, KSamplerAdvanced, LoadAudio, LoadImage, LoraLoaderModelOnly, ModelPatchLoader, ModelPatchTorchSettings, PainterAI2V, PainterAudioCut, PathchSageAttentionKJ, SetNode, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/单图出高动态音画视频加对口型_2031370411778248706.json, 视频生成/图生视频/短剧对白生成 图片转视频音频同步支持单图首尾帧_2020844422413422593.json, 视频生成/图生视频/首尾帧出高动态音画视频加对口型_2031577434885197826.json, 视频生成/图生视频/高动态对口型图生视频_2029600384762781697.json, 视频生成/图生视频/高动态音画视频口型一条龙-支持单图、首尾帧_2017232753040822273.json, 视频生成/文生视频/高动态音画同步图生视频_支持单图、首尾帧_2046419746307973122.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_370

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/单图出高动态音画视频加对口型_2031370411778248706.json、视频生成/图生视频/短剧对白生成 图片转视频音频同步支持单图首尾帧_2020844422413422593.json、视频生成/图生视频/首尾帧出高动态音画视频加对口型_2031577434885197826.json、视频生成/图生视频/高动态对口型图生视频_2029600384762781697.json、视频生成/图生视频/高动态音画视频口型一条龙-支持单图、首尾帧_2017232753040822273.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：50%

## 共有节点

全部 6 个 workflow 都包含：
- `AudioEncoderEncode`
- `AudioEncoderLoader`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `ColorMatch`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `INTConstant`
- `ImageFromBatch`
- `ImageResizeKJv2`
- `JWInteger`
- `KSamplerAdvanced`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelPatchLoader`
- `ModelPatchTorchSettings`
- `PainterAI2V`
- `PainterAudioCut`
- `PathchSageAttentionKJ`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `JoinStrings` —— 5/6 个有
- `PreviewAudio` —— 5/6 个有
- `Qwen3_VQA` —— 5/6 个有
- `ShowText|pysssss` —— 5/6 个有
- `SomethingToString` —— 5/6 个有
- `TextInput_` —— 5/6 个有
- `AudioSeparation` —— 4/6 个有
- `SaveAudio` —— 4/6 个有
- `TDQwen3TTSDefineSpeaker` —— 4/6 个有
- `TDQwen3TTSModelLoader` —— 4/6 个有
- `TDQwen3TTSMultiDialog` —— 4/6 个有
- `LayerUtility: PurgeVRAM V2` —— 2/6 个有
- `RIFE VFI` —— 2/6 个有
- `Float` —— 1/6 个有
- `GetImagesFromBatchIndexed` —— 1/6 个有
- `SaveImage` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 6 | 67% |
| Prompt 约束强度(CFG) | 4 | 4 - 6 | 6 | 83% |
| 采样算法 | 1 | 1 - 1 | 6 | 100% |
| 调度器 | euler | - | 6 | 100% |
| 重绘幅度 | simple | - | 6 | 83% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，6 个样本，一致性 67%
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 6，6 个样本，取值集中（一致性 83%）
- 采样算法 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，6 个样本，一致性 100%
- 重绘幅度 最常用 simple，6 个样本，一致性 83%
