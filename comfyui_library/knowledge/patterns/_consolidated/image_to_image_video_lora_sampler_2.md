---
name: image_to_image_video_lora_sampler_2
type: Image To Image
frequency: 10
level: strong
coverage: 0.9285
common_nodes: [AILab_QwenVL_Advanced, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CR Text, CR Text Concatenate, Display Any (rgthree), ImageFromBatch+, ImageResizeKJv2, ImpactInt, JWInteger, JjkText, KSampler, KSamplerAdvanced, LoadAudio, LoadImage, LoraLoaderModelOnly, ModelPatchTorchSettings, ModelSamplingSD3, PathchSageAttentionKJ, ProcessString, RH_LLMAPI_Pro_Node, Seed (rgthree), SimpleMath+, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader, VHS_VideoCombine, WanFirstLastFrameToVideo, easy anythingIndexSwitch, easy forLoopEnd, easy forLoopStart, easy imageListToImageBatch, easy promptLine, wanBlockSwap]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/2019692066992820226.json, 视频生成/图生视频/2021404969047433218.json, 视频生成/图生视频/2020743770496569345.json, 视频生成/图生视频/2014568371844554754.json, 视频生成/图生视频/2035185865479163905.json, 视频生成/图生视频/2014300434378268674.json, 视频生成/图生视频/2023718194728407042.json, 视频生成/图生视频/2015622701288792066.json, 视频生成/图生视频/2019748933689417730.json, 视频生成/文生视频/全自动可爱DORO_2032369998534021121.json]
source: knowledge_consolidation
---

# image_to_image_video_lora_sampler_2

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/2019692066992820226.json、视频生成/图生视频/2021404969047433218.json、视频生成/图生视频/2020743770496569345.json、视频生成/图生视频/2014568371844554754.json、视频生成/图生视频/2035185865479163905.json…）

- **类型**：Image To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 10 个 workflow 都包含：
- `AILab_QwenVL_Advanced`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CR Text`
- `CR Text Concatenate`
- `Display Any (rgthree)`
- `ImageFromBatch+`
- `ImageResizeKJv2`
- `ImpactInt`
- `JWInteger`
- `JjkText`
- `KSampler`
- `KSamplerAdvanced`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `ProcessString`
- `RH_LLMAPI_Pro_Node`
- `Seed (rgthree)`
- `SimpleMath+`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanFirstLastFrameToVideo`
- `easy anythingIndexSwitch`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy imageListToImageBatch`
- `easy promptLine`
- `wanBlockSwap`

**可变部分**（部分 workflow 才有）：
- `Fast Bypasser (rgthree)` —— 9/10 个有
- `LayerUtility: PurgeVRAM V2` —— 9/10 个有
- `Mute / Bypass Repeater (rgthree)` —— 9/10 个有
- `easy batchAnything` —— 9/10 个有
- `IfInnerExecute` —— 8/10 个有
- `Int` —— 8/10 个有
- `easy compare` —— 8/10 个有
- `easy imageCount` —— 8/10 个有
- `easy showAnything` —— 8/10 个有
- `CompressImages` —— 5/10 个有
- `AppendImageBatch` —— 1/10 个有
- `Bjornulf_ShowInt` —— 1/10 个有
- `GetNode` —— 1/10 个有
- `MathExpression|pysssss` —— 1/10 个有
- `PreviewImage` —— 1/10 个有
- `RH_LLMAPI_NODE` —— 1/10 个有
- `SaveStringKJ` —— 1/10 个有
- `SetNode` —— 1/10 个有
- `ToInt` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 10 | 60% |
| Prompt 约束强度(CFG) | 6 | 1 - 6 | 10 | 73% |
| 采样算法 | 1 | 1 - 1 | 9 | 100% |
| 调度器 | euler | - | 10 | 90% |
| 重绘幅度 | simple | - | 10 | 90% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 最常用 randomize，10 个样本，一致性 60%
- Prompt 约束强度(CFG) 中位数 6，观测区间 1 - 6，10 个样本
- 采样算法 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，10 个样本，一致性 90%
- 重绘幅度 最常用 simple，10 个样本，一致性 90%
- 高发问题（10/10 个样本）：Steps较低可能导致细节不足
