---
name: text_to_image_lora_sampler_clip_89
type: Text To Image
frequency: 15
level: strong
coverage: 0.7964
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/首尾帧参考生视频｜MiniMax H3 8步LoRa+Sage双重加速特效_2089827009160638465.json, 视频生成/图生视频/首尾帧图生视频｜minimaxH3 FL2VA开源直出_2093791140687466498.json, 视频生成/图生视频/首尾帧提示词自动扩写T8｜MinimaxH3角色一致性分镜图生视频_2091163950061809666.json, 视频生成/图生视频/首尾帧生视频In8加速版｜Minimax H3图生视频工作流_2088117119526465537.json, 视频生成/图生视频/首尾帧生视频版本｜傲雪AIGC MiniMax+H3角色一致性表演_2094716870489370626.json, 视频生成/图生视频/首尾帧视频图生成｜Minimax H3图生视频衔接_2095508493355806721.json, 视频生成/图生视频/高质量加速图生视频 Minimax H3 画质与速度兼顾快速出片_2094180356353249281.json, 视频生成/图生视频/高质量加速版图生视频｜Minimax H3一键高清生成_2094316328000778241.json, 视频生成/图生视频/高速一键出片图生视频｜H3模型人像写真生成_2093457952874254337.json, 视频生成/文生视频/15秒直出高清分辨率Mini Max H3漫剧工作流文生视频图生视频_2088391498671935489.json, 视频生成/文生视频/MiniMax H3 FL2VA单模型int8高清重绘｜9图3视频3音频文生视频_2090459732577439745.json, 视频生成/文生视频/Minimax H3双模二采｜文生视频图生视频视频生视频全能出片_2088728994442203137.json, 视频生成/文生视频/二采重绘V2｜H3海螺视频画质增强高清直出_2090143662247333890.json, 视频生成/文生视频/双模二采玩法｜Minimax H3文生图生视频再采样_2089071865905115138.json, 视频生成/文生视频/海螺H3二采重绘V2｜文生视频其它视频处理图生视频_2090420618834563073.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_89

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（视频生成/图生视频/首尾帧参考生视频｜MiniMax H3 8步LoRa+Sage双重加速特效_2089827009160638465.json、视频生成/图生视频/首尾帧图生视频｜minimaxH3 FL2VA开源直出_2093791140687466498.json、视频生成/图生视频/首尾帧提示词自动扩写T8｜MinimaxH3角色一致性分镜图生视频_2091163950061809666.json、视频生成/图生视频/首尾帧生视频In8加速版｜Minimax H3图生视频工作流_2088117119526465537.json、视频生成/图生视频/首尾帧生视频版本｜傲雪AIGC MiniMax+H3角色一致性表演_2094716870489370626.json…）

- **类型**：Text To Image
- **样本数**：15
- **可信度**：强结论
- **平均知识覆盖**：80%

## 共有节点

全部 15 个 workflow 都包含：
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
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `PrimitiveFloat` —— 14/15 个有
- `ResolutionSelector` —— 13/15 个有
- `CreateVideo` —— 10/15 个有
- `VHS_VideoCombine` —— 10/15 个有
- `PrimitiveStringMultiline` —— 9/15 个有
- `ImageResizeKJv2` —— 8/15 个有
- `MiniMaxH3ImageToVideo` —— 8/15 个有
- `easy showAnything` —— 8/15 个有
- `MiniMaxH3ReferenceToVideo` —— 7/15 个有
- `PT_H3ConcatAVLatent` —— 7/15 个有
- `VAEEncode` —— 7/15 个有
- `VAEEncodeAudio` —— 7/15 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 6/15 个有
- `LoadAudio` —— 6/15 个有
- `ModelAttentionBackend` —— 6/15 个有
- `SaveVideo` —— 6/15 个有
- `easy clearCacheAll` —— 6/15 个有
- `GetNode` —— 5/15 个有
- `INTConstant` —— 5/15 个有
- `RHLLMChatNode` —— 5/15 个有
- `SetNode` —— 5/15 个有
- `StringFunction|pysssss` —— 5/15 个有
- `VHS_LoadVideo` —— 5/15 个有
- `AudioCrop` —— 4/15 个有
- `Fast Groups Bypasser (rgthree)` —— 4/15 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 4/15 个有
- `PathchSageAttentionKJ` —— 4/15 个有
- `Text` —— 4/15 个有
- `EasyCache` —— 3/15 个有
- `MiniMaxH3BlockCacheT8` —— 3/15 个有
- `CR Text` —— 2/15 个有
- `CR Text Concatenate` —— 2/15 个有
- `FloatConstant` —— 2/15 个有
- `GetImageRangeFromBatch` —— 2/15 个有
- `PreviewImage` —— 2/15 个有
- `PurgeVRAM_UTK` —— 2/15 个有
- `RHHiddenNodes` —— 2/15 个有
- `ResizeShortestToNode` —— 2/15 个有
- `Any Switch (rgthree)` —— 1/15 个有
- `ImageResize+` —— 1/15 个有
- `LoraLoaderBypassModelOnly` —— 1/15 个有
- `SigmasGraph` —— 1/15 个有
- `SolAttnPatch` —— 1/15 个有
- `UniBlockSwap` —— 1/15 个有
- `easy cleanGpuUsed` —— 1/15 个有
- `easy int` —— 1/15 个有
- `忽略多组孤海` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 15 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 15 | 100% |
| 采样算法 | er_sde | - | 15 | 100% |
| 调度器 | beta | - | 15 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 15 | 100% |
| 宽度 | 80 | 80 - 80 | 15 | 100% |
| 高度 | 80 | 80 - 80 | 15 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 17/15 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，15 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，15 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，15 个样本，一致性 100%
- 调度器 最常用 beta，15 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，15 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，15 个样本，取值集中（一致性 100%）
- 高发问题（17/15 个样本）：Steps较低可能导致细节不足
