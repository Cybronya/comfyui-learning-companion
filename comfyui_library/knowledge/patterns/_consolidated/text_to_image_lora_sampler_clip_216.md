---
name: text_to_image_lora_sampler_clip_216
type: Text To Image
frequency: 9
level: strong
coverage: 0.794333
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/首尾帧参考生视频｜MiniMax H3 8步LoRa+Sage双重加速特效_2089827009160638465.json, 视频生成/图生视频/首尾帧图生视频｜minimaxH3 FL2VA开源直出_2093791140687466498.json, 视频生成/图生视频/首尾帧提示词自动扩写T8｜MinimaxH3角色一致性分镜图生视频_2091163950061809666.json, 视频生成/图生视频/首尾帧生视频In8加速版｜Minimax H3图生视频工作流_2088117119526465537.json, 视频生成/图生视频/首尾帧生视频版本｜傲雪AIGC MiniMax+H3角色一致性表演_2094716870489370626.json, 视频生成/图生视频/首尾帧视频图生成｜Minimax H3图生视频衔接_2095508493355806721.json, 视频生成/图生视频/高速一键出片图生视频｜H3模型人像写真生成_2093457952874254337.json, 视频生成/文生视频/H3 LightX2V二采高清文生视频图生视频生成_2088217634990018561.json, 视频生成/文生视频/Minimax H3文生首尾图参多合一生视频-自用版二采高清放大_2087394737073512450.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_216

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/首尾帧参考生视频｜MiniMax H3 8步LoRa+Sage双重加速特效_2089827009160638465.json、视频生成/图生视频/首尾帧图生视频｜minimaxH3 FL2VA开源直出_2093791140687466498.json、视频生成/图生视频/首尾帧提示词自动扩写T8｜MinimaxH3角色一致性分镜图生视频_2091163950061809666.json、视频生成/图生视频/首尾帧生视频In8加速版｜Minimax H3图生视频工作流_2088117119526465537.json、视频生成/图生视频/首尾帧生视频版本｜傲雪AIGC MiniMax+H3角色一致性表演_2094716870489370626.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：79%

## 共有节点

全部 9 个 workflow 都包含：
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
- `MiniMaxH3ImageToVideo` —— 8/9 个有
- `PrimitiveFloat` —— 8/9 个有
- `ResolutionSelector` —— 7/9 个有
- `CreateVideo` —— 5/9 个有
- `SaveVideo` —— 5/9 个有
- `VHS_VideoCombine` —— 5/9 个有
- `ImageResizeKJv2` —— 4/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/9 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 4/9 个有
- `Text` —— 4/9 个有
- `GetNode` —— 3/9 个有
- `PT_H3ConcatAVLatent` —— 3/9 个有
- `SetNode` —— 3/9 个有
- `VAEEncode` —— 3/9 个有
- `VAEEncodeAudio` —— 3/9 个有
- `easy showAnything` —— 3/9 个有
- `MiniMaxH3ReferenceToVideo` —— 2/9 个有
- `PathchSageAttentionKJ` —— 2/9 个有
- `PreviewImage` —— 2/9 个有
- `PrimitiveStringMultiline` —— 2/9 个有
- `RHHiddenNodes` —— 2/9 个有
- `Any Switch (rgthree)` —— 1/9 个有
- `Fast Groups Bypasser (rgthree)` —— 1/9 个有
- `ImageResize+` —— 1/9 个有
- `Int` —— 1/9 个有
- `MiniMaxChunkFeedForward` —— 1/9 个有
- `MiniMaxLowVRAMAttention` —— 1/9 个有
- `ModelAttentionBackend` —— 1/9 个有
- `easy cleanGpuUsed` —— 1/9 个有
- `easy int` —— 1/9 个有
- `忽略多组孤海` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 9 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 9 | 100% |
| 采样算法 | er_sde | - | 9 | 100% |
| 调度器 | beta | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |
| 宽度 | 80 | 80 - 80 | 9 | 100% |
| 高度 | 80 | 80 - 80 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，9 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，9 个样本，一致性 100%
- 调度器 最常用 beta，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高发问题（11/9 个样本）：Steps较低可能导致细节不足
